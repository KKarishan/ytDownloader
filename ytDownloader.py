# first install below library thorugh your terminal
# pip3 install pytube

from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("view: ", yt.views)

# Video Downloader
# yd = yt.streams.get_highest_resolution()
# yd.download('C:\\Users\\ABCD\\Desktop')

# Audio Downloader
audio_stream = yt.streams.filter(only_audio = True, file_extension='mp4').first()
audio_stream.download('C:\\Users\\ABCD\\Desktop\\Music', filename = f"{yt.title}.mp3")

print("Download Completed.")

# type below line in your terminal 
# python ytDownloader.py YouTubeLink
# or
# python3 ytDownloader.py YouTubeLink