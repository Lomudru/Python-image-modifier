from PIL import Image, ImageFilter
def Blurred(image,output,save=1):
    """
    Convertie l'image mit en paramètre
    ex : >>> Blurred("../grimm.jpeg","img")
    renvoie une image floutée et la sauvegarde dans le dossier img"""
    img=Image.open(image)
    img = img.filter(ImageFilter.BoxBlur(10))
    NameImage = image
    for i in range(len(image)):
        if image[i]=='/':
            NameImage=image[i+1:]
    if save==1:
        img.save(f"{output}/BlurredOf{NameImage}")
        return str(f"{output}/BlurredOf{NameImage}")
    else:
        img.save(f"temps/BlurredOf{NameImage}")
        return str(f"temps/BlurredOf{NameImage}")