from PIL import Image, ImageEnhance
def BlackAndWhite(image,output):
    img=Image.open(image)
    NameImage=image
    for i in range(len(image)):
        if image[i]=='/':
            NameImage=image[i+1:]
    filter = ImageEnhance.Color(img)
    img = filter.enhance(0)
    img.show()
    img.save(f"{output}/BlackAndWhiteOf{NameImage}")