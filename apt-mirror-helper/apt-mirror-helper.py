# coding=utf-8
import os
import sys
import gzip
import lzma
import logging

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger(__name__)

local_prefix = '/data/apt-mirror/mirror/mirrors.ustc.edu.cn'
# remote_prefix = 'rsync://rsync.mirrors.ustc.edu.cn/repo'
remote_prefix = 'rsync://mirrors.tuna.tsinghua.edu.cn'
include_file_name = 'Packages.include'
debian_stable_release = "buster"


def download_package_index(index_dir_x):
    source = os.path.join(remote_prefix, index_dir_x)
    target = os.path.join(local_prefix, index_dir_x)
    rsync_download(source, target)


def download_dist_index():
    source = os.path.join(remote_prefix, dist_name, "dists", dist_version)
    target = os.path.join(local_prefix, dist_name, "dists", dist_version)
    ext_params = "--filter='- */' --filter='+ *'"
    rsync_download(source, target, ext_params)
    if "debian" == dist_name:
        if debian_stable_release == dist_version:
            source = os.path.join(remote_prefix, dist_name, "zzz-dists", "stable")
        else:
            source = os.path.join(remote_prefix, dist_name, "zzz-dists", dist_version)
        rsync_download(source, target, ext_params)


def download_i18n():
    source = os.path.join(remote_prefix, dist_name, "dists", dist_version, pkg_type, "i18n")
    target = os.path.join(local_prefix, dist_name, "dists", dist_version, pkg_type, "i18n")
    rsync_download(source, target)


def download_dep11():
    source = os.path.join(remote_prefix, dist_name, "dists", dist_version, pkg_type, "dep11")
    target = os.path.join(local_prefix, dist_name, "dists", dist_version, pkg_type, "dep11")

    rsync_download(source, target)


def download_source():
    source = os.path.join(remote_prefix, dist_name, "dists", dist_version, pkg_type, "source")
    target = os.path.join(local_prefix, dist_name, "dists", dist_version, pkg_type, "source")
    rsync_download(source, target)


def read_package_index(index_dir):
    if dry_run:
        return
    content = ""
    dir_tree = dict()
    dir_set = set()
    target = os.path.join(local_prefix, index_dir, 'Packages.gz')
    f = None
    try:
        if os.path.exists(target):
            f = gzip.open(target, 'rb')
        else:
            target = os.path.join(local_prefix, index_dir, 'Packages.xz')
            f = lzma.open(target)
        for line in f.readlines():
            # print(type(line))
            prefix = 'Filename: '
            line = line.decode()
            if line.startswith(prefix):
                package = line[len(prefix):]
                content += "+ {}".format(package)
                while '/' in package:
                    package = package[:package.rindex('/')]
                    dir_set.add(package)
    finally:
        if f is not None:
            f.close()

    dir_rule = ''
    for d in dir_set:
        dir_rule += '+ {}\n'.format(d)
    dir_rule += content
    dir_rule += "- *\n"

    include_file = os.path.join(local_prefix, index_dir, include_file_name)
    with open(include_file, 'w') as f:
        f.write(dir_rule)


def parse_packages(package_file):
    packages = []
    with open(package_file) as fh:
        for line in fh.readlines():
            prefix = 'Filename: '
            if line.startswith(prefix):
                packages.append(line[len(prefix):])
    return packages


def download_packages(index_dir):
    log.info('dry_run {}'.format(dry_run))
    include_file = os.path.join(local_prefix, index_dir, include_file_name)
    source = os.path.join(remote_prefix, dist_name)
    target = os.path.join(local_prefix, dist_name)
    ext_param = '--include-from={}'.format(include_file)
    rsync_download(source, target, ext_param)


def rsync_download(source, target, ext_params=""):
    download_cmd = '''rsync \
    --recursive \
    --links \
    --perms \
    --times \
    --compress \
    --progress \
    --contimeout=600 \
    --timeout=600 \
     {} \
     {}/ \
     {}/'''.format(
        ext_params,
        source.strip(),
        target.strip())
    log.info(download_cmd)
    if not dry_run:
        os.system("mkdir -p {}".format(target))
        try:
            os.system(download_cmd)
            log.info('executed {}'.format(download_cmd))
        except Exception as e:
            log.error(e)


if __name__ == '__main__':
    params = sys.argv
    dry_run = True
    log.info(params)
    # sys.exit(0)
    if len(params) == 2:
        dry_run = False
    arch = 'amd64'
    plan = {
        "ubuntu": {
            "xenial": {
                "main": ["amd64", "i386"],
                "universe": ["amd64"],
                "multiverse": ["amd64"],
                "restricted": ["amd64"]
            },
            "xenial-updates": {
                "main": ["amd64"],
                "universe": ["amd64"],
                "multiverse": ["amd64"],
                "restricted": ["amd64"]
            },

            "xenial-backports": {
                "main": ["amd64", "i386"],
                "universe": ["amd64"],
                "multiverse": ["amd64"],
                "restricted": ["amd64"]
            },

            "xenial-security": {
                "main": ["amd64"],
                "universe": ["amd64"],
                "multiverse": ["amd64"],
                "restricted": ["amd64"]
            }
        },
        "debian": {
            "stretch": {
                "main": ["amd64"],
                "non-free": ["amd64"],
                "contrib": ["amd64"]
            },
            "stretch-updates": {
                "main": ["amd64"],
                "non-free": ["amd64"],
                "contrib": ["amd64"]
            },
            "stretch-proposed-updates": {
                "main": ["amd64"],
                "non-free": ["amd64"],
                "contrib": ["amd64"]
            },
            "stretch-backports": {
                "main": ["amd64"],
                "non-free": ["amd64"],
                "contrib": ["amd64"]
            },
            "stretch-backports-sloppy": {
                "main": ["amd64"],
                "non-free": ["amd64"],
                "contrib": ["amd64"]
            },
            "buster": {
                "main": ["amd64"],
                "non-free": ["amd64"],
                "contrib": ["amd64"]
            },
            "buster-updates": {
                "main": ["amd64"],
                "non-free": ["amd64"],
                "contrib": ["amd64"]
            },
            "buster-proposed-updates": {
                "main": ["amd64"],
                "non-free": ["amd64"],
                "contrib": ["amd64"]
            },
            "buster-backports": {
                "main": ["amd64"],
                "non-free": ["amd64"],
                "contrib": ["amd64"]
            }
        }
    }
    for dist_name, dist_versions in plan.items():
        for dist_version, pkg_types in dist_versions.items():
            download_dist_index()
            for pkg_type, arches in pkg_types.items():
                download_i18n()
                download_dep11()
                download_source()
                for arch in arches:
                    pass
                    index_dir = os.path.join(dist_name, 'dists/{}/{}/binary-{}'.format(dist_version, pkg_type, arch))
                    download_package_index(index_dir)
                    read_package_index(index_dir)
                    download_packages(index_dir)
