import unittest
import winreg


def walk_key(h, pre_key):
    key_num, val_num, lu = winreg.QueryInfoKey(h)
    walk_value(h, val_num, pre_key)
    if key_num > 0:
        for x in range(key_num):
            try:
                sub_key = winreg.EnumKey(h, x)
                xk = winreg.OpenKey(h, sub_key, access=winreg.KEY_READ)
                walk_key(xk, r'{}\{}'.format(pre_key, sub_key))
            except Exception as e:
                # print(pre_key, e, x, key_num)
                pass


def walk_value(h, val_num, prefix):
    if val_num > 0:
        for y in range(val_num):
            name, value, reg_type = winreg.EnumValue(h, y)
            pattern = 'Graybox.OPC.DAWrapper'
            if pattern in name or pattern in str(value):
                print(prefix, name, value, reg_type)
                # print(winreg.DeleteValue(h, name))




if __name__ == '__main__':
    all = [
        ("HKEY_LOCAL_MACHINE", winreg.HKEY_LOCAL_MACHINE),
        ("HKEY_CURRENT_USER", winreg.HKEY_CURRENT_USER),
        ("HKEY_CLASSES_ROOT", winreg.HKEY_CLASSES_ROOT),
        ("HKEY_USERS", winreg.HKEY_USERS),
        ("HKEY_USERS", winreg.HKEY_CURRENT_CONFIG)
    ]
    for e in all:
        h = winreg.ConnectRegistry(None, e[1])

        walk_key(h, e[0])
        winreg.CloseKey(h)
