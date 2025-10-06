# YouTube Downloader

A simple YouTube downloader for Termux that lets you download videos or playlists in **MP4** or **MP3** format with selectable quality. Built using Python and `yt-dlp`.

---

## Features

- Download individual videos or entire playlists.
- Choose between **Video (MP4)** or **Audio (MP3)**.
- Select quality: **Best** or **Worst**.
- Saves downloads in a dedicated `YTDownloads` folder.
- Works seamlessly on Termux and Linux terminals.

---

## Installation

### Install required packages

You need Python and `yt-dlp`. Optionally, `ffmpeg` is needed for audio extraction.

```bash

pkg update && pkg upgrade -y

pkg install python -y

pkg install ffmpeg -y

pip install yt-dlp

git clone https://github.com/sawwqib/YTDownloader.git
cd YTDownloader

python main.py
```
![Watch the demo](https://res.cloudinary.com/datfjlguq/image/upload/v1759749422/v6jzwpizgclwzdx1jjdc.gif)
