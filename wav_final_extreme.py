# import os
# import subprocess
# import whisper
# import datetime
# from pydub import AudioSegment

# # Set up paths
# input_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Extreme_Audios"
# output_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\wav_extreme"
# processing_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Processing_Files"

# wav_log_file_path = os.path.join(output_folder, "wav_files.txt")
# delete_mxf_log_file_path = os.path.join(processing_folder, "delete_copied_files.txt")
# spanish_log_file_path = os.path.join(processing_folder, "spanish_files.txt")
# processed_log_file_path = os.path.join(processing_folder, "processing_final_stage_files.txt")
# delete_wav_log_file_path = os.path.join(processing_folder, "delete_wav_files.txt")

# # Ensure necessary folders exist
# os.makedirs(output_folder, exist_ok=True)
# os.makedirs(processing_folder, exist_ok=True)

# # FFmpeg path
# ffmpeg_path = r"C:\Users\hgada\Downloads\ffmpeg\ffmpeg.exe"

# # Load already logged files to avoid reprocessing
# logged_files = set()
# if os.path.exists(wav_log_file_path):
#     with open(wav_log_file_path, "r") as log_file:
#         logged_files = {line.split(" -> ")[0] for line in log_file.readlines()}

# # Convert MXF to WAV
# mxf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mxf')]
# if mxf_files:
#     with open(wav_log_file_path, "a") as wav_log_file, open(delete_mxf_log_file_path, "a") as delete_log_file:
#         for mxf_file in mxf_files:
#             if mxf_file in logged_files:
#                 continue
#             input_file_path = os.path.join(input_folder, mxf_file)
#             output_file_wav = os.path.join(output_folder, os.path.splitext(mxf_file)[0] + ".wav")
#             command = f'"{ffmpeg_path}" -i "{input_file_path}" -acodec pcm_s16le -ar 44100 -ac 2 "{output_file_wav}"'
#             try:
#                 subprocess.run(command, shell=True, check=True)
#                 wav_log_file.write(f"{mxf_file} -> {output_file_wav}\n")
#                 os.remove(input_file_path)
#                 delete_log_file.write(f"{mxf_file} deleted from {input_folder}\n")
#             except subprocess.CalledProcessError as e:
#                 print(f"Error converting {mxf_file}: {e}")

# # Process WAV files with Whisper
# os.environ["PATH"] = r"C:\msys64\mingw64\bin" + os.pathsep + os.environ["PATH"]
# AudioSegment.ffmpeg = r"C:\msys64\mingw64\bin\ffmpeg.exe"
# AudioSegment.converter = r"C:\msys64\mingw64\bin\ffmpeg.exe"

# def detect_language(audio_file):
#     model = whisper.load_model("base")
#     result = model.transcribe(audio_file)
#     return result['language'] == 'es'

# processed_files = set()
# if os.path.exists(processed_log_file_path):
#     with open(processed_log_file_path, "r", encoding="utf-8") as log_file:
#         processed_files = set(line.strip().split(" - ")[0] for line in log_file.readlines())

# for wav_file in os.listdir(output_folder):
#     if not wav_file.endswith('.wav') or wav_file in processed_files:
#         continue
#     wav_path = os.path.join(output_folder, wav_file)
#     modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(wav_path)).strftime('%m%d%Y')
#     try:
#         is_spanish = detect_language(wav_path)
#         if is_spanish:
#             with open(spanish_log_file_path, "a", encoding="utf-8") as spanish_file:
#                 spanish_file.write(f"{wav_file} - {modified_date}\n")
#         with open(processed_log_file_path, "a", encoding="utf-8") as log_file:
#             log_file.write(f"{wav_file} - Processed - {modified_date}\n")
#         os.remove(wav_path)
#         with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
#             delete_file.write(f"{wav_file} - Deleted - {modified_date}\n")
#     except Exception as e:
#         print(f"Error processing {wav_file}: {e}")

# print("All conversions and processing complete.")


# ##try :

# import os
# import subprocess
# import whisper
# import datetime
# from pydub import AudioSegment

# # Set up paths
# input_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\extreme_audios"
# output_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\wav_extreme"
# processing_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Processing_Files"

# processing_1_log_path = os.path.join(processing_folder, "Processing_1.txt")
# wav_log_file_path = os.path.join(output_folder, "wav_files.txt")

# # Ensure necessary folders exist
# os.makedirs(output_folder, exist_ok=True)
# os.makedirs(processing_folder, exist_ok=True)

# # FFmpeg path
# ffmpeg_path = r"C:\Users\hgada\Downloads\ffmpeg\ffmpeg.exe"

# # Get today's date in MMDDYYYY format
# today_date = datetime.datetime.now().strftime('%m%d%Y')

# # Load already processed files to avoid reprocessing
# processed_files = set()
# if os.path.exists(processing_1_log_path):
#     with open(processing_1_log_path, "r", encoding="utf-8") as log_file:
#         processed_files = {line.strip() for line in log_file.readlines()}

# # Filter today's MXF files
# mxf_files = [
#     f for f in os.listdir(input_folder)
#     if f.lower().endswith('.mxf') and f not in processed_files and 
#     datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(input_folder, f))).strftime('%m%d%Y') == today_date
# ]

