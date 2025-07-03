# stay_awake.py
import time
import ctypes

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001

# Prevent sleep
ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)

try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    pass
