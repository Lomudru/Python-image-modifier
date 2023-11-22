from PIL import Image, ImageEnhance

def RotateImage(image,degre,output,save=1):
    img=Image.open(image) #ouverture de l'image avec PIL
    NameImage=image #NameImage et le chemin de l'image
    for i in range(len(image)): #parcourt chaque caractère de la chaîne représentant le chemin de l'image
        if image[i]=='/':
            NameImage=image[i+1:] #si il y a un / on prend uniquement le chemin qui se trouve apres ce /
    out = img.rotate(degre, expand=1) #pivote l'image de avec comme parametre degre
    if save==1: #si on a choisit de sauvegarder ou qu'on a rien fait
        out.save(f"{output}/RotateImageOf{NameImage}") #sauvegarde l'image dans le dossier output
        return str(f"{output}/RotateImageOf{NameImage}") #renvoie le chemin ou on a sauvegarder l'image modifier
    else: #si on a choisit de ne pas sauvegarder
        out.save(f"temps/RotateImageOf{NameImage}") #sauvegarde l'image dans un dossier temp
        return str(f"temps/RotateImageOf{NameImage}") #renvoie le chemin ou on a sauvegarder l'image modifier