#!/usr/bin/env python3

import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def __init__(self, download_folder, destination_folder):
        self.download_folder = download_folder
        self.destination_folder = destination_folder

    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            # Check if the file was created in the download folder
            if file_path.startswith(self.download_folder):
                # Determine the destination folder based on file type or other criteria
                destination = self.get_destination_folder(file_path)
                if destination:
                    self.move_file(file_path, destination)

    def get_destination_folder(self, file_path):
        # Implement your logic here to determine the destination folder
        # For example, based on file extension, keywords in the filename, etc.
        # Return the full path of the destination folder.
        # If no match is found, return None.
        # Example:

        if file_path.endswith(".pdf"):
            return os.path.join(self.destination_folder, "PDFs")
        elif "screenshot" in file_path.lower():
            return os.path.join(self.destination_folder, "Images", "Screenshots")
        elif file_path.endswith(".jpg") or file_path.endswith(".png"):
            return os.path.join(self.destination_folder, "Images")
        elif file_path.endswith(".circ"):
            return os.path.join(self.destination_folder, "Logisim_Circuits")
        
        else:
            return None

    def move_file(self, source, destination):
        try:
            shutil.move(source, destination)
            print(f"Moved {source} to {destination}")
        except Exception as e:
            print(f"Error moving {source} to {destination}: {str(e)}")

if __name__ == "__main__":
    download_folder = "/path/to/downloaded/files" 
    destination_folder = "/path/to/destination/folders" 

    event_handler = MyHandler(download_folder, destination_folder)
    observer = Observer()
    observer.schedule(event_handler, path=download_folder, recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("KeyboardInterrupt received. Stopping the script gracefully...")
        observer.stop()
    observer.join()
