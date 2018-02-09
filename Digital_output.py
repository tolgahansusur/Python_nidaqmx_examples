import nidaqmx
import time
from nidaqmx.constants import (
    LineGrouping)


with nidaqmx.Task() as task:
    task.do_channels.add_do_chan(
        'Dev3/port0/line0:3',
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

    
    print('0-15 integer values send to digital lines as binary conversion')

    for x in range(0,16):
        
        task.write(x) 
        time.sleep(0.25)# second sleep

    print("sequence is finished")
        





        
        
    



      

