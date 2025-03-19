# import subprocess

# # Define the paths of the scripts you want to run
# scripts = [
#     r"T:\Spanish Language Analysis\Code For All\copying_files_extreme.py",
#     r"T:\Spanish Language Analysis\Code For All\copying_files_spotgenie.py",
#     r"T:\Spanish Language Analysis\Code For All\copying_files_uploadspot.py"
# ]

# # Run all scripts in parallel
# processes = [subprocess.Popen(["python", script]) for script in scripts]

# # Wait for all scripts to complete
# for process in processes:
#     process.wait()

# print("All scripts have finished executing.")


import subprocess
import os

# Define the paths of the scripts you want to run
scripts = [
    r"T:\Spanish Language Analysis\Code For All\copying_files_extreme.py",
    r"T:\Spanish Language Analysis\Code For All\copying_files_spotgenie.py",
    r"T:\Spanish Language Analysis\Code For All\copying_files_uploadspot.py",
    r"T:\Spanish Language Analysis\Code For All\copying_files_comcast.py",
    r"T:\Spanish Language Analysis\Code For All\copying_files_centaur.py",
    r"T:\Spanish Language Analysis\Code For All\copying_files_videoexpress.py",
    r"T:\Spanish Language Analysis\Code For All\copying_files_yangaroo.py"
]

# Run all scripts in parallel without showing a terminal window
processes = [
    subprocess.Popen(
        ["python", script], 
        stdout=subprocess.DEVNULL,  # Suppress output
        stderr=subprocess.DEVNULL,  # Suppress errors
        creationflags=subprocess.CREATE_NO_WINDOW  # Hide console window (Windows only)
    ) 
    for script in scripts
]

# Wait for all scripts to complete
for process in processes:
    process.wait()
