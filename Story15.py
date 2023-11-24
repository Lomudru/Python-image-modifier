import os
from PIL import Image
from logger import *

def Make_gif(image, output):
    _, ext = os.path.splitext(image)
    if ext not in ('.jpg', '.jpeg', '.png'):
        print("Vous devez mettre en paramètre le chemin d'une image en format .jpg, .jpeg ou .png (GIF)")
        log(f"Erreur d'extension de l'image {image} dans GIF")
        return
    
    NameImage=image # NameImage est le chemin de l'image
    for i in range(len(image)): # Boucle qui parcours les charactère du chemin de l'image 
        if image[i]=='/': # Si il y as un "/"
            NameImage=image[i+1:] # On prend que ce qu'il y as après


    try:
        Files = os.listdir(image)
        Files = [Image.open(f"{image}/{file}") for file in sorted(Files)]
        log("Les images sont trasformées en gif")
    except:
        print("Le chemin vers l'image n'est pas bon ou n'existe pas. (GIF)")
        log(f"Erreur de chemin de l'image {image} dans GIF")
        return
    
    try:
        Files[0].save(f'{output}/Image.gif', save_all=True, append_images=Files[1:], optimize=False, duration=1000, loop=0)
    except:
        print("Le chemin vers la sauvegarde de votre image modifié n'est pas bon ou n'existe pas. (GIF)")
        log(f"Erreur pour le chemin de sauvegarde de {NameImage} dans GIF.")
        return