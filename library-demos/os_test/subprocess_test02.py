

import logging
from subprocess import PIPE, Popen

log = logging.getLogger(__name__)
if __name__ == '__main__':

    with Popen(["tail", "-f", "/tmp/test"], stdout=PIPE, stderr=PIPE, shell=True) as proc:
        # print(proc.stdout)
        print(proc.stdout.read())
