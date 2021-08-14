# /usr/bin/python3
# -*- coding:utf-8 -*-
"""
get images in vps and transfer to aliyun registry
"""
import base64
import json
import logging
import os
import sys
from collections import deque
from pathlib import Path

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
aliyun_registry_url = 'registry.cn-hangzhou.aliyuncs.com'
aliyun_registry_namespace = '/lisong'
local_registry_url = 'registry.lisong.pub:28500'
local_registry_namespace = '/sunrise'
acceptable_boolean = ("1", "true", 'yes', 'YES', 'y', 'Y')
"""
## 应用场景
1. 从包括 docker hub 仓库或镜像仓库下载镜像到本机，然后打为私有镜像仓库的名称然后推送到私有仓库
```
{
  "target_namespace": "<local-namespace>",
  "target_registry": "<local-repository>",
  "needs_push": true
}
```
2. 因为网络原因，从一台能访问原始镜像仓库的主机下载镜像，然后打为私有镜像仓库的名称然后推送到私有仓库(私有仓库公网可访问)
```
{
  "target_namespace": "<local-namespace>",
  "target_registry": "<local-repository>",
  "needs_push": true
}
```
3. 因为网络原因，从一台能访问原始镜像仓库的主机下载镜像，推送到中转镜像仓库(比如 阿里云)，再在本地机器从中转镜像仓库(比如 阿里云)拉取，然后打为私有镜像仓库的名称然后推送到私有仓库
远程配置
```
{
  "target_namespace": "<jump-namespace>",
  "target_registry": "<jump-repository>",
  "namespace_encode": true,
  "needs_push": true
}
```
本地配置
```
{
  "target_namespace": "<local-namespace>",
  "target_registry": "<local-repository>",
  "jump_namespace": "<jump-namespace>",
  "jump_registry": "<jump-repository>",
  "namespace_encode": true,
  "needs_push": true
}
```
4. 可以处理单个或同时处理多个镜像

## 说明
镜像格式  <name>:<tag>
镜像格式  <namespace>/<name>:<tag>
镜像格式  <registry>/<name>:<tag>
镜像格式  <registry>/<namespace>/<name>:<tag>

因为私有仓库使用的是 Harbor 所以对于没有 namespace 的镜像会推送到一个默认的 namespace， 有 namespace 就使用镜像的 namespace, 
但就需要在 Harbor 中创建对应的 project
"""


