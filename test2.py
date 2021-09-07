from PIL import Image

#读图片
img = Image.open('girl.png')

#放大或缩小图片
h = 60
w = 100
img = img.resize((w,h), Image.NEAREST)

charCode = list("$@B%8&WM#*oahkbdpqwmZO0QLCJ7788000666661123UYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

def getRGBtoGray(r,g,b,c):
    #255白色， 0 黑色
    length = len(charCode)
    '''
    基础知识 
　　对于彩色转灰度，有一个很著名的心理学公式：
    Gray = R*0.299 + G*0.587 + B*0.114
    '''
    gray = int(0.299 * r + 0.587 * g + 0.114 * b) 
    u = 256/length  #单位值
    return charCode[int(gray/u)]

char = ''
for i in range(h):
    for j in range(w):        
        char += getRGBtoGray(*img.getpixel((j,i)))
    char += '\n'

print(char)

