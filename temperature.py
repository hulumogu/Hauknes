def readTemperatureSensor(sensorName):
    tempfile = open("/sys/bus/w1/devices/" + sensorName + "/w1_slave")
    thetext = tempfile.read()
    tempfile.close()
    tempdata = thetext.split("\n")[1].split(" ")[9]
    temperature = float(tempdata[2:])
    temperature = temperature / 1000
    return temperature

temp1 = readTemperatureSensor("28-01204ff7560c")
print(temp1)   
temp2 = readTemperatureSensor("28-01204fe4a25e")
print(temp2)   
