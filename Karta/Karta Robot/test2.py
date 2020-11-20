#Intellektuell egendom av David Mörck 
import time
import random
import PIL
from PIL import Image, ImageTk
import PIL.Image
from tkinter import * 
from tkinter.ttk import *
from paho.mqtt import client as paho
maps = []
mapsL = []
SIZE = [7,7]
carpos = [4,2] #sätt in startpositionen
lego = [1,0] #skickas in av bilen
point = 0 #mellan 0 och 3

broker = 'maqiatto.com'
port = 1883
topic = "victor.fagerstrom@abbindustrigymnasium.se/karta"
# generate client ID with pub prefix randomly
client_id = "Jenny"

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = paho.Client(client_id)
    client.username_pw_set(username="victor.fagerstrom@abbindustrigymnasium.se",password="hejhej")
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1



def navigate():
    start=0

# def changemap(map):
#     c=0
#     for a in map:
#         for b in a:
#             if b == [0,0]:
#                 mapsL[c].extend((1,1,1))
#                 mapsL[c+1].extend((1,1,1))
#                 mapsL[c+2].extend((1,1,1))
#             if b == [1,0]:
#                 mapsL[c].extend((1,0,1))
#                 mapsL[c+1].extend((0,0,0))
#                 mapsL[c+2].extend((1,0,1))
#             if  b == [2,0]:
#                 mapsL[c].extend((1,1,1))
#                 mapsL[c+1].extend((0,0,0))
#                 mapsL[c+2].extend((1,1,1))
#             if b == [2,1]:
#                 mapsL[c].extend((1,0,1))
#                 mapsL[c+1].extend((1,0,1))
#                 mapsL[c+2].extend((1,0,1))
#             if b == [3,0]:
#                 mapsL[c].extend((1,0,1))
#                 mapsL[c+1].extend((1,0,0))
#                 mapsL[c+2].extend((1,0,1))
#             if b == [3,1]:
#                 mapsL[c].extend((1,0,1))
#                 mapsL[c+1].extend((0,0,0))
#                 mapsL[c+2].extend((1,1,1))
#             if b == [3,2]:
#                 mapsL[c].extend((1,0,1))
#                 mapsL[c+1].extend((0,0,1))
#                 mapsL[c+2].extend((1,0,1))
#             if b == [3,3]:
#                 mapsL[c].extend((1,1,1))
#                 mapsL[c+1].extend((0,0,0))
#                 mapsL[c+2].extend((1,0,1))
#             if b == [4,0]:
#                 mapsL[c].extend((1,1,1))
#                 mapsL[c+1].extend((1,0,0))
#                 mapsL[c+2].extend((1,0,1))
#             if b == [4,1]:
#                 mapsL[c].extend((1,0,1))
#                 mapsL[c+1].extend((1,0,0))
#                 mapsL[c+2].extend((1,1,1))
#             if b == [4,2]:
#                 mapsL[c].extend((1,0,1))
#                 mapsL[c+1].extend((0,0,1))
#                 mapsL[c+2].extend((1,1,1))
#             if b == [4,3]:
#                 mapsL[c].extend((1,1,1))
#                 mapsL[c+1].extend((0,0,1))
#                 mapsL[c+2].extend((1,0,1))
#         c=c+3
def generate_map(size):
    for a in range(0,size[0]):
        maps.append([])
        mapsL.append([])
        mapsL.append([])
        mapsL.append([])

        for b in range(0,size[1]):
            maps[a].append([0,0])

