from PIL import Image, ImageEnhance
from logger import *
import os

def BlackAndWhite(image,output,save=1):

    _, ext = os.path.splitext(image)
    if ext not in ('.jpg', '.jpeg', '.png'):
        print("Vous devez mettre en paramètre le chemin d'une image en format .jpg, .jpeg ou .png (BAW)")
        log(f"Erreur d'extension de l'image {image} dans BAW")
        return

    try:
        img=Image.open(image) # On Ouvre L'image 

    except:
        print("Le chemin vers l'image n'est pas bon ou n'existe pas. (BAW)")
        log(f"Erreur de chemin de l'image {image} dans BAW")
        return
    NameImage=image # NameImage est le chemin de l'image
    for i in range(len(image)): # Boucle qui parcours les charactère du chemin de l'image 
        if image[i]=='/': # Si il y as un "/"
            NameImage=image[i+1:] # On prend que ce qu'il y as après
    filter = ImageEnhance.Color(img) # On applique la couleur noir et blanc a l'image
    img = filter.enhance(0) 
    log(f"{NameImage} transformé en noir et blanc")

    try: 
        if save==1: # Vérifie si l'orsque l'on a appeler la fonction l'utilisateur veut sauvegarder l'image
            img.save(f"{output}/BlackAndWhiteOf{NameImage}")
            log(f"{NameImage} sauvegardée dans {output} (BAW)")
            return str(f"{output}/BlackAndWhiteOf{NameImage}")
        else:
            img.save(f"temps/BlackAndWhiteOf{NameImage}")
            log(f"{NameImage} sauvegardée dans temps/ (BAW)")
            return str(f"temps/BlackAndWhiteOf{NameImage}")
    except:
        print("Le chemin vers la sauvegarde de votre image modifié n'est pas bon ou n'existe pas. (BAW)")
        log(f"Erreur pour le chemin de sauvegarde de {NameImage} dans BAW.")
        return