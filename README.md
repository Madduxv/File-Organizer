# File-Organizer
This Python script helps you automatically organize files in your download folder by moving them to specific destination folders based on file type or other criteria. It utilizes the watchdog library to monitor the download folder for new files and applies custom rules for organizing them.

# Prerequisites

Before using this script, you should have the following installed on your system:

Python 3.x: You can download Python from the official website.

watchdog library: You can install it using pip:

pip install watchdog

# Getting Started
Clone or download this repository to your local machine.

Open the terminal and navigate to the directory containing the script.

Edit the script to set your download folder and destination folder paths. Update the following lines with your folder paths:
```
download_folder = "/path/to/your/download/folder"

destination_folder = "/path/to/your/destination/folder"
```
# Customizing the Organization Rules
You can customize the organization rules by modifying the get_destination_folder method in the script. By default, the script organizes files based on their extensions and filenames. You can add, remove, or modify conditions to match your requirements. 

# Running the Script
To run the script, open a terminal, navigate to the script's directory, and execute the following command:
```
nohup python file_saver.py &
```
The script will continuously monitor your download folder and organize new files based on your custom rules.

# Stopping the Script
To stop the script gracefully, use the following steps:

Find the process ID (PID) of the running script:
```
ps aux | grep file_saver.py
```
Terminate the process using the kill command:
```
kill PID
```
Replace PID with the process ID you found in step 1.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
