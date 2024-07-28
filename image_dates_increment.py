import os
import re
from datetime import datetime, timedelta
import platform
import subprocess

def change_file_creation_date(file_path, new_date):
    """
    Change the creation date of the file to new_date.
    """
    new_date_str = new_date.strftime('%Y%m%d%H%M.%S')

    if platform.system() == 'Windows':
        new_date_str = new_date.strftime('%Y-%m-%dT%H:%M:%S')
        subprocess.run(['powershell', '(Get-Item "{}").CreationTime=("{}")'.format(file_path, new_date_str)])
        subprocess.run(['powershell', '(Get-Item "{}").LastWriteTime=("{}")'.format(file_path, new_date_str)])
    else:
        os.utime(file_path, (new_date.timestamp(), new_date.timestamp()))

def update_photo_dates_incremental(directory):
    """
    Update the creation dates of photos in the given directory, starting from a specific date
    and incrementing by 1 day for each photo.
    """
    start_date = datetime(2023, 10, 1)
    current_date = start_date

    # Get list of all files in the directory
    files = os.listdir(directory)
    files.sort()  # Sort files to ensure they are processed in a specific order

    for filename in files:
        if filename.endswith('.jpg'):  # Check if the file is a jpg image
            file_path = os.path.join(directory, filename)
            change_file_creation_date(file_path, current_date)
            print(f'Updated {filename} to {current_date}')
            current_date += timedelta(days=1)  # Increment the date by 1 day

# Usage
directory_path = r'C:\Users\Anwender\Desktop\Samsung\Cloud invalid timestamp'
update_photo_dates_incremental(directory_path)
