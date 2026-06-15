#pip install pillow

from PIL import Image
from PIL.ExifTags import TAGS

from pathlib import Path
from datetime import datetime

#For HEIC files
import pillow_heif
pillow_heif.register_heif_opener()


jpg_path = Path("path/to/image.jpg")

# Date types:

# Image Metadata:
# DateTimeOriginal
# DateTimeDigitized
# DateTime

# File metadata:
# st_atime     - accessed
# st_mtime     - modified
# st_ctime     - changed
# st_birthtime - created


# Image
with Image.open(jpg_path) as img:
    info = img.info  #metadata dictionary
    exif_data = img.getexif()

tag_dict = {
    TAGS.get(tag, tag): value
    for tag, value
    in exif_data.items()}

print(info)
print(tag_dict)
print("\n")


# File
stats = jpg_path.stat()
print(type(stats))
accessed = str(datetime.fromtimestamp(stats.st_atime))
modified = str(datetime.fromtimestamp(stats.st_mtime))
changed = str(datetime.fromtimestamp(stats.st_ctime))
created = str(datetime.fromtimestamp(stats.st_birthtime))
print(accessed)
print(modified)
print(changed)
print(created)