# # Convert MXF to WAV but DO NOT delete MXF
# if mxf_files:
#     with open(wav_log_file_path, "a") as wav_log_file, open(processing_1_log_path, "a", encoding="utf-8") as processing_log:
#         for mxf_file in mxf_files:
#             input_file_path = os.path.join(input_folder, mxf_file)
#             output_file_wav = os.path.join(output_folder, os.path.splitext(mxf_file)[0] + ".wav")
#             command = f'"{ffmpeg_path}" -i "{input_file_path}" -acodec pcm_s16le -ar 44100 -ac 2 "{output_file_wav}"'
#             try:
#                 subprocess.run(command, shell=True, check=True)
#                 wav_log_file.write(f"{mxf_file} -> {output_file_wav}\n")
#                 processing_log.write(f"{mxf_file}\n")  # Mark file as processed
#             except subprocess.CalledProcessError as e:
#                 print(f"Error converting {mxf_file}: {e}")

# print("Today's MXF files have been processed and tracked in Processing_1.")


# import os
# import subprocess
# import whisper
# import datetime
# from pydub import AudioSegment

# # Set up paths
# input_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Extreme_Audios"
# output_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\wav_extreme"
# processing_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Processing_Files"

# processing_1_log_path = os.path.join(processing_folder, "Processing_1.txt")
# wav_log_file_path = os.path.join(output_folder, "wav_files.txt")

# # Ensure necessary folders exist
# os.makedirs(output_folder, exist_ok=True)
# os.makedirs(processing_folder, exist_ok=True)

# # FFmpeg path
# ffmpeg_path = r"C:\Users\hgada\Downloads\ffmpeg\ffmpeg.exe"

# # Get today's date in MMDDYYYY format
# today_date = datetime.datetime.now().strftime('%m%d%Y')

# # Load already processed files to avoid reprocessing
# processed_files = set()
# if os.path.exists(processing_1_log_path):
#     with open(processing_1_log_path, "r", encoding="utf-8") as log_file:
#         processed_files = {line.strip() for line in log_file.readlines()}

# # Filter today's MXF files
# mxf_files = [
#     f for f in os.listdir(input_folder)
#     if f.lower().endswith('.mxf') and f not in processed_files and 
#     datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(input_folder, f))).strftime('%m%d%Y') == today_date
# ]

# # Convert MXF to WAV but DO NOT delete MXF
# if mxf_files:
#     with open(wav_log_file_path, "a") as wav_log_file, open(processing_1_log_path, "a", encoding="utf-8") as processing_log:
#         for mxf_file in mxf_files:
#             input_file_path = os.path.join(input_folder, mxf_file)
#             output_file_wav = os.path.join(output_folder, os.path.splitext(mxf_file)[0] + ".wav")
#             command = f'"{ffmpeg_path}" -i "{input_file_path}" -acodec pcm_s16le -ar 44100 -ac 2 "{output_file_wav}"'
#             try:
#                 subprocess.run(command, shell=True, check=True)
#                 wav_log_file.write(f"{mxf_file} -> {output_file_wav}\n")
#                 processing_log.write(f"{mxf_file}\n")  # Mark file as processed
#             except subprocess.CalledProcessError as e:
#                 print(f"Error converting {mxf_file}: {e}")

# print("Today's MXF files have been processed and tracked in Processing_1.")




# import os
# import subprocess
# import whisper
# import datetime
# from pydub import AudioSegment

# # Set up paths
# input_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Extreme_Audios"
# output_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\wav_extreme"
# processing_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Processing_Files"

# wav_log_file_path = os.path.join(output_folder, "wav_files.txt")
# processed_log_file_path = os.path.join(processing_folder, "processing_final_stage_files.txt")
# spanish_log_file_path = os.path.join(processing_folder, "spanish_files.txt")
# delete_wav_log_file_path = os.path.join(processing_folder, "delete_wav_files.txt")

# # Ensure necessary folders exist
# os.makedirs(output_folder, exist_ok=True)
# os.makedirs(processing_folder, exist_ok=True)

# # FFmpeg path
# ffmpeg_path = r"C:\Users\hgada\Downloads\ffmpeg\ffmpeg.exe"

# # Load already logged files to avoid reprocessing
# logged_files = set()
# if os.path.exists(wav_log_file_path):
#     with open(wav_log_file_path, "r") as log_file:
#         logged_files = {line.split(" -> ")[0] for line in log_file.readlines()}

# # Convert MXF to WAV but DO NOT delete MXF
# mxf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mxf')]
# if mxf_files:
#     with open(wav_log_file_path, "a") as wav_log_file:
#         for mxf_file in mxf_files:
#             if mxf_file in logged_files:
#                 continue
#             input_file_path = os.path.join(input_folder, mxf_file)
#             output_file_wav = os.path.join(output_folder, os.path.splitext(mxf_file)[0] + ".wav")
#             command = f'"{ffmpeg_path}" -i "{input_file_path}" -acodec pcm_s16le -ar 44100 -ac 2 "{output_file_wav}"'
#             try:
#                 subprocess.run(command, shell=True, check=True)
#                 wav_log_file.write(f"{mxf_file} -> {output_file_wav}\n")
#             except subprocess.CalledProcessError as e:
#                 print(f"Error converting {mxf_file}: {e}")

