import os

from PIL import ImageGrab


img = ImageGrab.grab(bbox=(0,0,1920,1080))
img.save('full_screen_img.jpg')
# img = ImageGrab.grab()
# img.save('1.jpg')  # 保存在当前py文件同一层目录下
# img.save(r'E:\1.jpg')  # 保存在指定目录下，绝对路径
# picDir = 'E:\\'
# img.save(os.path.join(picDir, '1.jpg'))  # 保存在指定目录下，相对路径