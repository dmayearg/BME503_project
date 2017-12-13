from brian2.core.operations import network_operation

#from brian2 import *
#import matplotlib.pyplot as plt

execfile("stdpshapedata.py")

shapedatamatrix=[triround_1[0],triround_1[4],triround_1[5],
                 squround_1[0],squround_1[1],squround_1[23],
                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
                 triround_1[6],triround_1[7],triround_1[12],
                 squround_1[24],squround_1[25],squround_1[26],
                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
                 triround_1[28],triround_1[32],triround_1[33],
                 squround_1[31],squround_1[32],squround_1[33],
                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
                 triround_1[34],triround_1[35],triround_1[40],
                 squround_1[34],squround_2[0],squround_2[1],
                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
                 triround_1[41],triround_1[56],triround_1[57],
                 squround_2[2],squround_2[3],squround_2[4],
                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
                 triround_1[58],triround_1[59],triround_1[60],
                 squround_2[5],squround_2[6],squround_2[7],
                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
                 triround_1[9],triround_1[14],triround_1[30],
                 squround_1[3],squround_1[4],squround_1[5],
                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
                 triround_1[31],triround_2[0],triround_2[1],
                 squround_1[8],squround_1[9],squround_1[14],
                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
                 triround_2[7],triround_2[10],triround_2[11],
                 squround_1[35],squround_1[40],squround_1[43],
                 shapes_normal[2],shapes_normal[2],shapes_normal[2],
                 triround_2[12],triround_2[16],triround_2[17],
                 squround_2[10],squround_2[12],squround_2[15],
                 shapes_normal[2],shapes_normal[2],shapes_normal[2]]

idealansmatrix=[[1,0,0],[1,0,0],[1,0,0],
                [0,1,0],[0,1,0],[0,1,0],
                [0,0,1],[0,0,1],[0,0,1],
                [1,0,0],[1,0,0],[1,0,0],
                [0,1,0],[0,1,0],[0,1,0],
                [0,0,1],[0,0,1],[0,0,1],
                [1,0,0],[1,0,0],[1,0,0],
                [0,1,0],[0,1,0],[0,1,0],
                [0,0,1],[0,0,1],[0,0,1],
                [1,0,0],[1,0,0],[1,0,0],
                [0,1,0],[0,1,0],[0,1,0],
                [0,0,1],[0,0,1],[0,0,1],
                [1,0,0],[1,0,0],[1,0,0],
                [0,1,0],[0,1,0],[0,1,0],
                [0,0,1],[0,0,1],[0,0,1],
                [1,0,0],[1,0,0],[1,0,0],
                [0,1,0],[0,1,0],[0,1,0],
                [0,0,1],[0,0,1],[0,0,1],
                [1,0,0],[1,0,0],[1,0,0],
                [0,1,0],[0,1,0],[0,1,0],
                [0,0,1],[0,0,1],[0,0,1],
                [1,0,0],[1,0,0],[1,0,0],
                [0,1,0],[0,1,0],[0,1,0],
                [0,0,1],[0,0,1],[0,0,1],
                [1,0,0],[1,0,0],[1,0,0],
                [0,1,0],[0,1,0],[0,1,0],
                [0,0,1],[0,0,1],[0,0,1],
                [1,0,0],[1,0,0],[1,0,0],
                [0,1,0],[0,1,0],[0,1,0],
                [0,0,1],[0,0,1],[0,0,1]]


## INITIALIZE
mypixel = []
idealans = []
mypixel=shapedatamatrix[0] ### update the shape 
idealans=idealansmatrix[0] ### update the ideal output 

## fast spiking izhikevich model 
a = 0.1
b = 0.2
c = -65
d = 2

sens_tau_decay=1.5*ms ## maybe 1 for all or 2 ?
filt_tau_decay=2*ms
sum_tau_decay=2*ms
taupre=5*ms 
taupost=20*ms
Apre = 0.001
Apost = -Apre*1.05

sensormag=2.2 ## the very minimum is 1.3 for it to fire with 3 inputs to make sensor neuron fire
## to fire with 2 input "on" is about 2.2
filtg_synmaxval=0.15 ##// if this is too low there is no difference between circ and square
sumg_synmaxval=0.06 
duration = 1000*ms


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


##############################################################################
################################## NEURONS ##################################
##############################################################################



