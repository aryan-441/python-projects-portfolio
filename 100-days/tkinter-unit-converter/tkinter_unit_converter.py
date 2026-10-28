from tkinter import *

def calculate():
    mode = conversion_mode.get()
    if not user_input.get():
        result_value.config(text='0')
        return
    try:
        value = float(user_input.get())

        if mode == "Miles to Km":
            km = round(value * 1.60934,2)
            result_value.config(text=f"{km}")
        else:
            miles = round(value / 1.60934, 2)
            result_value.config(text=f'{miles}')
    except ValueError:
        result_value.config(text='Error')
  
    
window = Tk()
window.title('Miles to  Kilometre Converter')
window.config(padx=35,pady=35)
user_input = Entry(width=7)
user_input.grid(column=1,row=0)

modes = ['Miles to Km', 'Km to Miles']
conversion_mode = StringVar(window)
conversion_mode.set(modes[0])

def update_labels(*args): #tkinter will crash without args fsr
    if conversion_mode.get() == 'Miles to Km':
        input_label.config(text='miles')
        result_label.config(text='km')
    else:
        input_label.config(text='km')
        result_label.config(text='miles')
    result_value.config(text='0')



conversion_mode.trace_add("write", update_labels)

dropdown = OptionMenu(window, conversion_mode, *modes) #modes has astrix for unpacking
dropdown.grid(column=1, row=2, pady=10)

input_label = Label(text='Miles')
input_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

result_value = Label(text='0')
result_value.grid(column=1, row=1)

result_label = Label(text='km')
result_label.grid(column=2, row=1)

calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(column=1, row=3)

window.mainloop()