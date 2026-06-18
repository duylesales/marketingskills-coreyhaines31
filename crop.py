import sys
from PIL import Image

def crop_center_16_9(src_path, dst_path):
    try:
        img = Image.open(src_path)
        width, height = img.size
        target_height = int(width * 9 / 16)
        
        top = (height - target_height) // 2
        bottom = top + target_height
        
        cropped = img.crop((0, top, width, bottom))
        
        if cropped.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', cropped.size, (255, 255, 255))
            background.paste(cropped, mask=cropped.split()[3])
            cropped = background
        elif cropped.mode != 'RGB':
            cropped = cropped.convert('RGB')
            
        cropped.save(dst_path, 'JPEG', quality=95)
        print(f'Cropped successfully: {dst_path}')
    except Exception as e:
        print(f'Error cropping {src_path}: {e}')

if __name__ == "__main__":
    crop_center_16_9(sys.argv[1], sys.argv[2])