sensor_eqs = '''
dv/dt = ((0.04*v*v) + ( 5*v) + (140) - u + mag*I)/ms : 1
du/dt = a*((b*v)-u)/ms : 1
dg_exc/dt= (-g_exc/tau_decay) + (z_exc/ms) : 1 
dz_exc/dt = -z_exc/tau_decay : 1
synI_exc = -g_exc *(v-E_exc) : 1
I= (x0+x1+x2+x3+x4+x5+x6+x7+x8) :1
tau_decay : second
E_exc : 1
x0:1
x1:1
x2:1
x3:1
x4:1
x5:1
x6:1
x7:1
x8:1
mag:1
'''



sensors = NeuronGroup(36, sensor_eqs, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
sensors.v = c
sensors.u = c*b
sensors.mag = sensormag ## 1.3 or 1.4 or 1.5 or 2 tbh idk what im doing 
sensors.tau_decay = sens_tau_decay
sensors.g_exc=0
for x in range (0,6):
    for y in range (0,6):
        curr=(y*6)+x
        sensors.x0[curr]=mypixel[(y*3)][(x*3)]
        sensors.x1[curr]=mypixel[(y*3)][(x*3)+1]
        sensors.x2[curr]=mypixel[(y*3)][(x*3)+2]
        sensors.x3[curr]=mypixel[(y*3)+1][(x*3)]
        sensors.x4[curr]=mypixel[(y*3)+1][(x*3)+1]
        sensors.x5[curr]=mypixel[(y*3)+1][(x*3)+2]
        sensors.x6[curr]=mypixel[(y*3)+2][(x*3)]
        sensors.x7[curr]=mypixel[(y*3)+2][(x*3)+1]
        sensors.x8[curr]=mypixel[(y*3)+2][(x*3)+2]
        
        
filt_equ = '''
dv/dt = ((0.04*v*v) + ( 5*v) + (140) - u + synI_exc)/ms : 1
du/dt = a*((b*v)-u)/ms : 1
dg_exc/dt= (-g_exc/tau_decay) + (z_exc/ms) : 1 
dz_exc/dt = -z_exc/tau_decay : 1
synI_exc = -g_exc *(v-E_exc) : 1
tau_decay : second
E_exc : 1
'''
        
filt1 = NeuronGroup(16, filt_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt1.v = c
filt1.u = c*b
filt1.tau_decay = filt_tau_decay
#filt1.g_exc=0  

filt2 = NeuronGroup(16, filt_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt2.v = c
filt2.u = c*b
filt2.tau_decay = filt_tau_decay
#filt2.g_exc=0  

filt3 = NeuronGroup(16, filt_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt3.v = c
filt3.u = c*b
filt3.tau_decay = filt_tau_decay
#filt3.g_exc=0  

filt4 = NeuronGroup(16, filt_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt4.v = c
filt4.u = c*b
filt4.tau_decay = filt_tau_decay
#filt4.g_exc=0  

filtersize=16

sum_equ = '''
dv/dt = ((0.04*v*v) + ( 5*v) + (140) - u + synI_exc)/ms : 1
du/dt = a*((b*v)-u)/ms : 1
dg_exc/dt= (-g_exc/tau_decay) + (z_exc/ms) : 1 
dz_exc/dt = -z_exc/tau_decay : 1
synI_exc = -g_exc *(v-E_exc) : 1
tau_decay : second
E_exc : 1
'''
sumneur = NeuronGroup(16, sum_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
sumneur.v = c
sumneur.u = c*b
sumneur.tau_decay = sum_tau_decay



midneur16 = NeuronGroup(10, sum_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
midneur16.v = c
midneur16.u = c*b
midneur16.tau_decay = sum_tau_decay


shape_equ = '''
dv/dt = ((0.04*v*v) + ( 5*v) + (140) - u + synI_exc + clampedcurrent)/ms : 1
du/dt = a*((b*v)-u)/ms : 1
dg_exc/dt= (-g_exc/tau_decay) + (z_exc/ms) : 1 
dz_exc/dt = -z_exc/tau_decay : 1
synI_exc = -g_exc *(v-E_exc) : 1
tau_decay : second
E_exc : 1
clampedcurrent:1
'''
whichshape16 = NeuronGroup(3, shape_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
whichshape16.v = c
whichshape16.u = c*b
whichshape16.tau_decay = sum_tau_decay
whichshape16.clampedcurrent[0]=20
whichshape16.clampedcurrent[1]=0
whichshape16.clampedcurrent[2]=0
##############################################################################
################################## SYNAPSES ##################################
##############################################################################


syn_filt1 = Synapses(sensors, filt1, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
for x in range (0,3):
    for y in range(0,16):
        syn_filt1.connect(i=[filt1synpase[y][x]],j=[y])
syn_filt1.g_synmax=filtg_synmaxval
      
syn_filt2 = Synapses(sensors, filt2, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
for x in range (0,3):
    for y in range(0,16):
        syn_filt2.connect(i=[filt2synapse[y][x]],j=[y])
syn_filt2.g_synmax=filtg_synmaxval

  
syn_filt3 = Synapses(sensors, filt3, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
for x in range (0,3):
    for y in range(0,16):
        syn_filt3.connect(i=[filt3synapse[y][x]],j=[y])
syn_filt3.g_synmax=filtg_synmaxval

syn_filt4 = Synapses(sensors, filt4, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
for x in range (0,3):
    for y in range(0,16):
        syn_filt4.connect(i=[filt4synapse[y][x]],j=[y])
syn_filt4.g_synmax=filtg_synmaxval

##############################################################################
################################## SYNAPSES ##################################
########################## FILTER TO SUMMING NEURON ##########################
##############################################################################

syn_sum1 = Synapses(filt1, sumneur, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_sum1.connect(i=[0, 1, 4, 5],j=[0])
syn_sum1.connect(i=[2, 3, 6, 7],j=[1])
syn_sum1.connect(i=[8, 9,12,13],j=[2])
syn_sum1.connect(i=[10,11,14,15],j=[3])
syn_sum1.g_synmax=sumg_synmaxval

syn_sum2 = Synapses(filt2, sumneur, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_sum2.connect(i=[0, 1, 4, 5],j=[4])
syn_sum2.connect(i=[2, 3, 6, 7],j=[5])
syn_sum2.connect(i=[8, 9,12,13],j=[6])
syn_sum2.connect(i=[10,11,14,15],j=[7])
syn_sum2.g_synmax=sumg_synmaxval

syn_sum3 = Synapses(filt3, sumneur, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_sum3.connect(i=[0, 1, 4, 5],j=[8])
syn_sum3.connect(i=[2, 3, 6, 7],j=[9])
syn_sum3.connect(i=[8, 9,12,13],j=[10])
syn_sum3.connect(i=[10,11,14,15],j=[11])
syn_sum3.g_synmax=sumg_synmaxval

syn_sum4 = Synapses(filt4, sumneur, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_sum4.connect(i=[0, 1, 4, 5],j=[12])
syn_sum4.connect(i=[2, 3, 6, 7],j=[13])
syn_sum4.connect(i=[8, 9,12,13],j=[14])
syn_sum4.connect(i=[10,11,14,15],j=[15])
syn_sum4.g_synmax=sumg_synmaxval


######################### the crazy synapses ###########################
syn_eqns = '''
g_synmax: 1
w:1
dapre/dt=-apre/taupre : 1
dapost/dt=-apost/taupost : 1
'''
######################### ADD THE ON_PRE  AND ON_POST TRACES 
midsyn1 = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -0.2, 0.2)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -0.2, 0.2)''')
midsyn1.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[0])
midsyn1.w=weight16[0]

midsyn2 = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -0.2, 0.2)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -0.2, 0.2)''')
midsyn2.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[1])
midsyn2.w=weight16[1]

midsyn3 = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -0.2, 0.2)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -0.2, 0.2)''')
midsyn3.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[2])
midsyn3.w=weight16[2]

midsyn4 = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -0.2, 0.2)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -0.2, 0.2)''')
midsyn4.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[3])
midsyn4.w=weight16[3]

midsyn5 = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -0.2, 0.2)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -0.2, 0.2)''')
midsyn5.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[4])
midsyn5.w=weight16[4]

midsyn6 = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -0.2, 0.2)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -0.2, 0.2)''')
midsyn6.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[5])
midsyn6.w=weight16[5]

midsyn7 = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -0.2, 0.2)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -0.2, 0.2)''')
midsyn7.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[6])
midsyn7.w=weight16[6]

midsyn8 = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -0.2, 0.2)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -0.2, 0.2)''')
midsyn8.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[7])
midsyn8.w=weight16[7]

