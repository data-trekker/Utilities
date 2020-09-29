#!/usr/bin/env python
# coding: utf-8

# ## Utility to measure time taken by a code run 

# In[3]:


#import libs
import  time
import numpy as np

#create a timer class
class Timer: #@save
    """Records multiple running times"""
    def __init__(self):
        self.times = []
        self.start()
    
    def start(self):
        """start the timer"""
        self.tik = time.time() #current time
        
    def stop(self):
        """Stop the timer and record the time in a list"""
        self.times.append(time.time() - self.tik)
        return self.times[-1]
    
    def avg(self):
        """returns the average time"""
        return sum(self.times)/len(self.times)
    
    def sum(self):
        """returns the sum of time"""
        return sum(self.times)
    
    def cumsum(self):
        """Returns the accumulated time"""
        return np.array(self.times).cumsum().tolist()
    


# In[ ]:




