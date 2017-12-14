
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

##############################################################################
################################## SYNAPSES ##################################
##############################################################################

######################### the crazy synapses ###########################

midsyn1.g_synmax=myweights16[0]
midsyn2.g_synmax=myweights16[1]
midsyn3.g_synmax=myweights16[2]
midsyn4.g_synmax=myweights16[3]
midsyn5.g_synmax=myweights16[4]
midsyn6.g_synmax=myweights16[5]
midsyn7.g_synmax=myweights16[6]
midsyn8.g_synmax=myweights16[7]
midsyn9.g_synmax=myweights16[8]
midsyn10.g_synmax=myweights16[9]


shapesyn1.g_synmax=myweightsout[0]
shapesyn2.g_synmax=myweightsout[1]
shapesyn3.g_synmax=myweightsout[2]

################################## STATE MONITORS #############################

#MS = StateMonitor(sensors, ('v', 'I'), record=True)
#Msum=StateMonitor(sumneur, ('v'), record=True)
#Mmid=StateMonitor(midneur16, ('v'), record=True)
#Mshape=StateMonitor(whichshape16, ('v'), record=True)

spike_sum = SpikeMonitor(sumneur)
spike_mid16 = SpikeMonitor(midneur16)
spike_shape16 = SpikeMonitor(whichshape16)


run(duration)

myshapepercent=(numpy.array(spike_shape16.count).astype(float).tolist()/(sum(spike_shape16.count)))
myerror=((myshapepercent[0]-idealans[0])**2+(myshapepercent[1]-idealans[1])**2+(myshapepercent[2]-idealans[2])**2) ## for triangle
print numpy.array(spike_shape16.count).tolist(), myshapepercent, int(100*myerror)


show()

