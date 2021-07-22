print('Please wait while the program is loading...')

import dht
import machine
d = dht.DHT11(machine.Pin(4))
d.temperature()
d.humidity()

temperature = d.temperature()
humidity = d.humidity()
fahrenheit = (temperature * 1.8) + 32 # C° to F°

print("the current temp is " , fahrenheit )
print("the current rel hum is", humidity)
