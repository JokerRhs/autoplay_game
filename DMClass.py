import os
import random
from ctypes import WinDLL

from win32com import client


class DmClass(object):
    def __init__(self):
        self.path = os.getcwd()
        self.DmReg_path = os.path.join(self.path, "DmReg.dll")
        self.dm_path = os.path.join(self.path, "dm.dll")
        with open("注册码.txt", 'r') as f:
            self.registration_code = f.read().strip()

    def register_dm(self):
        DmReg = WinDLL(self.DmReg_path)
        DmReg.SetDllPathW(self.dm_path, 0)
        self.DM = client.Dispatch("dm.dmsoft")
        ret = self.DM.Reg(self.registration_code, None)
        if ret in [1, 2, 3]:
            return self.DM
        else:
            return "失败"

    def left_click(self, x, y, xr=5, yr=5, delay=random.choice([100, 200, 300])):
        self.DM.MoveToEx(x, y, xr, yr)
        self.DM.Delay(delay)
        self.DM.LeftClick()
        self.DM.Delay(delay)

    def right_click(self, x, y, xr=5, yr=5, delay=random.choice([100, 200, 300])):
        self.DM.MoveToEx(x, y, xr, yr)
        self.DM.Delay(delay)
        self.DM.RightClick()

    def find_str_fast(self, x1, y1, x2, y2, string1, color_format, sim=0.9, num=10):
        print("开始查找:%s" % string1)
        for i in range(num):
            self.DM.Delay(500)
            res = self.DM.FindStrFast(x1, y1, x2, y2, string1, color_format, sim)
            if res[0] != -1:
                print("找到%s" % string1)
                return res
        print("没有找到:%s" % string1)
        return None

    def find_pic(self, x1, y1, x2, y2, pic_name, delta_color="050505", sim=0.9, dir1=0, num=10):
        print("开始查找:%s" % pic_name)
        for i in range(num):
            self.DM.Delay(500)
            res = self.DM.FindPic(x1, y1, x2, y2, pic_name, delta_color, sim, dir1)
            if res[0] != -1:
                print("找到%s" % pic_name)
                return res
        print("没有找到:%s" % pic_name)
        return None

    def find_color(self, x1, y1, x2, y2, color, sim=0.9, dir1=0, num=10):
        print("开始查找:%s" % color)
        for i in range(num):
            self.DM.Delay(500)
            res = self.DM.FindColor(x1, y1, x2, y2, color, sim, dir1)
            if res[0] != 0:
                print("找到%s" % color)
                return res
        print("没有找到:%s" % color)
        return None

if __name__ == '__main__':
    dm = DmClass()
    DM = dm.register_dm()
    print(DM)
