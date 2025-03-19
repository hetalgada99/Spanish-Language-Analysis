
import subprocess
import os

# Define the paths of the scripts you want to run
scripts = [
    r"T:\Spanish Language Analysis\Code For All\wav_final_comcast.py"
    
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
