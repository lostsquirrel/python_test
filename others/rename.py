import os
from pathlib import Path
import re

prefix_pattern = re.compile(r"【第\d+课】")


def main():
    c = Path()
    for x in c.iterdir():
        if x.is_file():
            print(x.name)
            cmd = rename(x.name)
            exec_cmd(cmd)


def exec_cmd(cmd: str):
    print(cmd)
    os.system(cmd)


def rename(s: str) -> str:
    serial, name = remove_serial(remove_suffix(remove_prefix(s)))
    suffix = get_suffix(s)

    new_name = f'{serial:03d}-{name}{suffix}'
    cmd = f'mv "{s}" "{new_name}"'
    return cmd


def get_suffix(name: str) -> str:
    return name[name.rindex("."):]


def remove_serial(name: str) -> (int, str):
    _name = name.split("-", 2)
    return int(_name[0]), _name[1]


def remove_prefix(name: str) -> str:
    return prefix_pattern.sub("", name)


def remove_suffix(name: str) -> str:
    return name[:name.index(".")]


if __name__ == '__main__':
    # name = "【第9课】09-计算机及网站服务器硬件-机箱-电源介绍01_.mp4.flv.avi"
    # print(remove_serial(remove_prefix(name)))
    # print(rename(name))
    # print(rename(name))
    # print(get_suffix(name))
    # print(remove_prefix(name))
    # print(remove_suffix(name))
    main()
