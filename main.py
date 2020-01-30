# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

# Add a label with the text "Hello"
firstLabel = Label (window, text = "you eat all my beans") # Create the label 
firstLabel.grid (column=0, row=0)                   # Place on screen
lbl = Label(window, text="")
firstLabel = Label (window, text="Hello", font =("Arial Bold" , 70  ))
                                    # create the label 
                                    # Place on screen
# Place the label in the window at 0, 0
lbl.grid(column=0, row=0)


window.mainloop()     # Keep the window open
