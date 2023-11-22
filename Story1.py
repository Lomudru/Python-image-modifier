from PIL import Image, ImageEnhance
import os

def BlackAndWhite(image,output,save=1):

    _, ext = os.path.splitext(image)
    if ext not in ('.jpg', '.jpeg', '.png'):
        print("Vous devez mettre en paramètre le chemin d'une image en format .jpg, .jpeg ou .png (BAW)")
        return

    try:
        img=Image.open(image) # On Ouvre L'image 

    except:
        print("Le chemin vers l'image n'est pas bon ou n'existe pas. (BAW)")
        return
    NameImage=image # NameImage est le chemin de l'image
    for i in range(len(image)): # Boucle qui parcours les charactère du chemin de l'image 
        if image[i]=='/': # Si il y as un "/"
            NameImage=image[i+1:] # On prend que ce qu'il y as après
    filter = ImageEnhance.Color(img) # On applique la couleur noir et blanc a l'image
    img = filter.enhance(0) 

    try: 
        if save==1: # Vérifie si l'orsque l'on a appeler la fonction l'utilisateur veut sauvegarder l'image
            img.save(f"{output}/BlackAndWhiteOf{NameImage}")
            return str(f"{output}/BlackAndWhiteOf{NameImage}")
        else:
            img.save(f"temps/BlackAndWhiteOf{NameImage}")
            return str(f"temps/BlackAndWhiteOf{NameImage}")
    except:
        print("Le chemin vers la sauvegarde de votre image modifié n'est pas bon ou n'existe pas. (BAW)")
        return