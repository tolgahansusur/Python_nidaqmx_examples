import nidaqmx
import matplotlib.pyplot as plt
import numpy as np
from nidaqmx.constants import AcquisitionType, TaskMode
t = np.linspace(0, 1, 5000, endpoint=True)


plt.ion()
i=0

with nidaqmx.Task() as master_task:
    master_task.ai_channels.add_ai_voltage_chan("Dev3/ai1")

  
    master_task.timing.cfg_samp_clk_timing(
        50000, sample_mode=AcquisitionType.CONTINUOUS)
   


    master_task.control(TaskMode.TASK_COMMIT)

    master_task.start()


    while i<100:
        master_data = master_task.read(number_of_samples_per_channel=5000)
        plt.plot(t,master_data)
        plt.pause(0.01)
        plt.gcf().clear()
        i=i+1

    plt.close()
        
   
   
    
      

   


    
    

      
