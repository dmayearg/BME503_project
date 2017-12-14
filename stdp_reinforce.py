from brian2.core.operations import network_operation
from sympy.strategies.core import switch
import numpy as np
import random
from ShapeClass import shapeclass
from brian2 import *
from NetworkParameters import*
#import matplotlib.pyplot as plt

s = shapeclass()
filt_vertsynapse = s.filtersynapse()[0]
filt_horizsynapse = s.filtersynapse()[1]
filt_updiagsynapse = s.filtersynapse()[2]
filt_downdiagsynapse = s.filtersynapse()[3]
shapedatamatrix = s.simpleshapes()

a = 0.1

idealansmatrix=[[1,0,0],[0,1,0],[0,0,1]]

## INITIALIZE
mypixel = []
idealans = []
mypixel=shapedatamatrix[0] ### update the shape 
idealans=idealansmatrix[0] ### update the ideal output 

weights2hid = 2*weights_random*(np.random.random((hid_size,pool_size)) - 0.5)
weightsout = 2*weights_random*(np.random.random((out_size,hid_size))-0.5)

##############################################################################
################################## NEURONS ##################################
##############################################################################

sensor_eqs = '''
dv/dt = ((0.04*v*v) + ( 5*v) + (140) - u + mag*I)/ms : 1
du/dt = a*((b*v)-u)/ms : 1
dg_exc/dt= (-g_exc/tau_decay) + (z_exc/ms) : 1 
dz_exc/dt = -z_exc/tau_decay : 1
i_syn = -g_exc *(v-E_exc) : 1
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

sensors = NeuronGroup(36, sensor_eqs, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
sensors.v = c
sensors.u = c*b
sensors.mag = sensormag ## 1.3 or 1.4 or 1.5 or 2 tbh idk what im doing 
sensors.tau_decay = sens_tau_decay
sensors.g_exc=0
# Connects each sensor neuron to a group of pixels
for x in range (0,sense_size):
    for y in range (0,sense_size):
        curr=(y*sense_size)+x
        a = [sensors.x0[curr],sensors.x1[curr],sensors.x2[curr], sensors.x3[curr],
            sensors.x4[curr],sensors.x5[curr],sensors.x6[curr],sensors.x7[curr],
            sensors.x8[curr]]
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
dv/dt = ((0.04*v*v) + ( 5*v) + (140) - u + i_syn)/ms : 1
du/dt = a*((b*v)-u)/ms : 1
dg_exc/dt= (-g_exc/tau_decay) + (z_exc/ms) : 1 
dz_exc/dt = -z_exc/tau_decay : 1
i_syn = -g_exc *(v-E_exc) : 1
tau_decay : second
E_exc : 1
'''
        