class GeneralObject(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value


class TransferConfig(GeneralObject):

    def __init__(self) -> None:
        super().__init__()
        self.config_keys = self.keys()
        self.image = ""
        self.source = ""
        self.jump_namespace = ""
        self.jump_registry = ""
        # self.target: DockerImage = None
        self.target_namespace = ""
        self.target_registry = ""
        self.needs_push = False
        self.namespace_encode = False
        self.config_path = "config.json"
        self.image_path = "images.txt"
        self.dry_run = False

    def load_cmd_args(self, cmd_args: deque):
        if len(cmd_args) == 0:
            return

        x = cmd_args.popleft()
        if x.startswith("--"):
            _x = x[2:]
            if _x in self.config_keys:
                if not isinstance(self[_x], bool):
                    if len(cmd_args) > 0:
                        y = cmd_args.popleft()
                        self[_x] = y
                        log.info(f'load config {_x}={y}')
                    else:
                        raise AttributeError(f"none boolean property {_x} value not set")
                else:
                    if len(cmd_args) > 0:
                        if not cmd_args[0].startswith("--"):
                            y = cmd_args.popleft()
                            if y not in acceptable_boolean:
                                raise AttributeError(f"boolean property {_x} cannot accept none bool value {y}")
                            else:
                                self[_x] = True
                                log.info(f'load config {_x}=True')
                        else:
                            self[_x] = True
                            log.info(f'load config {_x}=True')
                    else:
                        self[_x] = True
                        log.info(f'load config {_x}=True')

            else:
                log.error(f'unknown key {_x}')

        self.load_cmd_args(cmd_args)

    def load_config_file(self):
        config_file = Path(self.config_path)
        if config_file.exists():
            config = json.loads(config_file.read_text())
            for k, v in config.items():
                log.info(f"load config from file {k}={v}")
            self.update(config)


class DockerImage(GeneralObject):

    def __init__(self) -> None:
        super().__init__()
        self.registry: str = ""
        self.namespace: str = ""
        self.name: str = ""
        self.tag: str = ""

    def __str__(self) -> str:
        if len(self.registry) > 0 and not self.namespace.endswith("/"):
            self.registry += "/"
        if len(self.namespace) > 0 and not self.namespace.endswith("/"):
            self.namespace += "/"
        return f'{self.registry}{self.namespace}{self.name}:{self.tag}'

    def parse_image(self, image: str):
        _image = image.split("/")
        _size = len(_image)
        tagged_name = _image[-1].strip()
        self.name, self.tag = tagged_name.split(":")
        if _size > 1:
            first_part = _image[0]
            if "." in first_part:
                self.registry = first_part
            else:
                self.namespace = first_part
        if _size == 3:
            self.namespace = _image[1]
        elif _size > 3:
            self.namespace = '{}'.format("/".join(_image[1:-1]))


class DockerImageTransfer:

    def __init__(self, image, direct):
        self.tagged_image_name = None
        self.registry_url = None
        self.registry_namespace = ''
        self.image = image
        print("download direct: %s" % direct)
        self.direct = direct
        self.parse_image()

    def transfer2aliyun(self):
        """
        在没有墙的环境下，下载镜像并打为 aliyun 的镜像，再推送
        """
        aliyun_image = self.get_aliyun_image()
        pull_image(self.image)
        tag_image(self.image, aliyun_image)
        push_image(aliyun_image)

    def transfer2origin(self):
        """
        在工作环境，从 aliyun 拉取对应的镜像，再打为原来的镜像名称
        """
        aliyun_image = self.get_aliyun_image()
        tag_image(aliyun_image, self.image)

    def transfer2local(self):
        remote_image = self.image
        if not self.direct:
            remote_image = self.get_aliyun_image()

        pull_image(remote_image)
        local_image = self.get_local_image()

        tag_image(remote_image, local_image)
        push_image(local_image)

    def get_aliyun_image(self):
        return '%s%s/%s%s' % (aliyun_registry_url, aliyun_registry_namespace, self.tagged_image_name,
                              self.registry_namespace.replace("/", "-"))

    def get_local_image(self):
        if len(self.registry_namespace) == 0:
            self.registry_namespace = local_registry_namespace
        return '%s%s/%s' % (local_registry_url, self.registry_namespace, self.tagged_image_name)

    def parse_image(self):
        c = self.image.count('/')

        if c > 1:
            name_space_start = self.image.find("/")
            name_space_end = self.image.rfind("/")
            self.tagged_image_name = self.image.strip('\n')[name_space_end + 1:]
            self.registry_namespace = self.image[name_space_start:name_space_end]
            self.registry_url = self.image[:name_space_start]

        elif c > 0:
            sep = self.image.rfind("/")
            self.tagged_image_name = self.image.strip('\n')[sep + 1:]
            self.registry_url = self.image[:sep]

        else:
            self.tagged_image_name = self.image

    def transfer_single(self, act):
        transfer_actions = {
            0: self.transfer2aliyun,
            1: self.transfer2origin,
            2: self.transfer2local
        }
        transfer_actions[act]()



def transfer_multiply(action, isDirect):
    fh = open('images.txt')
    action %= 10
    log.info("action %s ", action)
    x = 0

    for image in fh:
        w = DockerImageTransfer(image.strip('\n'), isDirect)
        w.transfer_single(action)
        x += 1
    log.info("%d images transfer" % x)


def pull_image(image: str, dry_run: bool = False):
    log.info(f"pull image {image}")
    if not dry_run:
        os.system(f'docker pull {image}')


def push_image(image: str, dry_run: bool = False):
    log.info(f"push image {image}")
    if not dry_run:
        os.system(f'docker push {image}')


def tag_image(source_image: str, target_image: str, dry_run: bool = False):
    log.info(f"tag image {source_image} to {target_image}")
    if not dry_run:
        os.system(f'docker tag {source_image} {target_image}')


def is_not_blank(source: str):
    return source is not None and len(source) > 0


def main():
    config = TransferConfig()
    config.load_cmd_args(deque(args))
    config.load_config_file()
    if is_not_blank(config.target_registry):
        if is_not_blank(config.image):
            image = config.image
            target_image = build_target_image(config, image)
            _target_image = str(target_image)
            if is_not_blank(config.jump_registry):
                jump_image = build_jump_image(config, image)
                source_image = str(jump_image)
            else:
                source_image = image
            push_image(source_image, config.dry_run)
            tag_image(source_image, _target_image, config.dry_run)
            push_image(_target_image, config.dry_run)

        if is_not_blank(config.image_path):
            with open(config.image_path) as fh:
                for image in fh:
                    build_target_image(config, image)
    else:
        # TODO 从中转仓库拉取镜像，打回原镜像
        pass


def build_jump_image(config: TransferConfig, image: str) -> DockerImage:
    origin_image = DockerImage()
    origin_image.parse_image(image)
    jump_image = DockerImage()
    jump_image.name = origin_image.name
    jump_image.tag = origin_image.tag
    if is_not_blank(config.jump_registry):
        jump_image.registry = config.jump_registry
        jump_image.namespace = config.jump_namespace
    if config.namespace_encode:
        jump_image.tag = encode_tag(origin_image)

    return jump_image


def build_target_image(config: TransferConfig, image: str) -> DockerImage:
    origin_image = DockerImage()
    origin_image.parse_image(image)
    target_image = DockerImage()
    target_image.registry = config.target_registry
    target_image.name = origin_image.name
    target_image.tag = origin_image.tag
    if config.namespace_encode:
        encoded_tag = encode_tag(origin_image)
        target_image.tag = encoded_tag
        target_image.namespace = config.target_namespace
    else:
        if is_not_blank(origin_image.namespace):
            target_image.namespace = origin_image.namespace
        else:
            target_image.namespace = config.target_namespace
    return target_image


def encode_tag(origin_image):
    if is_not_blank(origin_image.namespace):
        encoded_ns = base64.urlsafe_b64encode(origin_image.namespace.encode()).decode()
        encoded_tag = f"{origin_image.tag}-{encoded_ns}"
        return encoded_tag
    return origin_image.tag


if __name__ == '__main__':
    args = sys.argv
    log.info(f"got {len(args)} args")
    main()

    # 0 single image pass by arg tag and push to aliyun
    # 1 single image pass by arg pull from aliyun and tag to origin
    # 2 single image pass by arg pull from aliyun and tag to local
    # 10 multiply images pass by images.txt tag and push to aliyun
    # 11 multiply images pass by images.txt  pull from aliyun and tag to origin
    # 12 isdirect multiply images pass by images.txt  pull from aliyun and tag to local
    #
    # action = int(args[1])
    # registry_namespace = "/lisong"
    # isDirect = False
    # if len(args) == 1:
    #     help_message = '''
    #     1. single image process
    #     python docker_image_transfer.py <action> <image> <isDirect>
    #     action:
    #         0 single image pass by arg tag and push to aliyun
    #         1 single image pass by arg pull from aliyun and tag to origin
    #         2 single image pass by arg pull from aliyun and tag to local
    #     2. multiply images process
    #     python docker_image_transfer.py <action> <isDirect>
    #     action:
    #         10 multiply images pass by images.txt tag and push to aliyun
    #         11 multiply images pass by images.txt  pull from aliyun and tag to origin
    #         12 isdirect multiply images pass by images.txt  pull from aliyun and tag to local
    #     '''
    #     print(help_message)
    #     sys.exit(0)
    #
    # if action < 10:
    #     if len(args) > 3:
    #         isDirect = True
    #     DockerImageTransfer(args[2].strip('\n'), isDirect).transfer_single(action)
    # else:
    #     if len(args) > 2:
    #         isDirect = True
    #     transfer_multiply(action, isDirect)
