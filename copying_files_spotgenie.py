
# import os
# import shutil
# from datetime import datetime
# from concurrent.futures import ThreadPoolExecutor

# # Define the source and destination directories
# source_dir = r"\\htv-mstor\HTV-MSTOR\Systems\Florical\Incoming-AC\SpotGenie"
# destination_dir = r"T:\Spanish Language Analysis\Files Copying\Spot Genie MXF"
# log_file = r"T:\Spanish Language Analysis\Files Copying\Processing_Files\copying_spot_genie_files_logs.txt"

# # Ensure the destination directory exists
# os.makedirs(destination_dir, exist_ok=True)

# # Define the target date (16th March 2025)
# target_date = datetime(2025, 3, 16).date()

# # Read the log file to get the list of already copied files
# if os.path.exists(log_file):
#     with open(log_file, 'r') as file:
#         copied_files = set(file.read().splitlines())
# else:
#     copied_files = set()

# # Function to copy a file
# def copy_file(filename):
#     source_file = os.path.join(source_dir, filename)
#     destination_file = os.path.join(destination_dir, filename)

#     # Check if the file has the .mxf extension, is not copied yet, and was modified after the target date
#     if os.path.isfile(source_file) and filename.endswith('.mxf') and filename not in copied_files:
#         # Get the last modification time of the file
#         file_mod_time = os.path.getmtime(source_file)
#         file_date = datetime.fromtimestamp(file_mod_time).date()

#         # If the file was modified after the target date
#         if file_date > target_date:
#             try:
#                 # Copy the file
#                 shutil.copy(source_file, destination_file)
#                 print(f"Copied: {filename}")

#                 # Add the copied file to the log
#                 with open(log_file, 'a') as log:
#                     log.write(f"{filename}\n")
#             except Exception as e:
#                 print(f"Error copying {filename}: {e}")

# # Loop through each file in the source directory
# files_to_copy = [filename for filename in os.listdir(source_dir) if filename.endswith('.mxf')]

# # Use ThreadPoolExecutor to copy files concurrently
# with ThreadPoolExecutor(max_workers=4) as executor:
#     executor.map(copy_file, files_to_copy)

# print("File copy process completed!")




#updated dates :

##copying files after 16th feb 2025;

import os
import shutil
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Define the source and destination directories
source_dir = r"\\htv-mstor\HTV-MSTOR\Systems\Florical\Incoming-AC\SpotGenie"
destination_dir = r"T:\Spanish Language Analysis\Files Copying\Spot Genie MXF"
log_file = r"T:\Spanish Language Analysis\Files Copying\Processing_Files\copying_spot_genie_files_logs.txt"

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Define the target date (16th March 2025)
target_date = datetime(2025, 3, 18).date()

# Read the log file to get the list of already copied files
if os.path.exists(log_file):
    with open(log_file, 'r') as file:
        copied_files = set(file.read().splitlines())
else:
    copied_files = set()

# Function to copy a file
def copy_file(filename):
    source_file = os.path.join(source_dir, filename)
    destination_file = os.path.join(destination_dir, filename)

    # Check if the file has the .mxf extension, is not copied yet, and was modified after the target date
    if os.path.isfile(source_file) and filename.endswith('.mxf') and filename not in copied_files:
        # Get the last modification time of the file
        file_mod_time = os.path.getmtime(source_file)
        file_date = datetime.fromtimestamp(file_mod_time).date()

        # If the file was modified after the target date
        if file_date > target_date:
            try:
                # Copy the file
                shutil.copy(source_file, destination_file)
                print(f"Copied: {filename}")

                # Add the copied file to the log
                with open(log_file, 'a') as log:
                    log.write(f"{filename}\n")
            except Exception as e:
                print(f"Error copying {filename}: {e}")

# Loop through each file in the source directory
files_to_copy = [filename for filename in os.listdir(source_dir) if filename.endswith('.mxf')]

# Use ThreadPoolExecutor to copy files concurrently
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(copy_file, files_to_copy)

print("File copy process completed!")
