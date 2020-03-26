import os
from ctypes import WinDLL

from win32com import client


class DmClass(object):
    def __init__(self):
        self.path = os.getcwd()
        self.DmReg_path = os.path.join(self.path, "DmReg.dll")
        self.dm_path = os.path.join(self.path, "dm.dll")
        with open("注册码.txt", 'r') as f:
            self.registration_code = f.read().strip()

    def register_Dm(self):
        DmReg = WinDLL(self.DmReg_path)
        DmReg.SetDllPathW(self.dm_path, 0)
        DM = client.Dispatch("dm.dmsoft")
        ret = DM.Reg(self.registration_code, None)
        if ret in [1,2,3]:
            return DM
        else:
            return "失败"


if __name__ == '__main__':
    dm = DmClass()
    DM = dm.register_Dm()
    print(DM)