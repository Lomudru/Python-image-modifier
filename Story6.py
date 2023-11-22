from PIL import Image
import cv2

def WriteText(image, output, texte, position_x, position_y, size, save=1):
    images = cv2.imread(image) # Charge l'image depuis le chemin spécifié dans image
    imga = cv2.putText(images, texte, org=(position_x, position_y), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=size, color=(255, 255, 255), thickness=3) # Ajoute le texte spécifié à l'image chargée aux coordonnées indiquées
    NameImage = image # NameImage et le chemin de l'image
    for i in range(len(image)): # Parcourt chaque caractère de la chaîne représentant le chemin de l'image
        if image[i]=='/':
            NameImage=image[i+1:] # Si il y a un / on prend uniquement le chemin qui se trouve apres ce /
    if save == 1: # Si on a choisit de sauvegarder ou qu'on a rien fait
        cv2.imwrite(f"{output}/WriteTextOn{NameImage}", imga) # Sauvegarde l'image dans le dossier output
        return str(f"{output}/WriteTextOn{NameImage}") # Renvoie le chemin ou on a sauvegarder l'image modifier
    else: # Si on a choisit de ne pas sauvegarder
        cv2.imwrite(f"temps/WriteTextOn{NameImage}", imga) # Sauvegarde l'image dans un dossier temp
        return str(f"temps/WriteTextOn{NameImage}") # Renvoie le chemin ou on a sauvegarder l'image modifier