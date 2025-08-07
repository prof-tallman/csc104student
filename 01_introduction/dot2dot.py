
import tkinter as tk
from tkinter import ttk

class DotToDotApp:

    def __init__(self, root_frame):
        ''' Allocates and initializes the Dot2Dot App. '''

        # Attributes must reference the 'self' object (they were called Properties in C#)
        self.window = root_frame
        self.window.wm_title('Dot2Dot App')
        self.window.resizable(False, False)
        self.last_x = None
        self.last_y = None
        self.dot_size = tk.IntVar(value=3)
        self.dot_color = tk.StringVar(value='cornflowerblue')
        self.draw_lines = tk.BooleanVar(value=True)

        # Every widget becomes an Attribute
        # We link some of the widgets to Tk Variables that are themselves Attributes
        self.lbl_welcome = tk.Label(self.window, text='Click on the canvas to create a dot-to-dot drawing')
        self.cvs_drawing = tk.Canvas(self.window, width=300, height=300, highlightthickness=1, highlightbackground='steelblue', bg='white')
        self.btn_clear = tk.Button(self.window, text='Clear Dot-to-Dot', command=self.clear_handler)
        self.lbl_dotsize = tk.Label(self.window, text='Dot size:')
        self.scl_dotsize = tk.Scale(self.window, variable=self.dot_size, from_=2, to=10, orient=tk.HORIZONTAL)
        self.lbl_dotcolor = tk.Label(self.window, text='Dot color:')
        self.cmb_dotcolor = ttk.Combobox(self.window, textvariable=self.dot_color, state=['readonly'], values=['darkseagreen', 'cornflowerblue', 'lightcoral'])
        self.chk_drawlines = ttk.Checkbutton(self.window, text='Draw Lines', variable=self.draw_lines, onvalue=True, offvalue=False)

        # Layout the different widgets in the window
        self.lbl_welcome.grid(row=1, column=1, columnspan=3, pady=10)
        self.cvs_drawing.grid(row=2, column=1, rowspan=4, padx=10, pady=10)
        self.lbl_dotsize.grid(row=2, column=2)
        self.scl_dotsize.grid(row=2, column=3, pady=10, padx=10)
        self.lbl_dotcolor.grid(row=3, column=2)
        self.cmb_dotcolor.grid(row=3, column=3, pady=10, padx=10)
        self.chk_drawlines.grid(row=4, column=2, columnspan=2)
        self.btn_clear.grid(row=5, column=2, columnspan=2, pady=10, padx=10)

        # Setup event handlers that cannot be programmed using 'command='
        self.cvs_drawing.bind('<Button-1>', self.mouse_click_handler)
        return

    def mouse_click_handler(self, event):
        ''' Handles mouse clicks within the drawing canvas by displaying a new dot
            and connecting the last dot to this new dot with a line. '''

        # Create local variables that are easier to use
        offset = self.dot_size.get()
        color = self.dot_color.get()
        lines = self.draw_lines.get()

        # Create the next dot
        x1, x2 = event.x-offset, event.x+offset
        y1, y2 = event.y-offset, event.y+offset
        self.cvs_drawing.create_oval(x1, y1, x2, y2, fill=color)

        # Connect a line from the previous dot to the next dot
        if lines == True and self.last_x != None and self.last_y != None:
            self.cvs_drawing.create_line(self.last_x, self.last_y, event.x, event.y)

        # Update the previous coordinates to be the most recent mouse click
        self.last_x, self.last_y = event.x, event.y
        return

    def clear_handler(self):
        ''' Handles the 'Clear' button by erasing all dots. '''
        self.cvs_drawing.delete('all')
        self.last_x = self.last_y = None
        return


# Create a GUI window and enter the main event loop
window = tk.Tk()
app = DotToDotApp(window)
window.mainloop()
