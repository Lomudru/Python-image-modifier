from PIL import Image
def Resize(image,output):
    """
    Convertie l'image mit en paramètre
    ex : >>> Blurred("../grimm.jpeg","img")
    renvoie une image floutée et la sauvegarde dans le dossier img"""
    img=Image.open(image)
    img = img.resize((500, 256))
    for i in range(len(image)):
        if image[i]=='/':
            NameImage=image[i+1:]
    NameImage = image
    img.show()
    img.save(f"{output}/ResizeOf{NameImage}")
Resize("grimm.jpeg","img")