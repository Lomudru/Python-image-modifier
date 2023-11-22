import cv2 
import numpy as np 
def Dilatation(image,output,save=1): img = cv2.imread(image) # Ouvre l'image 
    NameImage = image # NameImage est le chemin de l'image 
    for i in range(len(image)): # Boucle qui parcours les charactère du chemin de l'image 
        if image[i]=='/': # Si il y as un "/" 
            NameImage=image[i+1:] # On prend que ce qu'il y as après 
    kernel = np.ones((10, 10), np.uint8) img_dilate = cv2.dilate(img, kernel, iterations=1) # Dilate l'image 
    if save==1: # Vérifie si l'utilisateur veut sauvegarder 
        cv2.imwrite(f"{output}/Dilated{NameImage}", img_dilate) 
        return str(f"{output}/Dilated{NameImage}") 
    else: 
        cv2.imwrite(f"temps/Dilated{NameImage}", img_dilate) 
        return str(f"temps/Dilated{NameImage}")