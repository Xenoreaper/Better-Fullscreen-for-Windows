# Better-Fullscreen-for-Windows
Makes fullscreen applications utilize another virtual desktop instead of forcing themselves over all other applications

## To Do
- ~~make windows consistently move to a new desktop~~
- ~~make windows actually move back to the primary desktop~~
- ~~solve issue of windows closing all together upon leaving fullscreen or changing their handle, hindering the removal of added desktops~~
- ~~make program not throw you back onto a different desktop because you're switching to another one~~
- ~~make multiple instances of Firefox work~~
- ~~solve issue of invalid window handles being used~~
- ~~remove desktops and window handles if they become invalid (due to program closure)~~
- improve logging
- make usage easier
- Overlay to switch through windows like Alt+Tab, replacing Win+Tab

## Issues
- Steam has a weird condition where it closes and immediately reopens in big picture, causing it to not be caught and moved correctly again

## Changelog
### 0.1.3
Changed
- Exit keybind from Q to Ctrl+Shift+F11
### 0.1.2
Fixed
- can now handle multiple fullscreen windows (as long as it's not more than one instance of Firefox)
### 0.1.1
Fixed
- can now handle a single fullscreen window
### 0.1.0
**Initial Upload**
Added bffw.py (Better Fullscreen for Windows) and VirtualDesktopAccessor.dll

## Includes
### [VirtualDesktopAccessor by Ciantic](https://github.com/Ciantic/VirtualDesktopAccessor)
Copyright (c) 2015-2023 Jari Otto Oskari Pennanen
