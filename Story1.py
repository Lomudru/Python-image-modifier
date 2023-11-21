from PIL import Image, ImageEnhance
def BlackAndWhite(image,output):
    img=Image.open(image)
    filter = ImageEnhance.Color(img)
    img = filter.enhance(0)
    img.show()
    img.save(f"{output}/BlackAndWhiteOf{image}")