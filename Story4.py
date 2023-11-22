from PIL import Image, ImageEnhance
def RotateImage(image,degre,output,save=1):
    img=Image.open(image)
    NameImage=image
    for i in range(len(image)):
        if image[i]=='/':
            NameImage=image[i+1:]
    out = img.rotate(degre, expand=1)
    if save==1:
        out.save(f"{output}/RotateImageOf{NameImage}")
        return str(f"{output}/RotateImageOf{NameImage}")
    else:
        out.save(f"temps/RotateImageOf{NameImage}")
        return str(f"temps/RotateImageOf{NameImage}")