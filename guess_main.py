
#triround_1=[mytri,0,1,2,3,4,5,6,7,8,9,
#            10,19,
#            20,21,22,23,24,25,26,
#            35,36,37,38,39,
#            40,41,42,43,44,45,46,47,48,49,
#            50,51,52,53,54,55,56,57,58,59,
#            60,61,62,
#            71,72,73,74,75,76,77,78,
#            103,104,106,107,108]
#
#triround_2=[11,12,13,14,
#            27,28,29,
#            30,31,32,33,34,
#            63,64,65,66,67,68,69,
#            70,79,
#            80,81,82,83,84,85,86,87,88,89,
#            90,91,92,93,94,95,96,99,
#            100,105,109,110]
#
#triround_3=[15,16,17,18,
#            97,98,
#            101,102]
#
#squround_1=[mysqu,0,1,2,3,4,5,6,7,8,9,10,11,12,13,
#            48,49,50,51,
#            65,66,67,68,
#            73,74,75,76,
#            81,82,83,84,
#            89,90,91,92,
#            97,98,99,100,
#            105,106,107,108,
#            113,114,115,116]
#
#squround_2=[14,15,16,17,18,19,20,21,22,23,24,25,
#            39,40,41,42,43,44,45,46,47,
#            69,70,71,72,
#            77,78,79,80,
#            85,86,87,88,
#            121,122,123,124,
#            129,130,131,132,
#            137,138,139,140]
#
#squround_3=[26,27,28,29,30,31,32,33,34,35,36,37,38,
#            52,53,54,55,56,57,58,59,60,61,62,63,64,
#            93,94,95,96,
#            101,102,103,104,
#            109,110,111,112,
#            117,118,119,120,
#            125,126,127,128,
#            133,134,135,136,
#            141,142,143,144]
#
#for thisx in range(1,len(triround_1)):
#    currentmatrix=weird_triangles1[triround_1[thisx]]
#    triround_1[thisx]=currentmatrix
#    
#for thisx in range(0,len(triround_2)):
#    currentmatrix=weird_triangles1[triround_2[thisx]]
#    triround_2[thisx]=currentmatrix
#
#for thisx in range(0,len(triround_3)):
#    currentmatrix=weird_triangles1[triround_3[thisx]]
#    triround_3[thisx]=currentmatrix
#    
#for thisx in range(1,len(squround_1)):
#    currentmatrix=weird_squares1[squround_1[thisx]]
#    squround_1[thisx]=currentmatrix
#    
#for thisx in range(0,len(squround_2)):
#    currentmatrix=weird_squares1[squround_2[thisx]]
#    squround_2[thisx]=currentmatrix
#
#for thisx in range(0,len(squround_3)):
#    currentmatrix=weird_squares1[squround_3[thisx]]
#    squround_3[thisx]=currentmatrix
#    


myweights16=weight16
myweightsout=weightsout
#### declare the shapes 

### declare myweights16
### declare myweightsout



idealans=[1,0,0]
mypixel=triround_1[0]
execfile("guesstheshape.py")
checking_tri1=[]
checking_tri2=[]
checking_tri3=[]
checking_squ1=[]
checking_squ2=[]
checking_squ3=[]

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
#print "squares round 3" 
#for thisx in range (0,len(squround_3)):
#    mypixel = squround_3[thisx]
#    print thisx
#    execfile("guessshape2.py")
#    checking_squ3.append(numpy.array(spike_shape16.count).tolist())
#    checking_squ3p.append(int(100*myerror))








basevalue= 50
print "checking percent error against base value of", basevalue 
print "triangle round 1" 
for thisx in range (0,len(triround_1)):
    if(checking_tri1p[thisx]>=basevalue):
        print thisx, "is above basevalue" 
print "triangle round 2" 
for thisx in range (0,len(triround_2)):
    if(checking_tri2p[thisx]>=basevalue):
        print thisx, "is above basevalue" 
print "triangle round 3" 
for thisx in range (0,len(triround_3)):
    if(checking_tri3p[thisx]>=basevalue):
        print thisx, "is above basevalue" 

basevalue=50
print "checking percent error against base value of", basevalue 
print "square round 1" 
for thisx in range (0,len(squround_1)):
    if(checking_squ1p[thisx]>=basevalue):
        print thisx, "is above basevalue" 
print "square round 2" 
for thisx in range (0,len(squround_2)):
    if(checking_squ2p[thisx]>=basevalue):
        print thisx, "is above basevalue" 
print "square round 3" 
for thisx in range (0,len(squround_3)):
    if(checking_squ3p[thisx]>=basevalue):
        print thisx, "is above basevalue" 
        
#basevalue= 0.60
#print "checking percent error against base value of", basevalue 
#print "triangle round 1" 
#for thisx in range (0,len(triround_1)):
#    if((float(checking_tri1[thisx][0])/sum(checking_tri1[thisx]))<=basevalue):
#        print thisx, "is above basevalue" 
#print "triangle round 2" 
#for thisx in range (0,len(triround_2)):
#    if((float(checking_tri2[thisx][0])/sum(checking_tri2[thisx]))<=basevalue):
#        print thisx, "is above basevalue" 
#print "triangle round 3" 
#for thisx in range (0,len(triround_3)):
#    if((float(checking_tri3[thisx][0])/sum(checking_tri3[thisx]))<=basevalue):
#        print thisx, "is above basevalue"
#        
#        
#basevalue= 0.5
#print "checking percent error against base value of", basevalue 
#print "square round 1" 
#for thisx in range (0,len(squround_1)):
#    if((float(checking_squ1[thisx][1])/sum(checking_squ1[thisx]))<=basevalue):
#        print thisx, "is above basevalue" 
#print "square round 2" 
#for thisx in range (0,len(squround_2)):
#    if((float(checking_squ2[thisx][1])/sum(checking_squ2[thisx]))<=basevalue):
#        print thisx, "is above basevalue" 
#print "square round 3" 
#for thisx in range (0,len(squround_3)):
#    if((float(checking_squ3[thisx][1])/sum(checking_squ3[thisx]))<=basevalue):
#        print thisx, "is above basevalue"
#        