
from brian2 import *
import matplotlib.pyplot as plt

## fast spiking izhikevich model 
# any stimulus above 4 will make this model spike
a = 0.1
b = 0.2
c = -65
d = 2

sens_tau_decay=1.5*ms ## maybe 1 for all or 2 ?
filt_tau_decay=2*ms
sum_tau_decay=2*ms

weightzzz=[[0.1, 0.2, 0.1, 0.15],
           [0.1, 0.1, 0.12, 0.1],
           [0.1, 0.3, 0.1, 0.1],
           [0.12, 0.1, 0.11, 0.1]]
weights2= [[0.13, 0.1, 0.14, 0.2],
           [0.1, 0.16, 0.1, 0.15],
           [0.13, 0.1, 0.1, 0.09]]

weight16  =  [[0.01,0.02,0.01,0.03, 0.02,0.06,0.01,0.08, 0.01,0.01,0.02,0.10, 0.01,0.02,0.12,0.1],
              [0.01,0.12,0.01,0.13, 0.02,0.06,0.01,0.18, 0.01,0.01,0.02,0.10, 0.01,0.12,0.12,0.2],
              [0.11,0.02,0.01,0.03, 0.02,0.06,0.01,0.08, 0.01,0.01,0.12,0.10, 0.11,0.02,0.15,0.1],
              [0.01,0.02,0.11,0.03, 0.02,0.16,0.01,0.08, 0.11,0.11,0.02,0.10, 0.01,0.02,0.12,0.2],
              [0.01,0.02,0.01,0.23, 0.02,0.06,0.01,0.08, 0.01,0.11,0.02,0.14, 0.01,0.02,0.12,0.1],
              [0.01,0.02,0.11,0.03, 0.02,0.16,0.01,0.08, 0.11,0.11,0.02,0.10, 0.01,0.02,0.19,0.2],
              [0.01,0.02,0.01,0.23, 0.02,0.06,0.31,0.08, 0.01,0.11,0.12,0.14, 0.01,0.02,0.12,0.1],
              [0.01,0.12,0.01,0.03, 0.02,0.16,0.01,0.08, 0.01,0.01,0.12,0.10, 0.01,0.12,0.12,0.2]]

weightsout=[[0.11,0.21, 0.01,0.01, 0.01,0.01, 0.01,0.09],
            [0.01,0.01, 0.11,0.11, 0.11,0.04, 0.05,0.08],
            [0.21,0.11, 0.01,0.01, 0.11,0.21, 0.20,0.01]]
### receiving neuron is the row number

sensormag=1.4 ## the very minimum is 1.3 for it to fire with 3 inputs to make sensor neuron fire
#fg_synpk=0.11
filtg_synmaxval=0.15 #(fg_synpk/(filt_tau_decay*exp(-1)))*ms // if this is too low there is no difference between circ and square
#sg_synpk=0.04 
sumg_synmaxval=0.06#(sg_synpk/(sum_tau_decay*exp(-1)))*ms
sumotherg_synmaxval=0.06
myotherpeak=0.1

duration = 1000*ms

print "filter_synmax"
print filtg_synmaxval
print "sum g_peak" 
print sumg_synmaxval
print "sum other g_peak" 
print sumotherg_synmaxval

figure(1)
mytri=[[0,0,0, 0,0,0, 0,1,0, 0,0,0, 0,0,0],  ##0
       [0,0,0, 0,0,0, 1,0,1, 0,0,0, 0,0,0],  ##01
       [0,0,0, 0,0,0, 1,0,1, 0,0,0, 0,0,0],  ##02
       [0,0,0, 0,0,1, 0,0,0, 1,0,0, 0,0,0],  ##03
       [0,0,0, 0,0,1, 0,0,0, 1,0,0, 0,0,0],  ##04
       [0,0,0, 0,1,0, 0,0,0, 0,1,0, 0,0,0],  ##05
       [0,0,0, 0,1,0, 0,0,0, 0,1,0, 0,0,0],  ##06
       [0,0,0, 1,0,0, 0,0,0, 0,0,1, 0,0,0],  ##07
       [0,0,0, 1,0,0, 0,0,0, 0,0,1, 0,0,0],  ##08
       [0,0,1, 0,0,0, 0,0,0, 0,0,0, 1,0,0],  ##9
       [0,0,1, 0,0,0, 0,0,0, 0,0,0, 1,0,0],  ##10
       [0,1,0, 0,0,0, 0,0,0, 0,0,0, 0,1,0],  ##11
       [0,1,0, 0,0,0, 0,0,0, 0,0,0, 0,1,0],  ##12
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##13
       [1,1,1, 1,1,1, 1,1,1, 1,1,1, 1,1,1]]  ##14

