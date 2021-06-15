from PIL import Image, ImageFilter

img = Image.open('./JPG/pikachu.jpg')

blured_img = img.filter(ImageFilter.BLUR)
blured_img.save("./JPG/blur.png", "png")

sharpen_img = img.filter(ImageFilter.SHARPEN)
sharpen_img.save("./JPG/sharp.png", "png")

grey_scale_img = img.convert('L')
grey_scale_img.save("./JPG/grey.png", "png")

grey_scale_img.show()

rotate_img = img.rotate(90)
rotate_img.save("./JPG/rotate.png", "png")

resized_img = img.resize((300, 300))
resized_img.save("./JPG/resized.png", "png")

cropped_img = img.crop((100, 100, 400, 400))
cropped_img.save("./JPG/cropped.png", "png")


