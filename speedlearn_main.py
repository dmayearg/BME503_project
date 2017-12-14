#execfile("shapedata.py")
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
#
#
#
##### declare the shapes 
#
#### declare myweights16
#### declare myweightsout
#
#normalshapes_sum=[]
#trisums1=[]
#trisums2=[]
#trisums3=[]
#squsums1=[]
#squsums2=[]
#squsums3=[]
#
#print "normalshapes" 
#for thisx in range (0,len(shapes_normal)):
#    mypixel = shapes_normal[thisx]
#    print thisx
#    execfile("speedlearn_first.py")
#    normalshapes_sum.append(numpy.array(spike_sum.count).tolist())
#
#idealans=[1,0,0]
#print "triangles round 1" 
#for thisx in range (0,len(triround_1)):
#    mypixel = triround_1[thisx]
#    print thisx
#    execfile("speedlearn_second.py")
#    trisums1.append(numpy.array(spike_sum.count).tolist())
#print "triangles round 2" 
#for thisx in range (0,len(triround_2)):
#    mypixel = triround_2[thisx]
#    print thisx
#    execfile("speedlearn_second.py")
#    trisums2.append(numpy.array(spike_sum.count).tolist())
#print "triangles round 3" 
#for thisx in range (0,len(triround_3)):
#    mypixel = triround_3[thisx]
#    print thisx
#    execfile("speedlearn_second.py")
#    trisums3.append(numpy.array(spike_sum.count).tolist())
#    
#idealans=[0,1,0] 
#print "squares round 1" 
#for thisx in range (0,len(squround_1)):
#    mypixel = squround_1[thisx]
#    print thisx
#    execfile("speedlearn_second.py")
#    squsums1.append(numpy.array(spike_sum.count).tolist())
#print "squares round 2" 
#for thisx in range (0,len(squround_2)):
#    mypixel = squround_2[thisx]
#    print thisx
#    execfile("speedlearn_second.py")
#    squsums2.append(numpy.array(spike_sum.count).tolist())
#print "squares round 3" 
#for thisx in range (0,len(squround_3)):
#    mypixel = squround_3[thisx]
#    print thisx
#    execfile("speedlearn_second.py")
#    squsums3.append(numpy.array(spike_sum.count).tolist())

weight16  =  [[0.08, -0.1 ,  0.03, -0.08,  0.13,  0.11, -0.04, -0.06, 
               0.1 ,  0.09,  0.12, -0.08,  0.05,  0.13,  0.13,  0.12],
              [0.1 , -0.07, -0.07, -0.06,  0.05,  0.02,  0.03,  0.15, 
               -0.05,  0.13,  0.06,  0.11,  0.15,  0.06,  0.17,  0.0],
              [0.15,  0.12, -0.02,  0.01, -0.03, -0.04,  0.06, -0.02, 
               0.02, -0.02,  0.11, -0.05,  0.  , -0.02,  0.15,  0.0],
              [0.07,  0.13, -0.08, -0.01,  0.11, -0.03,  0.1 ,  0.03, 
               -0.08,  0.12, -0.04,  0.17,  0.07,  0.08,  0.02, -0.06],
              [0.01,  0.13,  0.17,  0.01,  0.01, -0.1 ,  0.08,  0.05, 
               -0.07,  0.1 , -0.01,  0.17,  0.12,  0.04, -0.01,  0.17],
              [0.07,  0.03,  0.05,  0.07,  0.07,  0.  , -0.08,  0.12 , 
               -0.08,  0.09, -0.1 ,  0.03,  0.  ,  0.  , -0.09,  0.06],
              [-0.04, -0.1 , -0.05,  0.  ,  0.14, -0.07, -0.05,  0.08, 
               0.08, -0.05, -0.06,  0.  ,  0.12,  0.17, -0.07, -0.02],
              [0.09,  0.15,  0.11,  0.08,  0.13,  0.13,  0.17,  0.09, 
               0.11, -0.05,  0.03,  0.11,  0.07,  0.01,  0.01, -0.08],
              [0.15,  0.04, -0.04, -0.09,  0.12,  0.04,  0.14,  0.01, 
               0.05,  0.14,  0.01, -0.04,  0.02,  0.11, -0.08, -0.1],
              [0.03, -0.07,  0.1 , -0.09,  0.02, -0.03,  0.16,  0.13, 
               0.09,  0.07,  0.  ,  0.17,  0.  ,  0.17, -0.03, -0.09]]

