# Better-Fullscreen-for-Windows
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FXenoreaper%2FBetter-Fullscreen-for-Windows&label=Repository%20Visits&countColor=%230c7ebe&style=flat&labelStyle=none)
![GitHub License](https://img.shields.io/github/license/Xenoreaper/Better-Fullscreen-for-Windows)
![Python](https://img.shields.io/badge/Python-4B8BBE?style=flat&logo=python&logoColor=white)

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
- program hides in system tray
- startup at boot
- ignore list
- potentially include modules to make usage easier
- list of apps that should be handled like fullscreen windows (configurable)
- possibly compatibility with win10
- compatibility with arm version of Windows
- maybe switch to C#

## Issues
- Steam has a weird condition where it closes and immediately reopens in big picture, causing it to not be caught and moved correctly again
- Some fullscreen windows don't get recognized as such (ie Helldivers2)
- Only compatible with win11

## Changelog
see https://github.com/Xenoreaper/Better-Fullscreen-for-Windows/blob/main/CHANGELOG.md

## Includes
### [VirtualDesktopAccessor by Ciantic](https://github.com/Ciantic/VirtualDesktopAccessor)
> Copyright (c) 2015-2023 Jari Otto Oskari Pennanen
