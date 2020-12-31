import threading 
from threading import*
import time

d={} #'d' is the dictionary in which is used to store data

#Create Operation 
def create(key,value,timeout=0):
    if key in d:
        print("Error: This Key Already Exists") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32:
                    d[key]=l
            else:
                print("Error: Memory Limit Exceeded!!")
        else:
            print("Error: Invalind key_name!!)

#Read Operation            
def read(key):
    if key not in d:
        print("Error: Given Key Does Not Present In Database. Please Enter a Valid One") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                string=str(key)+":"+str(b[0]) 
                return string
            else:
                print("Error: Time to live of",key,"has expired")
        else:
            string=str(key)+":"+str(b[0])
            return string

#Delete Operation
def delete(key):
    if key not in d:
        print("Error: Given Key Does Not Present In Database. Please Enter a Valid One") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print("Key Is Successfully Deleted")
            else:
                print("Error: Time to live of",key,"has expired") 
        else:
            del d[key]
            print("Key is successfully deleted")

