import yt_dlp
import os

# ANSI Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Clear screen
os.system("clear")

# ASCII YouTube Logo with colors
logo = f"""
{RED}⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
"""

print(logo)
print(f"{BOLD}{CYAN}Visit: {YELLOW}https://sawwqib.vercel.app\n")
print(f"{BOLD}{GREEN}Welcome to the Termux YouTube Downloader!\n{RESET}")

# Step 1: Choose download type
print(f"{MAGENTA}1.{RESET} Video")
print(f"{MAGENTA}2.{RESET} Playlist")
while True:
    download_type = input(f"{BOLD}{CYAN}Select download type (1 or 2): {RESET}").strip()
    if download_type in ["1", "2"]:
        break
    print(f"{RED}Invalid choice. Enter 1 or 2.{RESET}")

# Step 2: Enter YouTube URL
url = input(f"{BOLD}{CYAN}Enter YouTube URL: {RESET}").strip()

# Step 3: Choose format
print(f"\n{MAGENTA}1.{RESET} MP4 (Video)")
print(f"{MAGENTA}2.{RESET} MP3 (Audio)")
while True:
    fmt_choice = input(f"{BOLD}{CYAN}Select format (1 or 2): {RESET}").strip()
    if fmt_choice == "1":
        file_format = "mp4"
        break
    elif fmt_choice == "2":
        file_format = "mp3"
        break
    print(f"{RED}Invalid choice. Enter 1 or 2.{RESET}")

# Step 4: Choose quality
print(f"\n{MAGENTA}1.{RESET} Best")
print(f"{MAGENTA}2.{RESET} Worst")
while True:
    q_choice = input(f"{BOLD}{CYAN}Select quality (1 or 2): {RESET}").strip()
    if q_choice == "1":
        quality = "best"
        break
    elif q_choice == "2":
        quality = "worst"
        break
    print(f"{RED}Invalid choice. Enter 1 or 2.{RESET}")

# Prepare output path
output_dir = os.path.join(os.getcwd(), "YTDownloads")
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "%(title)s.%(ext)s")

# Prepare yt-dlp options
if file_format == "mp3":
    ydl_opts = {
        "format": "bestaudio/best" if quality=="best" else "worstaudio",
        "outtmpl": output_file,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "noplaylist": download_type=="1"
    }
else:
    ydl_opts = {
        "format": "bestvideo+bestaudio/best" if quality=="best" else "worstvideo+worstaudio",
        "outtmpl": output_file,
        "noplaylist": download_type=="1"
    }

# Download process
print(f"\n{YELLOW}Downloading, please wait...{RESET}\n")
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"\n{GREEN}Download completed!{RESET}")
    print(f"{BOLD}Saved in: {CYAN}{output_dir}{RESET}")
except Exception as e:
    print(f"\n{RED}Download failed!{RESET}")
    print(f"Error: {e}")

print(f"\n{BOLD}{MAGENTA}Thank you for using YouTube Downloader!{RESET}")