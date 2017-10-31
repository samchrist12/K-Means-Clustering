import math

c1=[7.55,50.00] #cluster penjualan tinggi
c2=[5.25,28.75] #cluster penjualan menengah
c3=[3.20,14.80] #cluster penjualan rendah
new_c1=[]
new_c2=[]
new_c3=[]
dicdata={} #Untuk menampung data yang menjadi parameter perhitungan
c1cluster=[]
c2cluster=[]
c3cluster=[]
count=0
hitung = 1

#Hitung jarak euclidian
def euclidian(x1, y1, x2, y2):    
    S = 0.0
    S = math.sqrt(( ( float(x1) - y1 )**2 )+( ( float(x2) - y2 )**2 ))
    return S

#buka file dataset untuk diolah
with open('videogames.csv') as file:
    for line in file:
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
                c1cluster.append(x[0]) #masuk ke cluster penjualan tinggi
            elif valc2 < valc1 and valc2 < valc3:
                c2cluster.append(x[0]) #masuk ke cluster penjualan menengah
            elif valc3 < valc1 and valc3 < valc2:
                c3cluster.append(x[0]) #masuk ke cluster penjualan rendah
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
    
#Hitung ulang nilai centroid
while c1 != new_c1 and c2 != new_c2 and c3 != new_c3:
    hitung += 1
    c1 = list(new_c1)
    c2 = list(new_c2)
    c3 = list(new_c3)
    del c1cluster[:]
    del c2cluster[:]
    del c3cluster[:]
    with open('videogames.csv') as file:
        count = 0
        for line in file:
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
    
    #memasukan centroid baru
    new_c1.append(float(temp_osl1) / len(c1cluster))
    new_c1.append(float(temp_gsl1) / len(c1cluster))
    new_c2.append(float(temp_osl2) / len(c2cluster))
    new_c2.append(float(temp_gsl2) / len(c2cluster))
    new_c3.append(float(temp_osl3) / len(c3cluster))
    new_c3.append(float(temp_gsl3) / len(c3cluster))

#Output Program
print "CLUSTERING DONE"
print
print "JUMLAH ITERASI = ", hitung
print "CENTROID AKHIR CLUSTER 1 (Penjualan tinggi) = ", c1
print "CENTROID AKHIR CLUSTER 2 (Penjualan menengah) = ", c2
print "CENTROID AKHIR CLUSTER 3 (Penjualan rendah) = ", c3
print
print
print "=========HASIL CLUSTERING========="
print
print "CLUSTER 1 (Penjualan tinggi):"
print c1cluster
print
print
print
print "CLUSTER 2 (Penjualan menengah):"
print c2cluster
print
print
print
print "CLUSTER 3 (Penjualan rendah):"
print c3cluster

