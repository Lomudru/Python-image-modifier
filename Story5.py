from PIL import Image
import cv2

def Resize(image,output, largeur, longueur):
    """
    Convertie l'image mit en paramètre
    ex : >>> Blurred("../grimm.jpeg","img")
    renvoie une image floutée et la sauvegarde dans le dossier img"""
    img=Image.open(image)
    im = cv2.imread(image)
    whidth = im.shape[1]
    height = im.shape[0]
    img = img.resize((round(whidth * largeur), round(height * longueur)))
    for i in range(len(image)):
        if image[i]=='/':
            NameImage=image[i+1:]
    NameImage = image
    img.show()
    img.save(f"{output}/ResizeOf{NameImage}")
Resize("grimm.jpeg","img", 0.5, 0.5)