import sys
import abtechname
import pygameout
import tetris
import time

mode = 2
while mode not in [0, 1]:
    try:
        mode = input("Enter mode(0=DMX, 1=Pygame)")
        mode = int(mode)
    except:
        print("Invalid input")

init = None
update = None
get_input = None

if mode == 0:
    init = lambda: None
    update = lambda data: print(data)
    get_input = lambda: input("Enter data")
else:
    init = pygameout.init
    update = pygameout.update
    get_input = pygameout.get_input


print("1 - ABTech Logo")
print("2 - Tetris")
demo = int(input("Enter demo number"))

init()

if demo == 1:
    while True:
        input = get_input()
        data = abtechname.update(input)

        update(data)

if demo == 2:
    delta_time = 0
    last = time.time()  # Initialize `last` with the current time

    tetris.init()
    while True:
        current = time.time()  # Get the current time
        delta_time = current - last  # Calculate the time difference
        last = current  # Update `last` to the current time

        input = get_input()  # Retrieve user input
        data = tetris.update(input, delta_time*1000)  # Update the Tetris game logic

        if data:
            update(data)  # Update the display or state
