from PIL import Image
import os
from logger import *

def RotateImage(image,degre,output,save=1):

    _, ext = os.path.splitext(image)
    if ext not in ('.jpg', '.jpeg', '.png'):
        print("Vous devez mettre en paramètre le chemin d'une image en format .jpg, .jpeg ou .png (Rotate)")
        log(f"Erreur d'extension de l'image {image} dans Rotate")
        return

    if not(isinstance(degre, (float, int))):
        print('Vous devez rentrer des nombres entiers ou flottants en paramètre de RotateImage.')
        log(f"Erreur de paramètre (nombre de degré) de l'image {image} dans Rotate")
        return
    try:
        img=Image.open(image) #ouverture de l'image avec PIL
    except:
        print("Le chemin vers l'image n'est pas bon ou n'existe pas. (Rotate)")
        log(f"Erreur de chemin de l'image {image} dans Rotate")
        return
    
    NameImage=image #NameImage et le chemin de l'image
    for i in range(len(image)): #parcourt chaque caractère de la chaîne représentant le chemin de l'image
        if image[i]=='/':
            NameImage=image[i+1:] #si il y a un / on prend uniquement le chemin qui se trouve apres ce /
    out = img.rotate(degre, expand=1) #pivote l'image de avec comme parametre degre
    log(f"{NameImage} est pivotée de {degre} degré(s)")

    try:
        if save==1: #si on a choisit de sauvegarder ou qu'on a rien fait
            out.save(f"{output}/RotateImageOf{NameImage}") #sauvegarde l'image dans le dossier output
            log(f"{NameImage} sauvegardée dans {output} (Rotate)")
            return str(f"{output}/RotateImageOf{NameImage}") #renvoie le chemin ou on a sauvegarder l'image modifier
        else: #si on a choisit de ne pas sauvegarder
            out.save(f"temps/RotateImageOf{NameImage}") #sauvegarde l'image dans un dossier temp
            log(f"{NameImage} sauvegardée dans temps/ (Rotate)")
            return str(f"temps/RotateImageOf{NameImage}") #renvoie le chemin ou on a sauvegarder l'image modifier
    except:
        print("Le chemin vers la sauvegarde de votre image modifié n'est pas bon ou n'existe pas. (Rotate)")
        log(f"Erreur pour le chemin de sauvegarde de {NameImage} dans Rotate.")
        return