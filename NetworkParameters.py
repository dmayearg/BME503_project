from brian2 import *

duration = 0.5*second
dt_sim = 0.5*ms


## Neuron Model
a = 0.1
b = 0.2
c = -65
d = 2
sens_tau_decay=1.5*ms ## maybe 1 for all or 2 ?
filt_tau_decay=2*ms
sum_tau_decay=2*ms

sensormag=3 ## the very minimum is 1.3 for it to fire with 3 inputs to make sensor neuron fire
## to fire with 2 input "on" is about 2.2
filtg_synmaxval=0.15 ##// if this is too low there is no difference between circ and square
sumg_synmaxval=0.06 

g_synpk = 0.02
learng_synmaxval=(g_synpk/(sum_tau_decay/ms*exp(-1)))

## Network Size
image_size = 18 # 18x18
sense_size = 6 # 6x6
kernel_size = 3 #
filterstack_size = 16 # 4x4
pool_size = 16 # 4x4
hid_size = 1 # 10 neurons
out_size = 1 # 3 neurons

## Learning Parameters
wmax = 2
reward_mag = 1
taupre=5*ms 
taupost=10*ms
Apre = 0.00001
Apost = -Apre*1.05

# intialize random weights
weights_random = 0.3