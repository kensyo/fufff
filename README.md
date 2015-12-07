# fufff
An update script on flashplayer for firefox on Linux

## Overview
This script will download flashplayer for firefox on Linux and will install it.  
Concretely speaking, it places downloaded `libflashplayer.so` on `$HOME/.mozilla/plugins`.

Note that it replaces a current version of `libflashplayer.so` with the latest, Error handling is not enough,  
and that it so strongly depends on the html structure of [this web page](https://helpx.adobe.com/jp/flash-player/kb/235703.html) that it can become useless easily.

I have tested this script on Arch Linux.

Use this script **at your own risk**.

## Usage
This is a python3 script, and a main script is `main.py`.  
It may also be a good choice to use it with cron.
