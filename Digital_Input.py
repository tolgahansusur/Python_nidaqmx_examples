import nidaqmx
from nidaqmx.constants import (
    LineGrouping)


with nidaqmx.Task() as task:


    task.di_channels.add_di_chan("Dev3/port1/line0:3",
                                 line_grouping=LineGrouping.CHAN_PER_LINE)

    print('N Channel 1 Sample Read: ')
    data = task.read()
    print(data)


