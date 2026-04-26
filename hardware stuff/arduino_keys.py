import serial
import keyboard

ser = serial.Serial('COM6', 9600, timeout=0.1)

button_map = {
    'B0': 'w',   
    'B1': 's',
    'B2': 'space',  
}

distance_map = {
    'D20' : '1',
    'D50' : '2',
    'D100' : '3',
    'D200' : '4',
}

direction_map = {
    'JL': '5',
    'JR': '6',
    'JU': '7',
    'JD': '8',
}

last_zone = None
last_direction = None

print("Listening for button presses... (Ctrl+C to quit)")

while True:
    try: 
        line = ser.readline().decode('utf-8').strip()
        if not line:
            continue
        if line in button_map:
            key = button_map[line]
            print(f"Button {line} → {key}")
            keyboard.send(key)
        elif line in distance_map:
            key = distance_map[line]
            if line != last_zone:
                print(f"Distance {line} → {key}")
                keyboard.send(key)
            last_zone = line
        elif line in direction_map:
            key = direction_map[line]
            if line != last_direction:
                print(f"Direction {line} → {key}")
                keyboard.send(key)
            last_direction = line
        ser.reset_input_buffer()
    except (UnicodeDecodeError, ValueError):
        continue