weightsout=[[0.14, -0.08, -0.07,  0.04, -0.01,  0.14,  0.17, -0.02, -0.06,  0.1],
            [0.16,  0.08, -0.07, -0.08,  0.06, -0.05, -0.03, -0.01, -0.02,  0.12],
            [0.11, -0.01, -0.08,  0.01,  0.07,  0.02, -0.1 ,  0.15,  0.  ,  0.09]]



#shapedatamatrix=[triround_1[0],triround_1[4],triround_1[5],
#                 squround_1[0],squround_1[1],squround_1[23],
#                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
#                 triround_1[6],triround_1[7],triround_1[12],
#                 squround_1[24],squround_1[25],squround_1[26],
#                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
#                 triround_1[28],triround_1[32],triround_1[33],
#                 squround_1[31],squround_1[32],squround_1[33],
#                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
#                 triround_1[34],triround_1[35],triround_1[40],
#                 squround_1[34],squround_2[0],squround_2[1],
#                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
#                 triround_1[41],triround_1[56],triround_1[57],
#                 squround_2[2],squround_2[3],squround_2[4],
#                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
#                 triround_1[58],triround_1[59],triround_1[60],
#                 squround_2[5],squround_2[6],squround_2[7],
#                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
#                 triround_1[9],triround_1[14],triround_1[30],
#                 squround_1[3],squround_1[4],squround_1[5],
#                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
#                 triround_1[31],triround_2[0],triround_2[1],
#                 squround_1[8],squround_1[9],squround_1[14],
#                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
#                 triround_2[7],triround_2[10],triround_2[11],
#                 squround_1[35],squround_1[40],squround_1[43],
#                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
#                 triround_2[12],triround_2[16],triround_2[17],
#                 squround_2[10],squround_2[12],squround_2[15],
#                 shapes_normal[2],shapes_normal[2],shapes_normal[2]]
#
#sumssssmatrix = [trisums1[0],trisums1[4],trisums1[5],
#                 squsums1[0],squsums1[1],squsums1[23],
#                 normalshapes_sum[2],normalshapes_sum[2],normalshapes_sum[2],
#                 trisums1[6],trisums1[7],trisums1[12],
#                 squsums1[24],squsums1[25],squsums1[26],
#                 normalshapes_sum[2],normalshapes_sum[2],normalshapes_sum[2],
#                 trisums1[28],trisums1[32],trisums1[33],
#                 squsums1[31],squsums1[32],squsums1[33],
#                 normalshapes_sum[2],normalshapes_sum[2],normalshapes_sum[2],
#                 trisums1[34],trisums1[35],trisums1[40],
#                 squsums1[34],squsums2[0],squsums2[1],
#                 normalshapes_sum[2],normalshapes_sum[2],normalshapes_sum[2],
#                 trisums1[41],trisums1[56],trisums1[57],
#                 squsums2[2],squsums2[3],squsums2[4],
#                 normalshapes_sum[2],normalshapes_sum[2],normalshapes_sum[2],
#                 trisums1[58],trisums1[59],trisums1[60],
#                 squsums2[5],squsums2[6],squsums2[7],
#                 normalshapes_sum[2],normalshapes_sum[2],normalshapes_sum[2],
#                 trisums1[9],trisums1[14],trisums1[30],
#                 squsums1[3],squsums1[4],squsums1[5],
#                 normalshapes_sum[2],normalshapes_sum[2],normalshapes_sum[2],
#                 trisums1[31],trisums2[0],trisums2[1],
#                 squsums1[8],squsums1[9],squsums1[14],
#                 normalshapes_sum[2],normalshapes_sum[2],normalshapes_sum[2],
#                 trisums2[7],trisums2[10],trisums2[11],
#                 squsums1[35],squsums1[40],squsums1[43],
#                 normalshapes_sum[2],normalshapes_sum[2],normalshapes_sum[2],
#                 trisums2[12],trisums2[16],trisums2[17],
#                 squsums2[10],squsums2[12],squsums2[15],
#                 normalshapes_sum[2],normalshapes_sum[2],normalshapes_sum[2]]
#
#idealansmatrix=[[1,0,0],[1,0,0],[1,0,0],
#                [0,1,0],[0,1,0],[0,1,0],
#                [0,0,1],[0,0,1],[0,0,1],
#                [1,0,0],[1,0,0],[1,0,0],
#                [0,1,0],[0,1,0],[0,1,0],
#                [0,0,1],[0,0,1],[0,0,1],
#                [1,0,0],[1,0,0],[1,0,0],
#                [0,1,0],[0,1,0],[0,1,0],
#                [0,0,1],[0,0,1],[0,0,1],
#                [1,0,0],[1,0,0],[1,0,0],
#                [0,1,0],[0,1,0],[0,1,0],
#                [0,0,1],[0,0,1],[0,0,1],
#                [1,0,0],[1,0,0],[1,0,0],
#                [0,1,0],[0,1,0],[0,1,0],
#                [0,0,1],[0,0,1],[0,0,1],
#                [1,0,0],[1,0,0],[1,0,0],
#                [0,1,0],[0,1,0],[0,1,0],
#                [0,0,1],[0,0,1],[0,0,1],
#                [1,0,0],[1,0,0],[1,0,0],
#                [0,1,0],[0,1,0],[0,1,0],
#                [0,0,1],[0,0,1],[0,0,1],
#                [1,0,0],[1,0,0],[1,0,0],
#                [0,1,0],[0,1,0],[0,1,0],
#                [0,0,1],[0,0,1],[0,0,1],
#                [1,0,0],[1,0,0],[1,0,0],
#                [0,1,0],[0,1,0],[0,1,0],
#                [0,0,1],[0,0,1],[0,0,1],
#                [1,0,0],[1,0,0],[1,0,0],
#                [0,1,0],[0,1,0],[0,1,0],
#                [0,0,1],[0,0,1],[0,0,1]]

