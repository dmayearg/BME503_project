from brian2.core.operations import network_operation
from sympy.strategies.core import switch
import numpy as np
from ShapeClass import shapeclass
from NetworkParameters import*
import matplotlib.pyplot as plt
import random

from brian2 import *
#import matplotlib.pyplot as plt

#execfile("C:Users/Josh/Documents/GitHub/BME503_project/stdpshapedata.py")
s = shapeclass()
filt1synpase = s.filtersynapse()[0]
filt2synapse = s.filtersynapse()[1]
filt3synapse = s.filtersynapse()[2]
filt4synapse = s.filtersynapse()[3]
shapedatamatrix = s.simpleshapes()


idealansmatrix=[[1,0,0],[1,0,0],[1,0,0]]

## INITIALIZE
mypixel = []
idealans = []
mypixel=shapedatamatrix[0] ### update the shape 
idealans=idealansmatrix[0] ### update the ideal output 

weights2hid = 2*(np.random.random((hid_size,pool_size)))
weightsout = 2*(np.random.random((out_size,hid_size)))

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

sensors = NeuronGroup(sense_size**2, sensor_eqs, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
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
        
filt1 = NeuronGroup(filterstack_size, filt_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt1.v = c
filt1.u = c*b
filt1.tau_decay = filt_tau_decay
#filt1.g_exc=0  

filt2 = NeuronGroup(filterstack_size, filt_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt2.v = c
filt2.u = c*b
filt2.tau_decay = filt_tau_decay
#filt2.g_exc=0  

filt3 = NeuronGroup(filterstack_size, filt_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt3.v = c
filt3.u = c*b
filt3.tau_decay = filt_tau_decay
#filt3.g_exc=0  

filt4 = NeuronGroup(filterstack_size, filt_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt4.v = c
filt4.u = c*b
filt4.tau_decay = filt_tau_decay
#filt4.g_exc=0  

sum_equ = '''
dv/dt = ((0.04*v*v) + ( 5*v) + (140) - u + synI_exc)/ms : 1
du/dt = a*((b*v)-u)/ms : 1
dg_exc/dt= (-g_exc/tau_decay) + (z_exc/ms) : 1 
dz_exc/dt = -z_exc/tau_decay : 1
synI_exc = -g_exc *(v-E_exc) : 1
tau_decay : second
E_exc : 1
'''
sumneur = NeuronGroup(pool_size, sum_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
sumneur.v = c
sumneur.u = c*b
sumneur.tau_decay = sum_tau_decay

midneur16 = NeuronGroup(hid_size, sum_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
midneur16.v = c
midneur16.u = c*b
midneur16.tau_decay = sum_tau_decay

whichshape16 = NeuronGroup(out_size, sum_equ, clock=Clock(dt_sim), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
whichshape16.v = c
whichshape16.u = c*b
whichshape16.tau_decay = sum_tau_decay
##############################################################################
################################## SYNAPSES ##################################
##############################################################################

syn_filt1 = Synapses(sensors, filt1, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_filt2 = Synapses(sensors, filt2, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_filt3 = Synapses(sensors, filt3, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_filt4 = Synapses(sensors, filt4, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
for x in range (0,out_size):
    for y in range(0,filterstack_size):
        syn_filt1.connect(i=[filt1synpase[y][x]],j=[y])
        syn_filt2.connect(i=[filt2synapse[y][x]],j=[y])
        syn_filt3.connect(i=[filt3synapse[y][x]],j=[y])
        syn_filt4.connect(i=[filt4synapse[y][x]],j=[y])

syn_filt1.g_synmax=filtg_synmaxval
syn_filt2.g_synmax=filtg_synmaxval
syn_filt3.g_synmax=filtg_synmaxval
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
reward:1
dapre/dt=-apre/taupre : 1
dapost/dt=-apost/taupost : 1
'''
######################### ADD THE ON_PRE  AND ON_POST TRACES 
hidden_connections = Synapses(sumneur, midneur16, clock=sensors.clock,
                 model= syn_eqns, 
                 on_pre=''' g_exc += w
                            z_exc += g_synmax
                            apre += Apre
                            w = clip(w+reward*apost, 0, wmax)''',
                 on_post='''apost += Apost
                            w = clip(w+reward*apre, 0, wmax)''')
hidden_connections.connect()
hidden_connections.g_synmax = learng_synmaxval
hidden_connections.w = weights2hid
hidden_connections.reward = 0

out_connections = Synapses(midneur16, whichshape16, clock=sensors.clock,
                 model= syn_eqns, 
                 on_pre=''' g_exc += w
                            z_exc += g_synmax
                            apre += Apre
                            w = clip(w+reward*apost, 0, wmax)''',
                 on_post='''apost += Apost
                            w = clip(w+reward*apre, 0, wmax)''')
out_connections.connect()
out_connections.g_synmax = learng_synmaxval
out_connections.w = weightsout
out_connections.reward = 0

print(size(hidden_connections))
print(size(out_connections))
M = StateMonitor(whichshape16,('v','g_exc'),record=True)
M_hid = StateMonitor(midneur16,('v','g_exc'),record=True)
M_sum = StateMonitor(sumneur,('v','g_exc'),record=True)
spike = SpikeMonitor(whichshape16)
#S_tohid = StateMonitor(hidden_connections,('w'),record=True))
#S_toout = StateMonitor(out_connections,('w'),record=True))

# @network_operation(dt=1005*ms)
# def printWeights():
#     print(shapesyn1.w
#     print(mypixel
#     print(idealans

#    print(sum(shapesyn1.apre), sum(shapesyn1.apost),sum(shapesyn2.apre), sum(shapesyn2.apost),sum(shapesyn3.apre), sum(shapesyn3.apost)
#    return

@network_operation(dt=dt_sim*10)
def update_reinforce():
  idealans = idealansmatrix[0]
  #for i in out_connections:
  #  print(i.w)
    #print(i.reward)
  complexreward = [];
  for i in range(0,out_size):
    indices = [j for j, x in enumerate(spike.t/ms) if x==i]
    if indices:
      lastindex = indices[len(indices)-1]
      if spike[lastindex].t/ms == M[i].t[len(M[i].t/ms)-1]/ms:
        if idealans[i]==1:
          complexreward.append(1)
          out_connections[i].reward=1
        else:
          complexreward.append(-1)
          out_connections[i].reward=-1
      elif not (spike[lastindex].t/ms > M[i].t[len(M[i].t/ms)-1]/ms - 20):
        if idealans[i] == 1:
          complexreward.append[-1]
          out_connections[i].reward=-1
        else:
          complexreward.append(1)
          out_connections[i].reward=1
    else:
      complexreward = 1
      out_connections[i].reward = 1

  complexreward = np.mean(np.array(complexreward))
  for k in hidden_connections:
    k.reward = complexreward
  #print("complex",complexreward)

@network_operation(dt=dt_sim*10)
def update_normalize():
  for i in hidden_connections:
    i.w = clip(i.w,0,wmax)
    normalize = np.sum(np.sum(i.w))
    i.w = 2*i.w/normalize

  for i in out_connections:
    i.w = clip(i.w,0,wmax)
    normalize = np.sum(np.sum(i.w))
    i.w = 2*i.w/normalize


switch =  0
limit = len(shapedatamatrix)
mycount=1
@network_operation(dt=1000*ms)
def update_stuff():
    global mycount
    global mypixel
    global idealans
    global switch
    global limit
    switch = switch+1
    if switch > 5400 and mycount == 0:
        limit = 90
    mypixel=shapedatamatrix[0] ### update the shape 
    idealans=idealansmatrix[0] ### update the ideal output 
    #whichshape16.clampedcurrent[0]=idealans[0]*8
    #whichshape16.clampedcurrent[1]=idealans[1]*8
    #whichshape16.clampedcurrent[2]=idealans[2]*8
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
    #print(mypixel
    #print(idealans
#     print(mycount
#     print(idealans
#     print(((np.array(shapesyn1.w)*100000).astype(int)).astype(float)/1000
#     print(((np.array(shapesyn2.w)*100000).astype(int)).astype(float)/1000
#     print(((np.array(shapesyn3.w)*100000).astype(int)).astype(float)/1000
    return


# printNum = 0
# @network_operation(dt = 585*second)
# def writeFile():
#     global printNum
    
#     title_str = "Print Number: %d\n" %(printNum)
#     x = open('current_outputs.txt', 'a')
#     all_weights = [title_str,\
#         str((np.array(out_connections[0].w)*100).astype(int)) + ',\n',\
#         str((np.array(out_connections[1].w)*100).astype(int)) + ',\n',\
#         str((np.array(out_connections[2].w)*100).astype(int)) + ',\n\n',\
#         str((np.array(hidden_connections[0].w)*100).astype(int)) + ',\n',\
#         str((np.array(hidden_connections[1].w)*100).astype(int)) + ',\n',\
#         str((np.array(hidden_connections[2].w)*100).astype(int)) + ',\n',\
#         str((np.array(hidden_connections[3].w)*100).astype(int)) + ',\n',\
#         str((np.array(hidden_connections[4].w)*100).astype(int)) + ',\n',\
#         str((np.array(hidden_connections[5].w)*100).astype(int)) + ',\n',\
#         str((np.array(hidden_connections[6].w)*100).astype(int)) + ',\n',\
#         str((np.array(hidden_connections[7].w)*100).astype(int)) + ',\n',\
#         str((np.array(hidden_connections[8].w)*100).astype(int)) + ',\n',\
#         str((np.array(hidden_connections[9].w)*100).astype(int)) + ',\n\n']
    
#     printNum+=1
#     x.writelines(all_weights)
#     return

run(duration) ## run for a really long time 
figure(1)
for i in range(0,hid_size):
  plot(M_hid.t/ms,M_hid.v[i])
  plot(M.t/ms,M.v[i])
show()

# x = open('output.txt', 'w')
# all_weights = ["Final Iteration: \n",\
#     str(np.array(out_connections[0].w).tolist()) + ',\n',\
#     str(np.array(out_connections[1].w).tolist()) + ',\n',\
#     str(np.array(out_connections[2].w).tolist()) + ',\n\n',\
#     str(np.array(hidden_connections[0].w).tolist()) + ',\n',\
#     str(np.array(hidden_connections[1].w).tolist()) + ',\n',\
#     str(np.array(hidden_connections[2].w).tolist()) + ',\n',\
#     str(np.array(hidden_connections[3].w).tolist()) + ',\n',\
#     str(np.array(hidden_connections[4].w).tolist()) + ',\n',\
#     str(np.array(hidden_connections[5].w).tolist()) + ',\n',\
#     str(np.array(hidden_connections[6].w).tolist()) + ',\n',\
#     str(np.array(hidden_connections[7].w).tolist()) + ',\n',\
#     str(np.array(hidden_connections[8].w).tolist()) + ',\n',\
#     str(np.array(hidden_connections[9].w).tolist()) + ',\n\n']
# x.writelines(all_weights)

# for i in out_connections:
#   print(np.array(i.w))

# for i in hidden_connections:
#   print(np.array(i.w))

# hidden_connections = [None for _ in range(0,hid_size)]
# for i in range(0,hid_size):
#   current_synapse = Synapses(sumneur, midneur16, clock=sensors.clock,
#                    model= syn_eqns, 
#                    on_pre=''' g_exc += w
#                               z_exc+= g_synmax
#                               apre += Apre
#                               w = clip(w+reward*apost, 0, wmax)''',
#                    on_post='''apost += Apost
#                               w = clip(w+reward*apre, 0, wmax)''')
#   current_synapse.connect(i=range(0,pool_size),j=[i])
#   current_synapse.w=weights2hid[i]
#   current_synapse.g_synmax = learng_synmaxval
#   current_synapse.reward = 0
#   hidden_connections[i] = current_synapse

# ## Synapses from the Hidden layer to the Final output layer
# out_connections = [None for _ in range(0,out_size)]
# for i in range(0,out_size):
#   current_synapse = Synapses(midneur16, whichshape16, clock=sensors.clock,
#                    model= syn_eqns, 
#                    on_pre=''' g_exc += w
#                               z_exc += g_synmax
#                               apre += Apre
#                               w = clip(w+reward*apost, 0, wmax)''',
#                    on_post='''apost += Apost
#                               w = clip(w+reward*apre, 0, wmax)''')
#   current_synapse.connect(i=range(0,hid_size),j=[i])
#   current_synapse.g_synmax = learng_synmaxval
#   current_synapse.w=weightsout[i]
#   current_synapse.reward = 0
#   out_connections[i] = current_synapse
