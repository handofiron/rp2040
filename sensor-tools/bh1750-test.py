from machine import I2C, Pin
import time

# Initialize I2C communication
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# BH1750 address, 0x23(35)
# Read data in 1 Lux resolution
i2c.writeto(0x23, bytes([0x10]))

time.sleep(0.5)  # Wait for the measurement to complete

# Read data back from 0x20(32), 2 bytes
data = i2c.readfrom(0x23, 2)

# Convert the data to lux
lux = (data[0] << 8 | data[1]) / 1.2

print("Light Level: %.2f lux" % lux)
