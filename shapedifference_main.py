execfile("shapedata.py") 

normal_data_sens  = [0,0,0]
circle_data_sens  = [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
normal_data_sum  = normal_data_sens
circle_data_sum  = circle_data_sens
#triangle_data_sens  = [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 
#                       0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 
#                       0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 
#                       0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#                       0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
#square_data_sens  = [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 
#                     0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#                     0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#                     0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#                     0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0,
#                     0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]


#normal_data_filt1  = normal_data_sens
#triangle_data_filt1  = triangle_data_sens
#square_data_filt1  = square_data_sens
#circle_data_filt1  = circle_data_sens
#
#normal_data_filt2  = normal_data_sens
#triangle_data_filt2  = triangle_data_sens
#square_data_filt2  = square_data_sens
#circle_data_filt2  = circle_data_sens
#
#normal_data_filt3  = normal_data_sens
#triangle_data_filt3  = triangle_data_sens
#square_data_filt3  = square_data_sens
#circle_data_filt3  = circle_data_sens
#
#normal_data_filt4  = normal_data_sens
#triangle_data_filt4  = triangle_data_sens
#square_data_filt4  = square_data_sens
#circle_data_filt4  = circle_data_sens
#




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

triround_3=[15,16,17,18,97,98,101,102]


squround_1=[mysqu,0,1,2,3,4,5,6,7,8,9,
            10,11,12,13,
            65,66,67,68,
            81,82,83,84]

squround_2=[14,15,16,17,18,19,
            20,21,22,23,24,25,
            39,
            40,41,42,43,44,45,46,47,48,49,
            50,51,
            69,
            70,71,72,73,74,75,76,77,
            89,
            90,91,92,97,98,99,
            100,105,106,107,108,
            113,114,115,116,
            121,122,123,124,129,
            130,131,132,137,138,139,
            140]

squround_3=[26,27,28,29,
            30,31,32,33,34,35,36,37,38,
            52,53,54,55,56,57,58,59,
            60,61,62,63,64,
            78,79,
            80,85,86,87,88,
            93,94,95,96,
            101,102,103,104,109,
            110,111,112,117,118,119,
            120,125,126,127,128,
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


### 3 ROUNDS OF TRIANGLES 
### 3 ROUNDS OF SQUARES 
### 1 ROUND OF CIRCLES 

#    normal_data_filt1[thisx]=curr_spike_filt1
#    normal_data_filt2[thisx]=curr_spike_filt2
#    normal_data_filt3[thisx]=curr_spike_filt3
#    normal_data_filt4[thisx]=curr_spike_filt4
#    triangle_data_filt1[thisx]=curr_spike_filt1
#    triangle_data_filt2[thisx]=curr_spike_filt2
#    triangle_data_filt3[thisx]=curr_spike_filt3
#    triangle_data_filt4[thisx]=curr_spike_filt4


for thisx in range (0,3):
    mypixel = shapes_normal[thisx]
    print thisx
    execfile("sense_filter_sum_MORE.py")
    normal_data_sens[thisx]=curr_spike_sens
    normal_data_sum[thisx]=curr_spike_sum
    
for thisx in range (0,len(weird_circles1)):
    mypixel = weird_circles1[thisx]
    print thisx
    execfile("sense_filter_sum_MORE.py")
    circle_data_sens[thisx]=curr_spike_sens
    circle_data_sum[thisx]=curr_spike_sum
    
##    triround_1
for thisx in range (0,len(triround_1)):
    mypixel = triround_1[thisx]
    print thisx
    execfile("sense_filter_sum_MORE.py")
    triangle_data_sens[0][thisx]=curr_spike_sens
    triangle_data_sum[0][thisx]=curr_spike_sum

for thisx in range (0,len(squround_1)):
    mypixel = squround_1[thisx]
    print thisx
    execfile("sense_filter_sum_MORE.py")
    square_data_sens[0][thisx]=curr_spike_sens
    square_data_sum[0][thisx]=curr_spike_sum
    
#for thisx in range (0,len(triround_2)):
#    mypixel = triround_2[thisx]
#    print thisx
#    execfile("sense_filter_sum_MORE.py")
#    triangle_data_sens[1][thisx]=curr_spike_sens
#    triangle_data_sum[1][thisx]=curr_spike_sum
#
#for thisx in range (0,len(squround_2)):
#    mypixel = squround_2[thisx]
#    print thisx
#    execfile("sense_filter_sum_MORE.py")
#    square_data_sens[1][thisx]=curr_spike_sens
#    square_data_sum[1][thisx]=curr_spike_sum
#
#for thisx in range (0,len(triround_3)):
#    mypixel = triround_3[thisx]
#    print thisx
#    execfile("sense_filter_sum_MORE.py")
#    triangle_data_sens[2][thisx]=curr_spike_sens
#    triangle_data_sum[2][thisx]=curr_spike_sum
#    
#for thisx in range (0,len(squround_3)):
#    mypixel = squround_3[thisx]
#    print thisx
#    execfile("sense_filter_sum_MORE.py")
#    square_data_sens[2][thisx]=curr_spike_sens
#    square_data_sum[2][thisx]=curr_spike_sum


    
    
#curr_spike_sens = numpy.array(spike_sensors.count).astype(int)
#curr_spike_filt1 = numpy.array(spike_filt1.count).astype(int)
#curr_spike_filt2 =  numpy.array(spike_filt2.count).astype(int)
#curr_spike_filt3 =  numpy.array(spike_filt3.count).astype(int)
#curr_spike_filt4 =  numpy.array(spike_filt4.count).astype(int)
#curr_spike_sum =  numpy.array(spike_sum.count).astype(int)
#
#triangle_round1_1=[]
#triangle_round2_1=[]
#triangle_round1_2=[]
#triangle_round2_2=[]
#triangle_round1_3=[]
#triangle_round2_3=[]
#triangle_round1_4=[]
#triangle_round2_4=[]
#triangle_round3=[]
#
#square_round1_1=[]
#square_round2_1=[]
#square_round1_2=[]
#square_round2_2=[]
#square_round1_3=[]
#square_round2_3=[]
#square_round1_4=[]
#square_round2_4=[]
#square_round3=[]
###compare normal triangle to weird ones... 
#print "COMPARING NORMAL TRIANGLE TO ALL TRIANGLES "
### comparing by filter FILTER 1 
#print "COMPARING FILTER 1"
#for thisx in range(0,len(weird_triangles1)): 
#    if any(~((0.18*(normal_data_sum[0][0]))>=(triangle_data_sum[thisx][0]/10)) | ~((0.05*(normal_data_sum[0][0]))<=(triangle_data_sum[thisx][0]/10))):
#        if any(~((0.18*(triangle_data_sum[0][0]))>=(triangle_data_sum[thisx][0]/10)) | ~((0.05*(triangle_data_sum[0][0]))<=(triangle_data_sum[thisx][0]/10))):
#            print thisx 
#            triangle_round2_1.append(thisx)
#        else:
#            triangle_round1_1.append(thisx)
#    else:
#        triangle_round1_1.append(thisx)
#
### comparing by filter FILTER 2 
#print "COMPARING FILTER 2" 
#for thisx in range(0,len(weird_triangles1)):
#    if any(~((0.18*(normal_data_sum[0][1]))>=(triangle_data_sum[thisx][1]/10)) | ~((0.05*(normal_data_sum[0][1]))<=(triangle_data_sum[thisx][1]/10))):
#        if any(~((0.18*(triangle_data_sum[0][1]))>=(triangle_data_sum[thisx][1]/10)) | ~((0.05*(triangle_data_sum[0][1]))<=(triangle_data_sum[thisx][1]/10))):
#            print thisx 
#            triangle_round2_2.append(thisx)
#        else:
#            triangle_round1_2.append(thisx)
#    else:
#        triangle_round1_2.append(thisx)
#
#print "COMPARING FILTER 3" 
#for thisx in range(0,len(weird_triangles1)):
#    if any(~((0.18*(normal_data_sum[0][2]))>=(triangle_data_sum[thisx][2]/10)) | ~((0.05*(normal_data_sum[0][2]))<=(triangle_data_sum[thisx][2]/10))):
#        if any(~((0.18*(triangle_data_sum[0][2]))>=(triangle_data_sum[thisx][2]/10)) | ~((0.05*(triangle_data_sum[0][2]))<=(triangle_data_sum[thisx][2]/10))):
#            print thisx 
#            triangle_round2_3.append(thisx)
#        else:
#            triangle_round1_3.append(thisx)
#    else:
#        triangle_round1_3.append(thisx)
#        
#print "COMPARING FILTER 4" 
#for thisx in range(0,len(weird_triangles1)):
#    if any(~((0.18*(normal_data_sum[0][3]))>=(triangle_data_sum[thisx][3]/10)) | ~((0.05*(normal_data_sum[0][3]))<=(triangle_data_sum[thisx][3]/10))):
#        if any(~((0.18*(triangle_data_sum[0][3]))>=(triangle_data_sum[thisx][3]/10)) | ~((0.05*(triangle_data_sum[0][3]))<=(triangle_data_sum[thisx][3]/10))):
#            print thisx
#            triangle_round2_4.append(thisx)
#        else:
#            triangle_round1_4.append(thisx)
#    else:
#        triangle_round1_4.append(thisx)
###normal_data_sum[0]
##Out[13]: 
##array([[34, 34, 34, 34],
##       [34, 34, 32, 32],
##       [ 0, 34, 34, 20],
##       [34,  0, 20, 34]])
#        
#        
##array([[34, 34, 34, 34],
##       [32, 32, 34, 34],
##       [20, 34, 34,  0],
##       [34, 20,  0, 34]])
#        
#tri_round1=[0,0,0,0]
#tri_round1[0]=triangle_round1_1
#tri_round1[1]=triangle_round1_2
#tri_round1[2]=triangle_round1_3
#tri_round1[3]=triangle_round1_4
#
#print len(triangle_round1_1)
#print len(triangle_round1_2)
#print len(triangle_round1_3)
#print len(triangle_round1_4)
#print " " 
#print len(triangle_round2_1)
#print len(triangle_round2_2)
#print len(triangle_round2_3)
#print len(triangle_round2_4)
#
#
#
#
##for thisx in range(0,len(triangle_round1_1)):
# #   print triangle_data_sum[triangle_round1_1[x]]
#
#print "COMPARING NORMAL SQUARE TO ALL SQUARES "
#print "COMPARING FILTER 1"
#for thisx in range(0,len(weird_squares1)): 
#    if any(~((0.18*(normal_data_sum[1][0]))>=(square_data_sum[thisx][0]/10)) | ~((0.05*(normal_data_sum[1][0]))<=(square_data_sum[thisx][0]/10))):
#        print thisx 
#        square_round2_1.append(thisx)
#    else:
#        square_round1_1.append(thisx)
#
### comparing by filter FILTER 2 
#print "COMPARING FILTER 2" 
#for thisx in range(0,len(weird_squares1)):
#    if any(~((0.18*(normal_data_sum[1][1]))>=(square_data_sum[thisx][1]/10)) | ~((0.05*(normal_data_sum[1][1]))<=(square_data_sum[thisx][1]/10))):
#        print thisx
#        square_round2_2.append(thisx)
#    else:
#        square_round1_2.append(thisx)
#
#print "COMPARING FILTER 3" 
#for thisx in range(0,len(weird_squares1)):
#    if any(~((0.18*(normal_data_sum[1][2]))>=(square_data_sum[thisx][2]/10)) | ~((0.05*(normal_data_sum[1][2]))<=(square_data_sum[thisx][2]/10))):
#        print thisx 
#        square_round2_3.append(thisx)
#    else:
#        square_round1_3.append(thisx)
#        
#print "COMPARING FILTER 4" 
#for thisx in range(0,len(weird_squares1)):
#    if any(~((0.18*(normal_data_sum[1][3]))>=(square_data_sum[thisx][3]/10)) | ~((0.05*(normal_data_sum[1][3]))<=(square_data_sum[thisx][3]/10))):
#        print thisx 
#        square_round2_4.append(thisx)
#    else:
#        square_round1_4.append(thisx)



#for x in range (0,len(triround_1)):
#    myshapeshow = triround_1[x]
#    plt.imshow(myshapeshow,cmap='gray')
#    plt.show()
#for x in range (0,len(squround_1)):
#    myshapeshow = squround_1[x]
#    plt.imshow(myshapeshow,cmap='gray')
#    plt.show()
#for x in range (0,len(triround_2)):
#    myshapeshow = triround_2[x]
#    plt.imshow(myshapeshow,cmap='gray')
#    plt.show()
#for x in range (0,len(squround_2)):
#    myshapeshow = squround_2[x]
#    plt.imshow(myshapeshow,cmap='gray')
#    plt.show()
#for x in range (0,len(triround_3)):
#    myshapeshow = triround_3[x]
#    plt.imshow(myshapeshow,cmap='gray')
#    plt.show()
#for x in range (0,len(squround_3)):
#    myshapeshow = squround_3[x]
#    plt.imshow(myshapeshow,cmap='gray')
#    plt.show()
