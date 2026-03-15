from PIL import Image

def make_preview(size, n_colors):
    img = Image.open("image4.jpg")

    img = img.resize(size)
    img = img.quantize(colors=n_colors)

    img.save("res.bmp")

make_preview((400, 200), 65)