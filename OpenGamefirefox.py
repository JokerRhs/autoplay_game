import os
import time
import webbrowser as web

from DMClass import DmClass
from GameSetting import game_setting as gs


dm = DmClass()
DM = dm.register_dm()
DM.SetPath(os.path.join(os.getcwd(), ''))


class AutoLogin(object):

    def __init__(self):
        self.id_handle_dict = {}
        self.chrome_path = r"D:\火狐游览器\firefox.exe"
        self.window_handle = None
        self.window_process_id = None

    def open_window(self, url):
        web.register('firefox', None, web.BackgroundBrowser(self.chrome_path))
        web.get('firefox').open(url=url)

    def bind_window(self, game_name):
        binds_params = gs.get(game_name)
        self.window_handle = DM.FindWindowSuper('MozillaWindowClass', 2, 0, game_name, 0, 1)
        print(self.window_handle)
        self.window_process_id = DM.GetWindowProcessId(self.window_handle)
        self.id_handle_dict[self.window_process_id] = self.window_handle
        DM.BindWindowEx(self.window_handle, binds_params[0], binds_params[1], binds_params[2],
                        binds_params[3], binds_params[4])
        DM.SetWindowState(self.window_handle, 4)

    @staticmethod
    def login_auto(number, password):
        DM.EnableIme(0)  # 关闭输入法
        DM.EnableRealMouse(2, 20, 20)
        DM.EnableRealKeypad(1)
        DM.MoveToEx(1210, 339, 90, 5)
        DM.LeftClick()
        DM.Delays(100, 300)
        DM.KeyPressStr(number, 300)  # 账号
        DM.KeyDown(9)
        DM.Delays(100, 200)
        DM.KeyUp(9)
        DM.KeyPressStr(password, 300)  # 密码
        DM.KeyDown(9)
        DM.Delays(100, 200)
        DM.KeyUp(9)

    @staticmethod
    def unbind_window():
        DM.UnBindWindow()

    @staticmethod
    def click_login():
        DM.MoveToEx(1173, 450, 5, 5)
        DM.LeftClick()

    @staticmethod
    def detection_error():
        return DM.GetAveRGB(1130, 303, 1233, 326)


def click_sever():
    DM.Delays(100, 300)
    DM.MoveTo(1125, 418)
    DM.LeftClick()


def flash_true():
    DM.Delays(100, 300)
    DM.MoveTo(314, 60)
    DM.LeftClick()
    DM.Delays(100, 300)
    DM.MoveToEx(383, 156, 100, 5)
    DM.LeftClick()


if __name__ == '__main__':
    login_shell = AutoLogin()
    url = r'https://wan.liebao.cn/qizhan/server_list.html'
    login_shell.open_window(url)
    time.sleep(3)
    login_shell.bind_window(list(gs.keys())[0])
    rgb1 = login_shell.detection_error()

    with open('账号密码.txt', 'r') as f:
        num_pw = f.read()
    num = num_pw.split(';')[0]
    login_shell.login_auto(num, num)
    time.sleep(15)
    login_shell.click_login()
    rgb2 = login_shell.detection_error()
    if rgb1 != rgb2:
        time.sleep(20)
        login_shell.click_login()

    click_sever()
    flash_true()

    login_shell.unbind_window()






