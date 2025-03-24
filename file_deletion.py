# import os

# # Define the file paths
# folder_path = r"T:\Spanish Language Analysis\Files Copying\Extreme MXF"
# txt_file_path = r"T:\Spanish Language Analysis\Wav Files Conversion\Processing_Files\delete_extreme_wav_files.txt"

# # Step 1: Read the filenames from the txt file and extract only the filenames (ignoring timestamps)
# try:
#     with open(txt_file_path, 'r') as file:
#         files_to_delete = [line.split(' - ')[0].strip() for line in file.readlines() if line.strip()]
#         print("Files to delete (from txt):", files_to_delete)  # Debugging output
# except FileNotFoundError:
#     print(f"Error: The file {txt_file_path} does not exist.")
#     exit()

# # Step 2: List all files in the folder
# try:
#     folder_files = os.listdir(folder_path)
#     print("Files in the folder:", folder_files)  # Debugging output
# except FileNotFoundError:
#     print(f"Error: The folder {folder_path} does not exist.")
#     exit()

# # Step 3: Compare and delete matching files
# deleted_files = []  # To keep track of deleted files
# for file_name in folder_files:
#     print(f"Checking if {file_name} should be deleted...")  # Debugging output
#     if file_name in files_to_delete:
#         file_path = os.path.join(folder_path, file_name)
#         try:
#             os.remove(file_path)
#             deleted_files.append(file_name)
#             print(f"Deleted: {file_name}")
#         except Exception as e:
#             print(f"Failed to delete {file_name}: {e}")

# # Step 4: Final output
# if deleted_files:
#     print("\nDeleted the following files:")
#     for deleted in deleted_files:
#         print(deleted)
# else:
#     print("\nNo files were deleted.")


# ##it worked:
# import os

# # Define the file paths for Extreme MXF
# extreme_folder_path = r"T:\Spanish Language Analysis\Files Copying\Extreme MXF"
# extreme_txt_file_path = r"T:\Spanish Language Analysis\Wav Files Conversion\Processing_Files\delete_extreme_wav_files.txt"

# # Define the file paths for Comcast MXF
# comcast_folder_path = r"T:\Spanish Language Analysis\Files Copying\Comcast MXF"
# comcast_txt_file_path = r"T:\Spanish Language Analysis\Wav Files Conversion\Processing_Files\comcast_processing_final_stage_files.txt"

# # Function to delete files based on matching filenames in the txt file
# def delete_matching_files(folder_path, txt_file_path):
#     # Read the filenames from the txt file and extract only the filenames (ignoring timestamps)
#     with open(txt_file_path, 'r') as file:
#         files_to_delete = [line.split(' - ')[0].strip() for line in file.readlines() if line.strip()]

#     # List all files in the folder
#     folder_files = os.listdir(folder_path)

#     # Compare and delete matching files
#     for file_name in folder_files:
#         if file_name in files_to_delete:
#             file_path = os.path.join(folder_path, file_name)
#             try:
#                 os.remove(file_path)
#                 print(f"Deleted: {file_name}")
#             except Exception as e:
#                 print(f"Failed to delete {file_name}: {e}")

# # Delete files from Extreme MXF folder
# print("\nProcessing files in Extreme MXF folder:")
# delete_matching_files(extreme_folder_path, extreme_txt_file_path)

# # Delete files from Comcast MXF folder
# print("\nProcessing files in Comcast MXF folder:")
# delete_matching_files(comcast_folder_path, comcast_txt_file_path)


import os

# Define the file paths for each folder
folder_paths = [
    (r"T:\Spanish Language Analysis\Files Copying\Extreme MXF", r"T:\Spanish Language Analysis\Wav Files Conversion\Processing_Files\extreme_processing_final_stage_files.txt"),
    (r"T:\Spanish Language Analysis\Files Copying\Comcast MXF", r"T:\Spanish Language Analysis\Wav Files Conversion\Processing_Files\comcast_processing_final_stage_files.txt"),
    (r"T:\Spanish Language Analysis\Files Copying\Yangaroo MXF", r"T:\Spanish Language Analysis\Wav Files Conversion\Processing_Files\yangaroo_processing_final_stage_files.txt"),
    (r"T:\Spanish Language Analysis\Files Copying\Centaur MXF", r"T:\Spanish Language Analysis\Wav Files Conversion\Processing_Files\processing_final_stage_centaur_files.txt"),
    (r"T:\Spanish Language Analysis\Files Copying\Upload_Spots MXF", r"T:\Spanish Language Analysis\Wav Files Conversion\Processing_Files\processing_final_stage_us_files.txt")
]

# Function to delete files based on matching filenames in the txt file
def delete_matching_files(folder_path, txt_file_path):
    # Read the filenames from the txt file and extract only the filenames (ignoring timestamps)
    with open(txt_file_path, 'r') as file:
        files_to_delete = [line.split(' - ')[0].strip() for line in file.readlines() if line.strip()]

    # List all files in the folder
    folder_files = os.listdir(folder_path)

    # Compare and delete matching files
    for file_name in folder_files:
        if file_name in files_to_delete:
            file_path = os.path.join(folder_path, file_name)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_name} from {folder_path}")
            except Exception as e:
                print(f"Failed to delete {file_name}: {e}")

# Process each folder and its corresponding text file
for folder_path, txt_file_path in folder_paths:
    print(f"\nProcessing files in {folder_path}:")
    delete_matching_files(folder_path, txt_file_path)
