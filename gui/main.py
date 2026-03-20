import serial
import struct
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import collections

# Configuration
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE   = 115200
WINDOW_SIZE = 200
SAMPLES_PER_BUFFER = 1024

# Data buffer
data_deque = collections.deque([0] * WINDOW_SIZE, maxlen=WINDOW_SIZE)

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.1)
except Exception as e:
    print(f"Error opening serial port: {e}")
    exit()

# Setuo Plot
fig, ax = plt.subplots()
line,   = ax.plot(range(WINDOW_SIZE), data_deque)
ax.set_ylim(0, 4096)
ax.set_title("Pico 2 Live Oscilloscope")
ax.set_ylabel("ADC Value")
ax.set_xlabel("Samples")

def update(frame):

    bytes_to_read = ser.in_waiting
    if bytes_to_read >= 2:
        raw_data = ser.read(bytes_to_read - (bytes_to_read % 2))
        fmt = f"{len(raw_data)//2}H"
        samples = struct.unpack(fmt, raw_data)

        data_deque.extend(samples)

    line.set_ydata(data_deque)
    return line,

# Start animation
ani = FuncAnimation(fig, update, interval=10, blit=True)
plt.show()
ser.close()
