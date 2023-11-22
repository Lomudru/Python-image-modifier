from PIL import Image
import cv2

def Resize(image,output, largeur, longueur,save=1):
    """
    Convertie l'image mit en paramètre
    ex : >>> Resize("grimm.jpeg","img", 0.5, 0.5)
    renvoie une image redimensionnée et deux foix plus petite et la sauvegarde dans le dossier img"""
    img=Image.open(image)
    im = cv2.imread(image)
    whidth = im.shape[1]
    height = im.shape[0]
    img = img.resize((round(whidth * largeur), round(height * longueur)))
    NameImage = image
    for i in range(len(image)):
        if image[i]=='/':
            NameImage=image[i+1:]
    if save==1:
        img.save(f"{output}/ResizeOf{NameImage}")
        return str(f"{output}/ResizeOf{NameImage}")
    else:
        img.save(f"temps/ResizeOf{NameImage}")
        return str(f"temps/ResizeOf{NameImage}")