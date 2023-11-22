from PIL import Image, ImageEnhance
def BlackAndWhite(image,output,save=1):
    img=Image.open(image)
    NameImage=image
    for i in range(len(image)):
        if image[i]=='/':
            NameImage=image[i+1:]
    filter = ImageEnhance.Color(img)
    img = filter.enhance(0)
    if save==1:
        img.save(f"{output}/BlackAndWhiteOf{NameImage}")
        return str(f"{output}/BlackAndWhiteOf{NameImage}")
    else:
        img.save(f"temps/BlackAndWhiteOf{NameImage}")
        return str(f"temps/BlackAndWhiteOf{NameImage}")