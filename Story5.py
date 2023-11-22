from PIL import Image
import cv2
import os

def Resize(image,output, largeur, longueur,save=1):
    """
    Convertie l'image mit en paramètre
    ex : >>> Resize("grimm.jpeg","img", 0.5, 0.5)
    renvoie une image redimensionnée et deux foix plus petite et la sauvegarde dans le dossier img
    """
    _, ext = os.path.splitext(image)
    if ext not in ('.jpg', '.jpeg', '.png'):
        print("Vous devez mettre en paramètre le chemin d'une image en format .jpg, .jpeg ou .png (Resize)")
        return
    
    if not(isinstance(longueur, (float, int))) or not(isinstance(largeur, (float, int))):
        print('Vous devez rentrer des nombres entiers ou flottants en paramètre de Resize.')
        return


    # Sauvegarde l'image mit en paramètre dans la variable img
    try:
        img=Image.open(image)

    except:
        print("Le chemin vers l'image n'est pas bon ou n'existe pas. (Resize)")
        return
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
    try:
        if save==1:
            img.save(f"{output}/ResizeOf{NameImage}")
            return str(f"{output}/ResizeOf{NameImage}")
        else:
            img.save(f"temps/ResizeOf{NameImage}")
            return str(f"temps/ResizeOf{NameImage}")
    except:
        print("Le chemin vers la sauvegarde de votre image modifié n'est pas bon ou n'existe pas. (Resize)")
        return 

Resize('teste.png','imageAModif', 0.5, 0.5)