midsyn9 = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -0.2, 0.2)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -0.2, 0.2)''')
midsyn9.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[8])
midsyn9.w=weight16[8]

midsyn10 = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -0.2, 0.2)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -0.2, 0.2)''')
midsyn10.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[9])
midsyn10.w=weight16[9]

shapesyn1 = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -0.2, 0.2)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -0.2, 0.2)''')
shapesyn1.connect(i=[0,1,2,3,4,5,6,7,8,9],j=[0])
shapesyn1.w=weightsout[0]

shapesyn2 = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -0.2, 0.2)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -0.2, 0.2)''')
shapesyn2.connect(i=[0,1,2,3,4,5,6,7,8,9],j=[1])
shapesyn2.w=weightsout[1]

shapesyn3 = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -0.2, 0.2)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -0.2, 0.2)''')
shapesyn3.connect(i=[0,1,2,3,4,5,6,7,8,9],j=[2])
shapesyn3.w=weightsout[2]



    
mycount=1
# @network_operation(dt=1005*ms)
# def printWeights():
#     print shapesyn1.w
#     print mypixel
#     print idealans

@network_operation(dt=1000*ms)
def update_stuff():
    global mycount
    global mypixel
    global idealans
    mypixel=shapedatamatrix[mycount] ### update the shape 
    idealans=idealansmatrix[mycount] ### update the ideal output 
    whichshape16.clampedcurrent[0]=idealans[0]*8
    whichshape16.clampedcurrent[1]=idealans[1]*8
    whichshape16.clampedcurrent[2]=idealans[2]*8
    mycount=mycount+1
    if mycount == 54:
        mycount = 0
    for x in range (0,6):
        for y in range (0,6):
            curr=(y*6)+x
            sensors.x0[curr]=mypixel[(y*3)][(x*3)]
            sensors.x1[curr]=mypixel[(y*3)][(x*3)+1]
            sensors.x2[curr]=mypixel[(y*3)][(x*3)+2]
            sensors.x3[curr]=mypixel[(y*3)+1][(x*3)]
            sensors.x4[curr]=mypixel[(y*3)+1][(x*3)+1]
            sensors.x5[curr]=mypixel[(y*3)+1][(x*3)+2]
            sensors.x6[curr]=mypixel[(y*3)+2][(x*3)]
            sensors.x7[curr]=mypixel[(y*3)+2][(x*3)+1]
            sensors.x8[curr]=mypixel[(y*3)+2][(x*3)+2]
            
    sensors.v = c
    sensors.u = c*b
    sensors.g_exc = 0
    sensors.z_exc = 0
    filt1.v = c
    filt1.u = c*b
    filt1.g_exc = 0
    filt1.z_exc = 0
    filt2.v = c
    filt2.u = c*b
    filt2.g_exc = 0
    filt2.z_exc = 0
    filt3.v = c
    filt3.u = c*b
    filt3.g_exc = 0
    filt3.z_exc = 0
    filt4.v = c
    filt4.u = c*b
    filt4.g_exc = 0
    filt4.z_exc = 0
    sumneur.v = c
    sumneur.u = c*b
    sumneur.g_exc = 0
    sumneur.z_exc = 0
    midneur16.v = c
    midneur16.u = c*b
    midneur16.g_exc = 0
    midneur16.z_exc = 0
    whichshape16.v = c
    whichshape16.u = c*b
    whichshape16.g_exc = 0
    whichshape16.z_exc = 0
    #print mypixel
    #print idealans
    print shapesyn1.w
    print shapesyn2.w
    print shapesyn3.w
    print mycount
    return

run(5400*second) ## run for a really long time 

print numpy.array(shapesyn1.w)
print numpy.array(shapesyn2.w)
print numpy.array(shapesyn3.w)

print numpy.array(midsyn1.w)
print numpy.array(midsyn2.w)
print numpy.array(midsyn3.w)
print numpy.array(midsyn4.w)
print numpy.array(midsyn5.w)
print numpy.array(midsyn6.w)
print numpy.array(midsyn7.w)
print numpy.array(midsyn8.w)
print numpy.array(midsyn9.w)
print numpy.array(midsyn10.w)

show()

