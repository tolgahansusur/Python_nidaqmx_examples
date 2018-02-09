""" You can acquire analog inputs simultaously from two different  DAQ device""" 


import pprint
import nidaqmx
import matplotlib.pyplot as plt
import numpy as np
from nidaqmx.constants import AcquisitionType, TaskMode


Rate=1000
Sample_to_read=100

pp = pprint.PrettyPrinter(indent=2)
t = np.linspace(0, Sample_to_read/Rate, Sample_to_read, endpoint=True)
plt.ion()
i=0

Rate=1000
Sample_to_read=100


with nidaqmx.Task() as master_task, nidaqmx.Task() as slave_task:
    master_task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    slave_task.ai_channels.add_ai_voltage_chan("Dev4/ai0")

   
    master_task.timing.cfg_samp_clk_timing(
        Rate, sample_mode=AcquisitionType.CONTINUOUS)
    

    
    slave_task.timing.cfg_samp_clk_timing(
    Rate, sample_mode=AcquisitionType.CONTINUOUS)
    


   

    
    slave_task.start()
    master_task.start()

    while i<100:  # measurement 
        master_data = master_task.read(number_of_samples_per_channel=Sample_to_read)
        slave_data = master_task.read(number_of_samples_per_channel=Sample_to_read)
        
        plt.subplot(211)
        plt.plot(t,master_data)
        plt.xlabel('time(sec)')
        plt.ylabel('voltage(V)')


        plt.subplot(212)
        plt.plot(t,slave_data)
        plt.xlabel('time(sec)')
        plt.ylabel('voltage(V)')
        plt.show()


        plt.pause(0.01)
        plt.gcf().clear()
        i=i+1

    plt.close()