# # Process WAV files with Whisper
# os.environ["PATH"] = r"C:\msys64\mingw64\bin" + os.pathsep + os.environ["PATH"]
# AudioSegment.ffmpeg = r"C:\msys64\mingw64\bin\ffmpeg.exe"
# AudioSegment.converter = r"C:\msys64\mingw64\bin\ffmpeg.exe"

# def detect_language(audio_file):
#     model = whisper.load_model("base")
#     result = model.transcribe(audio_file)
#     return result['language'] == 'es'

# processed_files = set()
# if os.path.exists(processed_log_file_path):
#     with open(processed_log_file_path, "r", encoding="utf-8") as log_file:
#         processed_files = set(line.strip().split(" - ")[0] for line in log_file.readlines())

# for wav_file in os.listdir(output_folder):
#     if not wav_file.endswith('.wav') or wav_file in processed_files:
#         continue
#     wav_path = os.path.join(output_folder, wav_file)
#     modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(wav_path)).strftime('%m%d%Y')
#     try:
#         is_spanish = detect_language(wav_path)
#         if is_spanish:
#             with open(spanish_log_file_path, "a", encoding="utf-8") as spanish_file:
#                 spanish_file.write(f"{wav_file} - {modified_date}\n")
#         with open(processed_log_file_path, "a", encoding="utf-8") as log_file:
#             log_file.write(f"{wav_file} - Processed - {modified_date}\n")
        
#         # Delete only WAV file after processing
#         os.remove(wav_path)
#         with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
#             delete_file.write(f"{wav_file} - Deleted - {modified_date}\n")

#     except Exception as e:
#         print(f"Error processing {wav_file}: {e}")

# print("All conversions and processing complete.")



# import os
# import subprocess
# import whisper
# import datetime
# from pydub import AudioSegment

# # Set up paths
# input_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Extreme Audios"  # Update folder path
# output_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\wav_extreme"
# processing_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Processing_Files"

# wav_log_file_path = os.path.join(output_folder, "wav_files.txt")
# processed_log_file_path = os.path.join(processing_folder, "processing_final_stage_files.txt")
# spanish_log_file_path = os.path.join(processing_folder, "spanish_files.txt")
# delete_wav_log_file_path = os.path.join(processing_folder, "delete_wav_files.txt")

# # Ensure necessary folders exist
# os.makedirs(output_folder, exist_ok=True)
# os.makedirs(processing_folder, exist_ok=True)

# # FFmpeg path
# ffmpeg_path = r"C:\Users\hgada\Downloads\ffmpeg\ffmpeg.exe"

# # Load already logged files to avoid reprocessing
# logged_files = set()
# if os.path.exists(wav_log_file_path):
#     with open(wav_log_file_path, "r") as log_file:
#         logged_files = {line.split(" -> ")[0] for line in log_file.readlines()}

# # Get today's date
# today_date = datetime.datetime.today().strftime('%m%d%Y')

# # Convert MXF to WAV but DO NOT delete MXF (only today's date)
# mxf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mxf')]
# if mxf_files:
#     with open(wav_log_file_path, "a") as wav_log_file:
#         for mxf_file in mxf_files:
#             if mxf_file in logged_files:
#                 continue

#             input_file_path = os.path.join(input_folder, mxf_file)
#             modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(input_file_path)).strftime('%m%d%Y')

#             # Process only today's date
#             if modified_date == today_date:
#                 output_file_wav = os.path.join(output_folder, os.path.splitext(mxf_file)[0] + ".wav")
#                 command = f'"{ffmpeg_path}" -i "{input_file_path}" -acodec pcm_s16le -ar 44100 -ac 2 "{output_file_wav}"'
#                 try:
#                     subprocess.run(command, shell=True, check=True)
#                     wav_log_file.write(f"{mxf_file} -> {output_file_wav}\n")
#                 except subprocess.CalledProcessError as e:
#                     print(f"Error converting {mxf_file}: {e}")

# # Process WAV files with Whisper
# os.environ["PATH"] = r"C:\msys64\mingw64\bin" + os.pathsep + os.environ["PATH"]
# AudioSegment.ffmpeg = r"C:\msys64\mingw64\bin\ffmpeg.exe"
# AudioSegment.converter = r"C:\msys64\mingw64\bin\ffmpeg.exe"

# def detect_language(audio_file):
#     model = whisper.load_model("base")
#     result = model.transcribe(audio_file)
#     return result['language'] == 'es'

# processed_files = set()
# if os.path.exists(processed_log_file_path):
#     with open(processed_log_file_path, "r", encoding="utf-8") as log_file:
#         processed_files = set(line.strip().split(" - ")[0] for line in log_file.readlines())

# for wav_file in os.listdir(output_folder):
#     if not wav_file.endswith('.wav') or wav_file in processed_files:
#         continue
#     wav_path = os.path.join(output_folder, wav_file)
#     modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(wav_path)).strftime('%m%d%Y')
#     try:
#         is_spanish = detect_language(wav_path)
#         if is_spanish:
#             with open(spanish_log_file_path, "a", encoding="utf-8") as spanish_file:
#                 spanish_file.write(f"{wav_file} - {modified_date}\n")
#         with open(processed_log_file_path, "a", encoding="utf-8") as log_file:
#             log_file.write(f"{wav_file} - Processed - {modified_date}\n")
        
