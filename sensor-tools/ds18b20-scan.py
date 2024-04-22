import machine
import onewire
import ds18x20
import utime
import ujson
import os

# Initialize the OneWire bus on pin 7
ow = onewire.OneWire(machine.Pin(7))

# Scan for DS18B20 sensors on the bus
roms = ow.scan()

if len(roms) == 0:
    print("No DS18B20 sensors found on pin 7.")
else:
    print("DS18B20 sensors found on pin 7:")
    for rom in roms:
        print("Sensor Address:", rom)

    # Create a list of sensor addresses as hexadecimal strings
    sensor_addresses = [rom.hex() for rom in roms]

    # Specify the path to the "lib" directory on the flash
    lib_directory = '/lib/'

    # Check if the "lib" directory exists, and create it if not
    if not os.listdir(lib_directory):
        os.mkdir(lib_directory)

    # Save the addresses to a JSON file in the "lib" directory
    json_file_path = lib_directory + 'ds18b20_addresses.json'
    with open(json_file_path, 'w') as file:
        ujson.dump(sensor_addresses, file)

print("Addresses saved to /lib/ds18b20_addresses.json in flash.")
