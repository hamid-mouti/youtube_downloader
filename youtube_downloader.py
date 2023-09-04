import pytube
import tkinter as tk
from tkinter import filedialog
import time
import sys


def convert_youtube_to_mp4_single(youtube_url, folder_path):
  # Get the YouTube video object
  video = pytube.YouTube(youtube_url)

  # Get the video stream
  video_stream = video.streams.get_highest_resolution()

  file_name = video_stream.title
  print (f"Downloading {file_name}...")
  # Download the video stream
  video_stream.download(folder_path)
  print(f"{file_name} downloaded successfully!")


def convert_youtube_to_mp4_multiple(youtube_url, folder_path):
  # Get the YouTube video object
  video = pytube.YouTube(youtube_url)

  # Get the video stream
  video_stream = video.streams.get_highest_resolution()

  file_name = video_stream.title
  print (f"Downloading {file_name}...")
  # Download the video stream
  video_stream.download(folder_path)
  print(f"{file_name} downloaded successfully!")


def select_file():
    # Create a Tkinter root window with no visible UI
    root = tk.Tk()
    root.withdraw()

    # Open the file dialog to select a directory
    selected_file = filedialog.askopenfilename()

    # Check if the user selected a directory or canceled the dialog
    if selected_file:
        return selected_file
    else:
        return None

def select_directory():
    # Create a Tkinter root window with no visible UI
    root = tk.Tk()
    root.withdraw()

    # Open the file dialog to select a directory
    selected_directory = filedialog.askdirectory()

    # Check if the user selected a directory or canceled the dialog
    if selected_directory:
        return selected_directory
    else:
        raise ValueError("Directory must be selected in order to proceed!")


 

print("Before we begin, select output directory: ")
time.sleep(2)
try:
    folder_path = select_directory()
except ValueError as e:
    print(e)
    sys.exit(1)

print("\nDo you want to download a video or playlist?")
choice = input("\n1.video\n2.playlist\n\nInput: ")

if choice == "1":
    youtube_url = input("Enter the YouTube video URL: ")
    convert_youtube_to_mp4_single(youtube_url,folder_path)
elif choice == "2":
    print("\nDo you want to input the playlist URL or a text file containing a list of video URLs?")
    choice = input("\n1.url\n2.file\n\nInput: ")

    if choice == "1":
        url = input("\nEnter the playlist URL: ")
        convert_youtube_to_mp4_multiple(url,folder_path)
    elif choice == "2":
        print("Select files that contains youtube links.")
        file_path = select_file()
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    convert_youtube_to_mp4_single(line.strip(),folder_path)
        except FileNotFoundError:
            print(f"The file '{file_path}' was not found.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            sys.exit(1)
    else:
        print("Invalid choice.")
        sys.exit(1)

    
else:
    print("Invalid choice.")
    sys.exit(1)