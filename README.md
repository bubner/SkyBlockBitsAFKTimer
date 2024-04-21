# Hypixel SkyBlock AFK Bits Shutdown Timer

_A tool to automatically calculate the remaining time left for Bits AFKing in Hypixel SkyBlock, and will automatically shut down the computer once the timer has expired._

This small Python script simply calculates the time it will take for someone to get all of their Bits AFKed in SkyBlock, and then shut down the computer once it has finished!  

This script also accounts for Fame Rank and distribution intervals to ensure you collect all your bits. If you just want to know how much time it will take for you to collect your bits, substitute the values into this formula. <br>The formula used for the calculation is:

```py
timer_in_seconds = (bits_left / (250 * fame_rank_multiplier)) * 1800
```

To use this timer, run `main.py` on your machine using Python. May require root privileges to execute a shutdown system call.  

_This tool may be at maximum 30 minutes inaccurate, as the tool cannot know when the last time the 30 minute Bits handout was triggered.<br>This tool also cannot account for the Bits Talisman, as the chances are completely random._<br><br>
