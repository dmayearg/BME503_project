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


myerror_tri=[[],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[]]
myerror_squ=[[],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[]]
myerror_cir=[[],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], 
             [],[],[],[],[], [],[],[],[],[], [],[],[],[],[], [],[],[],[],[]]

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
    
#for thisx in range (0,3):
#print "triangle"
#mypixel = shapes_normal[0]
#idealans=[1,0,0]
#execfile("sense_filter_sum_learn.py")
#mypixel = triround_1[0]
#execfile("sense_filter_sum_learn.py")
#print "square"
#mypixel = shapes_normal[1]
#idealans=[0,1,0]
#execfile("sense_filter_sum_learn.py")
#print "circle"
#mypixel = shapes_normal[2]
#idealans=[0,0,1]
#execfile("sense_filter_sum_learn.py")
#print " "
#for myrunningcount in range(0,100):
#    print myrunningcount
#    mypixel = shapes_normal[0]
#    idealans=[1,0,0]
#    execfile("sense_filter_sum_learn.py")
#    mypixel = triround_1[0]
#    execfile("sense_filter_sum_learn.py")
#    mypixel = shapes_normal[1]
#    idealans=[0,1,0]
#    execfile("sense_filter_sum_learn.py")
#    mypixel = shapes_normal[2]
#    idealans=[0,0,1]
#    execfile("sense_filter_sum_learn.py")
#    print " " 
    
thisroundoferror=[0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 
                  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
                  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 
                  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
                  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 
                  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
                  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 
                  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
                  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 
                  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
                  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 
                  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
                  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 
                  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]



print "triangle"
mypixel = shapes_normal[0]
idealans=[1,0,0]
execfile("sense_filter_sum_learn.py")
#mypixel = triround_1[0]
#execfile("learning_stuff.py")
print "square"
mypixel = shapes_normal[1]
idealans=[0,1,0]
execfile("sense_filter_sum_learn.py")
print "circle"
mypixel = shapes_normal[2]
idealans=[0,0,1]
execfile("sense_filter_sum_learn.py")
print " "


for myrunningcount in range(0,5):
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
    mypixel = shapes_normal[0]
    idealans=[1,0,0]
    execfile("sense_filter_sum_learn.py")
    mypixel = shapes_normal[1]
    idealans=[0,1,0]
    execfile("sense_filter_sum_learn.py")
    mypixel = shapes_normal[2]
    idealans=[0,0,1]
    execfile("sense_filter_sum_learn.py")
    for othercoutzzz in range(0,10):
        execfile("singleit18.py")
    for somenum in range(0,6):
        myerror_tri[(somenum*3)].append(thisroundoferror[(somenum*9)])
        myerror_tri[(somenum*3)+1].append(thisroundoferror[(somenum*9)+1])
        myerror_tri[(somenum*3)+2].append(thisroundoferror[(somenum*9)+2])
        myerror_squ[(somenum*3)].append(thisroundoferror[(somenum*9)+3])
        myerror_squ[(somenum*3)+1].append(thisroundoferror[(somenum*9)+4])
        myerror_squ[(somenum*3)+2].append(thisroundoferror[(somenum*9)+5])
        myerror_cir[(somenum*3)].append(thisroundoferror[(somenum*9)+6])
        myerror_cir[(somenum*3)+1].append(thisroundoferror[(somenum*9)+7])
        myerror_cir[(somenum*3)+2].append(thisroundoferror[(somenum*9)+8])


for myrunningcount in range(0,10):
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
    mypixel = shapes_normal[0]
    idealans=[1,0,0]
    execfile("sense_filter_sum_learn.py")
    mypixel = shapes_normal[1]
    idealans=[0,1,0]
    execfile("sense_filter_sum_learn.py")
    mypixel = shapes_normal[2]
    idealans=[0,0,1]
    execfile("sense_filter_sum_learn.py")
    for othercoutzzz in range(0,10):
        execfile("singleit18.py")
    for somenum in range(0,10):
        myerror_tri[(somenum*3)].append(thisroundoferror[(somenum*9)])
        myerror_tri[(somenum*3)+1].append(thisroundoferror[(somenum*9)+1])
        myerror_tri[(somenum*3)+2].append(thisroundoferror[(somenum*9)+2])
        myerror_squ[(somenum*3)].append(thisroundoferror[(somenum*9)+3])
        myerror_squ[(somenum*3)+1].append(thisroundoferror[(somenum*9)+4])
        myerror_squ[(somenum*3)+2].append(thisroundoferror[(somenum*9)+5])
        myerror_cir[(somenum*3)].append(thisroundoferror[(somenum*9)+6])
        myerror_cir[(somenum*3)+1].append(thisroundoferror[(somenum*9)+7])
        myerror_cir[(somenum*3)+2].append(thisroundoferror[(somenum*9)+8])

