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

#def is_fullscreen(hwnd): # check if specific window is fullscreen
#    window_rect = win32gui.GetWindowRect(hwnd)
#
#    return full_screen_rect == window_rect

counter = 1

def move_window(window, desktop):
    vda.CreateDesktop()
    vda.MoveWindowToDesktopNumber(window, desktop)
    vda.GoToDesktopNumber(desktop)
    window_handles.append(window)
    #window_desktops.append(desktop)
    
    #vda.MoveWindowToDesktopNumber(window, desktop)
    #print(vda.MoveWindowToDesktopNumber(window, desktop))

def remove_desktop(desktop):
    vda.RemoveDesktop(desktop, 0)
    window_handles.remove(window_handles[desktop-1])
    #window_desktops.remove(window_desktops[desktop-1])

def force_remove_desktop(desktop):
    vda.RemoveDesktop(desktop, 0)
    window_handles.clear()

'''
while True:
    print(get_full_screen_window_handle())
    window_name = get_full_screen_window_name()
    window_handle = get_full_screen_window_handle()
    if counter == 0 and window_name: # check for fullscreen window and create desktop to move it to
        print(window_name + " --- " + str(window_handle))
        move_window(window_handle, desktop_count)
        counter += 1 # no real purpose yet
    #if counter == 1 and not is_fullscreen(window_handle): # check for window and remove desktop
    #    vda.RemoveDesktop(1, 0)
    if keyboard.is_pressed('q'): # close program
        break
    if keyboard.is_pressed('r'):
        print(str(window_handles[0]) + " --- " + str(window_desktops[0]))
    #if keyboard.is_pressed('w'):
    #    vda.MoveWindowToDesktopNumber(942213360, 1)
    #    print(vda.MoveWindowToDesktopNumber(942213360, 1))
    #if keyboard.on_press('e'):
    #    vda.MoveWindowToDesktopNumber(1444846, 1)
    #    print(vda.MoveWindowToDesktopNumber(1444846, 1))
    if keyboard.is_pressed('w'):
        vda.RemoveDesktop(1, 0)
    #keyboard.on_press_key('e', move_window(window_handle, 1))
'''
        
# if fullscreen: create desktop and move window to it
# if not fullscreen: remove desktop (and move window to desktop 1 if it still exists)
# if multiple fullscreen applications: create and move to seperate desktops
# if application is closed: remove corresponding desktop
# remember fullscreen applications and their desktops
        # 2d array with window handle and desktop number
# set desktop name to application name

# function: get name from handle
# replaces win+tab?

### handles do not stay the same when PC is restarted!!!
        
# check for fullscreen windows
# get window handle
# move window to new desktop 1
# remember window handle and according desktop
# check for fullscreen windows
 # if known is not: remove desktop and fall back to desktop 0
 #if new is found: move to new desktop 2
# repeat

# example
# window_handles = [<steam>, <firefox>, <game>]
# window_desktops = [1, 2, 3]
# desktop_count = 4
'''        
        for x in window_handles:
            if window_handles[x] == window_handle:
                if vda.GetCurrentDesktopNumber() == x+1:
                    vda.RemoveDesktop(1, 0)

            # window_handles[0] = <steam> == <steam>
                # desktop = 1 == 0+1 and 
'''

prev_window_handle = [0,0]
prev_window_name = ["void", "void"]

while True:
    desktop_count = vda.GetDesktopCount()
    window_name = get_full_screen_window_name()
    window_handle = get_full_screen_window_handle()

    
    if None == window_handle or window_name == "" or window_name == "Virtual desktop hotkey switching preview":
        ignored_window = True
        print("ignored window")
    else:
        ignored_window = False
        print(str(window_name) + " --- " + str(window_handle) + " <<< " + str(prev_window_name[0]) + " --- " + str(prev_window_handle[0]))
        print(str(vda.GetCurrentDesktopNumber()) + " | " + str(vda.GetCurrentDesktopNumber()+1) + " of " + str(desktop_count))

    if prev_window_name[0] == window_name:
        print("same name")

    if prev_window_name[0] == window_name and prev_window_handle[0] != window_handle:
        print("window error")
        prev_equal = True
        if vda.GetCurrentDesktopNumber() != 0:
            for x in range(len(window_handles)):
                if window_handles[x] == window_handle:
                    window_handles.remove(window_handles[x])
    else:
        prev_equal = False

    
    #print(for x in range(len(window_handles)): if window_handles[x] == window_handle: vda.IsWindowOnDesktopNumber(window_handle, x))

    if keyboard.is_pressed('q'): # close program
        break
    elif keyboard.is_pressed('w'):
        for i in range(desktop_count-1):
            force_remove_desktop(1)
    elif ignored_window == True and window_handle not in window_handles:
        continue
    elif window_handle not in window_handles and ignored_window == False and prev_equal == False:
        if vda.GetCurrentDesktopNumber() != 0 and window_handle != window_handles[vda.GetCurrentDesktopNumber()-1]:
            move_window(window_handle, desktop_count)
            print("false window moved")
        else:
            move_window(window_handle, desktop_count)
            print("new window moved")
    elif vda.GetCurrentDesktopNumber() != 0 and prev_equal == True: #elif vda.GetCurrentDesktopNumber() != 0 and window_handle not in window_handles:
        remove_desktop(vda.GetCurrentDesktopNumber())
        print("desktop removed")

    prev_window_handle[0] = prev_window_handle[1]
    prev_window_handle[1] = window_handle
    prev_window_name[0] = prev_window_name[1]
    prev_window_name[1] = window_name
    if window_name == "":
        prev_window_name[1] = "void"
    



# if current_desktop == 1 and window_handle != window_handles[0]:
    # remove desktop 1
# if window_handle nicht in window_handles:
    # move window to desktop_count