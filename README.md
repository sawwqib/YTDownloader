# Termux YouTube Downloader

A simple and YouTube downloader for Termux that lets you download videos or playlists in **MP4** or **MP3** format with selectable quality. Built using Python and `yt-dlp`.

---

## Features

- Download individual videos or entire playlists.
- Choose between **Video (MP4)** or **Audio (MP3)**.
- Select quality: **Best** or **Worst**.
- Saves downloads in a dedicated `YTDownloads` folder.
- Works seamlessly on Termux and Linux terminals.

---

## Installation

### 1. Install required packages

You need Python and `yt-dlp`. Optionally, `ffmpeg` is needed for audio extraction.

```bash
# Update packages
pkg update && pkg upgrade -y

# Install Python and pip
pkg install python -y

# Install ffmpeg (required for MP3 downloads)
pkg install ffmpeg -y

# Install yt-dlp
pip install yt-dlp

2. Clone this repository

git clone https://github.com/yourusername/termux-ytdownloader.git
cd termux-ytdownloader

3. Run the script

python main.py






Made with ❤️ by Saqib
