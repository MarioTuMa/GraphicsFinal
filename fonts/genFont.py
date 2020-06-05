fin = open("fonts/roboto.ppm","r")
fout = open("fonts/font.ppm","w")
print("Generating Font")
current = 0
x = fin.read()
arra = []
for i in range(480):
    arra.append([])
    for j in range(800):
        arra[-1].append([0,0,0])


count = 0
for i in x.split("\n"):
    if(len(i)>15):

        #print(i)
        for j in i.split(" "):
            count+=1
            if(len(j)!=0):
                j=str(int(int(j)/256))
                # if(int(j)>0):
                #     print(j)
                # if(int(j)!=255):
                #     print(j)

                arra[int(current/2400)][int(current/3)%800][current%3]=j
                current+=1
#         print(arr[min(int(current/800),479)])
# print(len(arr))
# print(len(arr[0]))

#print(count)
fout.write("P3\n800 480 \n255 \n")
for i in arra:
    for j in i:
        
        fout.write(str(j[0])+" "+str(j[1])+" "+str(j[2])+" ")
    fout.write("\n")
