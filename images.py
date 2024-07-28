import os
from PIL import Image
from PIL.ExifTags import TAGS
import datetime

def list_pictures(folder):
    """List all pictures in the given folder."""
    picture_files = []
    for root, _, files in os.walk(folder):
        for file in files:            
            picture_files.append(file)
    return picture_files

def rename_pictures(file_path):
    return

def delete_files(folder, filenames):
    """Delete files in the given folder if they exist in the filenames array."""
    i = 1
    for filename in filenames:
        print(i)
        i += 1
        file_path = os.path.join(folder, filename)
        if os.path.exists(file_path):
            #os.remove(file_path)
            print(f"Deleted: {file_path}")


def get_date_taken(path):
    exif = Image.open(path)._getexif()
    if not exif:
        raise Exception('Image {0} does not have EXIF data.'.format(path))
    else:
        print(exif[36867])
    #return exif[36867]

def rename_pictures(folder, filenames):
    """Rename pictures based on the date they were taken."""
    for filename in filenames:
        file_path = os.path.join(folder, filename)
        if os.path.exists(file_path):
            #print(file_path)
            date_taken = get_date_taken(file_path)
            if date_taken:
                date_str = date_taken.strftime('%Y-%m-%d')
                new_name = f"{date_str}_{filename}"
                new_file_path = os.path.join(folder, new_name)
                #os.rename(file_path, new_file_path)
                print(f"Renamed: {file_path} to {new_file_path}")
            else:
                #print(f"No date taken information for: {file_path}")
                pass
        else:
            print(f"File not found: {file_path}")
            

# Example usage
cloud = r'C:\Users\Anwender\Desktop\Samsung\Cloud'
cloud_pictures = list_pictures(cloud)

gag = r'C:\Users\Anwender\Desktop\Samsung\9GAG'
gag_pictures = list_pictures(gag)

cam = r'C:\Users\Anwender\Desktop\Samsung\Kamera'
cam_pictures = list_pictures(cam)

scr = r'C:\Users\Anwender\Desktop\Samsung\Screenshots'
scr_pictures = list_pictures(scr)

wai = r'C:\Users\Anwender\Desktop\Samsung\WhatsApp Images'
wai_pictures = list_pictures(wai)

wav = r'C:\Users\Anwender\Desktop\Samsung\WhatsApp Video'
wav_pictures = list_pictures(wav)

all_pictures = gag_pictures + cam_pictures + scr_pictures + wai_pictures + wav_pictures
paths = [cloud, gag, cam, scr, wai, wav]

#delete_files(cloud, all_pictures)
rename_pictures(gag, gag_pictures)