weightsout=numpy.array(weightsout)

for training_limit in range(0,2):
    for trainsof10 in range (0,500):
        for x in range(0,90):
            myshapesums=numpy.array(sumssssmatrix[x])
            myshapeidealans=numpy.array(idealansmatrix[x])
            #mysumpercent=numpy.array(1/(1+exp(-((numpy.array(myshapesums).astype(float)**(0.35)*2)-7))))
            mysumpercent=numpy.array(myshapesums).astype(float)/88
            midnums=numpy.dot(mysumpercent,(numpy.transpose((numpy.array(weight16)))))  #this should be 8 numbers in a row... tbhidk
            mymidpercent=(1/(1+exp(-(midnums*10-3)))) #8 numbers  ## maybe subtract a num....idk
            shapenums=numpy.dot(mymidpercent,(numpy.transpose((numpy.array(weightsout)))))
            myshapepercent=(1/(1+exp(-(shapenums*10-3)))) ## 3 numbers
            myerror=((myshapepercent[0]-myshapeidealans[0])**2+(myshapepercent[1]-myshapeidealans[1])**2+(myshapepercent[2]-myshapeidealans[2])**2) ## for triangle
            # print int(100*myerror)
            gradout=myshapepercent*(1-myshapepercent)*(myshapeidealans-myshapepercent)
            gradmid=mymidpercent*(1-mymidpercent)*((gradout[0]*weightsout[0])+(gradout[1]*weightsout[1])+(gradout[2]*weightsout[2]))
            weightsout[0]=clip(weightsout[0]+(0.001*mymidpercent*gradout[0]),-0.2,0.2)
            weightsout[1]=clip(weightsout[1]+(0.001*mymidpercent*gradout[1]),-0.2,0.2)
            weightsout[2]=clip(weightsout[2]+(0.001*mymidpercent*gradout[2]),-0.2,0.2)
            weight16[0]=clip(weight16[0]+(0.001*mysumpercent*gradmid[0]),-0.2,0.2)
            weight16[1]=clip(weight16[1]+(0.001*mysumpercent*gradmid[1]),-0.2,0.2)
            weight16[2]=clip(weight16[2]+(0.001*mysumpercent*gradmid[2]),-0.2,0.2)
            weight16[3]=clip(weight16[3]+(0.001*mysumpercent*gradmid[3]),-0.2,0.2)
            weight16[4]=clip(weight16[4]+(0.001*mysumpercent*gradmid[4]),-0.2,0.2)
            weight16[5]=clip(weight16[5]+(0.001*mysumpercent*gradmid[5]),-0.2,0.2)
            weight16[6]=clip(weight16[6]+(0.001*mysumpercent*gradmid[6]),-0.2,0.2)
            weight16[7]=clip(weight16[7]+(0.001*mysumpercent*gradmid[7]),-0.2,0.2)
            weight16[8]=clip(weight16[8]+(0.001*mysumpercent*gradmid[8]),-0.2,0.2)
            weight16[9]=clip(weight16[9]+(0.001*mysumpercent*gradmid[9]),-0.2,0.2)
    print training_limit
    print weight16
    print weightsout
