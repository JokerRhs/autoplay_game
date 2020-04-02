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
DM.Delay(5000)
print(pid_list)
for i in range(len(pid_list)):
    window_handle = DM.FindWindowByProcessId(pid_list[i], "Internet Explorer_Server", "")
    print(window_handle)
    binds_params = gs.get("七战")
    ret = DM.BindWindowEx(window_handle, binds_params[0], binds_params[1], binds_params[2],
                          binds_params[3], binds_params[4])
    DM.EnableRealMouse(2, 20, 20)
    DM.EnableRealKeypad(1)
    if ret == 1:
        print("网页绑定成功")
        DM.Delay(5000)
    else:
        raise NameError

logout_ret = dm.find_str_fast(970, 317, 1056, 358, "注销", "000000-666666")
if logout_ret is not None:
    x = int(logout_ret[1])
    y = int(logout_ret[2])
    print("注销坐标: %d, %d" % (x, y))
    dm.left_click(x, y)
    DM.Delays(100, 300)
else:
    login_ret = dm.find_str_fast(970, 337, 1059, 374, "马", "FDEFE8-021017")
    x = int(login_ret[1])
    y = int(login_ret[2])
    print("登录坐标: %d, %d" % (x, y))

DM.EnableIme(0)  # 关闭输入法
num_res = dm.find_str_fast(996, 208, 1066, 258, "邮", "b@000000-999999")
password_res = dm.find_str_fast(993, 240, 1064, 289, "密", "b@000000-999999")
yan_res = dm.find_str_fast(948, 273, 1019, 317, "验", "b@000000-999999")
if None not in [num_res, password_res, yan_res]:
    dm.left_click(num_res[1], num_res[2], 0, 0)
    DM.Delay(300)
    DM.KeyPressStr("sab653333", 300)  # 账号
    DM.Delay(300)
    dm.left_click(password_res[1], password_res[2], 0, 0)
    DM.Delay(300)
    DM.KeyPressStr("sab653333", 300)  # 密码
    DM.Delay(300)
    dm.left_click(yan_res[1], yan_res[2], 0, 0)
    DM.Delays(20000, 25000)
else:
    dm.left_click(1018, 236, 0, 0)
    DM.Delay(300)
    DM.KeyPressStr("sab653333", 300)  # 账号
    DM.Delay(300)
    dm.left_click(1003, 265, 0, 0)
    DM.KeyPressStr("sab653333", 300)  # 密码
    DM.Delay(300)
    dm.left_click(996, 292, 0, 0)
    DM.Delays(20000, 25000)


out_str = dm.find_str_fast(928, 243, 990, 280, "近", "000000-666666")
if out_str != None:
    two_str = dm.find_str_fast(909, 267, 1004, 302, "双", "b@000000-999999")
    if two_str != None:
        two_x = int(two_str[1])
        two_y = int(two_str[2])
        dm.left_click(two_x+5, two_y+3, 0, 0)
        print("服务器坐标: %d, %d" % (two_x+5, two_y+3))
        DM.Delays(20000, 25000)
    else:
        dm.left_click(970, 287, 0, 0)
        DM.Delays(20000, 25000)
