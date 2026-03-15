from PIL import Image, ImageDraw

def board(num, size):
    img_size = num * size
    img = Image.new("RGB", (img_size, img_size))
    draw = ImageDraw.Draw(img)

    for y in range(num):
        for x in range(num):
            if (x + y) % 2 == 0:
                color = "black"
            else:
                color = "white"
            draw.rectangle((x * size, y * size, (x+1) * size-1, (y+1) * size - 1), fill=color)

    img.save("res.png")

board(8, 50)