mysqu=[[1,1,1, 1,1,1, 1,1,1, 1,1,1, 1,1,1],  ##0
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##01
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##02
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##03
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##04
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##05
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##06
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##07
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##08
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##9
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##10
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##11
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##12
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##13
       [1,1,1, 1,1,1, 1,1,1, 1,1,1, 1,1,1]]  ##14

mycir=[[0,0,0, 0,0,0, 1,1,1, 0,0,0, 0,0,0],  ##0
       [0,0,0, 0,1,1, 0,0,0, 1,1,0, 0,0,0],   ##01
       [0,0,1, 1,0,0, 0,0,0, 0,0,1, 1,0,0],  ##02
       [0,0,1, 0,0,0, 0,0,0, 0,0,0, 1,0,0],  ##03
       [0,1,0, 0,0,0, 0,0,0, 0,0,0, 0,1,0],  ##04
       [0,1,0, 0,0,0, 0,0,0, 0,0,0, 0,1,0],  ##05
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##06
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##07
       [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1],  ##08
       [0,1,0, 0,0,0, 0,0,0, 0,0,0, 0,1,0],  ##9
       [0,1,0, 0,0,0, 0,0,0, 0,0,0, 0,1,0],  ##10
       [0,0,1, 0,0,0, 0,0,0, 0,0,0, 1,0,0],  ##11
       [0,0,1, 1,0,0, 0,0,0, 0,0,1, 1,0,0],  ##12
       [0,0,0, 0,1,1, 0,0,0, 1,1,0, 0,0,0],  ##13
       [0,0,0, 0,0,0, 1,1,1, 0,0,0, 0,0,0]]  ##14

mypixel=mytri
plt.imshow(mypixel,cmap='gray')

plt.show()

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


###sensors 
# 0  1  2  3  4 
# 5  6  7  8  9 
# 10 11 12 13 14
# 15 16 17 18 19
# 20 21 22 23 24

