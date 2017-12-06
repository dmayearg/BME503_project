
#from brian2 import *
#import matplotlib.pyplot as plt

#execfile("shapedata.py") 

## fast spiking izhikevich model 
# any stimulus above 4 will make this model spike
a = 0.1
b = 0.2
c = -65
d = 2

sens_tau_decay=1.5*ms ## maybe 1 for all or 2 ?
filt_tau_decay=2*ms
sum_tau_decay=2*ms




### receiving neuron is the row number

sensormag=2.2 ## the very minimum is 1.3 for it to fire with 3 inputs to make sensor neuron fire
## to fire with 2 input "on" is about 2.2
filtg_synmaxval=0.15 ##// if this is too low there is no difference between circ and square
sumg_synmaxval=0.06 


duration = 1000*ms

#print "filter_synmax"
#print filtg_synmaxval
#print "sum g_peak" 
#print sumg_synmaxval

#figure(1)
#plt.imshow(mypixel,cmap='gray')
#plt.show()

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

whichshape16 = NeuronGroup(3, sum_equ, clock=Clock(0.2*ms), method='euler',threshold = 'v >= 30', 
            reset = '''v = c; u = u + d ''')
whichshape16.v = c
whichshape16.u = c*b
whichshape16.tau_decay = sum_tau_decay

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

midsyn9 = Synapses(sumneur, midneur16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midsyn9.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[8])
midsyn9.g_synmax=weight16[8]

midsyn10 = Synapses(sumneur, midneur16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
midsyn10.connect(i=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],j=[9])
midsyn10.g_synmax=weight16[9]

