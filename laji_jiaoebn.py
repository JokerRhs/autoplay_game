#
# id_handle_dict = {}
# chromepath = r"D:\火狐游览器\firefox.exe"
# web.register('firefox', None, web.BackgroundBrowser(chromepath))
# web.get('firefox').open(r'https://wan.liebao.cn/qizhan/server_list.html')
#
# dm = DmClass()
# DM = dm.register_Dm()
# window_handle = DM.FindWindowSuper('MozillaWindowClass', 2, 0, '七战', 0, 1)
# window_process_id = DM.GetWindowProcessId(window_handle)
# id_handle_dict[window_process_id] = window_handle
#
# DM.BindWindowEx(window_handle, "gdi", "windows", "windows", "dx.public.active.api|dx.public.active.message", 101)
# DM.SetWindowState(window_handle, 4)
#
# DM.EnableIme(0)  # 关闭输入法
# DM.EnableRealMouse(2, 20, 20)
# DM.EnableRealKeypad(1)
# DM.MoveToEx(1210, 339, 90, 5)
# DM.LeftClick()
# DM.Delays(100, 300)
# DM.KeyPressStr('sab653333', 300)  # 账号
# DM.KeyDown(9)
# DM.Delays(100, 200)
# DM.KeyUp(9)
# DM.KeyPressStr('sab653333', 300)  # 密码
# DM.KeyDown(9)
# DM.Delays(100, 200)
# DM.KeyUp(9)
# time.sleep(15)  # 验证码
#
# DM.MoveToEx(1173, 450, 5, 5)
# DM.LeftClick()
#
# a = r'https://wan.liebao.cn/qizhan/server_list.html'
#
# print(id_handle_dict)
# DM.UnBindWindow()