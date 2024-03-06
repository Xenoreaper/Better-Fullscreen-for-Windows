"""
Better Fullscreen for Windows (bffw.py)

This program provides improved fullscreen functionality for Windows.
It automatically moves fullscreen applications to separate virtual desktops and moves them back when leaving fullscreen mode.

Author: Xenoreaper
Version: 0.1.3
Last Modified: 2024-03-05
License: MIT

Includes:
- VirtualDesktopAccessor.dll
    Author: Ciantic
    License: MIT
"""

import ctypes
import win32gui
import keyboard

c_bool = ctypes.c_bool
c_int = ctypes.c_int
#vda = ctypes.WinDLL("./VirtualDesktopAccessor.dll") # Load the DLL in cmd
vda = ctypes.WinDLL(".\\Better Fullscreen for Windows\\VirtualDesktopAccessor.dll") # Load the DLL in vsc
user32 = ctypes.windll.user32
user32.SetProcessDPIAware() # optional, makes functions return real pixel numbers instead of scaled values

full_screen_rect = (0, 0, user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))

window_handles = [] # list of window handles
window_desktops = [] # list of desktop numbers for each windowq

def get_full_screen_window_name(): # find the name of a fullscreen window
    def callback(hWnd, windows):
        try:
            rect = win32gui.GetWindowRect(hWnd)
            title = win32gui.GetWindowText(hWnd)
            if rect == full_screen_rect and title != "Windows Input Experience":
                windows.append(title)
        except:
            pass
    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows[0] if windows else None

def get_full_screen_window_handle(): # get handle of fullscreen window
    def callback(hWnd, windows):
        try:
            rect = win32gui.GetWindowRect(hWnd)
            title = win32gui.GetWindowText(hWnd)
            if rect == full_screen_rect and title != "Windows Input Experience" and title != "Program Manager":
                windows.append(hWnd)
        except:
            pass
    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows[0] if windows else None

def is_fullscreen(hwnd): # check if specific window is fullscreen
    rect = win32gui.GetWindowRect(hwnd)

    if rect == full_screen_rect:
        return True
    elif rect != full_screen_rect:
        return False
    else:
        return -1

def move_window(window, desktop): # to move create a desktop, move the window, go to it and remember it
    vda.CreateDesktop()
    vda.MoveWindowToDesktopNumber(window, desktop)
    vda.GoToDesktopNumber(desktop)
    window_handles.append(window)

def remove_desktop(desktop): # remove desktop and remove window from list
    vda.RemoveDesktop(desktop, 0)
    window_handles.remove(window_handles[desktop-1])

def force_remove_desktops(): # indiscriminately remove all desktops and clear the window list (probably a stump)
    for desktop in range(vda.GetDesktopCount()):
        vda.RemoveDesktop(desktop, 0)
    window_handles.clear()

prev_window_handle = 0
prev_window_name = "void"

while True:
    desktop_count = vda.GetDesktopCount()
    window_name = get_full_screen_window_name()
    window_handle = get_full_screen_window_handle()

    if prev_window_name == window_name and prev_window_handle != window_handle: # if window behaves weirdly remember it's the same window
        prev_equal = True
    else:
        prev_equal = False

    if None == window_handle or window_name == "" or window_name == "Virtual desktop hotkey switching preview" or prev_equal == True: # ignore certain windows
        ignored_window = True
    else:
        ignored_window = False

    print(vda.GetCurrentDesktopNumber())
    
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift') and keyboard.is_pressed('F11'): # close program
        force_remove_desktops()
        print("quitting")
        break
    elif window_handle not in window_handles and ignored_window == False: # if window is not in list, move it to a new desktop
        move_window(window_handle, desktop_count)
        print("window: " + str(window_handle) + " moved to desktop: " + str(desktop_count))
    elif desktop_count > len(window_handles)+1: # if desktop count is higher than window count, add None to window list (new desktop gets removed immediately after creation)
        window_handles.append(None)
    else: # if window is in list, check if it's still fullscreen and where it belongs
        for x in range(desktop_count-1):
            print("> " + str(vda.IsWindowOnDesktopNumber(window_handles[x], x+1)))
            try:
                if is_fullscreen(window_handles[x]) == False: # if window is not fullscreen, remove its desktop
                    print("removing desktop: " + str(x+1))
                    remove_desktop(x+1)
                    break
            except: # if window is not found, remove its desktop
                remove_desktop(x+1)
                break
        continue

    prev_window_handle = window_handle
    prev_window_name = window_name
