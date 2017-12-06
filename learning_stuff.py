
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

################################## STATE MONITORS #############################

#MS = StateMonitor(sensors, ('v', 'I'), record=True)
#Msum=StateMonitor(sumneur, ('v'), record=True)
spike_sum = SpikeMonitor(sumneur)
spike_mid16 = SpikeMonitor(midneur16)
spike_shape16 = SpikeMonitor(whichshape16)

run(duration)

mysumpercent=(1/(1+exp(-(((numpy.array(spike_sum.count).astype(float)/5)-7)))))
mymidpercent=(1/(1+exp(-(((numpy.array(spike_mid16.count).astype(float)/5)-7)))))

#mysumpercent=(1/(1+exp(-(log(numpy.array(spike_sum.count)+1)*2-7))))
#mymidpercent=(1/(1+exp(-(log(numpy.array(spike_mid16.count)+1)*2-7))))

#mysumpercent=(numpy.array(spike_sum.count).astype(float).tolist()/sum(spike_sum.count))
#mymidpercent=(numpy.array(spike_mid16.count).astype(float).tolist()/sum(spike_mid16.count))

myshapepercent=(numpy.array(spike_shape16.count).astype(float).tolist()/(sum(spike_shape16.count)+1))

myerror=((myshapepercent[0]-idealans[0])**2+(myshapepercent[1]-idealans[1])**2+(myshapepercent[2]-idealans[2])**2) ## for triangle


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


#print numpy.array(spike_sum.count).tolist()  #, numpy.array(spike_mid16.count).tolist(), numpy.array(spike_shape16.count).tolist()
#print numpy.array(spike_mid16.count).tolist()
#print numpy.array(spike_shape16.count).tolist()
#print int(100*myerror)

#print numpy.array(spike_sum.count).tolist()
#print numpy.array(spike_mid16.count).tolist()
#print numpy.array(spike_shape16.count).tolist()
#print int(100*myerror)
show()

