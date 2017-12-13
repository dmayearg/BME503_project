
#from brian2 import *
#import matplotlib.pyplot as plt

pixelcount=0
## fast spiking izhikevich model 
a = 0.1
b = 0.2
c = -65
d = 2

sens_tau_decay=1.5*ms ## maybe 1 for all or 2 ?
filt_tau_decay=2*ms
sum_tau_decay=2*ms


sensormag=2.2 ## the very minimum is 1.3 for it to fire with 3 inputs to make sensor neuron fire
## to fire with 2 input "on" is about 2.2
filtg_synmaxval=0.15 ##// if this is too low there is no difference between circ and square
sumg_synmaxval=0.06 


duration = 1000*ms



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
#Msum=StateMonitor(sumneur, ('v'), record=True)
#Mmid=StateMonitor(midneur16, ('v'), record=True)
#Mshape=StateMonitor(whichshape16, ('v'), record=True)

#spike_sensors = SpikeMonitor(sensors)
spike_sum = SpikeMonitor(sumneur)
spike_mid16 = SpikeMonitor(midneur16)
spike_shape16 = SpikeMonitor(whichshape16)

run(duration)


print numpy.array(spike_sum.count).tolist()
print numpy.array(spike_mid16.count).tolist()
print numpy.array(spike_shape16.count).tolist()


weightsout=numpy.array(weightsout)


##### yall dont need this part 
#mysumpercent=(1/(1+exp(-(((numpy.array(spike_sum.count).astype(float)/5)-7)))))
#mymidpercent=(1/(1+exp(-(((numpy.array(spike_mid16.count).astype(float)/5)-7)))))

mysumpercent=(1/(1+exp(-(log(numpy.array(spike_sum.count)+1)*2-7))))
mymidpercent=(1/(1+exp(-(log(numpy.array(spike_mid16.count)+1)*2-7))))

#mysumpercent=(numpy.array(spike_sum.count).astype(float).tolist()/sum(spike_sum.count))
#mymidpercent=(numpy.array(spike_mid16.count).astype(float).tolist()/sum(spike_mid16.count))
myshapepercent=(numpy.array(spike_shape16.count).astype(float).tolist()/(sum(spike_shape16.count)+1))

myerror=((myshapepercent[0]-idealans[0])**2+(myshapepercent[1]-idealans[1])**2+(myshapepercent[2]-idealans[2])**2) ## for triangle
#print int(100*myerror)
gradout=myshapepercent*(1-myshapepercent)*(idealans-myshapepercent)
gradmid=mymidpercent*(1-mymidpercent)*((gradout[0]*weightsout[0])+(gradout[1]*weightsout[1])+(gradout[2]*weightsout[2]))
weightsout[0]=clip(weightsout[0]+(0.01*mymidpercent*gradout[0]),-0.2,0.2)
weightsout[1]=clip(weightsout[1]+(0.01*mymidpercent*gradout[1]),-0.2,0.2)
weightsout[2]=clip(weightsout[2]+(0.01*mymidpercent*gradout[2]),-0.2,0.2)

weight16[0]=clip(weight16[0]+(0.05*mysumpercent*gradmid[0]),-0.2,0.2)
weight16[1]=clip(weight16[1]+(0.05*mysumpercent*gradmid[1]),-0.2,0.2)
weight16[2]=clip(weight16[2]+(0.05*mysumpercent*gradmid[2]),-0.2,0.2)
weight16[3]=clip(weight16[3]+(0.05*mysumpercent*gradmid[3]),-0.2,0.2)
weight16[4]=clip(weight16[4]+(0.05*mysumpercent*gradmid[4]),-0.2,0.2)
weight16[5]=clip(weight16[5]+(0.05*mysumpercent*gradmid[5]),-0.2,0.2)
weight16[6]=clip(weight16[6]+(0.05*mysumpercent*gradmid[6]),-0.2,0.2)
weight16[7]=clip(weight16[7]+(0.05*mysumpercent*gradmid[7]),-0.2,0.2)
weight16[8]=clip(weight16[8]+(0.05*mysumpercent*gradmid[8]),-0.2,0.2)
weight16[9]=clip(weight16[9]+(0.05*mysumpercent*gradmid[9]),-0.2,0.2)




