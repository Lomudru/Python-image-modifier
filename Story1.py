from PIL import Image, ImageEnhance
def BlackAndWhite(image,output,save=1):
    img=Image.open(image) # On Ouvre L'image 
    NameImage=image # NameImage est le chemin de l'image
    for i in range(len(image)): # Boucle qui parcours les charactère du chemin de l'image 
        if image[i]=='/': # Si il y as un "/"
            NameImage=image[i+1:] # On prend que ce qu'il y as après
    filter = ImageEnhance.Color(img) # On applique la couleur noir et blanc a l'image
    img = filter.enhance(0) 
    if save==1: # Vérifie si l'orsque l'on a appeler la fonction l'utilisateur veut sauvegarder l'image
        img.save(f"{output}/BlackAndWhiteOf{NameImage}")
        return str(f"{output}/BlackAndWhiteOf{NameImage}")
    else:
        img.save(f"temps/BlackAndWhiteOf{NameImage}")
        return str(f"temps/BlackAndWhiteOf{NameImage}")