def drive(piece):
    global carpos
    global point
    global maps

    if piece[0] == 1: #om lego-vägen är väg 1 spelar rotationen ingen roll
        maps[carpos[0]][carpos[1]] = piece
    else:
        if point == 0: #om bilen pekar "uppåt" ska ingen ändring göras
            maps[carpos[0]][carpos[1]] = piece
        elif point == 1: #om bilen pekar "åt höger" roteras rutorna 90grader åt vänster
            if piece[0] == 2:
                maps[carpos[0]][carpos[1]] = [piece[0],piece[1]-1]
            elif piece[0] == 3 or piece[0] == 4:
                if piece[1] == 0:
                    maps[carpos[0]][carpos[1]
                    ] = [piece[0],3]
                else:
                    maps[carpos[0]][carpos[1]] = [piece[0],piece[1]-1]
        elif point == 2: #om bilen pekar "nedåt" ska rutorna roteras 180grader
            if piece[0] == 2:
                maps[carpos[0]][carpos[1]] = piece
            elif piece[0] == 3 or piece[0] == 4:
                if piece[1] == 0 or piece[1] == 1:
                    maps[carpos[0]][carpos[1]] = [piece[0],piece[1]+2]
                elif piece[1] == 2 or piece[1]==3:
                    maps[carpos[0]][carpos[1]] = [piece[0],piece[1]-2]
        elif point == 3: #om bilen pekar "åt vänster" ska rutorna roteras 90grader åt höger
            if piece[0] == 2:
                maps[carpos[0]][carpos[1]] = [piece[0],piece[1]-1]
            elif piece[0] == 3 or piece[0] == 4:
                if piece[1] == 3:
                    maps[carpos[0]][carpos[1]] = [piece[0],0]
                else:
                    maps[carpos[0]][carpos[1]] = [piece[0],piece[1]+1]
    alt=[]
    if piece == [1,0]: #fyrvägskorsning
        alt.extend((0,1,3))
        print(alt)
        print("fyrväg")
    elif piece == [2,1]: #rak väg
        alt.append(0)
    elif piece == [3,0]: #trevägskorsning höger
        alt.extend((0,1))
    elif piece == [3,2]: #trevägskorsning höger-vänster
        alt.extend((1,3))
    elif piece == [3,3]: #trevägskorsning vänster
        alt.extend((1,3))
    elif piece == [4,0]: #svängande väg höger
        alt.append(1)
    elif piece == [4,3]: #svängande väg vänster
        alt.append(3)

    rand = random.randint(0,len(alt)-1) #nu slumpas ett val av riktning som bilen ska ta
    choice= alt[rand] 
    if choice == 0:
        print("Åk rakt på")
        move(choice) #kallar på funktionen move som flyttar på bilen i kartan
    elif choice == 1:
        move(choice)
        turn(1)
        print("Sväng höger")
    elif choice == 3:
        move(choice)
        turn(0)
        print("Sväng vänster")
    drawMap()
    return choice

def move(dir):
    global point
    global carpos
    if dir == 0:
        if point == 0:
            carpos[0] = carpos[0]-1
        elif point == 1:
            carpos[1] = carpos[1]+1
        elif point == 2:
            carpos[0] = carpos[0]+1
        elif point ==3:
            carpos[1] = carpos[1]-1
    elif dir == 1:
        if point == 0:
            carpos[1] = carpos[1]+1
        elif point == 1:
            carpos[0] = carpos[0]+1
        elif point == 2:
            carpos[1] = carpos[1]-1
        elif point == 3:
            carpos[0] = carpos[0]-1
    elif dir == 3:
        if point == 0:
            carpos[1] = carpos[1]-1
        elif point == 1:
            carpos[0] = carpos[0]-1
        elif point == 2:
            carpos[1] = carpos[1]+1
        elif point == 3:
            carpos[0] = carpos[0]+1

def turn(lr):
    global point
    if lr == 0:
        if point == 0:
            point = 3
        else:
            point = point - 1
    else:
        if point ==3:
            point=0
        else:
            point = point + 1
    return point

connect_mqtt()
generate_map(SIZE)


def subscribe(client: paho):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        bit = [int(msg.payload.decode()[1]),int(msg.payload.decode()[-2])]
        drive(bit)

    client.subscribe(topic)
    client.on_message = on_message


def drawMap():
    master = Tk() 
    master.geometry("520x520")
    size = 60,60
    img  = {}
    load = {}
    render = {}
    q=0
    for x in range(0,11):
        img[x] = {}
        load[x] = {}
        render[x] = {}
    for a in maps:
        print(a)
        for i in range(0,len(maps)):
            num = str(a[i]).replace(" ","").replace("[","").replace("]","")
            print(num)
            fp = open("./bilder/"+num+".jpg","rb")
            load[i][q] = PIL.Image.open(fp)
            load[i][q].thumbnail(size, PIL.Image.ANTIALIAS)
            render[i][q] = ImageTk.PhotoImage(load[i][q])
            img[i][q] = Label(image=render[i][q])
            img[i][q].grid(row = q, column = i,pady = 0)
        q +=1
    master.after(3000, lambda: master.destroy()) # Destroy the widget after 30 seconds
    master.mainloop()

def run():
    client = connect_mqtt()
    subscribe(client)
    #publish(client)
    client.loop_forever()

run()

# print(point)
# print(carpos)

# drive([1,0])
# print(point)
# print(carpos)

# drive([3,0])
# print(point)
# print(carpos)

# drive([4,3])
# print(point)
# print(carpos)

# drive([2,1])
# print(point)
# print(carpos)
#             fp = open("./bilder/"+num+".jpg","rb") 
