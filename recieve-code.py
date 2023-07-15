# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials UART Serial example"""
import board
import time
import busio
import digitalio

# For most CircuitPython boards:
#led = digitalio.DigitalInOut(board.LED)
pin = digitalio.DigitalInOut(board.A0)
pin.direction=digitalio.Direction.OUTPUT

# For QT Py M0:
# led = digitalio.DigitalInOut(board.SCK)
#led.direction = digitalio.Direction.OUTPUT

uart = busio.UART(board.TX, board.RX, baudrate=115200)
pin.value = False
time.sleep(0.2)
pin.value=True
time.sleep(0.2)
print(uart.readline())

uart.write(b"AT+FACTORY\r\n")
time.sleep(1)
print(uart.readline())
time.sleep(1)
print(uart.readline())
uart.write(b"AT+BAND=915000000\r\n")
print(uart.readline())
uart.write(b"AT+BAND=915000000\r\n")
print(uart.readline())
uart.write(b"AT+BAND=915000000\r\n")
print(uart.readline())
uart.write(b"AT+BAND=915000000\r\n")
print(uart.readline())
uart.write(b"AT+ADDRESS=255\r\n")
print(uart.readline())
uart.write("AT+CPIN?\r\n".encode("utf-8"))
print(uart.readline())
uart.write(b"AT+NETWORKID?\r\n")
print(uart.readline())
uart.write(b"AT+PARAMETER?\r\n")
print(uart.readline())
#uart.write(b"AT+NETWORKID=18\r\n")
#print(uart.readline())
#uart.write(b"AT+CPIN=\r\n")
#print(uart.readline())
while True:
    #uart.write("+RCV=116,5,TESTD,-99,40\r\n".encode('utf-8'))
    data = uart.readline()  # read up to 32 bytes
    # print(data)  # this is a bytearray type
    #print()
    #time.sleep(1)

    if data is not None:
        print(data)
        print(data.decode('utf-8'))
        #led.value = True

        # convert bytearray to string
        #data_string = ''.join([chr(b) for b in data])
        #print(data_string, end="")

        #led.value = False







"""# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of sending and recieving data with the RFM95 LoRa radio.
# Author: Tony DiCola
import board
import busio
import digitalio
import time
import alarm

import adafruit_rfm9x


# Define radio parameters.
RADIO_FREQ_MHZ = 433.0  # Frequency of the radio in Mhz. Must match your
# module! Can be a value like 915.0, 433.0, etc.

# Define pins connected to the chip, use these if wiring up the breakout according to the guide:
CS = digitalio.DigitalInOut(board.A1)
RESET = digitalio.DigitalInOut(board.A0)
# Or uncomment and instead use these if using a Feather M0 RFM9x board and the appropriate
# CircuitPython build:
# CS = digitalio.DigitalInOut(board.RFM9X_CS)
# RESET = digitalio.DigitalInOut(board.RFM9X_RST)

# Define the onboard LED"""
"""LED = digitalio.DigitalInOut(board.NEOPIXEL)
LED.direction = digitalio.Direction.OUTPUT
LED_POWER = digitalio.DigitalInOut(board.NEOPIXEL_POWER)
LED_POWER.direction = digitalio.Direction.OUTPUT
LED_POWER.value = False
LED.value = False"""

# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialze RFM radio
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# Note that the radio is configured in LoRa mode so you can't control sync
# word, encryption, frequency deviation, or other settings!

# You can however adjust the transmit power (in dB).  The default is 13 dB but
# high power radios like the RFM95 can go up to 23 dB:
rfm9x.tx_power = 5

# Send a packet.  Note you can only send a packet up to 252 bytes in length.
# This is a limitation of the radio packet size, so if you need to send larger
# amounts of data you will need to break it into smaller send calls.  Each send
# call will wait for the previous one to finish before continuing.
rfm9x.send(bytes("Hello world!\r\n", "utf-8"))
print("Sent Hello World message!")

# Wait to receive packets.  Note that this library can't receive data at a fast
# rate, in fact it can only receive and process one 252 byte packet at a time.
# This means you should only use this for low bandwidth scenarios, like sending
# and receiving a single message at a time.
print("Waiting for packets...")

rfm9x.send(bytes("Hello world!\r\n", "utf-8"))
rfm9x.sleep()
print("sent")
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 20)
alarm.exit_and_deep_sleep_until_alarms(time_alarm)
#while True:
#    time.sleep(0.05)
#    print("a")

#while True:
    #rfm9x.send(bytes("Hello world!\r\n", "utf-8"))
    #print("sent")
    #time.sleep(10)
   # time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 20)
   # alarm.exit_and_deep_sleep_until_alarms(time_alarm)
    #packet = rfm9x.receive()
    # Optionally change the receive timeout from its default of 0.5 seconds:
    # packet = rfm9x.receive(timeout=5.0)
    # If no packet was received during the timeout then None is returned.
    #if packet is None:
        # Packet has not been received
        #LED.value = False
        #print("Received nothing! Listening again...")
    #else:
        # Received a packet!
        #LED.value = True
        # Print out the raw bytes of the packet:
        #print("Received (raw bytes): {0}".format(packet))
        # And decode to ASCII text and print it too.  Note that you always
        # receive raw bytes and need to convert to a text format like ASCII
        # if you intend to do string processing on your data.  Make sure the
        # sending side is sending ASCII data before you try to decode!
        #packet_text = str(packet, "ascii")
        #print("Received (ASCII): {0}".format(packet_text))
        # Also read the RSSI (signal strength) of the last received message and
        # print it.
        #rssi = rfm9x.last_rssi
        #print("Received signal strength: {0} dB".format(rssi))

