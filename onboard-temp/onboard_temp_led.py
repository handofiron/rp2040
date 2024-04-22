from machine import Pin
import utime

# Onboard LED pin
led_pin = Pin("LED", Pin.OUT)

# Function to toggle LED state
def toggle_led():
    led_pin.toggle()

# Function to read temperature
def read_temperature():
    temp_sensor = machine.ADC(machine.ADC.CORE_TEMP)
    conversion_factor = 3.3 / (65535)
    reading = temp_sensor.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    return temperature

# Main loop
while True:
    temperature = read_temperature()
    print("Temperature: {:.2f} °C".format(temperature))

    # Flash LED based on temperature
    if temperature >= 30:
        toggle_led()
        utime.sleep(0.2)
        toggle_led()
        utime.sleep(0.2)
    else:
        toggle_led()
        utime.sleep(1)