#         # Delete only WAV file after processing
#         os.remove(wav_path)
#         with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
#             delete_file.write(f"{wav_file} - Deleted - {modified_date}\n")

#     except Exception as e:
#         print(f"Error processing {wav_file}: {e}")

# print("All conversions and processing complete.")



## deleting the copy of it from mxf

# import os
# import subprocess
# import whisper
# import datetime
# from pydub import AudioSegment

# # Set up paths
# input_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Extreme Audios"  # Update folder path
# output_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\wav_extreme"
# processing_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Processing_Files"

# wav_log_file_path = os.path.join(output_folder, "wav_files.txt")
# processed_log_file_path = os.path.join(processing_folder, "processing_final_stage_files.txt")
# spanish_log_file_path = os.path.join(processing_folder, "spanish_files.txt")
# delete_wav_log_file_path = os.path.join(processing_folder, "delete_wav_files.txt")

# # Ensure necessary folders exist
# os.makedirs(output_folder, exist_ok=True)
# os.makedirs(processing_folder, exist_ok=True)

# # FFmpeg path
# ffmpeg_path = r"C:\Users\hgada\Downloads\ffmpeg\ffmpeg.exe"

# # Load already logged files to avoid reprocessing
# logged_files = set()
# if os.path.exists(wav_log_file_path):
#     with open(wav_log_file_path, "r") as log_file:
#         logged_files = {line.split(" -> ")[0] for line in log_file.readlines()}

# # Get today's date
# today_date = datetime.datetime.today().strftime('%m%d%Y')

# # Convert MXF to WAV but DO NOT delete MXF (only today's date)
# mxf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mxf')]
# if mxf_files:
#     with open(wav_log_file_path, "a") as wav_log_file:
#         for mxf_file in mxf_files:
#             if mxf_file in logged_files:
#                 continue

#             input_file_path = os.path.join(input_folder, mxf_file)
#             modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(input_file_path)).strftime('%m%d%Y')

#             # Process only today's date
#             if modified_date == today_date:
#                 output_file_wav = os.path.join(output_folder, os.path.splitext(mxf_file)[0] + ".wav")
#                 command = f'"{ffmpeg_path}" -i "{input_file_path}" -acodec pcm_s16le -ar 44100 -ac 2 "{output_file_wav}"'
#                 try:
#                     subprocess.run(command, shell=True, check=True)
#                     wav_log_file.write(f"{mxf_file} -> {output_file_wav}\n")
                    
#                     # Delete the original MXF file after conversion
#                     os.remove(input_file_path)
#                     with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
#                         delete_file.write(f"{mxf_file} - Deleted - {modified_date}\n")
#                 except subprocess.CalledProcessError as e:
#                     print(f"Error converting {mxf_file}: {e}")

# # Process WAV files with Whisper
# os.environ["PATH"] = r"C:\msys64\mingw64\bin" + os.pathsep + os.environ["PATH"]
# AudioSegment.ffmpeg = r"C:\msys64\mingw64\bin\ffmpeg.exe"
# AudioSegment.converter = r"C:\msys64\mingw64\bin\ffmpeg.exe"

# def detect_language(audio_file):
#     model = whisper.load_model("base")
#     result = model.transcribe(audio_file)
#     return result['language'] == 'es'

# processed_files = set()
# if os.path.exists(processed_log_file_path):
#     with open(processed_log_file_path, "r", encoding="utf-8") as log_file:
#         processed_files = set(line.strip().split(" - ")[0] for line in log_file.readlines())

# for wav_file in os.listdir(output_folder):
#     if not wav_file.endswith('.wav') or wav_file in processed_files:
#         continue
#     wav_path = os.path.join(output_folder, wav_file)
#     modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(wav_path)).strftime('%m%d%Y')
#     try:
#         is_spanish = detect_language(wav_path)
#         if is_spanish:
#             with open(spanish_log_file_path, "a", encoding="utf-8") as spanish_file:
#                 spanish_file.write(f"{wav_file} - {modified_date}\n")
#         with open(processed_log_file_path, "a", encoding="utf-8") as log_file:
#             log_file.write(f"{wav_file} - Processed - {modified_date}\n")
        
#         # Delete only WAV file after processing
#         os.remove(wav_path)
#         with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
#             delete_file.write(f"{wav_file} - Deleted - {modified_date}\n")

#     except Exception as e:
#         print(f"Error processing {wav_file}: {e}")

# print("All conversions and processing complete.")



# ## simulatenousley doing it
# import os
# import subprocess
# import whisper
# import datetime
# from pydub import AudioSegment

# # Set up paths
# input_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Extreme Audios"  # Update folder path
# output_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\wav_extreme"
# processing_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Processing_Files"

# wav_log_file_path = os.path.join(output_folder, "wav_files.txt")
# processed_log_file_path = os.path.join(processing_folder, "processing_final_stage_files.txt")
# spanish_log_file_path = os.path.join(processing_folder, "spanish_files.txt")
# delete_wav_log_file_path = os.path.join(processing_folder, "delete_wav_files.txt")

# # Ensure necessary folders exist
# os.makedirs(output_folder, exist_ok=True)
# os.makedirs(processing_folder, exist_ok=True)

