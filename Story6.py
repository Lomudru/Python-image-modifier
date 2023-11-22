from PIL import Image
import cv2

def WriteText(image,output,texte,position_x,position_y,size,save=1):
    images= cv2.imread(image)
    imga = cv2.putText(images,texte,org=(position_x,position_y),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=size,color=(255,255,255),thickness=3)
    NameImage = image
    for i in range(len(image)):
        if image[i]=='/':
            NameImage=image[i+1:]
    if save==1:
        cv2.imwrite(f"{output}/WriteTextOn{NameImage}", imga)
        return str(f"{output}/WriteTextOn{NameImage}")
    else:
        cv2.imwrite(f"temps/WriteTextOn{NameImage}", imga)
        return str(f"temps/WriteTextOn{NameImage}")