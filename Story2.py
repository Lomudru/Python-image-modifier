from PIL import Image, ImageFilter
def Blurred(image,output,save=1):
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

    # Sauvegarde l'image ou le met dans un dossier temporaire temps
    if save==1:
        img.save(f"{output}/BlurredOf{NameImage}")
        return str(f"{output}/BlurredOf{NameImage}")
    else:
        img.save(f"temps/BlurredOf{NameImage}")
        return str(f"temps/BlurredOf{NameImage}")