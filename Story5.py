from PIL import Image
import cv2

def Resize(image,output, largeur, longueur,save=1):
    """
    Convertie l'image mit en paramètre
    ex : >>> Resize("grimm.jpeg","img", 0.5, 0.5)
    renvoie une image redimensionnée et deux foix plus petite et la sauvegarde dans le dossier img"""
    # Sauvegarde l'image mit en paramètre dans la variable img
    img=Image.open(image)
    # Sauvegarde la largeur et la hauteur de l'image pour les mettre dans les variables whidth et height
    im = cv2.imread(image)
    whidth = im.shape[1]
    height = im.shape[0]
    # Applique le filtre en multipliant la largeur et la longueur par les facteurs mis en paramètres
    img = img.resize((round(whidth * largeur), round(height * longueur)))
    # Vérifie si le chemin vers l'image contient des dossiers pour ne garder que le nom de l'image et son extension
    NameImage = image
    for i in range(len(image)):
        if image[i]=='/':
            NameImage=image[i+1:]
    # Sauvegarde l'image ou le met dans un dossier temporaire temps
    if save==1:
        img.save(f"{output}/ResizeOf{NameImage}")
        return str(f"{output}/ResizeOf{NameImage}")
    else:
        img.save(f"temps/ResizeOf{NameImage}")
        return str(f"temps/ResizeOf{NameImage}")