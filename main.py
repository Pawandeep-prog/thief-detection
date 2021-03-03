import tkinter as tk
import tkinter.font as font
from find_motion import find_motion


window =  tk.Tk()
window.title = "find stolen"
window.geometry("450x200")


#label
label = tk.Label(window, text="Welcome")
label.grid(row=0, column=1)
label['font'] = font.Font(size=35, weight='bold',family='Helvetica')

#button font
btn_font = font.Font(size=15, weight='bold',family='Helvetica')

#button main
button1 = tk.Button(window, text="spot diff",fg="green", height=3, width=10, command=find_motion)
button1['font'] = btn_font
button1.grid(row=1, pady=(25,10),padx=(10,0), column = 0)


#exit button
button2 = tk.Button(window, text="exit",fg="red", height=3, width=10, command=window.quit)
button2['font'] = btn_font
button2.grid(row=1, pady=(25,10), column=2)


#footer
label2 = tk.Label(window, text="thanks for using")
label2.grid(row=2, columnspan = 3)
label2['font'] = font.Font(size=20, weight='bold',family='Helvetica')


window.mainloop()

