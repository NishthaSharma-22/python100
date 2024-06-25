import pyscreenshot

image = pyscreenshot.grab(bbox=(50,50,100,100))

image.show()

image.save("Image1.png")