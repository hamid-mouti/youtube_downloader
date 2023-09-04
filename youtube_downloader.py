import pytube
import tkinter as tk
from tkinter import filedialog
import time
import sys
import os
from moviepy.editor import VideoFileClip



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

print("\nDo you wish to proceed with conversion to mp3?")
time.sleep(2)

user_input = input("\nSelect 'y' for yes or 'n' for no: ")

if (user_input == 'y'):
    print("ok")
elif(user_input == 'n'):
    print("Have a nice day!")
    sys.exit(1)


if (folder_path == None):
    print("You only have mp4 files now...")
    sys.exit(1)

print(f"\nYou selected {folder_path} to store your mp3 file(s).\n")

time.sleep(2)


# List all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".mp4"):
        # Get the full path to the MP4 file
        mp4_file_path = os.path.join(folder_path, filename)

        # Generate the corresponding MP3 filename
        mp3_filename = filename.replace(".mp4", ".mp3")
        mp3_file_path = os.path.join(folder_path, mp3_filename)

        # Load the MP4 file
        video = VideoFileClip(mp4_file_path)

        # Extract audio from video and save as MP3 in the same folder
        video.audio.write_audiofile(mp3_file_path)

        print(f"Converted {filename} to {mp3_filename}")

        # Remove the original MP4 file
        os.remove(mp4_file_path)
        print(f"Deleted {filename}")

print("Conversion and deletion complete!")