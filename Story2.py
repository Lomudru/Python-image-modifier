from PIL import Image, ImageFilter
def Blurred(image,output):
    """
    Convertie l'image mit en paramètre
    ex : >>> Blurred("../grimm.jpeg","img")
    renvoie une image floutée et la sauvegarde dans le dossier img"""
    img=Image.open(image)
    img = img.filter(ImageFilter.BoxBlur(10))
    img.show()
    img.save(f"{output}/BlurredOf{image}")
Blurred("grimm.jpeg","img")

