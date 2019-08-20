# coding=utf-8
import gzip
import unittest


class Test(unittest.TestCase):

    def testGzip(self):
        target = "Packages.gz"
        content = ""
        with gzip.open(target, 'rb') as f:
            for line in f.readlines():
                # print(type(line))
                prefix = 'Filename: '
                line = line.decode()
                if line.startswith(prefix):
                    content += "+ "
                    content += line[len(prefix):]
        content += "- *\n"
        with open('Packages.include', 'w') as f:
            f.write(content)

    def testTree(self):
        package = "pool/restricted/b/bcmwl/bcmwl-kernel-source_6.30.223.248+bdcom-0ubuntu8_amd64.deb"
        while '/' in package:
            package = package[:package.rindex('/')]

            print(package)

    def testXz(self):
        target = '/data/backup/Packages.xz'
        import lzma
        with lzma.open(target, 'rb') as f:
            for line in f.readlines():
                print(line)