## each neuron has these pixels 
## x0 x1 x2
## x3 x4 x5
## x6 x7 x8
sensors = NeuronGroup(25, sensor_eqs, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
sensors.v = c
sensors.u = c*b
sensors.mag = sensormag ## 1.3 or 1.4 or 1.5 or 2 tbh idk what im doing 
sensors.tau_decay = sens_tau_decay
sensors.g_exc=0
for x in range (0,5):
    for y in range (0,5):
        curr=(y*5)+x
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
        
filt1 = NeuronGroup(9, filt_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt1.v = c
filt1.u = c*b
filt1.tau_decay = filt_tau_decay
#filt1.g_exc=0  

filt2 = NeuronGroup(9, filt_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt2.v = c
filt2.u = c*b
filt2.tau_decay = filt_tau_decay
#filt2.g_exc=0  

filt3 = NeuronGroup(9, filt_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
filt3.v = c
filt3.u = c*b
filt3.tau_decay = filt_tau_decay
#filt3.g_exc=0  

filt4 = NeuronGroup(9, filt_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
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
sumneur = NeuronGroup(16, sum_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
sumneur.v = c
sumneur.u = c*b
sumneur.tau_decay = sum_tau_decay

othersum = NeuronGroup(8, sum_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
othersum.v = c
othersum.u = c*b
othersum.tau_decay = sum_tau_decay


midneur = NeuronGroup(4, sum_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
midneur.v = c
midneur.u = c*b
midneur.tau_decay = sum_tau_decay

whichshape = NeuronGroup(3, sum_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
whichshape.v = c
whichshape.u = c*b
whichshape.tau_decay = sum_tau_decay


midneur16 = NeuronGroup(8, sum_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
midneur16.v = c
midneur16.u = c*b
midneur16.tau_decay = sum_tau_decay

whichshape16 = NeuronGroup(3, sum_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
whichshape16.v = c
whichshape16.u = c*b
whichshape16.tau_decay = sum_tau_decay

##############################################################################
################################## SYNAPSES ##################################
##############################################################################

filt1synpase=[[1, 6, 11],
              [2, 7, 12],
              [3, 8, 13],
              [6, 11, 16],
              [7, 12, 17],
              [8, 13, 18],
              [11, 16, 21],
              [12, 17, 22],
              [13, 18, 23]]
#syn_filt1.connect(i=[1,6,11],j=[0])
#syn_filt1.connect(i=[2,7,12],j=[1])
#syn_filt1.connect(i=[3,8,13],j=[2])
#syn_filt1.connect(i=[6,11,16],j=[3])
#syn_filt1.connect(i=[7,12,17],j=[4])
#syn_filt1.connect(i=[8,13,18],j=[5])
#syn_filt1.connect(i=[11,16,21],j=[6])
#syn_filt1.connect(i=[12,17,22],j=[7])
#syn_filt1.connect(i=[13,18,23],j=[8])

syn_filt11 = Synapses(sensors, filt1, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
for x in range (0,3):
    for y in range(0,9):
        syn_filt11.connect(i=[filt1synpase[y][x]],j=[y])
syn_filt11.g_synmax=filtg_synmaxval

#syn_filt12 = Synapses(sensors, filt1, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
#for y in range(0,9):
#    syn_filt12.connect(i=[filt1synpase[y][1]],j=[y])
#syn_filt12.g_synmax=filtg_synmaxval
#syn_filt12.delay=2.5*ms
#
#syn_filt13 = Synapses(sensors, filt1, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
#for y in range(0,9):
#    syn_filt13.connect(i=[filt1synpase[y][2]],j=[y])
#syn_filt13.g_synmax=filtg_synmaxval
#syn_filt13.delay=5*ms

      
syn_filt2 = Synapses(sensors, filt2, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_filt2.connect(i=[5,6,7],j=[0,0,0])
syn_filt2.connect(i=[6,7,8],j=[1,1,1])
syn_filt2.connect(i=[7,8,9],j=[2,2,2])
syn_filt2.connect(i=[10,11,12],j=[3,3,3])
syn_filt2.connect(i=[11,12,13],j=[4,4,4])
syn_filt2.connect(i=[12,13,14],j=[5,5,5])
syn_filt2.connect(i=[15,16,17],j=[6,6,6])
syn_filt2.connect(i=[16,17,18],j=[7,7,7])
syn_filt2.connect(i=[17,18,19],j=[8,8,8])
syn_filt2.g_synmax=filtg_synmaxval

  
syn_filt3 = Synapses(sensors, filt3, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_filt3.connect(i=[0,6,12],j=[0,0,0])
syn_filt3.connect(i=[1,7,13],j=[1,1,1])
syn_filt3.connect(i=[2,8,14],j=[2,2,2])
syn_filt3.connect(i=[5,11,17],j=[3,3,3])
syn_filt3.connect(i=[6,12,18],j=[4,4,4])
syn_filt3.connect(i=[7,13,19],j=[5,5,5])
syn_filt3.connect(i=[10,16,22],j=[6,6,6])
syn_filt3.connect(i=[11,17,23],j=[7,7,7])
syn_filt3.connect(i=[12,18,24],j=[8,8,8])
syn_filt3.g_synmax=filtg_synmaxval

syn_filt4 = Synapses(sensors, filt4, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_filt4.connect(i=[2,6,10],j=[0])
syn_filt4.connect(i=[3,7,11],j=[1])
syn_filt4.connect(i=[4,8,12],j=[2])
syn_filt4.connect(i=[7,11,15],j=[3])
syn_filt4.connect(i=[8,12,16],j=[4])
syn_filt4.connect(i=[9,13,17],j=[5])
syn_filt4.connect(i=[12,16,20],j=[6])
syn_filt4.connect(i=[13,17,21],j=[7])
syn_filt4.connect(i=[14,18,22],j=[8])
syn_filt4.g_synmax=filtg_synmaxval


syn_sum1 = Synapses(filt1, sumneur, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_sum1.connect(i=[0,1,3,4],j=[0])
syn_sum1.connect(i=[1,2,4,5],j=[1])
syn_sum1.connect(i=[3,4,6,7],j=[2])
syn_sum1.connect(i=[4,5,7,8],j=[3])
syn_sum1.g_synmax=sumg_synmaxval

syn_sum2 = Synapses(filt2, sumneur, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_sum2.connect(i=[0,1,3,4],j=[4])
syn_sum2.connect(i=[1,2,4,5],j=[5])
syn_sum2.connect(i=[3,4,6,7],j=[6])
syn_sum2.connect(i=[4,5,7,8],j=[7])
syn_sum2.g_synmax=sumg_synmaxval

syn_sum3 = Synapses(filt3, sumneur, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_sum3.connect(i=[0,1,3,4],j=[8])
syn_sum3.connect(i=[1,2,4,5],j=[9])
syn_sum3.connect(i=[3,4,6,7],j=[10])
syn_sum3.connect(i=[4,5,7,8],j=[11])
syn_sum3.g_synmax=sumg_synmaxval

syn_sum4 = Synapses(filt4, sumneur, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_sum4.connect(i=[0,1,3,4],j=[12])
syn_sum4.connect(i=[1,2,4,5],j=[13])
syn_sum4.connect(i=[3,4,6,7],j=[14])
syn_sum4.connect(i=[4,5,7,8],j=[15])
syn_sum4.g_synmax=sumg_synmaxval





othersum1 = Synapses(filt1, othersum, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
othersum1.connect(i=[0,1,2,3,4,5,6,7,8],j=[0])
othersum1.g_synmax=sumotherg_synmaxval

othersum2 = Synapses(filt2, othersum, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
othersum2.connect(i=[0,1,2,3,4,5,6,7,8],j=[1])
othersum2.g_synmax=sumotherg_synmaxval

othersum3 = Synapses(filt3, othersum, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
othersum3.connect(i=[0,1,2,3,4,5,6,7,8],j=[2])
othersum3.g_synmax=sumotherg_synmaxval

othersum4 = Synapses(filt4, othersum, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
othersum4.connect(i=[0,1,2,3,4,5,6,7,8],j=[3])
othersum4.g_synmax=sumotherg_synmaxval

syn_sumz = Synapses(sumneur, othersum, clock=sensors.clock,model='''
                g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
syn_sumz.connect(i=[0,1,2,3],j=[4])
syn_sumz.connect(i=[4,5,6,7],j=[5])
syn_sumz.connect(i=[8,9,10,11],j=[6])
syn_sumz.connect(i=[12,13,14,15],j=[7])
syn_sumz.g_synmax=myotherpeak




######################### the crazy synapses ###########################

###only a few neurons 
midneur1 = Synapses(othersum, midneur, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midneur1.connect(i=[4,5,6,7],j=[0])
midneur1.g_synmax=weightzzz[0]

midneur2 = Synapses(othersum, midneur, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midneur2.connect(i=[4,5,6,7],j=[1])
midneur2.g_synmax=weightzzz[1]

midneur3 = Synapses(othersum, midneur, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midneur3.connect(i=[4,5,6,7],j=[2])
midneur3.g_synmax=weightzzz[2]

midneur4 = Synapses(othersum, midneur, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midneur4.connect(i=[4,5,6,7],j=[3])
midneur4.g_synmax=weightzzz[3]


synshape1 = Synapses(midneur, whichshape, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
synshape1.connect(i=[0,1,2,3],j=[0])
synshape1.g_synmax=weights2[0]

synshape2 = Synapses(midneur, whichshape, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
synshape2.connect(i=[0,1,2,3],j=[1])
synshape2.g_synmax=weights2[1]

synshape3 = Synapses(midneur, whichshape, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
synshape3.connect(i=[0,1,2,3],j=[2])
synshape3.g_synmax=weights2[2]



midsyn1 = Synapses(sumneur, midneur16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midsyn1.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[0])
midsyn1.g_synmax=weight16[0]

midsyn2 = Synapses(sumneur, midneur16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midsyn2.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[1])
midsyn2.g_synmax=weight16[1]

midsyn3 = Synapses(sumneur, midneur16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midsyn3.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[2])
midsyn3.g_synmax=weight16[2]

midsyn4 = Synapses(sumneur, midneur16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midsyn4.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[3])
midsyn4.g_synmax=weight16[3]

midsyn5 = Synapses(sumneur, midneur16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midsyn5.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[4])
midsyn5.g_synmax=weight16[4]

midsyn6 = Synapses(sumneur, midneur16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midsyn6.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[5])
midsyn6.g_synmax=weight16[5]

midsyn7 = Synapses(sumneur, midneur16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midsyn7.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[6])
midsyn7.g_synmax=weight16[6]

midsyn8 = Synapses(sumneur, midneur16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midsyn8.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[7])
midsyn8.g_synmax=weight16[7]


shapesyn1 = Synapses(midneur16, whichshape16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
shapesyn1.connect(i=[0,1,2,3,4,5,6,7],j=[0])
shapesyn1.g_synmax=weightsout[0]

shapesyn2 = Synapses(midneur16, whichshape16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
shapesyn2.connect(i=[0,1,2,3,4,5,6,7],j=[1])
shapesyn2.g_synmax=weightsout[1]

shapesyn3 = Synapses(midneur16, whichshape16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
shapesyn3.connect(i=[0,1,2,3,4,5,6,7],j=[2])
shapesyn3.g_synmax=weightsout[2]


################################## STATE MONITORS #############################

MS = StateMonitor(sensors, ('v', 'I'), record=True)
Mfilt1=StateMonitor(filt1, ('v','synI_exc'), record=True)
Mfilt2=StateMonitor(filt2, ('v'), record=True)
Mfilt3=StateMonitor(filt3, ('v'), record=True)
Mfilt4=StateMonitor(filt4, ('v'), record=True)
Msum=StateMonitor(sumneur, ('v'), record=True)
Mothersum=StateMonitor(othersum, ('v'), record=True)
Mmid=StateMonitor(midneur, ('v'), record=True)
Mshape=StateMonitor(whichshape, ('v'), record=True)

spike_sensors = SpikeMonitor(sensors)
spike_filt1 = SpikeMonitor(filt1)
spike_filt2 = SpikeMonitor(filt2)
spike_filt3 = SpikeMonitor(filt3)
spike_filt4 = SpikeMonitor(filt4)

spike_sum = SpikeMonitor(sumneur)
spike_othersum = SpikeMonitor(othersum)
spike_mid = SpikeMonitor(midneur)
spike_shape = SpikeMonitor(whichshape)

spike_mid16 = SpikeMonitor(midneur16)
spike_shape16 = SpikeMonitor(whichshape16)



run(duration,report='text')

#print spike_sensors.count

myspiking=[[0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],]

for x in range(0,5):
    for y in range(0,5):
        myspiking[y][x]=spike_sensors.count[(y*5)+x]
        
print myspiking
print spike_filt1.count
print spike_filt2.count
print spike_filt3.count
print spike_filt4.count
print spike_sum.count
print spike_othersum.count
print spike_mid.count
print spike_shape.count

print "figure 2 shows the sensor neurons firing"
figure(2)
for x in range(0,25):
    subplot(5,5,(x+1))
    plot(MS.t/ms, MS.v[x])
    axis([0,1000,-80,30])
    
print "figure 3 shows filter 1 (up/down)"
figure(3)
for x in range(0,9):
    subplot(3,3,(x+1))
    plot(Mfilt1.t/ms, Mfilt1.v[x])
    axis([0,1000,-80,30])
   
print "figure 4 shows filter 2 (left/right)"
figure(4)
for x in range(0,9):
    subplot(3,3,(x+1))
    plot(Mfilt2.t/ms, Mfilt2.v[x])
    axis([0,1000,-80,30])

print "figure 5 shows filter 3 (diagonal going down)"
figure(5)
for x in range(0,9):
    subplot(3,3,(x+1))
    plot(Mfilt3.t/ms, Mfilt3.v[x])
    axis([0,1000,-80,30])

print "figure 6 shows filter 4 (diagonal going up)"
figure(6)
for x in range(0,9):
    subplot(3,3,(x+1))
    plot(Mfilt4.t/ms, Mfilt4.v[x])
    axis([0,1000,-80,30])

print "figure 7 shows the 16 sum neurons (row 1 for filter 1 ...)"    
figure(7)
for x in range(0,16):
    subplot(4,4,(x+1))
    plot(Msum.t/ms, Msum.v[x])
    axis([0,1000,-80,30])

print "figure 8 shows the 8 sum neurons (row 1 = sums of 16 sum neurons)" 
print "(row 2 = sums all filter neurons (row 2, column 1 = filter 1))" 
figure(8)
for x in range(0,8):
    subplot(2,4,(x+1))
    plot(Mothersum.t/ms, Mothersum.v[x])
    axis([0,1000,-80,30])

print "figure 9 shows the mid neurons (not ready yet)"
figure(9)
for x in range(0,4):
    subplot(2,2,(x+1))
    plot(Mmid.t/ms, Mmid.v[x])
    axis([0,1000,-80,30])

print "figure 9 shows the final answer neurons (not ready yet)"
figure(10)
for x in range(0,3):
    subplot(1,3,(x+1))
    plot(Mshape.t/ms, Mshape.v[x])
    axis([0,1000,-80,30])
    
#figure(11)
#for x in range(0,9):
#    subplot(3,3,(x+1))
#    plot(Mfilt1.t/ms, Mfilt1.synI_exc[x])
#    axis([0,1000,-1,10])

print spike_mid16.count
print spike_shape16.count


show()

#<spikemonitor.count:   array([17, 17, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30], dtype=int32)>
#<spikemonitor_2.count: array([ 0,  0,  0,  0,  0,  0,  0,  0, 17, 30, 30, 17, 30, 17, 17, 30], dtype=int32)>
#<spikemonitor_1.count: array([ 0,  0,  0,  0,  0,  0,  0,  0,  0, 30, 30,  0, 30,  0,  0, 30], dtype=int32)>


#<spikemonitor_1.count: array([60, 60, 61, 61], dtype=int32)>
#<spikemonitor.count:   array([60, 60, 51, 51], dtype=int32)>
#<spikemonitor_2.count: array([60, 60, 30, 30], dtype=int32)>

