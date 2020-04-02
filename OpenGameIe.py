import os
import time
import webbrowser as web

import psutil

from DMClass import DmClass
from GameSetting import game_setting as gs


dm = DmClass()
DM = dm.register_dm()
DM.SetPath(os.path.join(os.getcwd(), 'orc'))
DM.SetShowErrorMsg(0)
DM.SetDict(0, "七战字库.txt")


app = DM.RunApp(os.path.join(os.getcwd(), '七战.exe'), 0)
if app == 1:
    pass
else:
    pass


pid_list = [proc.pid for proc in psutil.process_iter() if proc.name() == "七战.exe"]
print(pid_list)
handles = DM.EnumWindowByProcessId(pid_list[0], "", "WTWindow", 2+8)
handles_list = handles.split(",")
print(handles_list)
game_handle = DM.FindWindowEx(handles_list[0], "", "")
print(game_handle)
binds_params = gs.get("七战")
ret = DM.BindWindowEx(game_handle, binds_params[0], binds_params[1], binds_params[2],
                binds_params[3], binds_params[4])
DM.EnableRealMouse(2, 20, 20)
DM.EnableRealKeypad(1)

if ret == 1:
    print("网页绑定成功")
    time.sleep(5)
else:
    raise NameError

# logout_ret = dm.find_str_fast(970, 317, 1056, 358, "注销", "000000-666666")
# if logout_ret is not None:
#     x = int(logout_ret[1])
#     y = int(logout_ret[2])
#     print("注销坐标: %d, %d" % (x, y))
#     dm.left_click(x, y)
#     time.sleep(3)
# else:
#     login_ret = dm.find_str_fast(970, 337, 1059, 374, "马", "FDEFE8-021017")
#     x = int(login_ret[1])
#     y = int(login_ret[2])
#     print("登录坐标: %d, %d" % (x, y))
# time.sleep(30)
out_str = dm.find_str_fast(940, 254, 1041, 271, "近", "000000-666666")
if out_str != None:
    two_str = dm.find_str_fast(942, 281, 994, 293, "双", "b@000000-999999")
    if two_str != None:
        two_x = int(two_str[1])
        two_y = int(two_str[2])
        dm.left_click(two_x+5, two_y+3, 0, 0)
        print("服务器坐标: %d, %d" % (two_x, two_y))
        DM.Delays(20000, 25000)
    else:
        dm.left_click(967, 287, 0, 0)
        DM.Delays(20000, 25000)
day_pic = DM.FindPic(945, 790, 1019, 866, "背包.bmp", "050505", 0.8, 0)
print(day_pic)
if day_pic[0] != -1:
    print("进入游戏")

else:
    print('没有进入游戏')

DM.UnBindWindow()











