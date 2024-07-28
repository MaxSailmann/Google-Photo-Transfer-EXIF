import os
import subprocess

def list_videos(folder):
    """List all video files in the given folder."""
    video_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):  # Add other video formats if needed
                video_files.append(os.path.join(root, file))
    return video_files

def add_creation_date_with_ffmpeg(video_path, creation_time):
    ffmpeg_path = r'C:\Users\Anwender\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe'  # Update with the actual path
    
    output_path = os.path.join(os.path.dirname(video_path), 'output_' + os.path.basename(video_path))
    command = [
        ffmpeg_path,
        '-i', video_path,
        '-metadata', f'creation_time={creation_time}',
        '-codec', 'copy', output_path
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Creation time added successfully to {output_path}")
    else:
        print(f"Error adding creation time to {video_path}: {result.stderr}")

def extract_date_from_filename(filename):
    # Extract date from filename assuming format "VID-YYYYMMDD-WAxxxx"
    base_name = os.path.basename(filename)
    date_part = base_name.split('-')[1]
    year = date_part[:4]
    month = date_part[4:6]
    day = date_part[6:8]
    return f'{year}-{month}-{day}T00:00:00'  # Defaulting time to 00:00:00

def process_videos(video_list):
    for video_path in video_list:
        creation_time = extract_date_from_filename(video_path)
        print(creation_time)
        add_creation_date_with_ffmpeg(video_path, creation_time)
        print(f"Processed {video_path} with date {creation_time}")

wav = r'C:\Users\Anwender\Desktop\Samsung\Cloud timestamp fix'
video_files = list_videos(wav)
print(f"Found {len(video_files)} video files.")
process_videos(video_files)
