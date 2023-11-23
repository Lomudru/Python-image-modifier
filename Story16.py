import cv2
import os
from logger import *

def FaceDetection(image, output, save = 1):

    _, ext = os.path.splitext(image)
    if ext not in ('.jpg', '.jpeg', '.png'):
        print("Vous devez mettre en paramètre le chemin d'une image en format .jpg, .jpeg ou .png (Face)")
        log(f"Erreur d'extension de l'image {image} dans Face")
        return

    NameImage = image # NameImage et le chemin de l'image
    for i in range(len(image)): # Parcourt chaque caractère de la chaîne représentant le chemin de l'image
        if image[i]=='/':
            NameImage=image[i+1:] # Si il y a un / on prend uniquement le chemin qui se trouve apres ce /

    try:
        img = cv2.imread(image)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detecte les visages
        face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        face = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
        )
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4) # Dessinne le rectangle
    except:
        print("Le chemin vers l'image n'est pas bon ou n'existe pas. (Face)")
        log(f"Erreur de chemin de l'image {NameImage} dans Face")
        return


    try:
        if save == 1: # Si on a choisit de sauvegarder ou qu'on a rien fait
            cv2.imwrite(f"{output}/FaceDetectionOn{NameImage}", img) # Sauvegarde l'image dans le dossier output
            log(f"{NameImage} sauvegardée dans {output} (Face)")
            return str(f"{output}/FaceDetectionOn{NameImage}") # Renvoie le chemin ou on a sauvegarder l'image modifier
        else: # Si on a choisit de ne pas sauvegarder
            cv2.imwrite(f"temps/FaceDetectionOn{NameImage}", img) # Sauvegarde l'image dans un dossier temp
            log(f"{NameImage} sauvegardée dans temps/ (Face)")
            return str(f"temps/FaceDetectionOn{NameImage}") # Renvoie le chemin ou on a sauvegarder l'image modifier
    except:
        print("Le chemin vers la sauvegarde de votre image modifié n'est pas bon ou n'existe pas. (Face)")
        log(f"Erreur pour le chemin de sauvegarde de {NameImage} dans Face.")
        return