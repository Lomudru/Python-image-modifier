import cv2
import os
from logger import *

def Aquarelle(image, output, save = 1):

    _, ext = os.path.splitext(image)
    if ext not in ('.jpg', '.jpeg', '.png'):
        print("Vous devez mettre en paramètre le chemin d'une image en format .jpg, .jpeg ou .png (Aqua)")
        log(f"Erreur d'extension de l'image {image} dans Aqua")
        return

    NameImage = image # NameImage et le chemin de l'image
    for i in range(len(image)): # Parcourt chaque caractère de la chaîne représentant le chemin de l'image
        if image[i]=='/':
            NameImage=image[i+1:] # Si il y a un / on prend uniquement le chemin qui se trouve apres ce /

    try:
        img = cv2.imread(image)
        res = cv2.stylization(img, sigma_s=60, sigma_r=0.6) # Rendue aquarelle
    except:
        print("Le chemin vers l'image n'est pas bon ou n'existe pas. (Aqua)")
        log(f"Erreur de chemin de l'image {image} dans Aqua")
        return


    try:
        if save == 1: # Si on a choisit de sauvegarder ou qu'on a rien fait
            cv2.imwrite(f"{output}/AquarelleOn{NameImage}", res) # Sauvegarde l'image dans le dossier output
            log(f"{NameImage} sauvegardée dans {output} (Aqua)")
            return str(f"{output}/AquarelleOn{NameImage}") # Renvoie le chemin ou on a sauvegarder l'image modifier
        else: # Si on a choisit de ne pas sauvegarder
            cv2.imwrite(f"temps/AquarelleOn{NameImage}", res) # Sauvegarde l'image dans un dossier temp
            log(f"{NameImage} sauvegardée dans temps/ (Aqua)")
            return str(f"temps/AquarelleOn{NameImage}") # Renvoie le chemin ou on a sauvegarder l'image modifier
    except:
        print("Le chemin vers la sauvegarde de votre image modifié n'est pas bon ou n'existe pas. (Aqua)")
        log(f"Erreur pour le chemin de sauvegarde de {NameImage} dans Aqua.")
        return