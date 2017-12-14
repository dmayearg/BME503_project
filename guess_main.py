#### declare the shapes 

### declare myweights16
### declare myweightsout
execfile("othershapedata.py")
the_circles=[mycir,mycir1,mycir2,mycir3,mycir4,mycir5,mycir6]

myweightsout=array([[-0.2       , -0.2       ,  0.19852755,  0.19853219, -0.2       ,
         0.19996079,  0.19852732,  0.19985608,  0.19995407,  0.19852708],
       [ 0.19771631,  0.19780156,  0.1999977 ,  0.1999977 , -0.1074794 ,
        -0.19992949,  0.1999977 , -0.19973005, -0.1999184 ,  0.1999977 ],
       [ 0.2       ,  0.2       , -0.19999767, -0.19999767,  0.2       ,
        -0.19999767, -0.19999767, -0.19999767, -0.19999767, -0.19999767]])
        
myweights16=[array([-0.19999928, -0.19999893, -0.19999902, -0.19999946, -0.19999961,
        -0.19999961, -0.19999961, -0.19999961,  0.02348892,  0.18562212,
         0.16387306, -0.0585527 ,  0.18619162,  0.06853455,  0.07236497,
         0.2       ]),
 array([-0.1999992 , -0.1999992 , -0.19999953, -0.19999906, -0.19999953,
        -0.19999953, -0.19999953, -0.19999953, -0.1328873 ,  0.2       ,
         0.10109649,  0.11470585,  0.2       , -0.00092948,  0.10217235,
         0.15803934]),
 array([ 0.2       ,  0.2       ,  0.09483648,  0.12452555,  0.08596926,
         0.07608743,  0.1758143 ,  0.09619938,  0.2       , -0.0140569 ,
         0.09420941,  0.2       , -0.00157512,  0.2       ,  0.2       ,
         0.04349485]),
 array([ 0.1784561 ,  0.2       ,  0.03068053,  0.10057364,  0.2       ,
         0.0790181 ,  0.2       ,  0.14052451,  0.2       ,  0.10363066,
        -0.03870499,  0.2       ,  0.05668273,  0.2       ,  0.2       ,
         0.00038998]),
 array([-0.19999968, -0.1178446 , -0.08997498, -0.19999967, -0.19999969,
        -0.19999969, -0.18833345, -0.19999969, -0.19999969,  0.2       ,
         0.2       , -0.114792  ,  0.2       , -0.19999969, -0.19999969,
         0.2       ]),
 array([ 0.19999965,  0.19999965,  0.19999968,  0.19999968,  0.19999968,
         0.19999968,  0.19999968,  0.19999968,  0.00917881,  0.04042681,
        -0.06343884,  0.03907349,  0.0435083 ,  0.01728579, -0.011651  ,
         0.0121897 ]),
 array([ 0.08674406,  0.02828223,  0.07907648,  0.12914911,  0.2       ,
         0.05884113,  0.07863923,  0.2       ,  0.2       , -0.02327804,
        -0.03368358,  0.2       ,  0.13020273,  0.2       ,  0.2       ,
         0.04882523]),
 array([ 0.19999889,  0.19999889,  0.19999891,  0.19999891,  0.19999891,
         0.19999891,  0.19999891,  0.19999891,  0.09926838, -0.11730993,
        -0.01857419,  0.08570053,  0.00058998, -0.01332098,  0.00982631,
        -0.14767197]),
 array([ 0.19999959,  0.19999959,  0.19999966,  0.19999966,  0.19999966,
         0.19999966,  0.19999966,  0.19999966,  0.06010369,  0.03246977,
         0.0161694 ,  0.0036122 , -0.04098424,  0.06886325, -0.0290184 ,
        -0.10270667]),
 array([ 0.11759352,  0.01685282,  0.18817461, -0.00213681,  0.10848006,
         0.05810763,  0.2       ,  0.2       ,  0.2       ,  0.09051267,
         0.02456108,  0.2       ,  0.02402074,  0.2       ,  0.2       ,
        -0.01700424])]
        
idealans=[1,0,0]
mypixel=triround_1[0]
execfile("guesstheshape.py")
checking_tri1=[]
checking_tri2=[]
checking_tri3=[]
checking_squ1=[]
checking_squ2=[]
checking_squ3=[]

checking_cir=[]
checking_cirp=[]
checking_tri1p=[]
checking_tri2p=[]
checking_tri3p=[]
checking_squ1p=[]
checking_squ2p=[]
checking_squ3p=[]

