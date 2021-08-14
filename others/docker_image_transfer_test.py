import json
import unittest

from others.docker_image_transfer import DockerImage, TransferConfig, build_target_image, build_jump_image


class MyTestCase(unittest.TestCase):
    def test_image(self):
        images = (
            "nginx:1.14.2",
            "registry.lisong.pub/nginx:1.14.2",
            "registry.lisong.pub/sunrise/nginx:1.14.2",
            "registry.lisong.pub/lisong/test/nginx:1.14.2",
            "coredns/coredns:1.8.4",
            "quay.io/coreos/flannel:v0.11.0-amd64",
        )
        for image in images:
            img = DockerImage()
            img.parse_image(image)
            print(json.dumps(img))
            self.assertEqual(image, str(img))

    def test_build_image(self):
        config = TransferConfig()
        config.config_path = "/tmp/config.json"
        config.load_config_file()
        tests = (
            ("nginx:1.14.2", "registry.lisong.pub:28500/sunrise/nginx:1.14.2"),
            ("coredns/coredns:1.8.4", "registry.lisong.pub:28500/coredns/coredns:1.8.4"),
            ("quay.io/coreos/flannel:v0.11.0-amd64", "registry.lisong.pub:28500/coreos/flannel:v0.11.0-amd64"),
        )
        for source, expected in tests:
            target = build_target_image(config, source)

            print(target)
            self.assertEqual(expected, str(target))

    def test_build_target_image_encode(self):
        config = TransferConfig()
        config.config_path = "/tmp/config2.json"
        config.load_config_file()
        tests = (
            ("k8s.gcr.io/pause:3.1", "registry.cn-hangzhou.aliyuncs.com/lisong/pause:3.1"),
            ("nginx:1.14.2", "registry.cn-hangzhou.aliyuncs.com/lisong/nginx:1.14.2"),
            ("coredns/coredns:1.8.4", "registry.cn-hangzhou.aliyuncs.com/lisong/coredns:1.8.4"),
            ("quay.io/coreos/flannel:v0.11.0-amd64", "registry.cn-hangzhou.aliyuncs.com/lisong/flannel:v0.11.0-amd64"),
        )
        for source, expected in tests:
            target = build_target_image(config, source)

            print(target)
            self.assertTrue(str(target).startswith(expected))

    def test_build_source_image(self):
        config = TransferConfig()
        config.config_path = "/tmp/config3.json"
        config.load_config_file()
        tests = (
            ("k8s.gcr.io/pause:3.1", "registry.cn-hangzhou.aliyuncs.com/lisong/pause:3.1"),
            ("nginx:1.14.2", "registry.cn-hangzhou.aliyuncs.com/lisong/nginx:1.14.2"),
            ("coredns/coredns:1.8.4", "registry.cn-hangzhou.aliyuncs.com/lisong/coredns:1.8.4"),
            ("quay.io/coreos/flannel:v0.11.0-amd64", "registry.cn-hangzhou.aliyuncs.com/lisong/flannel:v0.11.0-amd64"),
        )
        for source, expected in tests:
            _source = build_jump_image(config, source)
            print(_source)
            self.assertTrue(str(_source).startswith(expected))


if __name__ == '__main__':
    unittest.main()
