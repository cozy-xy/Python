from pywinauto import application
import pywinauto.mouse
from pywinauto.keyboard import send_keys
# import psutil
import time
from PIL import ImageGrab

# pywinauto.mouse.click(button='left', coords=(0, 0))

# pywinauto.mouse.double_click(button='left', coords=(0, 0))

# pywinauto.mouse.move(coords=(0, 0))

# pywinauto.mouse.press(button='left', coords=(0, 0))

# pywinauto.mouse.release(button='left', coords=(0, 0))
# pywinauto.mouse.right_click(coords=(0, 0))

# pywinauto.mouse.scroll(coords=(0, 0), wheel_dist=1)

# pywinauto.mouse.wheel_click(coords=(0, 0))


creator = application.Application(backend='uia').start('D:\\APP\\Creator\\NibiruCreator.exe')
time.sleep(20)
# creator['Diglog'].print_control_identifiers()   # 获取所有控件
main_window = creator.window(title="NibiruCreator", auto_id="NibiruMainWindow", control_type="Window")  # 主窗口
preview = creator.window(title="预览", auto_id="ScenePreviewWidget", control_type="Window")  # 预览窗户

# 测试项目需要在项目列表的第一个位置
pywinauto.mouse.double_click(button='left', coords=(552, 167))
time.sleep(5)
# creator['Diglog'].print_control_identifiers()
send_keys('{F5}')
time.sleep(1)
send_keys('{ESC}')
time.sleep(2)
send_keys('{F5}')
time.sleep(2)


# 使用psutil来判断
# def proc_exist(process_name):
#     pl = psutil.pids()
#     for pid in pl:
#         if psutil.Process(pid).name() == process_name:
#             return pid
#
#
# if isinstance(proc_exist('NibiruCreator.exe'), int):
#     print('NibiruCreator is running')
# else:
#     print('no such process...')


# 测试代码
for i in range(1, 1001):
    print("测试次数----------"+str(i))
    if main_window.exists():  # 如果主窗口存在，则执行切换操作
        # VR端
        pywinauto.mouse.click(button='left', coords=(894, 70))
        pywinauto.mouse.move(coords=(890, 90))
        pywinauto.mouse.click(button='left', coords=(890, 90))
        time.sleep(2)
        # 电脑端
        pywinauto.mouse.click(button='left', coords=(894, 70))
        pywinauto.mouse.move(coords=(895, 110))
        pywinauto.mouse.click(button='left', coords=(895, 110))
        time.sleep(2)
        # 手机端
        pywinauto.mouse.click(button='left', coords=(894, 70))
        pywinauto.mouse.move(coords=(894, 130))
        pywinauto.mouse.click(button='left', coords=(894, 130))
        time.sleep(2)
        # 电视端
        pywinauto.mouse.click(button='left', coords=(894, 70))
        pywinauto.mouse.move(coords=(893, 150))
        pywinauto.mouse.click(button='left', coords=(893, 150))
        time.sleep(2)
    else:
        img = ImageGrab.grab(bbox=(0,0,1920,1080))
        img.save('full_screen_img.jpg')
        print("\033[0;31m\tCreator发生崩溃！！！\033[0m")
        break