#for myrunningcount in range(0,6):
#    print " " 
#    print myrunningcount
#    print weight16
#    print weightsout
#    mynew_weightout_neverused.append(weightsout.tolist())
#    mynew_weight16_neverused.append([weight16[0].tolist(),
#                                     weight16[1].tolist(),
#                                     weight16[2].tolist(),
#                                     weight16[3].tolist(),
#                                     weight16[4].tolist(),
#                                     weight16[5].tolist(),
#                                     weight16[6].tolist(),
#                                     weight16[7].tolist(),
#                                     weight16[8].tolist(),
#                                     weight16[9].tolist()])
#    mypixel = shapes_normal[0]
#    idealans=[1,0,0]
#    execfile("sense_filter_sum_learn.py")
#    mypixel = shapes_normal[1]
#    idealans=[0,1,0]
#    execfile("sense_filter_sum_learn.py")
#    mypixel = shapes_normal[2]
#    idealans=[0,0,1]
#    execfile("sense_filter_sum_learn.py")
#    for othercoutzzz in range(0,8):
#        execfile("singleiteration.py")
#    for somenum in range(0,36):
#        myerror_tri[(somenum*3)].append(thisroundoferror[(somenum*9)])
#        myerror_tri[(somenum*3)+1].append(thisroundoferror[(somenum*9)+1])
#        myerror_tri[(somenum*3)+2].append(thisroundoferror[(somenum*9)+2])
#        myerror_squ[(somenum*3)].append(thisroundoferror[(somenum*9)+3])
#        myerror_squ[(somenum*3)+1].append(thisroundoferror[(somenum*9)+4])
#        myerror_squ[(somenum*3)+2].append(thisroundoferror[(somenum*9)+5])
#        myerror_cir[(somenum*3)].append(thisroundoferror[(somenum*9)+6])
#        myerror_cir[(somenum*3)+1].append(thisroundoferror[(somenum*9)+7])
#        myerror_cir[(somenum*3)+2].append(thisroundoferror[(somenum*9)+8])
#        
#        
#        
#for myrunningcount in range(0,5):
#    print " " 
#    print myrunningcount
#    print weight16
#    print weightsout
#    mynew_weightout_neverused.append(weightsout.tolist())
#    mynew_weight16_neverused.append([weight16[0].tolist(),
#                                     weight16[1].tolist(),
#                                     weight16[2].tolist(),
#                                     weight16[3].tolist(),
#                                     weight16[4].tolist(),
#                                     weight16[5].tolist(),
#                                     weight16[6].tolist(),
#                                     weight16[7].tolist(),
#                                     weight16[8].tolist(),
#                                     weight16[9].tolist()])
#    mypixel = shapes_normal[0]
#    idealans=[1,0,0]
#    execfile("sense_filter_sum_learn.py")
#    mypixel = shapes_normal[1]
#    idealans=[0,1,0]
#    execfile("sense_filter_sum_learn.py")
#    mypixel = shapes_normal[2]
#    idealans=[0,0,1]
#    execfile("sense_filter_sum_learn.py")
#    for othercoutzzz in range(0,10):
#        execfile("singleiteration.py")
#    for somenum in range(0,36):
#        myerror_tri[(somenum*3)].append(thisroundoferror[(somenum*9)])
#        myerror_tri[(somenum*3)+1].append(thisroundoferror[(somenum*9)+1])
#        myerror_tri[(somenum*3)+2].append(thisroundoferror[(somenum*9)+2])
#        myerror_squ[(somenum*3)].append(thisroundoferror[(somenum*9)+3])
#        myerror_squ[(somenum*3)+1].append(thisroundoferror[(somenum*9)+4])
#        myerror_squ[(somenum*3)+2].append(thisroundoferror[(somenum*9)+5])
#        myerror_cir[(somenum*3)].append(thisroundoferror[(somenum*9)+6])
#        myerror_cir[(somenum*3)+1].append(thisroundoferror[(somenum*9)+7])
#        myerror_cir[(somenum*3)+2].append(thisroundoferror[(somenum*9)+8])
    
