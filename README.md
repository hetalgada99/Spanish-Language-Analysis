# Automated File Processing for Spanish Language Analysis

## Overview
This project automates the process of copying, converting, analyzing, and processing media files across multiple directories. The workflow includes file copying, audio extraction, language detection, logging, and automated email notifications.

## Workflow Summary
1. **File Copying:**
   - Copies `.mxf` files from source directories to a destination folder.
   - Ensures only new and recently modified files are processed.
   - Logs copied files to prevent duplicate processing.

2. **Conversion to WAV:**
   - Converts `.mxf` files to `.wav` format using FFmpeg.
   - Deletes the original `.mxf` files post-conversion.

3. **Language Detection:**
   - Uses Whisper AI to analyze the audio and detect Spanish language content.
   - Logs Spanish-identified files separately.

4. **Logging & Tracking:**
   - Maintains logs for copied, converted, processed, and deleted files.
   - Stores logs in a structured format for tracking and debugging.

5. **Automated Email Alerts:**
   - Sends an email notification when a Spanish-language file is detected.
   - Uses Microsoft Outlook via `win32com.client` to send alerts.

## Folder Structure
The script operates on seven main directories, each following the same automated workflow:

1. **Yangaroo MXF:**
   - Source: `\\htv-mstor\HTV-MSTOR\Systems\Florical\Incoming-AC\Yangaroo`
   - Destination: `T:\Spanish Language Analysis\Files Copying\Yangaroo MXF`
   - Processed files are converted to WAV and analyzed.

2. **Wav Files Conversion:**
   - Source: `T:\Spanish Language Analysis\Files Copying\Yangaroo MXF`
   - Output: `T:\Spanish Language Analysis\Wav Files Conversion\wav_yangaroo`
   - Logs conversion details in `wav_yangaroo_files.txt`.

3. **Processing Files:**
   - Stores intermediate logs and tracking files.
   - Maintains a log of processed files and deleted files.

4. **Spanish Language Detected:**
   - Stores logs of detected Spanish-language files.
   - Sends email notifications upon detection.

5. **FFmpeg Processing:**
   - Uses `ffmpeg.exe` for audio extraction.
   - Configured for `pydub` integration.

6. **Logging & Deletion Management:**
   - Logs details of all processed and deleted files.
   - Prevents reprocessing of files.

7. **Email Notification System:**
   - Sends automated alerts for Spanish-language detections.
   - Uses Outlook email client for notifications.

## Dependencies
- Python 3
- `ffmpeg`
- `whisper` (for AI language detection)
- `pydub`
- `win32com.client` (for Outlook email)
- `concurrent.futures` (for multi-threading file operations)

## Execution
- Run the script to process files automatically.
- Ensure FFmpeg and required dependencies are installed and configured.
- Monitor log files for any errors or missing files.

## Notes
- Ensure correct permissions to access network drives.
- Modify source and destination paths as needed.
- Email notifications require an active Outlook session.

## Contact
For any issues or enhancements, reach out to `hetal.gada@hearst.com`.

