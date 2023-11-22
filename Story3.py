import cv2 
import numpy as np 
from logger import *
import os

def Dilatation(image,output,save=1): 
    _, ext = os.path.splitext(image)
    if ext not in ('.jpg', '.jpeg', '.png'):
        print("Vous devez mettre en paramètre le chemin d'une image en format .jpg, .jpeg ou .png (Dilatation)")
        log(f"Erreur d'extension de l'image {image} dans Dilatation")
        return

    try:
        img = cv2.imread(image) # Ouvre l'image 
    except:
        print("Le chemin vers l'image n'est pas bon ou n'existe pas. (Dilatation)")
        log(f"Erreur de chemin de l'image {image} dans Dilatation")
        return
    
    NameImage = image # NameImage est le chemin de l'image 
    for i in range(len(image)): # Boucle qui parcours les charactère du chemin de l'image 
        if image[i]=='/': # Si il y as un "/" 
            NameImage=image[i+1:] # On prend que ce qu'il y as après 
    kernel = np.ones((10, 10), np.uint8) 
    img_dilate = cv2.dilate(img, kernel, iterations=1) # Dilate l'image 
    log(f"{NameImage} est dilatée")

    try:
        if save==1: # Vérifie si l'utilisateur veut sauvegarder 
            cv2.imwrite(f"{output}/Dilated{NameImage}", img_dilate) 
            log(f"{NameImage} sauvegardée dans {output} (Dilatation)")
            return str(f"{output}/Dilated{NameImage}") 
        else: 
            cv2.imwrite(f"temps/Dilated{NameImage}", img_dilate) 
            log(f"{NameImage} sauvegardée dans temps/ (Dilatation)")
            return str(f"temps/Dilated{NameImage}")
    except:
        print("Le chemin vers la sauvegarde de votre image modifié n'est pas bon ou n'existe pas. (Dilatation)")
        log(f"Erreur pour le chemin de sauvegarde de {NameImage} dans Dilatation.")
        return