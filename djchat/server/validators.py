import os

from PIL import Image
from rest_framework.exceptions import ValidationError


def validate_icon_image_size(image):
    if image:
        with Image.open(image) as img:
            if img.width > 70 or img.height > 70:
                raise ValidationError(f"The allowed dimention of image are 70x70 size of image you uploaded are {img.width}x{img.height}")


def validate_image_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extenstions = [".jpg", ".jpeg", ".png", ".gif"]
    # 
    if not ext.lower() in valid_extenstions:
        raise ValidationError(f"Unsupported file extensions")