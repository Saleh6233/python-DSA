from PIL import Image, ImageFilter
# img = Image.open("./Pokedex/210 - pikachu.jpg")
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("blurPikachu.png", 'png')

# filtered_img = img.convert('L')
# filtered_img.save("greyPikachu.png", 'png')
# filtered_img.show()
# crooked = filtered_img.rotate(180)
# crooked.save("greyPikachu.png", 'png')

# resize = filtered_img.resize((300, 300))
# resize.save("greyPikachu.png", 'png')

# box1 = (100, 100, 400, 400)
# region = filtered_img.crop(box1)
# region.save("greyPikachu.png", 'png')

img = Image.open('./212 - astro.jpg')
print(img.size)

img.thumbnail((400, 400))
img.save('thumbnail.jpg')

print(img.size)
