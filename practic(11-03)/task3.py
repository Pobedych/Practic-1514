from PIL import Image

def twist_image(input_file_name, output_file_name):
    img = Image.open(input_file_name)

    w, h = img.size

    left = img.crop((0,0,w//2,h))
    right = img.crop((w//2,0,w,h))

    new_img = Image.new("RGB", (w,h))
    new_img.paste(right,(0,0))
    new_img.paste(left,(w//2,0))

    new_img.save(output_file_name)

twist_image("3.jpg", "new_3.jpg")