# # FFmpeg path
# ffmpeg_path = r"C:\Users\hgada\Downloads\ffmpeg\ffmpeg.exe"

# # Load already logged files to avoid reprocessing
# logged_files = set()
# if os.path.exists(wav_log_file_path):
#     with open(wav_log_file_path, "r") as log_file:
#         logged_files = {line.split(" -> ")[0] for line in log_file.readlines()}

# # Get today's date
# today_date = datetime.datetime.today().strftime('%m%d%Y')

# # Process MXF files and immediately check for language and analyze
# os.environ["PATH"] = r"C:\msys64\mingw64\bin" + os.pathsep + os.environ["PATH"]
# AudioSegment.ffmpeg = r"C:\msys64\mingw64\bin\ffmpeg.exe"
# AudioSegment.converter = r"C:\msys64\mingw64\bin\ffmpeg.exe"

# def detect_language(audio_file):
#     model = whisper.load_model("base")
#     result = model.transcribe(audio_file)
#     return result['language'] == 'es'

# # Load processed files log
# processed_files = set()
# if os.path.exists(processed_log_file_path):
#     with open(processed_log_file_path, "r", encoding="utf-8") as log_file:
#         processed_files = set(line.strip().split(" - ")[0] for line in log_file.readlines())

# # Convert MXF to WAV and process it
# mxf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mxf')]
# if mxf_files:
#     with open(wav_log_file_path, "a") as wav_log_file:
#         for mxf_file in mxf_files:
#             if mxf_file in logged_files:
#                 continue

#             input_file_path = os.path.join(input_folder, mxf_file)
#             modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(input_file_path)).strftime('%m%d%Y')

#             # Process only today's date
#             if modified_date == today_date:
#                 output_file_wav = os.path.join(output_folder, os.path.splitext(mxf_file)[0] + ".wav")
#                 command = f'"{ffmpeg_path}" -i "{input_file_path}" -acodec pcm_s16le -ar 44100 -ac 2 "{output_file_wav}"'
#                 try:
#                     subprocess.run(command, shell=True, check=True)
#                     wav_log_file.write(f"{mxf_file} -> {output_file_wav}\n")
                    
#                     # Delete the original MXF file after conversion
#                     os.remove(input_file_path)
#                     with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
#                         delete_file.write(f"{mxf_file} - Deleted - {modified_date}\n")
                    
#                     # Immediately analyze the converted WAV file
#                     if output_file_wav.endswith(".wav"):
#                         is_spanish = detect_language(output_file_wav)
#                         if is_spanish:
#                             with open(spanish_log_file_path, "a", encoding="utf-8") as spanish_file:
#                                 spanish_file.write(f"{mxf_file} - {modified_date}\n")
                        
#                         # Log the processed file
#                         with open(processed_log_file_path, "a", encoding="utf-8") as processed_file:
#                             processed_file.write(f"{mxf_file} - Processed - {modified_date}\n")
                        
#                         # Delete the WAV file after processing
#                         os.remove(output_file_wav)
#                         with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
#                             delete_file.write(f"{mxf_file} - Deleted - {modified_date}\n")

#                 except subprocess.CalledProcessError as e:
#                     print(f"Error converting {mxf_file}: {e}")

# print("All conversions and processing complete.")



##today's dated files :

# import os
# import subprocess
# import whisper
# import datetime
# from pydub import AudioSegment

# # Set up paths
# input_folder = r"T:\Spanish Language Analysis\Files Copying\Extreme MXF"  # Update folder path
# output_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\wav_extreme"
# processing_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Processing_Files"

# wav_log_file_path = os.path.join(output_folder, "wav_files.txt")
# processed_log_file_path = os.path.join(processing_folder, "processing_final_stage_files.txt")
# spanish_log_file_path = os.path.join(processing_folder, "spanish_files.txt")
# delete_wav_log_file_path = os.path.join(processing_folder, "delete_wav_files.txt")

# # Ensure necessary folders exist
# os.makedirs(output_folder, exist_ok=True)
# os.makedirs(processing_folder, exist_ok=True)

# # FFmpeg path
# ffmpeg_path = r"C:\Users\hgada\Downloads\ffmpeg\ffmpeg.exe"

# # Load already logged files to avoid reprocessing
# logged_files = set()
# if os.path.exists(wav_log_file_path):
#     with open(wav_log_file_path, "r") as log_file:
#         logged_files = {line.split(" -> ")[0] for line in log_file.readlines()}

# # Get today's date
# today_date = datetime.datetime.today().strftime('%m%d%Y')

# # Process MXF files and immediately check for language and analyze
# os.environ["PATH"] = r"C:\msys64\mingw64\bin" + os.pathsep + os.environ["PATH"]
# AudioSegment.ffmpeg = r"C:\msys64\mingw64\bin\ffmpeg.exe"
# AudioSegment.converter = r"C:\msys64\mingw64\bin\ffmpeg.exe"

# def detect_language(audio_file):
#     model = whisper.load_model("base")
#     result = model.transcribe(audio_file)
#     return result['language'] == 'es'

# # Load processed files log
# processed_files = set()
# if os.path.exists(processed_log_file_path):
#     with open(processed_log_file_path, "r", encoding="utf-8") as log_file:
#         processed_files = set(line.strip().split(" - ")[0] for line in log_file.readlines())

