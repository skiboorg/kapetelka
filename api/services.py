from random import choices
import string
from PIL import Image
from io import BytesIO


def create_slug(char_num):
    """Рандомный slug"""
    slug = ''.join(choices(string.ascii_lowercase + string.digits, k=char_num))
    return slug


def image_resize_and_watermark(image,watermarked,new_w,new_h):
    fill_color = '#fff'
    base_image = Image.open(image)
    if base_image.mode in ('RGBA', 'LA'):
        background = Image.new(base_image.mode[:-1], base_image.size, fill_color)
        background.paste(base_image, base_image.split()[-1])
        base_image = background
    blob = BytesIO()
    width, height = base_image.size
    transparent = Image.new('RGB', (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.thumbnail((new_w, new_h), Image.ANTIALIAS)
    if watermarked:
        watermark = Image.open('static/img/wm.png')
        transparent.paste(watermark, (50, 50), mask=watermark)
    # transparent.show()
    transparent.save(blob, 'JPEG')
    return blob