#[34, 34, 34, 34, 34, 34, 32, 32, 0, 34, 34, 20, 34, 0, 20, 34]  #triangle
#[0, 0, 0, 0, 0, 0, 0, 0, 20, 34, 34, 20, 34, 20, 20, 34]        #square
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 34, 0, 34, 0, 0, 34]            #circle
#
#[34, 34, 34, 34, 34, 34, 32, 32, 0, 34, 34, 20, 34, 0, 20, 34]  #triangle
#[34, 34, 34, 34, 32, 32, 34, 34, 20, 34, 34, 0, 34, 20, 0, 34]  #tri
#[34, 32, 34, 32, 34, 34, 34, 34, 0, 34, 34, 20, 34, 20, 0, 34]
#[32, 34, 32, 34, 34, 34, 34, 34, 20, 34, 34, 0, 34, 0, 20, 34]
#[33, 33, 29, 29, 33, 33, 33, 33, 0, 63, 33, 21, 63, 0, 21, 33]
#[34, 34, 33, 33, 33, 33, 34, 34, 0, 34, 34, 34, 34, 0, 34, 34]
#
#[0, 0, 0, 0, 0, 0, 0, 0, 20, 34, 34, 20, 34, 20, 20, 34] # square
#[1, 1, 1, 1, 1, 1, 1, 1, 39, 66, 66, 39, 66, 39, 39, 66]
#[1, 1, 1, 1, 1, 1, 1, 1, 21, 66, 66, 21, 66, 21, 21, 66]
#[0, 0, 1, 1, 1, 0, 1, 0, 20, 34, 66, 20, 24, 20, 39, 24]
#[1, 1, 0, 0, 0, 1, 0, 1, 20, 66, 34, 20, 24, 39, 20, 24]
#[0, 0, 1, 1, 0, 1, 0, 1, 34, 24, 24, 21, 34, 6, 6, 66]
#[1, 1, 0, 0, 1, 0, 1, 0, 21, 24, 24, 34, 66, 6, 6, 34]
#[1, 1, 1, 1, 1, 1, 1, 1, 47, 66, 87, 47, 66, 39, 58, 66]
#[1, 1, 1, 1, 1, 1, 1, 1, 47, 87, 66, 47, 66, 58, 39, 66]
#
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 34, 0, 34, 0, 0, 34] ## all circles



#[34, 34, 34, 34, 34, 34, 32, 32, 0, 34, 34, 20, 34, 0, 20, 34] # circle
#[34, 34, 34, 34, 32, 32, 34, 34, 20, 34, 34, 0, 34, 20, 0, 34] # circle1
#[33, 33, 29, 29, 33, 33, 33, 33, 0, 63, 33, 21, 63, 0, 21, 33] # circle4
#
#[0, 0, 0, 0, 0, 0, 0, 0, 20, 34, 34, 20, 34, 20, 20, 34] ## square
#[1, 1, 1, 1, 1, 1, 1, 1, 39, 66, 66, 39, 66, 39, 39, 66] ## square1
#
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 34, 0, 34, 0, 0, 34]  ## circle #also all the circles are the same 

#for myrunningcount in range(0,1000):
#    mypixel = shapes_normal[0]
#    print "triangle"
#    idealans=[1,0,0]
#    execfile("sense_filter_sum_learn.py")
    
    
    
#for thisx in range (0,len(triround_1)):
#    mypixel = triround_1[thisx]
#    print thisx
#    idealans=[1,0,0]
#    execfile("sense_filter_sum_learn.py")
        
        
        
####### DOOOO THIS THING AFTER YOU RUN EVERYTHING 

#summmmofcount=[]
#for otherxthing in range(0,len(myerror_tri[0])):
#    count_error_thisthing=0
#    for myexrn in range(0,108):
#        count_error_thisthing+=myerror_tri[myexrn][otherxthing]
#    summmmofcount.append(count_error_thisthing/108)
#print summmmofcount
#
#summmmofcount=[]
#for otherxthing in range(0,len(myerror_squ[0])):
#    count_error_thisthing=0
#    for myexrn in range(0,108):
#        count_error_thisthing+=myerror_squ[myexrn][otherxthing]
#    summmmofcount.append(count_error_thisthing/108)
#print summmmofcount
#
#summmmofcount=[]
#for otherxthing in range(0,len(myerror_cir[0])):
#    count_error_thisthing=0
#    for myexrn in range(0,108):
#        count_error_thisthing+=myerror_cir[myexrn][otherxthing]
#    summmmofcount.append(count_error_thisthing/108)
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
    
    