# # Convert MXF to WAV and process it
# mxf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mxf')]
# if mxf_files:
#     with open(wav_log_file_path, "a") as wav_log_file:
#         for mxf_file in mxf_files:
#             if mxf_file in logged_files:
#                 continue

#             input_file_path = os.path.join(input_folder, mxf_file)
#             modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(input_file_path)).strftime('%m%d%Y')

#             # Process only today's date
#             if modified_date == today_date:
#                 output_file_wav = os.path.join(output_folder, os.path.splitext(mxf_file)[0] + ".wav")
#                 command = f'"{ffmpeg_path}" -i "{input_file_path}" -acodec pcm_s16le -ar 44100 -ac 2 "{output_file_wav}"'
#                 try:
#                     subprocess.run(command, shell=True, check=True)
#                     wav_log_file.write(f"{mxf_file} -> {output_file_wav}\n")
                    
#                     # Delete the original MXF file after conversion
#                     os.remove(input_file_path)
#                     with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
#                         delete_file.write(f"{mxf_file} - Deleted - {modified_date}\n")
                    
#                     # Immediately analyze the converted WAV file
#                     if output_file_wav.endswith(".wav"):
#                         is_spanish = detect_language(output_file_wav)
#                         if is_spanish:
#                             with open(spanish_log_file_path, "a", encoding="utf-8") as spanish_file:
#                                 spanish_file.write(f"{mxf_file} - {modified_date}\n")
                        
#                         # Log the processed file
#                         with open(processed_log_file_path, "a", encoding="utf-8") as processed_file:
#                             processed_file.write(f"{mxf_file} - Processed - {modified_date}\n")
                        
#                         # Delete the WAV file after processing
#                         os.remove(output_file_wav)
#                         with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
#                             delete_file.write(f"{mxf_file} - Deleted - {modified_date}\n")

#                 except subprocess.CalledProcessError as e:
#                     print(f"Error converting {mxf_file}: {e}")

# print("All conversions and processing complete.")


##not only today's file it should take, take any if present in that source folder



# import os
# import subprocess
# import whisper
# import datetime
# from pydub import AudioSegment

# # Set up paths
# input_folder = r"T:\Spanish Language Analysis\Files Copying\Extreme MXF"  # Update folder path
# output_folder = r"T:\Spanish Language Analysis\Wav Files Conversion\wav_extreme"
# processing_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Processing_Files"

# wav_log_file_path = os.path.join(output_folder, "wav_files.txt")
# processed_log_file_path = os.path.join(processing_folder, "processing_final_stage_files.txt")
# spanish_log_file_path = os.path.join(processing_folder, "extreme_spanish_files.txt")
# delete_wav_log_file_path = os.path.join(processing_folder, "delete_wav_files.txt")

# # Ensure necessary folders exist
# os.makedirs(output_folder, exist_ok=True)
# os.makedirs(processing_folder, exist_ok=True)

# # FFmpeg path
# ffmpeg_path = r"C:\Users\hgada\Downloads\ffmpeg\ffmpeg.exe"

# # Load already logged files to avoid reprocessing
# logged_files = set()
# if os.path.exists(wav_log_file_path):
#     with open(wav_log_file_path, "r") as log_file:
#         logged_files = {line.split(" -> ")[0] for line in log_file.readlines()}

# # Get today's date
# today_date = datetime.datetime.today().strftime('%m%d%Y')

# # Process MXF files and immediately check for language and analyze
# os.environ["PATH"] = r"C:\msys64\mingw64\bin" + os.pathsep + os.environ["PATH"]
# AudioSegment.ffmpeg = r"C:\msys64\mingw64\bin\ffmpeg.exe"
# AudioSegment.converter = r"C:\msys64\mingw64\bin\ffmpeg.exe"

# def detect_language(audio_file):
#     model = whisper.load_model("base")
#     result = model.transcribe(audio_file)
#     return result['language'] == 'es'

# # Load processed files log
# processed_files = set()
# if os.path.exists(processed_log_file_path):
#     with open(processed_log_file_path, "r", encoding="utf-8") as log_file:
#         processed_files = set(line.strip().split(" - ")[0] for line in log_file.readlines())

# # Convert MXF to WAV and process it
# mxf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mxf')]
# if mxf_files:
#     with open(wav_log_file_path, "a") as wav_log_file:
#         for mxf_file in mxf_files:
#             if mxf_file in logged_files:
#                 continue

#             input_file_path = os.path.join(input_folder, mxf_file)
#             modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(input_file_path)).strftime('%m%d%Y')

#             output_file_wav = os.path.join(output_folder, os.path.splitext(mxf_file)[0] + ".wav")
#             command = f'"{ffmpeg_path}" -i "{input_file_path}" -acodec pcm_s16le -ar 44100 -ac 2 "{output_file_wav}"'
#             try:
#                 subprocess.run(command, shell=True, check=True)
#                 wav_log_file.write(f"{mxf_file} -> {output_file_wav}\n")
                
#                 # Delete the original MXF file after conversion
#                 os.remove(input_file_path)
#                 with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
#                     delete_file.write(f"{mxf_file} - Deleted - {modified_date}\n")
                
