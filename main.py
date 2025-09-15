import qrcode

link=input("Enter the link: ")
img_name=input("Enter the image name: ")
img = qrcode.make(link)
img.save(img_name+".jpg")