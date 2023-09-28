import tkinter as tk


 
def convert_weight():
    try:
 
        input_weight = float(entry_weight.get())
        
       
        selected_unit = unit_choice.get()
        if selected_unit == "Kilograms to Pounds":
            converted_weight = input_weight * 2.20462
        elif selected_unit == "Pounds to Kilograms":
            converted_weight = input_weight / 2.20462
        elif selected_unit == "Grams to Ounces":
            converted_weight = input_weight * 0.035274
        elif selected_unit == "Ounces to Grams":
            converted_weight = input_weight / 0.035274
        elif selected_unit == "Tonnes to Kilograms":
            converted_weight = input_weight / 2000
        elif selected_unit == "Kilograms to Tonnes":
            converted_weight = input_weight / 2000
                        
                    
        else:
            converted_weight = input_weight
        
 
        result_label.config(text=f"Converted Weight: {converted_weight:.2f} {selected_unit.split(' to ')[1]}")
    except ValueError:
        result_label.config(text="Please enter a valid number!")


window = tk.Tk()
window.title("Weight Converter")
window.geometry("400x500")
#window.configure(bg = "grey")
window.resizable(False, False)





label = tk.Label(window, text="Enter Weight:")
label.pack()


entry_weight = tk.Entry(window)
entry_weight.pack()

unit_choice = tk.StringVar()
unit_choice.set("Kilograms to Pounds")

unit_menu = tk.OptionMenu(window, unit_choice, "Kilograms to Pounds", "Pounds to Kilograms", "Grams to Ounces", "Ounces to Grams", "Tonnes to Kilograms", "Kilograms to Tonnes" )
unit_menu.pack()

convert_button = tk.Button(window, text="Convert", activeforeground= "", command=convert_weight)
convert_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()


