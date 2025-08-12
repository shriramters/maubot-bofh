# BOFH Excuse Maubot Plugin

A simple maubot plugin that provides a random, technically-plausible excuse upon request. Perfect for any situation where you need to deflect blame with jargon.

When a user in a room types `!excuse`, the bot will post a random line from the classic "Bastard Operator From Hell" excuses file.

## Usage

To get an excuse, simply type the following command in a room where the bot is present:
```
!excuse
```

The bot will respond with a new message in the chat, for example:

> Robotic tape changer mistook operator's tie for a backup tape.

## Installation

1.  Build the plugin using the `mbc build` command.
2.  Upload the generated `.mbp` file to your maubot instance via the web UI.
3.  Create an instance of the plugin, assigning it to a client (bot user).
4.  Invite the bot user to any rooms where you want to use it.

## Disclaimer

This plugin is provided "as is". The excuses are sourced from a file reflecting the humor of the 1990s. Some content may be considered politically incorrect by modern standards, and the author of this plugin is not responsible for the content of the excuses.

## Source & License

The list of excuses used by this bot is sourced from the classic **BOFH Excuse File**.

-   **Original Source:** [https://pages.cs.wisc.edu/~ballard/bofh/excuses](https://pages.cs.wisc.edu/~ballard/bofh/excuses)

The author of the original list has placed this into the public domain. (as per this [source](https://metadata.ftp-master.debian.org/changelogs//main/f/fortunes-bofh-excuses/fortunes-bofh-excuses_1.2-3_copyright))

This maubot plugin is provided under the LGPL-3. Feel free to modify and redistribute it.

