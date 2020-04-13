import os

import psutil

from DMClass import DmClass
from GameSetting import game_setting as gs


dm = DmClass()
DM = dm.register_dm()
DM.SetPath(os.path.join(os.getcwd(), 'orc'))
DM.SetShowErrorMsg(0)
DM.SetDict(0, "七战字库.txt")

pid_list = [proc.pid for proc in psutil.process_iter() if proc.name() == "七战.exe"]
DM.Delay(5000)
print(pid_list)
for i in range(len(pid_list)):
    window_handle = DM.FindWindowByProcessId(pid_list[i], "Internet Explorer_Server", "")
    print(window_handle)
    binds_params = gs.get("七战")
    ret = DM.BindWindowEx(window_handle, binds_params[0], binds_params[1], binds_params[2],
                          binds_params[3], binds_params[4])
    # DM.EnableRealMouse(1, 20, 30)
    DM.EnableRealKeypad(1)
    DM.SetWindowState(window_handle, 12)
    if ret == 1:
        print("网页绑定成功")
        DM.Delay(5000)
    else:
        raise NameError


day_pic = DM.FindPic(953, 836, 1005, 894, "背包.bmp", "050505", 0.8, 0)
print(day_pic)
if day_pic[0] != -1:
    print("进入游戏")

    # gift_ret = dm.find_str_fast(364, 102, 515, 208, "福利大厅", "000000-aaaaaa")
    # gao_ret = dm.find_str_fast(419, 490, 495, 560, "告", "000000-aaaaaa")
    # gong_ret = dm.find_str_fast(851, 175, 943, 260, "公", "b@000000-999999")

    # if gift_ret or gong_ret:
    #     ji_pin_ret = dm.find_str_fast(339, 417, 451, 502, "自动消失", "000000-aaaaaa")
    #     if ji_pin_ret is not None:
    #         DM.Delay(100)
    #         dm.left_click(ji_pin_ret[1]+123, ji_pin_ret[2]-190)
    #
    #     DM.Delay(300)
    #
    #     red_color = dm.find_color(659, 416, 717, 463, "A37E7A-5B7662", 0.9, 0)
    #     if red_color is not None:
    #         jing_ret = dm.find_str_fast(411, 348, 474, 390, "经", "b@000000-999999")
    #         if jing_ret is not None:
    #             print(jing_ret)
    #             dm.left_click(jing_ret[1], jing_ret[2])
    #             print("点击离线经验")
    #         DM.Delay(1000)
    #
    #     ling_qu_ret = dm.find_color(1139, 453, 1214, 478, "B49983-4B6470", 0.8, 0)
    #     if ling_qu_ret is not None:
    #         print(ling_qu_ret)
    #         dm.left_click(ling_qu_ret[1]+20, ling_qu_ret[2]+10, 0, 0)
    #         # DM.Delay(1000)
    #         # dm.left_click(1149, 465, 20, 5)
    #         print("点击领取离线经验")
    #
    #     DM.Delay(1000)
    #     true_ret = dm.find_color(789, 535, 819, 550, "6A3513-6A3514|AC6B23-0B0704|EAA341-041611|6A3513-6A3513", 0.9, 0)
    #     # true_ret = dm.find_pic(761,479,851,546, "离线确认.bmp")
    #     if true_ret is not None:
    #         print(true_ret)
    #         dm.left_click(true_ret[1], true_ret[2])
    #         print("点击确认领取离线经验")

        # red_color = dm.find_color(493, 396, 552, 438, "A37E7A-5B7662", 0.9, 0)
        # zi_yuan_ret = dm.find_pic(369, 391, 497, 468, "资源追回.bmp")
        # ji_pin_ret = dm.find_str_fast(339, 417, 451, 502, "自动消失", "000000-aaaaaa")
        # if ji_pin_ret is not None:
        #     DM.Delay(100)
        #     dm.left_click(ji_pin_ret[1] + 123, ji_pin_ret[2] - 190)
        # if red_color is not None:
        #     if zi_yuan_ret is not None:
        #         print(zi_yuan_ret)
        #         dm.left_click(zi_yuan_ret[1], zi_yuan_ret[2])
        #         print("点击资源追回")
        # DM.Delay(1000)
        # zhui_hui_ret = dm.find_color(974, 368, 1089, 399, "6A3513-6A3513|EFAD3A-0A150A", 0.8)
        # if zhui_hui_ret is not None:
        #     dm.left_click(zhui_hui_ret[1], zhui_hui_ret[2])
        #     DM.Delay(1000)
        # que_ren_ret = dm.find_color(696, 540, 774, 563, "6A3513-6A3513|D0923A-2E2F1B", 0.8, 0)
        # if que_ren_ret is not None:
        #     dm.left_click(que_ren_ret[1], que_ren_ret[2])
        #     DM.Delay(1000)

    free_yuan_bao = dm.find_color(1296, 824, 1328, 878, "FF0000-FFFFFF|CE8978-317672", 0.8, 0)
    if free_yuan_bao is not None:
        dm.left_click(free_yuan_bao[1], free_yuan_bao[2])
        DM.Delay(1000)
        today_happy_ret = dm.find_pic(346, 685, 423, 759, "今日活跃.bmp")
        if today_happy_ret is None:
            dm.left_click(free_yuan_bao[1], free_yuan_bao[2])




    DM.UnBindWindow()

else:
    print('没有进入游戏')