#print (numpy.array(mynew_weight16_neverused[33][0])*100).astype(int)==(numpy.array(mynew_weight16_neverused[34][0])*100).astype(int)
#print (numpy.array(mynew_weight16_neverused[33][1])*100).astype(int)==(numpy.array(mynew_weight16_neverused[34][1])*100).astype(int)
#print (numpy.array(mynew_weight16_neverused[33][2])*100).astype(int)==(numpy.array(mynew_weight16_neverused[34][2])*100).astype(int)
#print (numpy.array(mynew_weight16_neverused[33][3])*100).astype(int)==(numpy.array(mynew_weight16_neverused[34][3])*100).astype(int)
#print (numpy.array(mynew_weight16_neverused[33][4])*100).astype(int)==(numpy.array(mynew_weight16_neverused[34][4])*100).astype(int)
#print (numpy.array(mynew_weight16_neverused[33][5])*100).astype(int)==(numpy.array(mynew_weight16_neverused[34][5])*100).astype(int)
#print (numpy.array(mynew_weight16_neverused[33][6])*100).astype(int)==(numpy.array(mynew_weight16_neverused[34][6])*100).astype(int)
#print (numpy.array(mynew_weight16_neverused[33][7])*100).astype(int)==(numpy.array(mynew_weight16_neverused[34][7])*100).astype(int)




### after 250 runs of the original 
#[array([-0.07638602, -0.05685437,  0.02311014,  0.06310116, -0.00695437,
#         0.11307102, -0.07682737, -0.01672541,  0.15      ,  0.00922845,
#         0.14984146,  0.15      , -0.04486159,  0.15      ,  0.02579504,
#         0.01537461]),
# array([-0.0281322 , -0.03884103, -0.06884457, -0.08885465, -0.03943497,
#         0.10059907, -0.02924515, -0.04909465,  0.0686469 ,  0.15      ,
#         0.12698184, -0.02171466,  0.15      ,  0.15      ,  0.03039247,
#         0.15      ]),
# array([ 0.0774183 ,  0.1499996 ,  0.01809151,  0.12816511,  0.1499996 ,
#        -0.04120937,  0.01852243,  0.04840599, -0.00811033,  0.00377619,
#        -0.02709695,  0.00508506,  0.06343131,  0.04262318,  0.1287957 ,
#        -0.01624666]),
# array([ 0.05900154,  0.05025042,  0.03004574,  0.06009578,  0.14999575,
#         0.09090122, -0.0294264 ,  0.14999824, -0.12439125,  0.15      ,
#         0.15      , -0.12195403,  0.15      , -0.03172398,  0.03063798,
#         0.15      ]),
# array([-0.04507863,  0.08442384, -0.05532698, -0.01540112, -0.09561447,
#        -0.09561312,  0.06436555,  0.00443747,  0.06645891,  0.14560551,
#         0.07594635,  0.02593867,  0.15      ,  0.08220471,  0.07918231,
#         0.04594764]),
# array([-0.04844359,  0.05157442,  0.12157861,  0.071573  , -0.06837966,
#         0.11162204, -0.07839086, -0.0783931 , -0.07167353,  0.09171741,
#         0.15      ,  0.13833878,  0.09210499,  0.10823562, -0.04217088,
#         0.15      ]),
# array([-0.04675499,  0.07239357, -0.06740212,  0.03248304,  0.0321031 ,
#         0.00209229, -0.0077049 , -0.09759294,  0.15      ,  0.15      ,
#         0.15      ,  0.04678499,  0.07895975,  0.04228295,  0.10795647,
#         0.15      ]),
# array([ 0.01093908,  0.13117938, -0.05896581,  0.06104696,  0.07156699,
#         0.04150851,  0.0914763 ,  0.1113799 , -0.03040368, -0.03950175,
#         0.10214957,  0.09246443, -0.06733553,  0.08199775,  0.15      ,
#         0.13204972]),
# array([ 0.09397575,  0.1499991 ,  0.10504868,  0.14506238,  0.1499991 ,
#         0.05590429,  0.09567325,  0.11548044,  0.02710342,  0.14308801,
#         0.10474537,  0.02042004, -0.05528315,  0.058258  , -0.01525904,
#        -0.06350203]),
# array([ 0.00772121,  0.07793073,  0.12780643, -0.04219347,  0.0981634 ,
#        -0.04178417,  0.07813825,  0.06815578,  0.15      ,  0.13504975,
#        -0.00587626,  0.07976501,  0.0242636 ,  0.07263196,  0.04418251,
#        -0.0250944 ])]

#weightsout
#array([[-0.01385135, -0.15      ,  0.14976592,  0.14854409, -0.08937733,
#         0.14776773, -0.02167841,  0.14915618,  0.14938388,  0.14908119],
#       [ 0.14900845,  0.14706847, -0.14893192, -0.14904689,  0.14666269,
#         0.05747557,  0.14706847,  0.14926712, -0.14904067,  0.1491592 ],
#       [-0.14858378,  0.15      , -0.15      ,  0.15      ,  0.15      ,
#         0.15      ,  0.15      , -0.14895323, -0.14688179, -0.14869455]])
#    
    
    
    
    