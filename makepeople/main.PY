import ctypes
import os
import threading
from playsound import playsound
import time

def set_wallpaper_and_play_sound(image_path, sound_path):
    # 使用 ctypes 調用 Windows API 更改桌面背景
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    # 播放聲音
    playsound(sound_path)

for i in range(1,7):
    print(i)

    # 設定圖片路徑
    image_path = rf"assets/{i}.jpg"
    if not os.path.isabs(image_path):
        image_path = os.path.abspath(image_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    # 設定聲音路徑
    sound_path = rf"assets/{i}.wav"
    if not os.path.isabs(sound_path):
        sound_path = os.path.abspath(sound_path)
    
    # 使用執行緒同時設置壁紙並播放聲音
    thread = threading.Thread(target=set_wallpaper_and_play_sound, args=(image_path, sound_path))
    thread.start()
    thread.join()  # 等待執行緒完成

    # 如果需要在每次更換之間添加延遲
    time.sleep(0.5)  # 延遲 1 秒