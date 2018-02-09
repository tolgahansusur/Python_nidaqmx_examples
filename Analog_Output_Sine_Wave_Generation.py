import nidaqmx
import numpy as np
import time
from nidaqmx.constants import AcquisitionType, TaskMode


Fs = 8000
f = 20
sample = 8000
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)

with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan('Dev3/ao0')

    task.timing.cfg_samp_clk_timing(8000,sample_mode=AcquisitionType.CONTINUOUS)
    

    

    print('Generation is started')
    task.write(y)
    task.control(TaskMode.TASK_COMMIT)
    task.start()
    

    while True:
        print("generating")
        time.sleep(1)
