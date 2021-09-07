from PIL import Image


charCode = list("$@B%8&WM#*oahkbdpqwmZO0QLCJ7788000666661123UYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")  
def getRGBtoGray(r,g,b,c):
    length = len(charCode)
    '''
    基础知识 
　　对于彩色转灰度，有一个很著名的心理学公式：
    Gray = R*0.299 + G*0.587 + B*0.114
    '''
    gray = int(0.299 * r + 0.587 * g + 0.114 * b) 
    u = 256/length  #单位值
    return charCode[int(gray/u)]

file = 'w.png'
img = Image.open(file)
w = 100
h = 50
img = img.resize((w,h), Image.NEAREST)
char = ''
for i in range(h):
    for j in range(w):
        char += getRGBtoGray(*img.getpixel((j,i)))
    char += '\n'
print(char)



