import tkinter as tk
import RPi.GPIO as GPIO

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins for LEDs
LED_pins = [17, 18, 22]
for pin in LED_pins:
    GPIO.setup(pin, GPIO.OUT)

def turn_on_led(led_index):
    # Turn off all LEDs
    for pin in LED_pins:
        GPIO.output(pin, GPIO.LOW)
    # Turn on the selected LED
    GPIO.output(LED_pins[led_index], GPIO.HIGH)

def exit_gui():
    # Cleanup GPIO
    for pin in LED_pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
    root.destroy()

def led_radio_clicked(led_index):
    turn_on_led(led_index)

# Create the GUI
root = tk.Tk()
root.title("LED Controller")

# Create radio buttons for LEDs
led_var = tk.IntVar()
led_var.set(-1)  # Set default selection to the none selected
for i in range(len(LED_pins)):
    tk.Radiobutton(root, text="LED {}".format(i+1), variable=led_var, value=i, command=lambda i=i: led_radio_clicked(i)).pack()

# Create exit button
exit_button = tk.Button(root, text="Exit", command=exit_gui)
exit_button.pack()

root.mainloop()