@network_operation(dt=1000*ms)
def update_plots():
    num_iterations=18
    #mysumpercent=(1/(1+exp(-(((numpy.array(spike_sum.count).astype(float)/5)-7)))))
    #mymidpercent=(1/(1+exp(-(((numpy.array(spike_mid16.count).astype(float)/5)-7)))))
    mysumpercent=(1/(1+exp(-(log(numpy.array(spike_sum.count)+1)*2-7))))
    mymidpercent=(1/(1+exp(-(log(numpy.array(spike_mid16.count)+1)*2-7))))
    #mysumpercent=(numpy.array(spike_sum.count).astype(float).tolist()/sum(spike_sum.count))
    #mymidpercent=(numpy.array(spike_mid16.count).astype(float).tolist()/sum(spike_mid16.count))
    myshapepercent=(numpy.array(spike_shape16.count).astype(float).tolist()/(sum(spike_shape16.count)+1))
    myerror=((myshapepercent[0]-idealans[0])**2+(myshapepercent[1]-idealans[1])**2+(myshapepercent[2]-idealans[2])**2) ## for triangle
    gradout=myshapepercent*(1-myshapepercent)*(idealans-myshapepercent)
    gradmid=mymidpercent*(1-mymidpercent)*((gradout[0]*weightsout[0])+(gradout[1]*weightsout[1])+(gradout[2]*weightsout[2]))
    weightsout[0]=clip(weightsout[0]+(0.01*mymidpercent*gradout[0]),-0.2,0.2)
    weightsout[1]=clip(weightsout[1]+(0.01*mymidpercent*gradout[1]),-0.2,0.2)
    weightsout[2]=clip(weightsout[2]+(0.01*mymidpercent*gradout[2]),-0.2,0.2)
    weight16[0]=clip(weight16[0]+(0.05*mysumpercent*gradmid[0]),-0.2,0.2)
    weight16[1]=clip(weight16[1]+(0.05*mysumpercent*gradmid[1]),-0.2,0.2)
    weight16[2]=clip(weight16[2]+(0.05*mysumpercent*gradmid[2]),-0.2,0.2)
    weight16[3]=clip(weight16[3]+(0.05*mysumpercent*gradmid[3]),-0.2,0.2)
    weight16[4]=clip(weight16[4]+(0.05*mysumpercent*gradmid[4]),-0.2,0.2)
    weight16[5]=clip(weight16[5]+(0.05*mysumpercent*gradmid[5]),-0.2,0.2)
    weight16[6]=clip(weight16[6]+(0.05*mysumpercent*gradmid[6]),-0.2,0.2)
    weight16[7]=clip(weight16[7]+(0.05*mysumpercent*gradmid[7]),-0.2,0.2)
    weight16[8]=clip(weight16[8]+(0.05*mysumpercent*gradmid[8]),-0.2,0.2)
    weight16[9]=clip(weight16[9]+(0.05*mysumpercent*gradmid[9]),-0.2,0.2)
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
    
    midsyn1.g_synmax=weight16[0]
    midsyn2.g_synmax=weight16[1]
    midsyn3.g_synmax=weight16[2]
    midsyn4.g_synmax=weight16[3]
    midsyn5.g_synmax=weight16[4]
    midsyn6.g_synmax=weight16[5]
    midsyn7.g_synmax=weight16[6]
    midsyn8.g_synmax=weight16[7]
    midsyn9.g_synmax=weight16[8]
    midsyn10.g_synmax=weight16[9]
    shapesyn1.g_synmax=weightsout[0]
    shapesyn2.g_synmax=weightsout[1]
    shapesyn3.g_synmax=weightsout[2]    
    
    
    pixelcount=pixelcount+1
    mypixel=thisrunpixels[pixelcount]
    
    spike_sum = SpikeMonitor(sumneur)
    spike_mid16 = SpikeMonitor(midneur16)
    spike_shape16 = SpikeMonitor(whichshape16)
    

run(1000*ms*num_iterations)
show()

