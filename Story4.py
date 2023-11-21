from PIL import Image, ImageEnhance
def RotateImage(image,degre,output):
    img=Image.open(image)
    NameImage=image
    for i in range(len(image)):
        if image[i]=='/':
            NameImage=image[i+1:]
    out = img.rotate(degre, expand=1)
    out.show()
    out.save(f"{output}/RotateImageOf{NameImage}")

RotateImage("teste.png",45,'img')