#                 # Immediately analyze the converted WAV file
#                 if output_file_wav.endswith(".wav"):
#                     is_spanish = detect_language(output_file_wav)
#                     if is_spanish:
#                         with open(spanish_log_file_path, "a", encoding="utf-8") as spanish_file:
#                             spanish_file.write(f"{mxf_file} - {modified_date}\n")
                    
#                     # Log the processed file
#                     with open(processed_log_file_path, "a", encoding="utf-8") as processed_file:
#                         processed_file.write(f"{mxf_file} - Processed - {modified_date}\n")
                    
#                     # Delete the WAV file after processing
#                     os.remove(output_file_wav)
#                     with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
#                         delete_file.write(f"{mxf_file} - Deleted - {modified_date}\n")

#             except subprocess.CalledProcessError as e:
#                 print(f"Error converting {mxf_file}: {e}")

# print("All conversions and processing complete.")



# import os
# import subprocess
# import whisper
# import datetime
# from pydub import AudioSegment

# # Set up paths
# input_folder = r"T:\Spanish Language Analysis\Files Copying\Extreme MXF"  # MXF Source Folder
# output_folder = r"T:\Spanish Language Analysis\Wav Files Conversion\wav_extreme"  # WAV Output Folder
# processing_folder = r"T:\Spanish Language Analysis\Copying HTVMotor_Extreme\Processing_Files"

# wav_log_file_path = os.path.join(output_folder, "wav_extreme_files.txt")
# processed_log_file_path = os.path.join(processing_folder, "extreme_processing_final_stage_files.txt")
# spanish_log_file_path = os.path.join(processing_folder, "extreme_spanish_files.txt")
# delete_wav_log_file_path = os.path.join(processing_folder, "delete_wav_files.txt")

# # Ensure necessary folders exist
# os.makedirs(output_folder, exist_ok=True)
# os.makedirs(processing_folder, exist_ok=True)

# # FFmpeg path
# ffmpeg_path = r"C:\Users\hgada\Downloads\ffmpeg\ffmpeg.exe"

# # Load already logged files to avoid reprocessing
# logged_files = set()
# if os.path.exists(wav_log_file_path):
#     with open(wav_log_file_path, "r") as log_file:
#         logged_files = {line.split(" -> ")[0] for line in log_file.readlines()}

# # Get today's date
# today_date = datetime.datetime.today().strftime('%m%d%Y')

# # Configure FFmpeg for pydub
# os.environ["PATH"] = r"C:\msys64\mingw64\bin" + os.pathsep + os.environ["PATH"]
# AudioSegment.ffmpeg = r"C:\msys64\mingw64\bin\ffmpeg.exe"
# AudioSegment.converter = r"C:\msys64\mingw64\bin\ffmpeg.exe"

# def detect_language(audio_file):
#     """Detects if the audio file is in Spanish using Whisper AI."""
#     model = whisper.load_model("base")
#     result = model.transcribe(audio_file)
#     return result['language'] == 'es'

# # Load processed files log
# processed_files = set()
# if os.path.exists(processed_log_file_path):
#     with open(processed_log_file_path, "r", encoding="utf-8") as log_file:
#         processed_files = set(line.strip().split(" - ")[0] for line in log_file.readlines())

# # Convert MXF to WAV and process it
# mxf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mxf')]

# if mxf_files:
#     with open(wav_log_file_path, "a") as wav_log_file:
#         for mxf_file in mxf_files:
#             if mxf_file in logged_files:
#                 continue

#             input_file_path = os.path.join(input_folder, mxf_file)
#             modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(input_file_path)).strftime('%m%d%Y')

#             output_file_wav = os.path.join(output_folder, os.path.splitext(mxf_file)[0] + ".wav")
#             command = f'"{ffmpeg_path}" -i "{input_file_path}" -acodec pcm_s16le -ar 44100 -ac 2 "{output_file_wav}"'

#             try:
#                 subprocess.run(command, shell=True, check=True)
#                 wav_log_file.write(f"{mxf_file} -> {output_file_wav}\n")

#                 # Delete the original MXF file after successful conversion
#                 try:
#                     os.remove(input_file_path)
#                     with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
#                         delete_file.write(f"{mxf_file} - Deleted - {modified_date}\n")
#                 except Exception as e:
#                     print(f"Error deleting {mxf_file}: {e}")

#                 # Analyze the converted WAV file
#                 if output_file_wav.endswith(".wav"):
#                     is_spanish = detect_language(output_file_wav)
#                     if is_spanish:
#                         with open(spanish_log_file_path, "a", encoding="utf-8") as spanish_file:
#                             spanish_file.write(f"{mxf_file} - {modified_date}\n")

#                     # Log the processed file
#                     with open(processed_log_file_path, "a", encoding="utf-8") as processed_file:
#                         processed_file.write(f"{mxf_file} - Processed - {modified_date}\n")

#                     # Delete the WAV file after processing
#                     try:
#                         os.remove(output_file_wav)
#                         with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
#                             delete_file.write(f"{mxf_file} - Deleted - {modified_date}\n")
#                     except Exception as e:
#                         print(f"Error deleting {output_file_wav}: {e}")

#             except subprocess.CalledProcessError as e:
#                 print(f"Error converting {mxf_file}: {e}")

# print("All conversions and processing complete.")



###with Email:

