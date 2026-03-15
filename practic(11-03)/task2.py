from PIL import Image, ImageDraw


img = Image.new("RGB", (500, 220), "white")
draw = ImageDraw.Draw(img)

# Буква Л
draw.line((40, 180, 80, 40), fill="black", width=8)
draw.line((80, 40, 120, 180), fill="black", width=8)

# Буква Е
draw.line((170, 40, 170, 180), fill="black", width=8)
draw.line((170, 40, 250, 40), fill="black", width=8)
draw.line((170, 110, 235, 110), fill="black", width=8)
draw.line((170, 180, 250, 180), fill="black", width=8)

# Буква В
draw.line((300, 40, 300, 180), fill="black", width=8)
draw.rectangle((300, 40, 380, 105), outline="black", width=8)
draw.rectangle((300, 105, 380, 180), outline="black", width=8)

img.save("name.png")
