#### THIS IS A SINGLE ITERATION

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