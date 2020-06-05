


fin = open("fonts/font.ppm","r")
x = fin.read()
arra = []
for i in range(480):
    arra.append([])
    for j in range(800):
        arra[-1].append([0,0,0])

current = 0
for i in x.split("\n"):
    if(len(i)>15):
        for j in i.split(" "):
            if(len(j)!=0):

                j=int(j)
                arra[int(current/2400)][int(current/3)%800][current%3]=j
                current+=1

l1 = 'abcdefghijklmnopqrstuvwxyz'
l2= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l3 = '0123456789.:,;(*!?}^)#${%^&-+@'

l1splitters = []
for i in range(300):
    sum = 0
    for j in range(4,25):
        sum+=int(arra[j][i][0])
    if(sum>=20.5375*255):
        if(len(l1splitters)>0 and l1splitters[-1]==i-1):
            l1splitters[-1]+=1
        else:
            l1splitters.append(i)



for char in l1:
    print(char)
    starty=4
    startx=l1splitters[l1.index(char)]
    endx = l1splitters[l1.index(char)+1]
    endy = 25
    charArray = []

    for i in range(starty,endy):

        charArray.append(arra[i][startx:endx])

    fout = open("chars/"+char+".ppm","w")
    fout.write("P3\n"+str(abs(startx-endx))+" "+str(abs(starty-endy))+" \n255 \n")
    for i in charArray:
        for j in i:
            fout.write(str(j[0])+" "+str(j[1])+" "+str(j[2])+" ")
        fout.write("\n")

l2splitters = []
for i in range(350):
    sum = 0
    for j in range(26,49):
        sum+=int(arra[j][i][0])
    if(sum>=22.49825*255):
        if(len(l2splitters)>0 and l2splitters[-1]==i-1):
            l2splitters[-1]+=1
        else:
            l2splitters.append(i)



for char in l2:
    print(char)
    starty=26
    startx=l2splitters[l2.index(char)]
    endx = l2splitters[l2.index(char)+1]
    endy = 49
    charArray = []

    for i in range(starty,endy):

        charArray.append(arra[i][startx:endx])

    fout = open("chars/big"+char+".ppm","w")
    fout.write("P3\n"+str(abs(startx-endx))+" "+str(abs(starty-endy))+" \n255 \n")
    for i in charArray:
        for j in i:
            fout.write(str(j[0])+" "+str(j[1])+" "+str(j[2])+" ")
        fout.write("\n")

l3splitters = []
for i in range(350):
    sum = 0
    for j in range(50,68):
        sum+=int(arra[j][i][0])
    if(sum>=17.7*255):
        if(len(l3splitters)>0 and l3splitters[-1]==i-1):
            l3splitters[-1]+=1
        else:
            l3splitters.append(i)


for char in l3:
    print(char)
    starty=50
    startx=l3splitters[l3.index(char)]
    endx = l3splitters[l3.index(char)+1]
    endy = 68
    charArray = []

    for i in range(starty,endy):

        charArray.append(arra[i][startx:endx])

    fout = open("chars/"+char+".ppm","w")
    fout.write("P3\n"+str(abs(startx-endx))+" "+str(abs(starty-endy))+" \n255 \n")
    for i in charArray:
        for j in i:
            fout.write(str(j[0])+" "+str(j[1])+" "+str(j[2])+" ")
        fout.write("\n")


