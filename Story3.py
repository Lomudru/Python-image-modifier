import cv2 
import numpy as np 

def Dilatation(image,output):
    img = cv2.imread(image) 
    NameImage = image
    for i in range(len(image)):
        if image[i]=='/':
            NameImage=image[i+1:]
    kernel = np.ones((10, 10), np.uint8)
    img_dilate = cv2.dilate(img, kernel, iterations=1) 
    cv2.imwrite(f"{output}/Dilated{NameImage}", img_dilate)
Dilatation("02_Accueil_Hover_Menu.png","img")