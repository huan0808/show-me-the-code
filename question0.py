from PIL import Image,ImageDraw
im=Image.open('huan.jpg')
draw=ImageDraw.Draw(im)
draw.line((900,50,800,150),fill=128)#xiexian
draw.line((800,150,930,150),fill=128)#hengxian
draw.line((900,50,900,200),fill=128)#shuxian
im.show()
