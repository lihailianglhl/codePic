from PIL import Image
import argparse

charCode = list("$@B%8&WM#*oahkbdpqwmZO0QLCJ7788000666661123UYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")  
# 灰度函数
# 将256灰度映射到charCode字符上  0 是黑色  255 白色 灰度值0-255对照表
def rgbToGray(r,g,b,alpha = 256):
    length = len(charCode)
    '''
    基础知识 
　　对于彩色转灰度，有一个很著名的心理学公式：
    Gray = R*0.299 + G*0.587 + B*0.114
    '''
    gray = int(0.299 * r + 0.587 * g + 0.114 * b) 
    u = 256/length  #单位值
    return charCode[int(gray/u)]

# 存储函数
# 将字符串保存到文件中
def outputFile(filename,char):
    #字符画输出到文件
    if filename:
        with open(filename,'w') as f:
            f.write(char)

# 脚本参数
def setParser():
    # 命令行输入参数处理方法
    parser = argparse.ArgumentParser() 
    parser.add_argument('file')     #输入文件
    parser.add_argument('-o', '--output', default = 'outputfile.txt')   #输出文件
    parser.add_argument('--width', type = int, default = 80) #输出字符画宽
    parser.add_argument('--height', type = int, default = 80) #输出字符画高
    
    #获取参数
    args = parser.parse_args()
    return args.file,args.width,args.height,args.output

 
if __name__ == '__main__':

    IMG,WIDTH,HEIGHT,OUTPUTF = setParser()     

    im = Image.open(IMG)
    #重新调整图片大小
    im = im.resize((WIDTH,HEIGHT), Image.NORMAL)
 
    char = ""
    #循环图片每个像素点，并转换成灰度值 
    for i in range(HEIGHT):
        for j in range(WIDTH):
            char += rgbToGray(*im.getpixel((j,i))) #该函数检索指定坐标点的像素的RGB颜色值
        char += '\n'
 
    print(char)
    outputFile(OUTPUTF,char)
 
