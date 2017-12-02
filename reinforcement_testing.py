from brian2 import *
import random
import numpy as np 
import matplotlib.pyplot as plt

  
duration=4000*ms
div=0.01*ms
stimlist=numpy.zeros(4000)
# pulselist=numpy.arange(10,4000,40)
# stimlist[pulselist]=1 

pulselist=numpy.arange(10,500,40)
stimlist[pulselist]=1 

pulselist2=numpy.arange(1010,1500,40)
stimlist[pulselist2]=1    

pulselist2=numpy.arange(2010,2500,40)
stimlist[pulselist2]=1  

pulselist2=numpy.arange(3010,3500,40)
stimlist[pulselist2]=1  

#duration = .02*second

A1=TimedArray(stimlist*mV/mV,dt=.001*second)
I1=A1

stimlist=numpy.zeros(4000)
# pulselist=numpy.arange(10,4000,40)
# stimlist[pulselist]=1 

pulselist=numpy.arange(510,1000,40)
stimlist[pulselist]=1 
pulselist2=numpy.arange(1510,2000,40)
stimlist[pulselist2]=1    
pulselist2=numpy.arange(2510,3000,40)
stimlist[pulselist2]=1    
pulselist2=numpy.arange(3510,4000,40)
stimlist[pulselist2]=1    

#duration = .02*second

A2=TimedArray(stimlist*mV/mV,dt=.001*second)
I2=A2

a = 0.1
b = 0.2
c = -65
d = 2

dt=0.1*ms
tau_ampa=2*ms
tau_gaba=3*ms
g_synpk=0.02
g_synmaxval=(g_synpk/(tau_ampa/ms*exp(-1)))
E = 0


eqs = '''
dv/dt = (0.04*v**2 + 5*v + 140 - u + mag1*I1(t)+mag2*I2(t) + i_syn)/ms: 1
du/dt = a*(b*v - u)/ms : 1
i_syn = g_ampa*(E-v) : 1

dg_ampa/dt = -g_ampa/tau_ampa + z_a/ms: 1
dz_a/dt = -z_a/tau_ampa : 1

mag1 : 1
mag2 : 1
x : meter
y : meter
std : 1
'''

Grs1 = NeuronGroup(1,eqs, clock=Clock(dt), threshold = 'v >= 30', reset = '''
	v = c
	u = u + d
''')

Grs2 = NeuronGroup(1,eqs, clock=Clock(dt), threshold = 'v >= 30', reset = '''
	v = c
	u = u + d 
''')

Grs3 = NeuronGroup(1,eqs, clock=Clock(dt), threshold = 'v >= 30', reset = '''
	v = c
	u = u + d 
''')

Grs4 = NeuronGroup(1,eqs, clock=Clock(dt), threshold = 'v >= 30', reset = '''
	v = c
	u = u + d 
''')

taupre = taupost = 20*ms
wmax = 2*.8
Apre = 0.01
Apost = -Apre*taupre/taupost*1.05

Sr1 = Synapses(Grs1, Grs3, clock=Grs1.clock,model='''
        	w : 1
        	dapre/dt = -apre/taupre : 1 
        	dapost/dt = -apost/taupost : 1
        	reward:1
        	g_synmax:1
        	''',
		on_pre='''
		g_ampa += w
		z_a+=g_synmax
		apre += Apre
             	w = clip(w+reward*apost, 0, wmax)
		''',
		on_post='''
		apost += Apost
		w = clip(w+reward*apre, 0, wmax)
		''')            
		                                                                                                                        		                                                                                                                        
Sr1.connect(i=[0],j=[0])
Sr1.g_synmax = g_synmaxval
Sr1.w=0.5
Sr1.reward=1

Sr2 = Synapses(Grs2, Grs3, clock=Grs1.clock,model='''
        	w : 1
        	dapre/dt = -apre/taupre : 1 
        	dapost/dt = -apost/taupost : 1
        	reward:1
        	g_synmax:1
        	''',
		on_pre='''
		g_ampa += w
		z_a+=g_synmax
		apre += Apre
             	w = clip(w+reward*apost, 0, wmax)
		''',
		on_post='''
		apost += Apost
		w = clip(w+reward*apre, 0, wmax)
		''')            
		                                                                                                                        		                                                                                                                        
Sr2.connect(i=[0],j=[0])
Sr2.w=0.5
Sr2.g_synmax = g_synmaxval
Sr2.reward=-1

Sr3 = Synapses(Grs3, Grs4, clock=Grs1.clock,model='''
        	g_synmax:1''',
		on_pre='''
		z_a+=g_synmax
		''')            
		                                                                                                                        		                                                                                                                        
Sr3.connect(i=[0],j=[0])
Sr3.g_synmax = g_synmaxval

#Regular Spiking

Grs1.v = -65
Grs1.u = b*(Grs1.v)
Grs1.mag1=40
Grs1.mag2=0

Grs2.v = -65
Grs2.u = b*(Grs2.v)
Grs2.mag1=0
Grs2.mag2=40

Grs3.v = -65
Grs3.u = b*(Grs3.v)
Grs3.mag1=0
Grs3.mag2=0

Grs4.v = -65
Grs4.u = b*(Grs4.v)
Grs4.mag1=0
Grs4.mag2=0

#M = StateMonitor(G,'v',record=True)
M = StateMonitor(Grs1,('v','g_ampa'),record=True)
M2 = StateMonitor(Grs2,('v','g_ampa'),record=True)
M3 = StateMonitor(Grs3,('v','g_ampa'),record=True)
M4 = StateMonitor(Grs4,('v','g_ampa'),record=True)
S=StateMonitor(Sr1,('apre','apost','w'),record=True)
S2=StateMonitor(Sr2,('apre','apost','w'),record=True)
spike = SpikeMonitor(Grs3)
spiketarget = SpikeMonitor(Grs1)

@network_operation(dt=1*ms)
def update_normalize():
    normalize = Sr1.w+Sr2.w
    Sr1.w = Sr1.w/normalize
    Sr2.w = Sr2.w/normalize
    return
    
@network_operation(dt=1*ms)
def update_reward():
    if len(M.t/ms) != 0:
        if any(spike.t/ms>M.t[len(M.t/ms)-1]/ms-10) and any(spike.t/ms<M.t[len(M.t/ms)-1]/ms+10):
            if any(spiketarget.t/ms>M.t[len(M.t/ms)-1]/ms-10) and any(spiketarget.t/ms<M.t[len(M.t/ms)-1]/ms+10):
                Sr1.reward = 1
                Sr2.reward = 1
        else:
            Sr1.reward = -1
            Sr2.reward = -1
    return

run(duration)
subplot(511)
plot(M.t/ms, M.v[0])
subplot(512)
plot(M.t/ms, M2.v[0],'r')
subplot(513)
plot(M.t/ms, M3.v[0])
subplot(514)
plot(M.t/ms, S.w[0])
subplot(515)
plot(M.t/ms, S2.w[0])
#vis_directed(Sre,Stc)
show()