idealans=[1,0,0]
print "triangles round 1" 
for thisx in range (0,len(triround_1)):
    mypixel = triround_1[thisx]
    print thisx
    execfile("guessshape2.py")
    checking_tri1.append(numpy.array(spike_shape16.count).tolist())
    checking_tri1p.append(int(100*myerror))
print "triangles round 2" 
for thisx in range (0,len(triround_2)):
    mypixel = triround_2[thisx]
    print thisx
    execfile("guessshape2.py")
    checking_tri2.append(numpy.array(spike_shape16.count).tolist())
    checking_tri2p.append(int(100*myerror))
print "triangles round 3" 
for thisx in range (0,len(triround_3)):
    mypixel = triround_3[thisx]
    print thisx
    execfile("guessshape2.py")
    checking_tri3.append(numpy.array(spike_shape16.count).tolist())
    checking_tri3p.append(int(100*myerror))
    
idealans=[0,1,0] 
print "squares round 1" 
for thisx in range (0,len(squround_1)):
    mypixel = squround_1[thisx]
    print thisx
    execfile("guessshape2.py")
    checking_squ1.append(numpy.array(spike_shape16.count).tolist())
    checking_squ1p.append(int(100*myerror))
print "squares round 2" 
for thisx in range (0,len(squround_2)):
    mypixel = squround_2[thisx]
    print thisx
    execfile("guessshape2.py")
    checking_squ2.append(numpy.array(spike_shape16.count).tolist())
    checking_squ2p.append(int(100*myerror))
print "squares round 3" 
for thisx in range (0,len(squround_3)):
    mypixel = squround_3[thisx]
    print thisx
    execfile("guessshape2.py")
    checking_squ3.append(numpy.array(spike_shape16.count).tolist())
    checking_squ3p.append(int(100*myerror))

idealans = [0,0,1]
print "circles" 
for thisx in range (0,len(the_circles)):
    mypixel = the_circles[thisx]
    print thisx, idealans
    execfile("guessshape2.py")
    checking_cir.append(numpy.array(spike_shape16.count).tolist())
    checking_cirp.append(int(100*myerror))





# basevalue= 38
# print "checking percent error against base value of", basevalue 
# print "triangle round 1" 
# for thisx in range (0,len(triround_1)):
#     if(checking_tri1p[thisx]>=basevalue):
#         print thisx, "is above basevalue" 
# print "triangle round 2" 
# for thisx in range (0,len(triround_2)):
#     if(checking_tri2p[thisx]>=basevalue):
#         print thisx, "is above basevalue" 
# print "triangle round 3" 
# for thisx in range (0,len(triround_3)):
#     if(checking_tri3p[thisx]>=basevalue):
#         print thisx, "is above basevalue" 
# 
# basevalue=38
# print "checking percent error against base value of", basevalue 
# print "square round 1" 
# for thisx in range (0,len(squround_1)):
#     if(checking_squ1p[thisx]>=basevalue):
#         print thisx, "is above basevalue" 
# print "square round 2" 
# for thisx in range (0,len(squround_2)):
#     if(checking_squ2p[thisx]>=basevalue):
#         print thisx, "is above basevalue" 
# print "square round 3" 
# for thisx in range (0,len(squround_3)):
#     if(checking_squ3p[thisx]>=basevalue):
#         print thisx, "is above basevalue" 
#         
#         
# 
#         
# basevalue= 0.50
# print "checking percent error against base value of", basevalue 
# print "triangle round 1" 
# for thisx in range (0,len(triround_1)):
#     if((float(checking_tri1[thisx][0])/sum(checking_tri1[thisx]))<=basevalue):
#         print thisx, float(checking_tri1[thisx][0])/sum(checking_tri1[thisx])
# print "triangle round 2" 
# for thisx in range (0,len(triround_2)):
#     if((float(checking_tri2[thisx][0])/sum(checking_tri2[thisx]))<=basevalue):
#         print thisx, "is above basevalue" 
# print "triangle round 3" 
# for thisx in range (0,len(triround_3)):
#     if((float(checking_tri3[thisx][0])/sum(checking_tri3[thisx]))<=basevalue):
#         print thisx, "is above basevalue"
#         
# basevalue= 0.5
# print "checking percent error against base value of", basevalue 
# print "square round 1" 
# for thisx in range (0,len(squround_1)):
#     if((float(checking_squ1[thisx][1])/sum(checking_squ1[thisx]))<=basevalue):
#         print thisx, float(checking_squ1[thisx][1])/max(checking_squ1[thisx])
# print "square round 2" 
# for thisx in range (0,len(squround_2)):
#     if((float(checking_squ2[thisx][1])/sum(checking_squ2[thisx]))<=basevalue):
#         print thisx, float(checking_squ2[thisx][1])/max(checking_squ2[thisx]) 
# print "square round 3" 
# for thisx in range (0,len(squround_3)):
#     if((float(checking_squ3[thisx][1])/sum(checking_squ3[thisx]))<=basevalue):
#         print thisx, float(checking_squ3[thisx][1])/max(checking_squ3[thisx]) 


