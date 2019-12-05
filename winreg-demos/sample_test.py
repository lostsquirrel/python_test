# coding=utf-8
import unittest
import winreg

from simple import walk_key


class MyTestCase(unittest.TestCase):

    def test_connect(self):
        all = [
            ("HKEY_LOCAL_MACHINE", winreg.HKEY_LOCAL_MACHINE),
            ("HKEY_CURRENT_USER", winreg.HKEY_CURRENT_USER),
            ("HKEY_CLASSES_ROOT", winreg.HKEY_CLASSES_ROOT)
        ]
        e = all[0]
        h = winreg.ConnectRegistry(None, e[1])

        walk_key(h, e[0])
        winreg.CloseKey(h)

    def test_something(self):
        self.assertEqual(True, False)

    def test_delete(self):
        h = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        k = winreg.OpenKeyEx(h, r"SOFTWARE\Classes\.htm\OpenWithProgIds", access=winreg.KEY_SET_VALUE)
        winreg.DeleteValue(k, "2345ExplorerHTML")
        winreg.FlushKey()
        winreg.CloseKey(h)

    def test_read_target_key(self):
        h = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        k = winreg.OpenKeyEx(h, r"SOFTWARE\Classes\.htm\OpenWithProgIds")
        key_num, val_num, lu = winreg.QueryInfoKey(k)
        print(key_num, val_num, lu)
        if val_num > 0:
            for y in range(val_num):
                name, value, reg_type = winreg.EnumValue(k, y)
                print(name, value, reg_type, y, val_num)
        winreg.CloseKey(h)


if __name__ == '__main__':
    unittest.main()
