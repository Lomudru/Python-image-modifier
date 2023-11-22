from PIL import Image
import cv2
import os
from logger import *

def WriteText(image, output, texte, position_x, position_y, size, save=1):

    _, ext = os.path.splitext(image)
    if ext not in ('.jpg', '.jpeg', '.png'):
        print("Vous devez mettre en paramètre le chemin d'une image en format .jpg, .jpeg ou .png (Write)")
        log(f"Erreur d'extension de l'image {image} dans Write")
        return
    
    if not(isinstance(position_x, (float, int))) or not(isinstance(position_y, (float, int))) or position_x < 0 or position_y < 0:
        print('Vous devez rentrer des nombres entiers ou flottants positifs en paramètre de WriteText pour les positions x et y.')
        log(f"Erreur de paramètre (facteur(s) longueur et/ou largeur) de l'image {image} dans Write")
        return
    
    if not(isinstance(texte, str)):
        print('Le texte mis en paramètre doit être entre guillemets.')
        log(f"Erreur de paramètre texte de l'image {image} dans Write")

    try:
        images = cv2.imread(image) # Charge l'image depuis le chemin spécifié dans image
    except:
        print("Le chemin vers l'image n'est pas bon ou n'existe pas. (Write)")
        log(f"Erreur de chemin de l'image {image} dans Write")
        return
    
    imga = cv2.putText(images, texte, org=(position_x, position_y), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=size, color=(255, 255, 255), thickness=3) # Ajoute le texte spécifié à l'image chargée aux coordonnées indiquées
    log(f"Le texte {texte} a été mis sur l'image {NameImage} au coordonnée : {position_x} x, {position_y} y")

    NameImage = image # NameImage et le chemin de l'image
    for i in range(len(image)): # Parcourt chaque caractère de la chaîne représentant le chemin de l'image
        if image[i]=='/':
            NameImage=image[i+1:] # Si il y a un / on prend uniquement le chemin qui se trouve apres ce /
    
    try:
        if save == 1: # Si on a choisit de sauvegarder ou qu'on a rien fait
            cv2.imwrite(f"{output}/WriteTextOn{NameImage}", imga) # Sauvegarde l'image dans le dossier output
            log(f"{NameImage} sauvegardée dans {output} (Write)")
            return str(f"{output}/WriteTextOn{NameImage}") # Renvoie le chemin ou on a sauvegarder l'image modifier
        else: # Si on a choisit de ne pas sauvegarder
            cv2.imwrite(f"temps/WriteTextOn{NameImage}", imga) # Sauvegarde l'image dans un dossier temp
            log(f"{NameImage} sauvegardée dans temps/ (Write)")
            return str(f"temps/WriteTextOn{NameImage}") # Renvoie le chemin ou on a sauvegarder l'image modifier
    except:
        print("Le chemin vers la sauvegarde de votre image modifié n'est pas bon ou n'existe pas. (Write)")
        log(f"Erreur pour le chemin de sauvegarde de {NameImage} dans Write.")
        return