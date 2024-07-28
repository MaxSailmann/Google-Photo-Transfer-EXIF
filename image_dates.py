import os
import re
from datetime import datetime
import platform
import subprocess

def change_file_creation_date(file_path, new_date):
    """
    Change the creation date of the file to new_date.
    """
    # Convert new_date to a format suitable for the `touch` command
    new_date_str = new_date.strftime('%Y%m%d%H%M.%S')

    if platform.system() == 'Windows':
        # On Windows, use powershell to change the creation time
        new_date_str = new_date.strftime('%Y-%m-%dT%H:%M:%S')
        subprocess.run(['powershell', '(Get-Item "{}").CreationTime=("{}")'.format(file_path, new_date_str)])
        subprocess.run(['powershell', '(Get-Item "{}").LastWriteTime=("{}")'.format(file_path, new_date_str)])
    else:
        # On Unix-based systems, use the touch command to set the modification time
        os.utime(file_path, (new_date.timestamp(), new_date.timestamp()))

def update_photo_dates(directory):
    """
    Update the creation dates of photos in the given directory based on their filenames.
    """
    i = 0
    for filename in os.listdir(directory):
        if filename.startswith('VID-') and filename.endswith('.mp4'):
            match = re.match(r'VID-(\d{4})(\d{2})(\d{2})-WA\d{4}\.mp4', filename)
            if match:
                i += 1
                year, month, day = match.groups()
                new_date = datetime(int(year), int(month), int(day))
                file_path = os.path.join(directory, filename)
                change_file_creation_date(file_path, new_date)
                print(f'Updated {filename} to {new_date}')
    print(i)

# Usage
directory_path = r'C:\Users\Anwender\Desktop\Samsung\Cloud timestamp fix'
update_photo_dates(directory_path)
