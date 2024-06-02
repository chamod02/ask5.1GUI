import gpiod
import tkinter as tk

# Define LED Pins
RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

# Define location of GPIO
chip = gpiod.Chip('gpiochip4')

# Create variables for each LED
red_line = chip.get_line(RED_PIN)
green_line = chip.get_line(GREEN_PIN)
blue_line = chip.get_line(BLUE_PIN)

# Set the LEDs as outputs
red_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
green_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
blue_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

# Function to turn off all LEDs
def all_off():
    red_line.set_value(0)
    green_line.set_value(0)
    blue_line.set_value(0)

# Functions to turn on each LED
def red_on():
    all_off()
    red_line.set_value(1)

def green_on():
    all_off()
    green_line.set_value(1)

def blue_on():
    all_off()
    blue_line.set_value(1)

# Create the GUI application
app = tk.Tk()
app.title("LED Control")

# Add radio buttons to the GUI
led_var = tk.StringVar()

red_radio = tk.Radiobutton(app, text="Red LED", variable=led_var, value="red", command=red_on)
red_radio.pack()

green_radio = tk.Radiobutton(app, text="Green LED", variable=led_var, value="green", command=green_on)
green_radio.pack()

blue_radio = tk.Radiobutton(app, text="Blue LED", variable=led_var, value="blue", command=blue_on)
blue_radio.pack()

# Add exit button to the GUI
exit_button = tk.Button(app, text="Exit", command=app.quit)
exit_button.pack()

# Start the Tkinter event loop
app.mainloop()

# Clean up GPIO on exit
all_off()
red_line.release()
green_line.release()
blue_line.release()