total_error_thisround=0
for x in range(0,90):
    myshapesums=numpy.array(sumssssmatrix[x])
    myshapeidealans=numpy.array(idealansmatrix[x])
    #mysumpercent=numpy.array(1/(1+exp(-(log(numpy.array(myshapesums)+1)*2.5-7))))
    mysumpercent=numpy.array(myshapesums).astype(float)/88
    #mysumpercent=numpy.array(1/(1+exp(-((numpy.array(myshapesums).astype(float)**(0.35)*2)-7))))
    midnums=numpy.dot(mysumpercent,(numpy.transpose((numpy.array(weight16)))))  #this should be 8 numbers in a row... tbhidk
    mymidpercent=(1/(1+exp(-(midnums*10-3)))) #8 numbers  ## maybe subtract a num....idk
    shapenums=numpy.dot(mymidpercent,(numpy.transpose((numpy.array(weightsout)))))
    myshapepercent=(1/(1+exp(-(shapenums*10-3)))) ## 3 numbers
#    print myshapesums
#    print mysumpercent
    print mymidpercent
    print shapenums
    print myshapepercent
    myerror=((myshapepercent[0]-myshapeidealans[0])**2+(myshapepercent[1]-myshapeidealans[1])**2+(myshapepercent[2]-myshapeidealans[2])**2) ## for triangle
    total_error_thisround=total_error_thisround+(100*myerror)
    print int(100*myerror), myshapeidealans
print total_error_thisround

myweights16=weight16
myweightsout=weightsout

print "normalshapes" 
for thisx in range (0,len(shapes_normal)):
    mypixel = shapes_normal[thisx]
    print thisx
    execfile("guesstheshape.py")
#basevalue= 20
#print "checking percent error against base value of", basevalue 
#print "triangle round 1" 
#for thisx in range (0,len(triround_1)):
#    if(checking_tri1p[thisx]>=basevalue):
#        print thisx, "is above basevalue" 
#print "triangle round 2" 
#for thisx in range (0,len(triround_2)):
#    if(checking_tri2p[thisx]>=basevalue):
#        print thisx, "is above basevalue" 
#print "triangle round 3" 
#for thisx in range (0,len(triround_3)):
#    if(checking_tri3p[thisx]>=basevalue):
#        print thisx, "is above basevalue" 
#
#basevalue=30
#print "checking percent error against base value of", basevalue 
#print "square round 1" 
#for thisx in range (0,len(squround_1)):
#    if(checking_squ1p[thisx]>=basevalue):
#        print thisx, "is above basevalue" 
#print "square round 2" 
#for thisx in range (0,len(squround_2)):
#    if(checking_squ2p[thisx]>=basevalue):
#        print thisx, "is above basevalue" 
#print "square round 3" 
#for thisx in range (0,len(squround_3)):
#    if(checking_squ3p[thisx]>=basevalue):
#        print thisx, "is above basevalue" 
#        
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