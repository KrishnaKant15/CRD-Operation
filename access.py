import code as x  #importing the main file as a library 

#Create Operation
x.create("ab",25)

x.create("src",70,3600) #{to create a key with key_name,value given and with time-to-live property}
 
#Read Operation
x.read("ab") #{returns the value of the respective key in json format} 


x.read("src") {#it returns the value of the respective key in json format if the time-to-live is not expired else it returns an ERROR}


#Create Operation
x.create("ab",50)  {#it returns an ERROR since the key_name already exists in the database}

#Delete Operation
x.delete("ab")  {#it deletes the respective key and its value from the database}

#access these using multiple threads as
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
#continues till  tn