spikes_tri_1=[]
for x in range(0,len(triround_1)):
    spikes_tri_1.append(checking_tri1[x][0])
for x in range(0,len(triround_2)):
    spikes_tri_1.append(checking_tri2[x][0])
for x in range(0,len(triround_3)):
    spikes_tri_1.append(checking_tri3[x][0])
    
spikes_tri_2=[]
for x in range(0,len(triround_1)):
    spikes_tri_2.append(checking_tri1[x][1])
for x in range(0,len(triround_2)):
    spikes_tri_2.append(checking_tri2[x][1])
for x in range(0,len(triround_3)):
    spikes_tri_2.append(checking_tri3[x][1])
    
spikes_tri_3=[]
for x in range(0,len(triround_1)):
    spikes_tri_3.append(checking_tri1[x][2])
for x in range(0,len(triround_2)):
    spikes_tri_3.append(checking_tri2[x][2])
for x in range(0,len(triround_3)):
    spikes_tri_3.append(checking_tri3[x][2])
    
spikes_squ_1=[]
for x in range(0,len(squround_1)):
    spikes_squ_1.append(checking_squ1[x][0])
for x in range(0,len(triround_2)):
    spikes_squ_1.append(checking_squ2[x][0])
spikes_squ_2=[]
for x in range(0,len(triround_1)):
    spikes_squ_2.append(checking_squ1[x][1])
for x in range(0,len(triround_2)):
    spikes_squ_2.append(checking_squ2[x][1])
spikes_squ_3=[]
for x in range(0,len(triround_1)):
    spikes_squ_3.append(checking_squ1[x][2])
for x in range(0,len(triround_2)):
    spikes_squ_3.append(checking_squ2[x][2])

spikes_squ_1=[]
for x in range(0,len(squround_1)):
    spikes_squ_1.append(checking_squ1[x][0])
for x in range(0,len(squround_2)):
    spikes_squ_1.append(checking_squ2[x][0])
spikes_squ_2=[]
for x in range(0,len(squround_1)):
    spikes_squ_2.append(checking_squ1[x][1])
for x in range(0,len(squround_2)):
    spikes_squ_2.append(checking_squ2[x][1])
spikes_squ_3=[]
for x in range(0,len(squround_1)):
    spikes_squ_3.append(checking_squ1[x][2])
for x in range(0,len(squround_2)):
    spikes_squ_3.append(checking_squ2[x][2])

spikes_cir_1=[]
for x in range(0,len(this_circles)):
    spikes_cir_1.append(checking_cir[x][0])
spikes_cir_2=[]
for x in range(0,len(this_circles)):
    spikes_cir_2.append(checking_cir[x][1])
spikes_cir_3=[]
for x in range(0,len(this_circles)):
    spikes_cir_3.append(checking_cir[x][2])

figure(1)
for x in range(0,len(triround_1)):
    plot(1,checking_tri1[x][0],'*r')
    plot(2,checking_tri1[x][1],'*r')
    plot(3,checking_tri1[x][2],'*r')
for x in range(0,len(triround_2)):
    plot(1,checking_tri2[x][0],'*b')
    plot(2,checking_tri2[x][1],'*b')
    plot(3,checking_tri2[x][2],'*b')
for x in range(0,len(triround_3)):
    plot(1,checking_tri3[x][0],'*g')
    plot(2,checking_tri3[x][1],'*g')
    plot(3,checking_tri3[x][2],'*g')
    

figure(2)
for x in range(0,len(squround_1)):
    plot(1,checking_squ1[x][0],'*r')
    plot(2,checking_squ1[x][1],'*r')
    plot(3,checking_squ1[x][2],'*r')
for x in range(0,len(squround_2)):
    plot(1,checking_squ2[x][0],'*b')
    plot(2,checking_squ2[x][1],'*b')
    plot(3,checking_squ2[x][2],'*b')