shapesyn1 = Synapses(midneur16, whichshape16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
shapesyn1.connect(i=[0,1,2,3,4,5,6,7,8,9],j=[0])
shapesyn1.g_synmax=weightsout[0]

shapesyn2 = Synapses(midneur16, whichshape16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
shapesyn2.connect(i=[0,1,2,3,4,5,6,7,8,9],j=[1])
shapesyn2.g_synmax=weightsout[1]

shapesyn3 = Synapses(midneur16, whichshape16, clock=sensors.clock,model='''g_synmax: 1 ''', on_pre=''' z_exc+= g_synmax ''')
shapesyn3.connect(i=[0,1,2,3,4,5,6,7,8,9],j=[2])
shapesyn3.g_synmax=weightsout[2]

################################## STATE MONITORS #############################

#MS = StateMonitor(sensors, ('v', 'I'), record=True)
#Mfilt1=StateMonitor(filt1, ('v','synI_exc'), record=True)
#Mfilt2=StateMonitor(filt2, ('v'), record=True)
#Mfilt3=StateMonitor(filt3, ('v'), record=True)
#Mfilt4=StateMonitor(filt4, ('v'), record=True)
#Msum=StateMonitor(sumneur, ('v'), record=True)

#Mmid=StateMonitor(midneur16, ('v'), record=True)
#Mshape=StateMonitor(whichshape16, ('v'), record=True)

#spike_sensors = SpikeMonitor(sensors)
#spike_filt1 = SpikeMonitor(filt1)
#spike_filt2 = SpikeMonitor(filt2)
#spike_filt3 = SpikeMonitor(filt3)
#spike_filt4 = SpikeMonitor(filt4)
spike_sum = SpikeMonitor(sumneur)

spike_mid16 = SpikeMonitor(midneur16)
spike_shape16 = SpikeMonitor(whichshape16)

#run(duration,report='text')
run(duration)

#print spike_sensors.count
#curr_spike_sens = numpy.array(spike_sensors.count).astype(int).reshape((6,6))
#curr_spike_filt1 = numpy.array(spike_filt1.count).astype(int).reshape((4,4))
#curr_spike_filt2 =  numpy.array(spike_filt2.count).astype(int).reshape((4,4))
#curr_spike_filt3 =  numpy.array(spike_filt3.count).astype(int).reshape((4,4))
#curr_spike_filt4 =  numpy.array(spike_filt4.count).astype(int).reshape((4,4))
#curr_spike_sum =  numpy.array(spike_sum.count).astype(int).reshape((4,4))
        
#print curr_spike_sens
#print curr_spike_filt1
#print curr_spike_filt2
#print curr_spike_filt3
#print curr_spike_filt4
#print curr_spike_sum
#print spike_mid16.count
print numpy.array(spike_sum.count).tolist()
print numpy.array(spike_mid16.count).tolist()
print numpy.array(spike_shape16.count).tolist()


weightsout=numpy.array(weightsout)

#mysumpercent=(1/(1+exp(-(((numpy.array(spike_sum.count).astype(float)/5)-7)))))
#mymidpercent=(1/(1+exp(-(((numpy.array(spike_mid16.count).astype(float)/5)-7)))))

#mysumpercent=(1/(1+exp(-(log(numpy.array(spike_sum.count)+1)*2-7))))
#mymidpercent=(1/(1+exp(-(log(numpy.array(spike_mid16.count)+1)*2-7))))

mysumpercent=(numpy.array(spike_sum.count).astype(float).tolist()/sum(spike_sum.count))
mymidpercent=(numpy.array(spike_mid16.count).astype(float).tolist()/sum(spike_mid16.count))
myshapepercent=(numpy.array(spike_shape16.count).astype(float).tolist()/(sum(spike_shape16.count)+1))

myerror=((myshapepercent[0]-idealans[0])**2+(myshapepercent[1]-idealans[1])**2+(myshapepercent[2]-idealans[2])**2) ## for triangle
print int(100*myerror)

gradout=myshapepercent*(1-myshapepercent)*(idealans-myshapepercent)
gradmid=mymidpercent*(1-mymidpercent)*((gradout[0]*weightsout[0])+(gradout[1]*weightsout[1])+(gradout[2]*weightsout[2]))

weightsout[0]=clip(weightsout[0]+(0.01*mymidpercent*gradout[0]),-0.19,0.19)
weightsout[1]=clip(weightsout[1]+(0.01*mymidpercent*gradout[1]),-0.19,0.19)
weightsout[2]=clip(weightsout[2]+(0.01*mymidpercent*gradout[2]),-0.19,0.19)

weight16[0]=clip(weight16[0]+(0.05*mysumpercent*gradmid[0]),-0.19,0.19)
weight16[1]=clip(weight16[1]+(0.05*mysumpercent*gradmid[1]),-0.19,0.19)
weight16[2]=clip(weight16[2]+(0.05*mysumpercent*gradmid[2]),-0.19,0.19)
weight16[3]=clip(weight16[3]+(0.05*mysumpercent*gradmid[3]),-0.19,0.19)
weight16[4]=clip(weight16[4]+(0.05*mysumpercent*gradmid[4]),-0.19,0.19)
weight16[5]=clip(weight16[5]+(0.05*mysumpercent*gradmid[5]),-0.19,0.19)
weight16[6]=clip(weight16[6]+(0.05*mysumpercent*gradmid[6]),-0.19,0.19)
weight16[7]=clip(weight16[7]+(0.05*mysumpercent*gradmid[7]),-0.19,0.19)
weight16[8]=clip(weight16[8]+(0.05*mysumpercent*gradmid[8]),-0.19,0.19)
weight16[9]=clip(weight16[9]+(0.05*mysumpercent*gradmid[9]),-0.19,0.19)
#myerror=((myans[0])**2+(myans[1]-1)**2+(myans[2])**2) ## for square
#myerror=((myans[0])**2+(myans[1])**2+(myans[2]-1)**2) ## for circle


#gradmid[0]=mymidpercent[0]*(1-mymidpercent)*((gradout[0]*weightsout[0][0])+(gradout[1]*weightsout[1][0])+(gradout[2]*weightsout[2][0]))
#gradmid[1]=mymidpercent[1]*(1-mymidpercent)*((gradout[0]*weightsout[0][1])+(gradout[1]*weightsout[1][1])+(gradout[2]*weightsout[2][1]))
#gradmid[2]=mymidpercent[2]*(1-mymidpercent)*((gradout[0]*weightsout[0][2])+(gradout[1]*weightsout[1][2])+(gradout[2]*weightsout[2][2]))     
#gradmid[3]=mymidpercent[3]*(1-mymidpercent)*((gradout[0]*weightsout[0][3])+(gradout[1]*weightsout[1][3])+(gradout[2]*weightsout[2][3]))
#gradmid[4]=mymidpercent[4]*(1-mymidpercent)*((gradout[0]*weightsout[0][4])+(gradout[1]*weightsout[1][4])+(gradout[2]*weightsout[2][4]))
#gradmid[5]=mymidpercent[5]*(1-mymidpercent)*((gradout[0]*weightsout[0][5])+(gradout[1]*weightsout[1][5])+(gradout[2]*weightsout[2][5]))     
#gradmid[6]=mymidpercent[6]*(1-mymidpercent)*((gradout[0]*weightsout[0][6])+(gradout[1]*weightsout[1][6])+(gradout[2]*weightsout[2][6]))
#gradmid[7]=mymidpercent[7]*(1-mymidpercent)*((gradout[0]*weightsout[0][7])+(gradout[1]*weightsout[1][7])+(gradout[2]*weightsout[2][7]))





#weightchangemid[0]=0.1*mysumpercent*gradmid[0]
#weightchangemid[1]=0.1*mysumpercent*gradmid[1]
#weightchangemid[2]=0.1*mysumpercent*gradmid[2]




#print "figure 2 shows the sensor neurons firing"
#figure(2)
#for x in range(0,36):
#    subplot(6,6,(x+1))
#    plot(MS.t/ms, MS.v[x])
#    axis([0,1000,-80,30])
    
##print "figure 3 shows filter 1 (up/down)"
#uncomment the statemonitors!!!!!
#figure(3)
#for x in range(0,16):
#    subplot(4,4,(x+1))
#    plot(Mfilt1.t/ms, Mfilt1.v[x])
#    axis([0,1000,-80,30])
#   
##print "figure 4 shows filter 2 (left/right)"
#figure(4)
#for x in range(0,16):
#    subplot(4,4,(x+1))
#    plot(Mfilt2.t/ms, Mfilt2.v[x])
#    axis([0,1000,-80,30])
#
##print "figure 5 shows filter 3 (diagonal going down)"
#figure(5)
#for x in range(0,16):
#    subplot(4,4,(x+1))
#    plot(Mfilt3.t/ms, Mfilt3.v[x])
#    axis([0,1000,-80,30])
#
##print "figure 6 shows filter 4 (diagonal going up)"
#figure(6)
#for x in range(0,16):
#    subplot(4,4,(x+1))
#    plot(Mfilt4.t/ms, Mfilt4.v[x])
#    axis([0,1000,-80,30])

#print "figure 7 shows the 16 sum neurons (row 1 for filter 1 ...)"    
#figure(7)
#for x in range(0,16):
#    subplot(4,4,(x+1))
#    plot(Msum.t/ms, Msum.v[x])
#    axis([0,1000,-80,30])



#print "figure 9 shows the mid neurons (not ready yet)"
#figure(9)
#for x in range(0,8):
#    subplot(2,4,(x+1))
#    plot(Mmid.t/ms, Mmid.v[x])
#    axis([0,1000,-80,30])
#
#print "figure 10 shows the final answer neurons (not ready yet)"
#figure(10)
#for x in range(0,3):
#    subplot(1,3,(x+1))
#    plot(Mshape.t/ms, Mshape.v[x])
#    axis([0,1000,-80,30])
#    




show()

#<spikemonitor.count:   array([17, 17, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30], dtype=int32)>
#<spikemonitor_2.count: array([ 0,  0,  0,  0,  0,  0,  0,  0, 17, 30, 30, 17, 30, 17, 17, 30], dtype=int32)>
#<spikemonitor_1.count: array([ 0,  0,  0,  0,  0,  0,  0,  0,  0, 30, 30,  0, 30,  0,  0, 30], dtype=int32)>


#<spikemonitor_1.count: array([60, 60, 61, 61], dtype=int32)>
#<spikemonitor.count:   array([60, 60, 51, 51], dtype=int32)>
#<spikemonitor_2.count: array([60, 60, 30, 30], dtype=int32)>

