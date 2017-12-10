#### declare the shapes 
basevalue= 60

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
    execfile("guesstheshape.py")
    checking_tri1.append(numpy.array(spike_shape16.count).tolist())
    checking_tri1p.append(int(100*myerror))
print "triangles round 2" 
for thisx in range (0,len(triround_2)):
    mypixel = triround_2[thisx]
    print thisx
    execfile("guesstheshape.py")
    checking_tri2.append(numpy.array(spike_shape16.count).tolist())
    checking_tri2p.append(int(100*myerror))
print "triangles round 3" 
for thisx in range (0,len(triround_3)):
    mypixel = triround_3[thisx]
    print thisx
    execfile("guesstheshape.py")
    checking_tri3.append(numpy.array(spike_shape16.count).tolist())
    checking_tri3p.append(int(100*myerror))
    
idealans=[0,1,0] 
print "squares round 1" 
for thisx in range (0,len(squround_1)):
    mypixel = squround_1[thisx]
    print thisx
    execfile("guesstheshape.py")
    checking_squ1.append(numpy.array(spike_shape16.count).tolist())
    checking_squ1p.append(int(100*myerror))
print "squares round 2" 
for thisx in range (0,len(squround_2)):
    mypixel = squround_2[thisx]
    print thisx
    execfile("guesstheshape.py")
    checking_squ2.append(numpy.array(spike_shape16.count).tolist())
    checking_squ2p.append(int(100*myerror))
print "squares round 3" 
for thisx in range (0,len(squround_3)):
    mypixel = squround_3[thisx]
    print thisx
    execfile("guesstheshape.py")
    checking_squ3.append(numpy.array(spike_shape16.count).tolist())
    checking_squ3p.append(int(100*myerror))


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