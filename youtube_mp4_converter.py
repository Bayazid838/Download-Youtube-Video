from pytube import YouTube  
from tkinter import filedialog
import tkinter as 

def download_video(url, save_path):
    try:
        yt = YouTube(url) 
        stream = yt.streams.filter(progressive=True, file_extension="mp4")
        hd_stream = stream.get_highest_resolution()
        hd_stream.download(output_path=save_path)
        print("Video has been downloaded successfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()  
    if folder:
        print("Selected folder:", folder)
        return folder

window = tkinter.Tk()
window.withdraw()

if __name__ == "__main__":
    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Download Started...")
        download_video(video_url, save_dir)
    else:
        print("Invalid video url!")
