import sensor,image,lcd

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_vflip(0)
sensor.set_hmirror(0)
sensor.run(1)


from fpioa_manager import fm
from machine import UART
from board import board_info

fm.register(board_info.PIN15, fm.fpioa.UART1_TX, force=True)

uart_A = UART(UART.UART1, 9600,8,0,0, timeout=1000, read_buf_len=4096)


width = 224

height = 224

areaM = (int(width/2)-45,40,90,height)

areaL = (0, 0, 60, 124)

areaR = (164, 0, 60, 124)

areaU = (60, 0, 104, 40)

def findMiddleRects(Area):
    binary = img.copy().binary([(90,200)])
    rects = binary.find_rects(roi=Area)
    print(len(rects))
    for obj in rects:
       if obj.rect()[3] < 100:
        if obj.rect()[3] > height:
            print(obj.rect()[3],height)
        displayimg.draw_rectangle(obj.rect(),thickness=4, color=(255,0,0))

def findRectsPixels(Area):
    binary = img.copy().binary([(90,200)])
    rects = binary.find_rects(roi=Area)
    print(len(rects))
    pixels = 0
    for obj in rects:
       if obj.rect()[3] < 100:
        if obj.rect()[3] > height:
            print(obj.rect()[3],height)
        displayimg.draw_rectangle(obj.rect(),thickness=4, color=(255,0,0))
        pixels = pixels + (obj[2]*obj[3])
    return pixels


def drawMidLine(Area):

    _line = img.get_regression([

(255,255)],roi=Area)

    if(_line):
        degrees = _line.theta()
        img.draw_line(_line.line(), color = (255, 0, 0))
        difference_value = 0
        if degrees < 60 or degrees > 120:
            if degrees > 90:
                difference_value = degrees - 180
            else:
                difference_value = degrees
            print("DIFFERENCE IN DEGREES: " + str(difference_value))
            uart_A.write(str(difference_value))
        displayimg.draw_line(_line.line(),thickness=4,color = (0,0,255))
        displayimg.draw_string(2,2,str(difference_value), color=(0,0,0), scale=2)





while(True):
    #img = sensor.snapshot().binary([(0,100)])
    displayimg = sensor.snapshot()
    img = displayimg.to_grayscale(copy=True)
    displayimg.draw_rectangle(areaM,thickness=2, color=(0,255,0))
    displayimg.draw_rectangle(areaL,thickness=2, color=(0,255,0))
    displayimg.draw_rectangle(areaR,thickness=2, color=(0,255,0))
    displayimg.draw_rectangle(areaU,thickness=2, color=(255,0,0))

    if findRectsPixels(areaL) >= 1500:
        print("PixelsL: "+str(findRectsPixels(areaL))+" Övergångsställe vänster")
        #uart_A.write("Övergångsställe vänster"))
    else:
        print("PixelsL: "+str(findRectsPixels(areaL)))
    if findRectsPixels(areaR) >= 1500:
        print("PixelsR: "+str(findRectsPixels(areaR))+" Övergångsställe höger")
        #uart_A.write("Övergångsställe höger"))
    else:
        print("PixelsR: "+str(findRectsPixels(areaR)))

    if findRectsPixels(areaU) >= 1300:
        print("PixelsR: "+str(findRectsPixels(areaU))+" Övergångsställe Rakt Fram")
        #uart_A.write("Övergångsställe rakt fram"))
    else:
        print("PixelsU: "+str(findRectsPixels(areaU)))
        findMiddleRects(areaM)
        drawMidLine(areaM)
    #img.draw_line(int(width/2),0,int(width/2),height)
    #displayimg.draw_rectangle(0,0,40,height,thickness=2, color=(0,255,0))



    lcd.display(displayimg)




