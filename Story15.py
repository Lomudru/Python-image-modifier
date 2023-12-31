import os
from PIL import Image
from logger import *

def Make_gif(dossier, output):
    # Vérifie si l'information envoyer est bien un dossier
    if os.path.isfile(dossier):
        print("Vous devez mettre en paramètre le chemin d'un dossier (GIF)")
        log(f"Erreur d'extension du dossier {dossier} dans GIF")
        return


    try:
        # Liste les fichier du dossier
        Files = os.listdir(dossier)
        # Les ouvre en tant qu'image
        Files = [Image.open(f"{dossier}/{file}") for file in sorted(Files)]
        for i in Files:
            Files[Files.index(i)] = i.resize((256,256))
    except:
        print("Le chemin vers le dossier n'est pas bon ou n'existe pas. (GIF)")
        log(f"Erreur de chemin du dossier {dossier} dans GIF")
        return
    
    try:
        # Crée le gif
        Files[0].save(f'{output}/Image.gif', save_all=True, append_images=Files[1:], optimize=False, duration=1000, loop=0)
        log("Les images sont trasformées en gif")
    except:
        print("Le chemin vers la sauvegarde de votre GIF n'est pas bon ou n'existe pas. (GIF)")
        log(f"Erreur pour le chemin de sauvegarde du GIF dans la fonction GIF.")
        return