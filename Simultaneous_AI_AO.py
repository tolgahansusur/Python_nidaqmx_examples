
import numpy as np
import nidaqmx
import matplotlib.pyplot as plt
from nidaqmx.constants import AcquisitionType, TaskMode

""" Creating Sine wave for Analog output generation"""

Fs = 8000  # sampling frequency
f = 5  # frequency of signal
sample = 8000  # time domain array size
x = np.arange(sample)  # time domain array
y = np.sin(2 * np.pi * f * x / Fs)  # sine wave

""" Done """

""" Configuration for both analog input and output"""

with nidaqmx.Task() as master_task, nidaqmx.Task() as slave_task:
    master_task.ai_channels.add_ai_voltage_chan("Dev3/ai2")  # analog input port is reserved
    slave_task.ao_channels.add_ao_voltage_chan("Dev3/ao0")  # analog output port is reserved

    master_task.timing.cfg_samp_clk_timing(
        8000, sample_mode=AcquisitionType.CONTINUOUS)  # analog input port is configured for continuous 8000 s/s )

    slave_task.timing.cfg_samp_clk_timing(
        8000, sample_mode=AcquisitionType.CONTINUOUS)  # analog output port is configured for continous 8000 s/S


    """ Done """

    """ Start generating AO and reading AI"""

    slave_task.write(y)  # analog output buffer is filled with sine wave
    slave_task.control(TaskMode.TASK_COMMIT)  # analog output port is committed

    master_task.control(TaskMode.TASK_COMMIT)  # analog input port is committed

    print('Acqusition is started')
    slave_task.start()
    master_task.start()

    """ Done """

    while True:
        master_data = master_task.read(
            number_of_samples_per_channel=8000)  # analog input sample per read value is 8000, so min. period can be 1sec

        plt.plot(x / Fs, master_data)
        plt.pause(0.01)
        plt.gcf().clear()




