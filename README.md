# holo's SkyBlockBitsAFKTimer

**[Download for Windows](https://github.com/holo-lb/SkyBlockBitsAFKTimer/releases/download/v1.1/SkyBlockBitsAFKTimerv1.1-win.exe)**<br>
_A tool to automatically calculate the remaining time left for Bits AFKing in Hypixel SkyBlock, and will automatically shut down the computer once the timer has expired._

**If your antivirus flags the release file, you may need to whitelist it! As this script calls an OS shutdown command, it can be seen as malware, however, it is not. If you still don't feel safe about the release file being flagged, then feel free to download the source code and simply run/build it yourself!**

This small Python script simply calculates the time it will take for someone to get all of their Bits AFKed in SkyBlock, and then shut down the computer once it has finished!
This script also accounts for Fame Rank and distribution intervals to ensure you collect all your bits. If you just want to know how much time it will take for you to collect your bits, substitute the values into this formula. <br>The formula used for the calculation is:

```py
timer_in_seconds = (bits_left / (250 * fame_rank_multiplier)) * 1800
```

Supports both Windows and Unix-like operating systems, and has been compiled into an executable with PyInstaller.
This tool will finally let you AFK bits on any machine and not have to worry about turning your computer off once done! Leave this script running in the background and go to bed!<br><br>
_Tool may be at maximum 30 minutes inaccurate, as the tool cannot know when the last time the 30 minute Bits handout was triggered.<br>This tool also cannot account for the Bits Talisman, as the chances are completely random._<br><br>
Program created by [@hololb](https://github.com/hololb), 2022.
