#!/usr/bin/python3
import os
import sys


def get_suffix(name: str) -> str:
    return name.split(".")[-1]


def get_prefix(name: str) -> str:
    return name.split("|")[0]


if __name__ == '__main__':
    args = sys.argv
    name = args[1]
    target = args[2]
    cmd = "ffmpeg -i '{}' -codec copy {}.{}".format(name, target, get_suffix(name))
    print(cmd)
    os.system(cmd)
