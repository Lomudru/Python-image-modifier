from PIL import Image, ImageFilter
def Blurred(image,output):
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
    
    img.show()
    img.save(f"{output}/BlurredOf{NameImage}")
Blurred("grimm.jpeg","img")