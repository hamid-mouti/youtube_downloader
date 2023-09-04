import os
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog
import time
import sys

def select_directory():
    print("\nSelect directory of mp4 file(s) to convert them to mp3: ")
    time.sleep(2)
    # Create a Tkinter root window with no visible UI
    root = tk.Tk()
    root.withdraw()

    # Open the file dialog to select a directory
    selected_directory = filedialog.askdirectory()

    # Check if the user selected a directory or canceled the dialog
    if selected_directory:
        return selected_directory
    else:
        return None


print("\nDo you wish to proceed with conversion to mp3?")
time.sleep(2)

user_input = input("\nSelect 'y' for yes or 'n' for no: ")

if (user_input == 'y'):
    print("ok")
elif(user_input == 'n'):
    print("Have a nice day!")
    sys.exit(1)

# Path to the folder containing the MP4 files
folder_path = select_directory()

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
