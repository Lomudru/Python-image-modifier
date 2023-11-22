from PIL import Image, ImageFilter
def Blurred(image,output):
    """
    Convertie l'image mit en paramètre
    ex : >>> Blurred("../grimm.jpeg","img")
    renvoie une image floutée et la sauvegarde dans le dossier img
    """
    # Sauvegarde l'image mit en paramètre dans la variable img
    img=Image.open(image)
    # Applique le filtre
    img = img.filter(ImageFilter.BoxBlur(10))
    # Vérifie si le chemin vers l'image contient des dossiers pour ne garder que le nom de l'image et son extension
    NameImage = image
    for i in range(len(image)):
        if image[i]=='/':
            NameImage=image[i+1:]
    
    img.show()
    img.save(f"{output}/BlurredOf{NameImage}")
Blurred("grimm.jpeg","img")