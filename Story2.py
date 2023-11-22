from PIL import Image, ImageFilter
import os

def Blurred(image,output,save=1):
    """
    Convertie l'image mit en paramètre
    ex : >>> Blurred("../grimm.jpeg","img")
    renvoie une image floutée et la sauvegarde dans le dossier img
    """

    _, ext = os.path.splitext(image)
    if ext not in ('.jpg', '.jpeg', '.png'):
        print("Vous devez mettre en paramètre le chemin d'une image en format .jpg, .jpeg ou .png (Blurred)")
        return
    
    try:
        # Sauvegarde l'image mit en paramètre dans la variable img
        img=Image.open(image)

    except:
        print("Le chemin vers l'image n'est pas bon ou n'existe pas. (Blurred)")
        return

    # Applique le filtre
    img = img.filter(ImageFilter.BoxBlur(10))

    # Vérifie si le chemin vers l'image contient des dossiers pour ne garder que le nom de l'image et son extension
    NameImage = image
    for i in range(len(image)):
        if image[i]=='/':
            NameImage=image[i+1:]

    try:
        # Sauvegarde l'image ou le met dans un dossier temporaire temps
        if save==1:
            img.save(f"{output}/BlurredOf{NameImage}")
            return str(f"{output}/BlurredOf{NameImage}")
        else:
            img.save(f"temps/BlurredOf{NameImage}")
            return str(f"temps/BlurredOf{NameImage}")
    except:
        print("Le chemin vers la sauvegarde de votre image modifié n'est pas bon ou n'existe pas. (Blurred)")
        return