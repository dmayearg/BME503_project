execfile("shapedata.py") 

normal_data_sens  = [0,0,0]
circle_data_sens  = [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
normal_data_sum  = normal_data_sens
circle_data_sum  = circle_data_sens

#myweightout =[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
#myweight16  =[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#              0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]

mynew_weightout_neverused=[]
mynew_weight16_neverused=[]


myerror_tri=[[],[],[],[],[],[],[],[],[]]
myerror_squ=[[],[],[],[],[],[],[],[],[]]
myerror_cir=[[],[],[],[],[],[],[],[],[]]

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
        



triround_1=[mytri,0,1,2,3,4,5,6,7,8,9,
            10,19,
            20,21,22,23,24,25,26,
            35,36,37,38,39,
            40,41,42,43,44,45,46,47,48,49,
            50,51,52,53,54,55,56,57,58,59,
            60,61,62,
            71,72,73,74,75,76,77,78,
            103,104,106,107,108]

triround_2=[11,12,13,14,
            27,28,29,
            30,31,32,33,34,
            63,64,65,66,67,68,69,
            70,79,
            80,81,82,83,84,85,86,87,88,89,
            90,91,92,93,94,95,96,99,
            100,105,109,110]

triround_3=[15,16,17,18,
            97,98,
            101,102]




squround_1=[mysqu,0,1,2,3,4,5,6,7,8,9,10,11,12,13,
            48,49,50,51,
            65,66,67,68,
            73,74,75,76,
            81,82,83,84,
            89,90,91,92,
            97,98,99,100,
            105,106,107,108,
            113,114,115,116]

squround_2=[14,15,16,17,18,19,20,21,22,23,24,25,
            39,40,41,42,43,44,45,46,47,
            69,70,71,72,
            77,78,79,80,
            85,86,87,88,
            121,122,123,124,
            129,130,131,132,
            137,138,139,140]

squround_3=[26,27,28,29,30,31,32,33,34,35,36,37,38,
            52,53,54,55,56,57,58,59,60,61,62,63,64,
            93,94,95,96,
            101,102,103,104,
            109,110,111,112,
            117,118,119,120,
            125,126,127,128,
            133,134,135,136,
            141,142,143,144]

triangle_data_sens = [triround_1,triround_2,triround_3]
square_data_sens = [squround_1,squround_2,squround_3]

triangle_data_sum  = triangle_data_sens
square_data_sum  = square_data_sens

for thisx in range(1,len(triround_1)):
    currentmatrix=weird_triangles1[triround_1[thisx]]
    triround_1[thisx]=currentmatrix
    
for thisx in range(0,len(triround_2)):
    currentmatrix=weird_triangles1[triround_2[thisx]]
    triround_2[thisx]=currentmatrix

for thisx in range(0,len(triround_3)):
    currentmatrix=weird_triangles1[triround_3[thisx]]
    triround_3[thisx]=currentmatrix
    
for thisx in range(1,len(squround_1)):
    currentmatrix=weird_squares1[squround_1[thisx]]
    squround_1[thisx]=currentmatrix
    
for thisx in range(0,len(squround_2)):
    currentmatrix=weird_squares1[squround_2[thisx]]
    squround_2[thisx]=currentmatrix

for thisx in range(0,len(squround_3)):
    currentmatrix=weird_squares1[squround_3[thisx]]
    squround_3[thisx]=currentmatrix
    

thisroundoferror=[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,0,0]



print "triangle"
mypixel = shapes_normal[0]
idealans=[1,0,0]
execfile("sense_filter_sum_learn.py")
#mypixel = triround_1[0]
#execfile("learning_stuff.py")
print "square"
mypixel = shapes_normal[1]
idealans=[0,1,0]
execfile("learning_stuff.py")
print "circle"
mypixel = shapes_normal[2]
idealans=[0,0,1]
execfile("learning_stuff.py")
print " "


for myrunningcount in range(0,20):
    print " " 
    print myrunningcount
    print weight16
    print weightsout
    mynew_weightout_neverused.append(weightsout.tolist())
    mynew_weight16_neverused.append([weight16[0].tolist(),
                                     weight16[1].tolist(),
                                     weight16[2].tolist(),
                                     weight16[3].tolist(),
                                     weight16[4].tolist(),
                                     weight16[5].tolist(),
                                     weight16[6].tolist(),
                                     weight16[7].tolist(),
                                     weight16[8].tolist(),
                                     weight16[9].tolist()])
    myerror_tri[0].append(thisroundoferror[0])
    myerror_tri[1].append(thisroundoferror[1])
    myerror_tri[2].append(thisroundoferror[2])
    myerror_squ[0].append(thisroundoferror[3])
    myerror_squ[1].append(thisroundoferror[4])
    myerror_squ[2].append(thisroundoferror[5])
    myerror_cir[0].append(thisroundoferror[6])
    myerror_cir[1].append(thisroundoferror[7])
    myerror_cir[2].append(thisroundoferror[8])
    myerror_tri[3].append(thisroundoferror[9])
    myerror_tri[4].append(thisroundoferror[10])
    myerror_tri[5].append(thisroundoferror[11])
    myerror_squ[3].append(thisroundoferror[12])
    myerror_squ[4].append(thisroundoferror[13])
    myerror_squ[5].append(thisroundoferror[14])
    myerror_cir[3].append(thisroundoferror[15])
    myerror_cir[4].append(thisroundoferror[16])
    myerror_cir[5].append(thisroundoferror[17])
    myerror_tri[6].append(thisroundoferror[18])
    myerror_tri[7].append(thisroundoferror[19])
    myerror_squ[6].append(thisroundoferror[20])
    myerror_squ[7].append(thisroundoferror[21])
    myerror_squ[8].append(thisroundoferror[22])
    myerror_cir[6].append(thisroundoferror[23])
    myerror_cir[7].append(thisroundoferror[24])
    mypixel = shapes_normal[0]
    idealans=[1,0,0]
    execfile("sense_filter_sum_learn.py")
    mypixel = shapes_normal[1]
    idealans=[0,1,0]
    execfile("sense_filter_sum_learn.py")
    mypixel = shapes_normal[2]
    idealans=[0,0,1]
    execfile("sense_filter_sum_learn.py")
    for othercoutzzz in range(0,25):
        thisroundoferror=[]
        mypixel = shapes_normal[0]
        idealans=[1,0,0]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        mypixel = triround_1[1]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        mypixel = triround_1[2]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        
        mypixel = shapes_normal[1]
        idealans=[0,1,0]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        mypixel = squround_1[1]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        mypixel = squround_1[14]  ## or 6 or 7 or 8  or 9 
        execfile("learning_stuff.py")  #maybe 19
        thisroundoferror.append(int(100*myerror))
        
        mypixel = shapes_normal[2]
        idealans=[0,0,1]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        execfile("learning_stuff.py")
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        
        idealans=[1,0,0]
        mypixel = triround_1[3]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        mypixel = triround_1[4]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        mypixel = triround_1[9]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        idealans=[0,1,0]
        mypixel = squround_1[6]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        mypixel = squround_1[7]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        mypixel = squround_2[6]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        mypixel = shapes_normal[2]
        idealans=[0,0,1]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        execfile("learning_stuff.py")
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        
        idealans=[1,0,0]
        mypixel = triround_1[36]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        mypixel = triround_1[48]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        idealans=[0,1,0]
        mypixel = squround_2[7]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        mypixel = squround_2[17]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        mypixel = squround_2[18]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        mypixel = shapes_normal[2]
        idealans=[0,0,1]
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        execfile("learning_stuff.py")
        execfile("learning_stuff.py")
        thisroundoferror.append(int(100*myerror))
        print thisroundoferror


        
####### DOOOO THIS THING AFTER YOU RUN EVERYTHING 

#summmmofcount=[]
#for otherxthing in range(0,len(myerror_tri[0])):
#    count_error_thisthing=0
#    for myexrn in range(0,8):
#        count_error_thisthing+=myerror_tri[myexrn][otherxthing]
#    summmmofcount.append(count_error_thisthing/8)
#print summmmofcount
#
#summmmofcount=[]
#for otherxthing in range(0,len(myerror_squ[0])):
#    count_error_thisthing=0
#    for myexrn in range(0,9):
#        count_error_thisthing+=myerror_squ[myexrn][otherxthing]
#    summmmofcount.append(count_error_thisthing/9)
#print summmmofcount
#
#summmmofcount=[]
#for otherxthing in range(0,len(myerror_cir[0])):
#    count_error_thisthing=0
#    for myexrn in range(0,8):
#        count_error_thisthing+=myerror_cir[myexrn][otherxthing]
#    summmmofcount.append(count_error_thisthing/8)
#print summmmofcount
#
#for otherxthing in range(0,len(mynew_weightout_neverused)):
#    print (numpy.array(mynew_weightout_neverused[otherxthing][0])*100).astype(int)
#    print (numpy.array(mynew_weightout_neverused[otherxthing][1])*100).astype(int)
#    print (numpy.array(mynew_weightout_neverused[otherxthing][2])*100).astype(int)
#    print " " 
#for otherxthing in range(0,len(mynew_weight16_neverused)):
#    print (numpy.array(mynew_weight16_neverused[otherxthing][0])*100).astype(int)
#    print (numpy.array(mynew_weight16_neverused[otherxthing][1])*100).astype(int)
#    print (numpy.array(mynew_weight16_neverused[otherxthing][2])*100).astype(int)
#    print (numpy.array(mynew_weight16_neverused[otherxthing][3])*100).astype(int)
#    print (numpy.array(mynew_weight16_neverused[otherxthing][4])*100).astype(int)
#    print (numpy.array(mynew_weight16_neverused[otherxthing][5])*100).astype(int)
#    print (numpy.array(mynew_weight16_neverused[otherxthing][6])*100).astype(int)
#    print (numpy.array(mynew_weight16_neverused[otherxthing][7])*100).astype(int)
#    print " "
#    
    
  
    
    
    