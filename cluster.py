import math

c1=[0.6,8.01]
c2=[0.67,3.87]
c3=[0.1,0.88]
new_c1=[]
new_c2=[]
new_c3=[]
dicdata={}
c1cluster=[]
c2cluster=[]
c3cluster=[]
count=0
hitung = 1

def euclidian(x1, y1, x2, y2):    
    S = 0.0
    S = math.sqrt(( ( float(x1) - y1 )**2 )+( ( float(x2) - y2 )**2 ))
    return S
   
with open('videogames.csv') as f:
    for line in f:
        count = count + 1
        if count == 1:
            continue
        else:
            x = line.split(',')
            dicdata[x[0]] = {'OTHERSALES':x[8], 'GLOBALSALES':x[9]}
            valc1=euclidian(x[8],c1[0],x[9],c1[1])
            valc2=euclidian(x[8],c2[0],x[9],c2[1])
            valc3=euclidian(x[8],c3[0],x[9],c3[1])
            if valc1 < valc2 and valc1 < valc3:
                c1cluster.append(x[0])
            elif valc2 < valc1 and valc2 < valc3:
                c2cluster.append(x[0])
            elif valc3 < valc1 and valc3 < valc2:
                c3cluster.append(x[0])
            else:
                c1cluster.append(x[0])

temp_osl1 = 0
temp_gsl1 = 0
temp_osl2 = 0
temp_gsl2 = 0
temp_osl3 = 0
temp_gsl3 = 0
for i in c1cluster:
    temp_osl1 = temp_osl1 + float(dicdata[i]['OTHERSALES'])
    temp_gsl1 = temp_gsl1 + float(dicdata[i]['GLOBALSALES'])
for j in c2cluster:
    temp_osl2 = temp_osl2 + float(dicdata[j]['OTHERSALES'])
    temp_gsl2 = temp_gsl2 + float(dicdata[j]['GLOBALSALES'])
for k in c3cluster:
    temp_osl3 = temp_osl3 + float(dicdata[k]['OTHERSALES'])
    temp_gsl3 = temp_gsl3 + float(dicdata[k]['GLOBALSALES'])

new_c1.append(float(temp_osl1) / len(c1cluster))
new_c1.append(float(temp_gsl1) / len(c1cluster))
new_c2.append(float(temp_osl2) / len(c2cluster))
new_c2.append(float(temp_gsl2) / len(c2cluster))
new_c3.append(float(temp_osl3) / len(c3cluster))
new_c3.append(float(temp_gsl3) / len(c3cluster))
    
while c1 != new_c1 and c2 != new_c2 and c3 != new_c3:
    hitung += 1
    c1 = list(new_c1)
    c2 = list(new_c2)
    c3 = list(new_c3)
    del c1cluster[:]
    del c2cluster[:]
    del c3cluster[:]
    with open('videogames.csv') as f:
        count = 0
        for line in f:
            count = count + 1
            if count == 1:
                continue
            else:
                x = line.split(',')
                valc1=euclidian(x[8],c1[0],x[9],c1[1])
                valc2=euclidian(x[8],c2[0],x[9],c2[1])
                valc3=euclidian(x[8],c3[0],x[9],c3[1])
                if valc1 < valc2 and valc1 < valc3:
                    c1cluster.append(x[0])
                elif valc2 < valc1 and valc2 < valc3:
                    c2cluster.append(x[0])
                elif valc3 < valc1 and valc3 < valc2:
                    c3cluster.append(x[0])
                else:
                    c1cluster.append(x[0])

    del new_c1[:]
    del new_c2[:]
    del new_c3[:]
    temp_osl1 = 0
    temp_gsl1 = 0
    temp_osl2 = 0
    temp_gsl2 = 0
    temp_osl3 = 0
    temp_gsl3 = 0
    for i in c1cluster:
        temp_osl1 = temp_osl1 + float(dicdata[i]['OTHERSALES'])
        temp_gsl1 = temp_gsl1 + float(dicdata[i]['GLOBALSALES'])
    for j in c2cluster:
        temp_osl2 = temp_osl2 + float(dicdata[j]['OTHERSALES'])
        temp_gsl2 = temp_gsl2 + float(dicdata[j]['GLOBALSALES'])
    for k in c3cluster:
        temp_osl3 = temp_osl3 + float(dicdata[k]['OTHERSALES'])
        temp_gsl3 = temp_gsl3 + float(dicdata[k]['GLOBALSALES'])

    new_c1.append(float(temp_osl1) / len(c1cluster))
    new_c1.append(float(temp_gsl1) / len(c1cluster))
    new_c2.append(float(temp_osl2) / len(c2cluster))
    new_c2.append(float(temp_gsl2) / len(c2cluster))
    new_c3.append(float(temp_osl3) / len(c3cluster))
    new_c3.append(float(temp_gsl3) / len(c3cluster))

print "CLUSTERING DONE"
print
print "JUMLAH ITERASI = ", hitung
print "CENTROID AKHIR CLUSTER 1 = ", c1
print "CENTROID AKHIR CLUSTER 2 = ", c2
print "CENTROID AKHIR CLUSTER 3 = ", c3
print
print
print "=========HASIL CLUSTERING========="
print
print "CLUSTER 1:"
print c1cluster
print
print
print
print "CLUSTER 2:"
print c2cluster
print
print
print
print "CLUSTER 3:"
print c3cluster

