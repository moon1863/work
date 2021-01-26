#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from collections import OrderedDict 


# In[2]:


df = pd.read_csv (r'C:\Users\Tadpole\Desktop\work\testA.csv')


# In[3]:


df2 = pd.read_csv (r'C:\Users\Tadpole\Desktop\work\testB.csv')


# In[32]:


class label:
     def __init__(self,driveID,date):
            self.driveID = driveID
            self.date = date
            self.ridelist = []
class ride:
    def __init__(self,orginlat,orginlong,destlat,destlong,rideID,timeorgin,timedest,actordwell):
        
        self.orginlat = orginlat
        self.orginlong = orginlong
        self.destlat = destlat
        self.destlong = destlong
        self.rideID = rideID
        self.timeorgin = timeorgin
        self.timedest = timedest
        self.actordwell = actordwell
        self.distance = distance
    


# In[5]:


labellist = []


# In[6]:



for x in range(len(df)):
    
    driveID = df.iloc[x]['active_driver_id']
    
    dateandtimeorgin = df.iloc[x]['started_on']
    date,trash = dateandtimeorgin.split(' ')
    
    
    labellist.append( label(driveID, date))






for x in range(len(df)):
    driveID = df.iloc[x]['active_driver_id']
    orginlat = df.iloc[x]['start_location_lat']
    orginlong = df.iloc[x]['start_location_long']
    destlat = df.iloc[x]['end_location_lat']
    destlong = df.iloc[x]['end_location_long']
    rideID = df.iloc[x]['RIDE_ID']
    
    dateandtimeorgin = df.iloc[x]['started_on']
    date,timeorgin = dateandtimeorgin.split(' ')
    
    dateandtimedest =  df.iloc[x]['completed_on']
    date,timedest = dateandtimedest.split(' ')
    
    distance = df.iloc[x]['distance_travelled']
    
    actordwell = 'active'
    
   
    for obj in labellist:
        if obj.date == date and obj.driveID == driveID:
            obj.ridelist.append( ride(orginlat,orginlong,destlat,destlong,rideID,timeorgin,timedest,actordwell))
           
         

   

        
    


# In[31]:



for obj in labellist:
    counter = 0
    print( '\nDriverID =',obj.driveID, '\nDate =',obj.date, sep =' ' )
    for obj in obj.ridelist:
        print('\n')
        print("ride",counter)
        print('orginlat =',obj.orginlat)
        print('orginlong =',obj.orginlong)
        print('destlat =',obj.destlat)
        print('destlong =',obj.destlong)
        print('rideID =',obj.rideID)
        print('time of orgin =',obj.timeorgin)
        print('time of destination =',obj.timedest)
        print('status =',obj.actordwell)
        
        counter = counter + 1
        


# In[ ]:





# In[ ]:





# In[ ]:




