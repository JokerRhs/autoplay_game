import random
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver


__browser_url = r'C:\Users\Administrator.USER-20191006KT\AppData\Roaming\360se6\Application\360se.exe'  ##360浏览器的地址
chrome_options = Options()
chrome_options.binary_location = __browser_url
executable_path = r"D:\python解释器3.68\chromedriver.exe"
user_data_default = r'--user-data-dir=c:\users\administrator.user-20191006kt\appdata\roaming\360se6\User Data'
chrome_options.add_argument(user_data_default)
driver = webdriver.Chrome(executable_path, chrome_options=chrome_options)
# driver.implicitly_wait(time.sleep(random.randint(1,3)))
driver.get('https://wan.liebao.cn/qizhan/')
driver.maximize_window()