filt_vert = NeuronGroup(16, filt_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt_vert.v = c
filt_vert.u = c*b
filt_vert.tau_decay = filt_tau_decay
#filt_vert.g_exc=0  

filt_horiz = NeuronGroup(16, filt_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt_horiz.v = c
filt_horiz.u = c*b
filt_horiz.tau_decay = filt_tau_decay
#filt_horiz.g_exc=0  

filt_updiag = NeuronGroup(16, filt_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt_updiag.v = c
filt_updiag.u = c*b
filt_updiag.tau_decay = filt_tau_decay
#filt_updiag.g_exc=0  

filt_downdiag = NeuronGroup(16, filt_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt_downdiag.v = c
filt_downdiag.u = c*b
filt_downdiag.tau_decay = filt_tau_decay
#filt_downdiag.g_exc=0  

filtersize=16

sum_equ = '''
dv/dt = ((0.04*v*v) + ( 5*v) + (140) - u + i_syn)/ms : 1
du/dt = a*((b*v)-u)/ms : 1
dg_exc/dt= (-g_exc/tau_decay) + (z_exc/ms) : 1 
dz_exc/dt = -z_exc/tau_decay : 1
i_syn = -g_exc *(v-E_exc) : 1
tau_decay : second
E_exc : 1
'''
sumneur = NeuronGroup(16, sum_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
sumneur.v = c
sumneur.u = c*b
sumneur.tau_decay = sum_tau_decay

midneur16 = NeuronGroup(10, sum_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
midneur16.v = c
midneur16.u = c*b
midneur16.tau_decay = sum_tau_decay

shape_equ = '''
dv/dt = ((0.04*v*v) + ( 5*v) + (140) - u + (i_syn/10) + clampedcurrent)/ms : 1
du/dt = a*((b*v)-u)/ms : 1
dg_exc/dt= (-g_exc/tau_decay) + (z_exc/ms) : 1 
dz_exc/dt = -z_exc/tau_decay : 1
i_syn = -g_exc *(v-E_exc) : 1
tau_decay : second
E_exc : 1
clampedcurrent:1
'''
whichshape16 = NeuronGroup(3, shape_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
whichshape16.v = c
whichshape16.u = c*b
whichshape16.tau_decay = sum_tau_decay
whichshape16.clampedcurrent[0]=0
whichshape16.clampedcurrent[1]=0
whichshape16.clampedcurrent[2]=0
##############################################################################
################################## SYNAPSES ##################################
##############################################################################


syn_filt_vert = Synapses(sensors, filt_vert, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
for x in range (0,3):
    for y in range(0,16):
        syn_filt_vert.connect(i=[filt_vertsynapse[y][x]],j=[y])
syn_filt_vert.g_synmax=filtg_synmaxval
      
syn_filt_horiz = Synapses(sensors, filt_horiz, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
for x in range (0,3):
    for y in range(0,16):
        syn_filt_horiz.connect(i=[filt_horizsynapse[y][x]],j=[y])
syn_filt_horiz.g_synmax=filtg_synmaxval

  
syn_filt_updiag = Synapses(sensors, filt_updiag, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
for x in range (0,3):
    for y in range(0,16):
        syn_filt_updiag.connect(i=[filt_updiagsynapse[y][x]],j=[y])
syn_filt_updiag.g_synmax=filtg_synmaxval

syn_filt_downdiag = Synapses(sensors, filt_downdiag, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
for x in range (0,3):
    for y in range(0,16):
        syn_filt_downdiag.connect(i=[filt_downdiagsynapse[y][x]],j=[y])
syn_filt_downdiag.g_synmax=filtg_synmaxval

##############################################################################
################################## SYNAPSES ##################################
########################## FILTER TO SUMMING NEURON ##########################
##############################################################################

syn_sum1 = Synapses(filt_vert, sumneur, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_sum1.connect(i=[0, 1, 4, 5],j=[0])
syn_sum1.connect(i=[2, 3, 6, 7],j=[1])
syn_sum1.connect(i=[8, 9,12,13],j=[2])
syn_sum1.connect(i=[10,11,14,15],j=[3])
syn_sum1.g_synmax=sumg_synmaxval

syn_sum2 = Synapses(filt_horiz, sumneur, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_sum2.connect(i=[0, 1, 4, 5],j=[4])
syn_sum2.connect(i=[2, 3, 6, 7],j=[5])
syn_sum2.connect(i=[8, 9,12,13],j=[6])
syn_sum2.connect(i=[10,11,14,15],j=[7])
syn_sum2.g_synmax=sumg_synmaxval

syn_sum3 = Synapses(filt_updiag, sumneur, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_sum3.connect(i=[0, 1, 4, 5],j=[8])
syn_sum3.connect(i=[2, 3, 6, 7],j=[9])
syn_sum3.connect(i=[8, 9,12,13],j=[10])
syn_sum3.connect(i=[10,11,14,15],j=[11])
syn_sum3.g_synmax=sumg_synmaxval

syn_sum4 = Synapses(filt_downdiag, sumneur, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_sum4.connect(i=[0, 1, 4, 5],j=[12])
syn_sum4.connect(i=[2, 3, 6, 7],j=[13])
syn_sum4.connect(i=[8, 9,12,13],j=[14])
syn_sum4.connect(i=[10,11,14,15],j=[15])
syn_sum4.g_synmax=sumg_synmaxval

#### Synapses that learn in the final 3 layers
## Learning decay model
syn_eqns = '''
g_synmax: 1
w:1
reward:1
dapre/dt=-apre/taupre : 1
dapost/dt=-apost/taupost : 1
'''
## Synapses from the Pooling layer to the Hidden Layer
hidden_connections = []
for i in range(0,hid_size):
  current_synapse = Synapses(sumneur, midneur16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -wmax, wmax)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -wmax, wmax)''')
  current_synapse.connect(i=range(0,pool_size),j=[i])
  current_synapse.w=weights2hid[i]
  hidden_connections.append(current_synapse)

## Synapses from the Hidden layer to the Final output layer
out_connections = []
for i in range(0,out_size):
  current_synapse = Synapses(midneur16, whichshape16, clock=sensors.clock,
                   model= syn_eqns, 
                   on_pre=''' z_exc+= w 
                              apre += Apre
                              w = clip(w+apost, -wmax, wmax)''',
                   on_post='''apost += Apost
                              w = clip(w+apre, -wmax, wmax)''')
  current_synapse.connect(i=range(0,hid_size),j=[i])
  current_synapse.w=weightsout[i]
  out_connections.append(current_synapse)
    
mycount=0
# @network_operation(dt=1005*ms)
# def printWeights():
#     print out_connections[]1.w
#     print mypixel
#     print idealans

#    print sum(out_connections[]1.apre), sum(out_connections[]1.apost),sum(out_connections[]2.apre), sum(out_connections[]2.apost),sum(out_connections[]3.apre), sum(out_connections[]3.apost)
#    return

switch =  0
limit = len(shapedatamatrix)
# @network_opration
# def update_reinforce(dt = dt_sim):

@network_operation(dt=1000*ms)
def update_simulation():
    global mycount
    global mypixel
    global idealans
    global switch
    global limit
    switch = switch+1
    if switch > 5400 and mycount == 0:
        limit = 90
    mypixel=shapedatamatrix[mycount] ### update the shape 
    idealans=idealansmatrix[mycount] ### update the ideal output
    mycount=mycount+1
    if mycount == limit:
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
    filt_vert.v = c
    filt_vert.u = c*b
    filt_vert.g_exc = 0
    filt_vert.z_exc = 0
    filt_horiz.v = c
    filt_horiz.u = c*b
    filt_horiz.g_exc = 0
    filt_horiz.z_exc = 0
    filt_updiag.v = c
    filt_updiag.u = c*b
    filt_updiag.g_exc = 0
    filt_updiag.z_exc = 0
    filt_downdiag.v = c
    filt_downdiag.u = c*b
    filt_downdiag.g_exc = 0
    filt_downdiag.z_exc = 0
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
#     print mycount
#     print idealans
#     print ((np.array(out_connections[]1.w)*100000).astype(int)).astype(float)/1000
#     print ((np.array(out_connections[]2.w)*100000).astype(int)).astype(float)/1000
#     print ((np.array(out_connections[]3.w)*100000).astype(int)).astype(float)/1000
    return


printNum = 0
@network_operation(dt = 585*second)
def writeFile():
    global printNum
    
    title_str = "Print Number: %d\n" %(printNum)
    x = open('current_outputs.txt', 'a')
    all_weights = [title_str,\
        str((np.array(out_connections[0].w)*100).astype(int)) + ',\n',\
        str((np.array(out_connections[1].w)*100).astype(int)) + ',\n',\
        str((np.array(out_connections[2].w)*100).astype(int)) + ',\n\n',\
        str((np.array(hidden_connections[0].w)*100).astype(int)) + ',\n',\
        str((np.array(hidden_connections[1].w)*100).astype(int)) + ',\n',\
        str((np.array(hidden_connections[2].w)*100).astype(int)) + ',\n',\
        str((np.array(hidden_connections[3].w)*100).astype(int)) + ',\n',\
        str((np.array(hidden_connections[4].w)*100).astype(int)) + ',\n',\
        str((np.array(hidden_connections[5].w)*100).astype(int)) + ',\n',\
        str((np.array(hidden_connections[6].w)*100).astype(int)) + ',\n',\
        str((np.array(hidden_connections[7].w)*100).astype(int)) + ',\n',\
        str((np.array(hidden_connections[8].w)*100).astype(int)) + ',\n',\
        str((np.array(hidden_connections[9].w)*100).astype(int)) + ',\n\n']
    
    printNum+=1
    x.writelines(all_weights)
    return

run(duration) ## run for a really long time 

x = open('output.txt', 'w')
all_weights = ["Final Iteration: \n",\
    str(np.array(out_connections[0].w).tolist()) + ',\n',\
    str(np.array(out_connections[1].w).tolist()) + ',\n',\
    str(np.array(out_connections[2].w).tolist()) + ',\n\n',\
    str(np.array(hidden_connections[0].w).tolist()) + ',\n',\
    str(np.array(hidden_connections[1].w).tolist()) + ',\n',\
    str(np.array(hidden_connections[2].w).tolist()) + ',\n',\
    str(np.array(hidden_connections[3].w).tolist()) + ',\n',\
    str(np.array(hidden_connections[4].w).tolist()) + ',\n',\
    str(np.array(hidden_connections[5].w).tolist()) + ',\n',\
    str(np.array(hidden_connections[6].w).tolist()) + ',\n',\
    str(np.array(hidden_connections[7].w).tolist()) + ',\n',\
    str(np.array(hidden_connections[8].w).tolist()) + ',\n',\
    str(np.array(hidden_connections[9].w).tolist()) + ',\n\n']
x.writelines(all_weights)

print(np.array(out_connections[0].w))
print(np.array(out_connections[1].w))
print(np.array(out_connections[2].w))

print(np.array(hidden_connections[0].w))
print(np.array(hidden_connections[1].w))
print(np.array(hidden_connections[2].w))
print(np.array(hidden_connections[3].w))
print(np.array(hidden_connections[4].w))
print(np.array(hidden_connections[5].w))
print(np.array(hidden_connections[6].w))
print(np.array(hidden_connections[7].w))
print(np.array(hidden_connections[8].w))
print(np.array(hidden_connections[9].w))

show()
