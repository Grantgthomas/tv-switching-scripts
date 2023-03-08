import time
import pyautogui
import subprocess
import psutil
import win32con
import win32api
import win32gui



def switch_display_1():
    if check_disp() == 2:
        for x in range(2):
            pyautogui.hotkey('win', 'p')
            time.sleep(.1)
        pyautogui.hotkey('enter')
        set_resolution(2, 2560, 1440)
        time.sleep(.1)
        pyautogui.hotkey('escsape')
        time.sleep(.1)
        monitor_script()
    else:
        pass



def switch_display_2():
    if check_disp() == 1:
        for x in range(4):
            pyautogui.hotkey('win', 'p')
            time.sleep(.1)
        pyautogui.hotkey('enter')
        set_resolution(2, 3840, 2160)
        time.sleep(.1)
        tv_script()
        #stop_process('Rainmeter')
        #stop_process('wallpaper32')
        #time.sleep(.1)
        #pyautogui.hotkey('escape')
    else:
        pass
    


def set_resolution(display_num, width, height):
    # Use the subprocess module to run the command to set the display resolution
    try:
        subprocess.run('.\Qres\QRes.exe /x:{} /y:{} /c:32 /r:60 /d:{}'.format(width,height,display_num))
    finally:
        pass

def stop_process(process_name):
    # Use the subprocess module to run the command to stop the specified process
    subprocess.call(f'taskkill /f /im {process_name}.exe', shell=True)

def check_procs(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

#check which display is running by resolution
def check_disp():
    all_monitors = win32api.EnumDisplayMonitors()
    xres = all_monitors[0][2]
    if xres[3] == 1440:
       return 1
    if xres[3] == 2160:
        return 2
    return 0

def tv_script():
    subprocess.call('TVMode.bat')

def monitor_script():
    subprocess.call('MonitorMode.bat')