import os
import subprocess
import whisper
import datetime
from pydub import AudioSegment
import win32com.client as win32

# Set up paths
input_folder = r"T:\Spanish Language Analysis\Files Copying\Extreme MXF"  # MXF Source Folder
output_folder = r"T:\Spanish Language Analysis\Wav Files Conversion\wav_extreme"  # WAV Output Folder
processing_folder = r"T:\Spanish Language Analysis\Wav Files Conversion\Processing_Files"
spanish_folder = r"T:\Spanish Language Analysis\Spanish Language Detected"

wav_log_file_path = os.path.join(output_folder, "wav_extreme_files.txt")
processed_log_file_path = os.path.join(processing_folder, "extreme_processing_final_stage_files.txt")
spanish_log_file_path = os.path.join(spanish_folder, "extreme_spanish_files.txt")
delete_wav_log_file_path = os.path.join(processing_folder, "delete_extreme_wav_files.txt")

# Ensure necessary folders exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(processing_folder, exist_ok=True)

# FFmpeg path
ffmpeg_path = r"C:\Users\hgada\Downloads\ffmpeg\ffmpeg.exe"

# Load already logged files to avoid reprocessing
logged_files = set()
if os.path.exists(wav_log_file_path):
    with open(wav_log_file_path, "r") as log_file:
        logged_files = {line.split(" -> ")[0] for line in log_file.readlines()}

# Configure FFmpeg for pydub
os.environ["PATH"] = r"C:\msys64\mingw64\bin" + os.pathsep + os.environ["PATH"]
AudioSegment.ffmpeg = r"C:\msys64\mingw64\bin\ffmpeg.exe"
AudioSegment.converter = r"C:\msys64\mingw64\bin\ffmpeg.exe"

def detect_language(audio_file):
    """Detects if the audio file is in Spanish using Whisper AI."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    return result['language'] == 'es'

def send_email_with_outlook(latest_spanish_file, modified_date):
    """Send an email using Outlook through win32com"""
    
    # Create an Outlook application object
    outlook = win32.Dispatch('Outlook.Application')
    
    # Create a new mail item (email)
    mail = outlook.CreateItem(0)
    
    # Set up the email subject with the file name
    mail.Subject = f'Spanish Language Detected for Extreme Reach: {latest_spanish_file}'
    
    # Construct the email body
    mail.Body = f"""Hey Team, 

Detected Spanish Language Video: {latest_spanish_file}  
Date & Time: {modified_date}  

Best,  
Hetal"""  # Your name in the email body

    # Set recipient
    mail.To = 'Omar.Zahraman@hearst.com'  # Replace with the recipient's email
    mail.CC = 'hetal.gada@hearst.com'
    try:
        # Send the email
        mail.Send()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Convert MXF to WAV and process it
mxf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mxf')]

if mxf_files:
    with open(wav_log_file_path, "a") as wav_log_file:
        latest_spanish_file = None  # To hold the latest Spanish detected file name
        latest_modified_date = None  # To store the date of the latest detected Spanish file

        for mxf_file in mxf_files:
            if mxf_file in logged_files:
                continue

            input_file_path = os.path.join(input_folder, mxf_file)
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(input_file_path)).strftime('%m-%d-%Y %I:%M %p')  # Changed format to include time

            output_file_wav = os.path.join(output_folder, os.path.splitext(mxf_file)[0] + ".wav")
            command = f'"{ffmpeg_path}" -i "{input_file_path}" -acodec pcm_s16le -ar 44100 -ac 2 "{output_file_wav}"'

            try:
                subprocess.run(command, shell=True, check=True)
                wav_log_file.write(f"{mxf_file} -> {output_file_wav}\n")

                # Delete the original MXF file after successful conversion
                try:
                    os.remove(input_file_path)
                    with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
                        delete_file.write(f"{mxf_file} - Deleted - {modified_date}\n")
                except Exception as e:
                    print(f"Error deleting {mxf_file}: {e}")

                # Analyze the converted WAV file
                if output_file_wav.endswith(".wav"):
                    is_spanish = detect_language(output_file_wav)
                    if is_spanish:
                        latest_spanish_file = mxf_file  # Update with the latest detected Spanish file
                        latest_modified_date = modified_date  # Store the date of the detected Spanish file
                        with open(spanish_log_file_path, "a", encoding="utf-8") as spanish_file:
                            spanish_file.write(f"{mxf_file} - {modified_date}\n")

                    # Log the processed file
                    with open(processed_log_file_path, "a", encoding="utf-8") as processed_file:
                        processed_file.write(f"{mxf_file} - Processed - {modified_date}\n")

                    # Delete the WAV file after processing
                    try:
                        os.remove(output_file_wav)
                        with open(delete_wav_log_file_path, "a", encoding="utf-8") as delete_file:
                            delete_file.write(f"{mxf_file} - Deleted - {modified_date}\n")
                    except Exception as e:
                        print(f"Error deleting {output_file_wav}: {e}")

            except subprocess.CalledProcessError as e:
                print(f"Error converting {mxf_file}: {e}")

        # After processing all files, send the email with the latest Spanish file detected
        if latest_spanish_file and latest_modified_date:
            send_email_with_outlook(latest_spanish_file, latest_modified_date)

print("All conversions and processing complete.")