day_pic = DM.FindPic(953, 836, 1005, 894, "背包.bmp", "050505", 0.8, 0)
print(day_pic)
if day_pic[0] != -1:
    print("进入游戏")

    gift_ret = dm.find_str_fast(364, 102, 515, 208, "福利大厅", "000000-aaaaaa")
    gao_ret = dm.find_str_fast(419, 490, 495, 560, "告", "000000-aaaaaa")
    gong_ret = dm.find_str_fast(851, 175, 943, 260, "公", "b@000000-999999")

    if gift_ret or gao_ret or gong_ret:
        ji_pin_ret = dm.find_str_fast(339, 417, 451, 502, "自动消失", "000000-aaaaaa")
        if ji_pin_ret is not None:
            DM.Delay(100)
            dm.left_click(ji_pin_ret[1]+123, ji_pin_ret[2]-190)

        DM.Delay(300)
        DM.FindColorEx(659, 416, 717, 463, "3C30F3|5A59F4", 0.9, 0)
        red_color = dm.find_color_ex(659, 416, 717, 463, "3C30F3|5A59F4", 0.9, 0)
        if red_color is not None:
            jing_ret = dm.find_str_fast(411, 348, 474, 390, "经", "b@000000-999999")
            if jing_ret is not None:
                print(jing_ret)
                dm.left_click(jing_ret[1], jing_ret[2])
                print("点击离线经验")
            DM.Delays(1000, 3000)

        ling_qu_ret = dm.find_color_ex(1297, 564, 1385, 599, "3DCBF7|36A5F5|15396F", 0.9, 0)
        if ling_qu_ret is not None:
            print(ling_qu_ret)
            dm.left_click(ling_qu_ret[1], ling_qu_ret[2])
            print("点击领取离线经验")

        DM.Delay(1000)
        true_ret = dm.find_color_ex(919, 607, 1016, 647, "13356F|39B1F3|A4FCFC|9AF0FE", 0.9, 0)
        if true_ret is not None:
            print(true_ret)
            dm.left_click(true_ret[1], true_ret[2])
            print("点击确认领取离线经验")
        # mian_ret = dm.find_str_fast(1119, 468, 1197, 527, "免", "b@000000-bbbbbb", 1.0)
        # free_ret = dm.find_pic(1086, 424, 1197, 514, "50.bmp", "050505", 0.8, 0)
        # if mian_ret is not None:
        #     pass
        # if free_ret is not None:
        #     print(free_ret)
        #     dm.left_click(free_ret[1], free_ret[2])
        #     print("点击领取离线经验")

        # FindColor
        # 659, 416, 717, 463, "4F49FA", intX, intY
        #
        # FindColorEx
        # 633, 360, 670, 400, "CCECF9", 0, 0.7, intX, intY



        sign_ret = dm.find_pic(501, 307, 541, 343, "红点.bmp", "050505", 0.9, 0)
        if sign_ret is not None:
            print(sign_ret)
            ji_pin_ret = dm.find_str_fast(339, 417, 451, 502, "自动消失", "000000-aaaaaa")
            if ji_pin_ret is not None:
                close_ret = dm.find_pic(414, 158, 503, 218, "极品掉落关闭.bmp", "050505", 0.8, 0)
                if close_ret is not None:
                    DM.Delay(100)
                    dm.left_click(close_ret[1], close_ret[2])
                else:
                    dm.left_click(488, 266)
            DM.Delays(1000, 2000)
            # login_out_ret = dm.find_str_fast(365, 455, 412, 469, "自动消失", "000000-aaaaaa")

        else:
            pass
    else:
        pass



    # close_ret = dm.find_pic(1217, 163, 1307, 236, "关闭按钮.bmp", "050505", 0.9, 0)
    # DM.Delays(1000, 3000)
    # if close_ret is not None:
    #     print(close_ret)
    #     dm.left_click(close_ret[1], close_ret[2])
    #     print("点击关闭福利大厅")
    #
    # DM.Delays(1000, 3000)
    #
    # recharge_ret = dm.find_pic(658, 272, 723, 336, "首充大礼的可.bmp", "050505", 0.9, 0)
    # if recharge_ret is not None:
    #     recharge_ret = dm.find_pic(1248, 240, 1308, 296, "首充大礼的关闭按钮.bmp", "050505", 0.8, 0)
    #     DM.Delays(1000, 3000)
    #     if recharge_ret is not None:
    #         print(recharge_ret)
    #         dm.left_click(recharge_ret[1], recharge_ret[2])
    #         print("点击关闭首充大礼")
    # DM.Delays(1000, 3000)
    #
    # free_ret = dm.find_pic(1272, 816, 1362, 866, "免费元宝.bmp", "050505", 0.8, 0)
    # if free_ret is not None:
    #     DM.Delays(1000, 3000)
    #     print(free_ret)
    #     dm.left_click(free_ret[1], free_ret[2])
    #     print("打开免费元宝")
    #
    # yuanbao_ret = dm.find_pic(333, 223, 1045, 659, "元宝矿1.bmp", "050505", 0.8, 0)
    # if yuanbao_ret is not None:
    #     DM.Delays(1000, 3000)
    #     print(yuanbao_ret)
    #     dm.left_click(yuanbao_ret[1], yuanbao_ret[2])
    #     print("点击元宝矿")
    DM.UnBindWindow()

else:
    print('没有进入游戏')













