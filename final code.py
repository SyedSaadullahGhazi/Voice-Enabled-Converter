import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage 
from PIL import ImageTk, Image
import speech_recognition as sr
import threading


def convert_temperature():
    try:
        temp_input = float(temp_entry.get())
        if temp_var.get() == "Celsius":
            tempf = ((temp_input * 9) / 5) + 32
            tempk = temp_input + 273.15
            result_label.config(text=f"{round(tempf, 2)} Fahrenheit\n{round(tempk, 2)} Kelvin")
        elif temp_var.get() == "Fahrenheit":
            tempc = ((temp_input - 32) * 5) / 9
            tempk = ((temp_input - 32) * 5) / 9 + 273.15
            result_label.config(text=f"{round(tempc, 2)} Celsius\n{round(tempk, 2)} Kelvin")
        elif temp_var.get() == "Kelvin":
            tempf = ((temp_input - 273.15) * 9) / 5 + 32
            tempc = temp_input - 273.15
            result_label.config(text=f"{round(tempc, 2)} Celsius\n{round(tempf, 2)} Fahrenheit")
        else:
            result_label.config(text="Invalid Input!")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

def convert_weight():
    try:
        weight_input = float(weight_entry.get())
        if weight_var.get() == "Kilograms":
            g = weight_input * 1000
            lb = weight_input * 2.20462
            oz = weight_input * 35.274
            result_label.config(text=f"{round(g, 3)} grams\n{round(lb, 3)} pounds\n{round(oz, 3)} ounces")
        elif weight_var.get() == "Grams":
            kg = weight_input / 1000
            lb = weight_input / 453.6
            oz = weight_input / 28.35
            result_label.config(text=f"{round(kg, 3)} kilograms\n{round(lb, 3)} pounds\n{round(oz, 3)} ounces")
        elif weight_var.get() == "Pounds":
            kg = weight_input / 2.205
            g = weight_input * 453.6
            oz = weight_input * 16
            result_label.config(text=f"{round(kg, 3)} kilograms\n{round(g, 3)} grams\n{round(oz, 3)} ounces")
        elif weight_var.get() == "Ounces":
            kg = weight_input / 35.274
            g = weight_input * 28.35
            lb = weight_input / 16
            result_label.config(text=f"{round(kg, 3)} kilograms\n{round(g, 3)} grams\n{round(lb, 3)} pounds")
        else:
            result_label.config(text="Invalid Input!")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

def convert_length():
    try:
        length_input = float(length_entry.get())
        if length_var.get() == "Metres":
            km = length_input / 1000
            inc = length_input * 39.37
            ft = length_input * 3.281
            yd = length_input * 1.094
            mi = length_input / 1609
            result_label.config(text=f"{round(km, 3)} km\n{round(inc, 3)} inches\n{round(ft, 3)} feet\n{round(yd, 3)} yards\n{round(mi, 3)} miles")
        elif length_var.get() == "Kilometres":
            m = length_input * 1000
            inc = length_input * 39370
            ft = length_input * 3281
            yd = length_input * 1094
            mi = length_input / 1.609
            result_label.config(text=f"{round(m, 3)} metres\n{round(inc, 3)} inches\n{round(ft, 3)} feet\n{round(yd, 3)} yards\n{round(mi, 3)} miles")
        elif length_var.get() == "Inches":
            m = length_input / 39.37
            km = length_input / 39370
            ft = length_input / 12
            yd = length_input / 36
            mi = length_input / 63360
            result_label.config(text=f"{round(m, 3)} metres\n{round(km, 3)} kilometres\n{round(ft, 3)} feet\n{round(yd, 3)} yards\n{round(mi, 3)} miles")
        elif length_var.get() == "Feet":
            m = length_input / 3.281
            km = length_input / 3281
            yd = length_input / 3
            mi = length_input / 5280
            inc = length_input * 12
            result_label.config(text=f"{round(m, 3)} metres\n{round(km, 3)} kilometres\n{round(yd, 3)} yards\n{round(mi, 3)} miles\n{round(inc, 3)} inches")
        elif length_var.get() == "Yards":
            m = length_input / 1.094
            km = length_input / 1094
            mi = length_input / 1760
            inc = length_input * 36
            ft = length_input / 3
            result_label.config(text=f"{round(m, 3)} metres\n{round(km, 3)} kilometres\n{round(mi, 3)} miles\n{round(inc, 3)} inches\n{round(ft, 3)} feet")
        elif length_var.get() == "Miles":
            m = length_input * 1609
            km = length_input * 1.609
            inc = length_input * 63360
            ft = length_input * 5280
            yd = length_input * 1760
            result_label.config(text=f"{round(m, 3)} metres\n{round(km, 3)} kilometres\n{round(inc, 3)} inches\n{round(ft, 3)} feet\n{round(yd, 3)} yards")
        else:
            result_label.config(text="Invalid Input!")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

def convert_pressure():
    try:
        pressure_input = float(pressure_entry.get())
        if pressure_var.get() == "Pascal":
            bar = pressure_input / 100000
            psi = pressure_input / 6895
            stda = pressure_input / 101300
            torr = pressure_input / 133.3
            result_label.config(text=f"{round(bar, 9)} bar\n{round(psi, 9)} pound per square inch\n{round(stda, 9)} std. atmosphere\n{round(torr, 9)} torr")
        elif pressure_var.get() == "Bar":
            pascal = pressure_input * 100000
            psi = pressure_input * 14.504
            stda = pressure_input / 1.013
            torr = pressure_input * 750.1
            result_label.config(text=f"{round(pascal, 9)} pascal\n{round(psi, 9)} pound per square inch\n{round(stda, 9)} std. atmosphere\n{round(torr, 9)} torr")
        elif pressure_var.get() == "Pound per Square Inch":
            bar = pressure_input / 15.504
            pascal = pressure_input * 6895
            stda = pressure_input / 14.696
            torr = pressure_input * 51.715
            result_label.config(text=f"{round(bar, 9)} bar\n{round(pascal, 9)} pascal\n{round(stda, 9)} std. atmosphere\n{round(torr, 9)} torr")
        elif pressure_var.get() == "Std. Atmosphere":
            bar = pressure_input * 1.013
            pascal = pressure_input * 101300
            psi = pressure_input * 14.696
            torr = pressure_input * 760
            result_label.config(text=f"{round(bar, 9)} bar\n{round(pascal, 9)} pascal\n{round(psi, 9)} pound per square inch\n{round(torr, 9)} torr")
        elif pressure_var.get() == "Torr":
            bar = pressure_input / 750.1
            pascal = pressure_input * 133.3
            psi = pressure_input / 51.715
            stda = pressure_input / 760
            result_label.config(text=f"{round(bar, 9)} bar\n{round(pascal, 9)} pascal\n{round(psi, 9)} pound per square inch\n{round(stda, 9)} std. atmosphere")
        else:
            result_label.config(text="Invalid Input!")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

def convert_time():
    try:
        time_input = float(time_entry.get())
        if time_var.get() == "Hours":
            minute = time_input * 60
            sec = time_input * 3600
            ms = time_input * 3600000
            day = time_input / 24
            week = time_input / 168
            result_label.config(text=f"{round(minute, 3)} minutes\n{round(sec, 3)} seconds\n{round(ms, 3)} milliseconds\n{round(day, 3)} days\n{round(week, 3)} weeks")
        elif time_var.get() == "Minutes":
            hour = time_input / 60
            sec = time_input * 60
            ms = time_input * 60000
            day = time_input / 1440
            week = time_input / 10080
            result_label.config(text=f"{round(hour, 3)} hours\n{round(sec, 3)} seconds\n{round(ms, 3)} milliseconds\n{round(day, 3)} days\n{round(week, 3)} weeks")
        elif time_var.get() == "Seconds":
            hour = time_input / 3600
            minute = time_input / 60
            ms = time_input * 1000
            day = time_input / 86400
            week = time_input / 604800
            result_label.config(text=f"{round(hour, 3)} hours\n{round(minute, 3)} minutes\n{round(ms, 3)} milliseconds\n{round(day, 3)} days\n{round(week, 3)} weeks")
        elif time_var.get() == "Milliseconds":
            hour = time_input / 3600000
            minute = time_input / 60000
            sec = time_input / 1000
            day = time_input / 86400000
            week = time_input / 604800000
            result_label.config(text=f"{round(hour, 3)} hours\n{round(minute, 3)} minutes\n{round(sec, 3)} seconds\n{round(day, 3)} days\n{round(week, 3)} weeks")
        elif time_var.get() == "Days":
            hour = time_input * 24
            minute = time_input * 1440
            sec = time_input * 86400
            ms = time_input * 86400000
            week = time_input / 7
            result_label.config(text=f"{round(hour, 3)} hours\n{round(minute, 3)} minutes\n{round(sec, 3)} seconds\n{round(ms, 3)} milliseconds\n{round(week, 3)} weeks")
        elif time_var.get() == "Weeks":
            hour = time_input * 168
            minute = time_input * 10080
            sec = time_input * 604800
            ms = time_input * 604800000
            day = time_input * 7
            result_label.config(text=f"{round(hour, 3)} hours\n{round(minute, 3)} minutes\n{round(sec, 3)} seconds\n{round(ms, 3)} milliseconds\n{round(day, 3)} days")
        else:
            result_label.config(text="Invalid Input!")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")
# Function to handle voice command recognition
def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            result_label.config(text="Listening for command...")
            audio_data = recognizer.listen(source)
            command = recognizer.recognize_google(audio_data)
            print("Recognized Text:", command)
            process_voice_command(command)
        except sr.UnknownValueError:
            result_label.config(text="Sorry, I did not understand that.")
        except sr.RequestError:
            result_label.config(text="Could not request results; check your network connection.")

# Function to process recognized voice commands
def process_voice_command(command):
    command = command.lower()
    try:
        if "convert temperature" in command:
            temp_entry.delete(0, tk.END)
            temp_value = extract_value(command)
            if temp_value:
                temp_entry.insert(0, temp_value)
            if "celsius" in command:
                temp_var.set("Celsius")
            elif "fahrenheit" in command:
                temp_var.set("Fahrenheit")
            elif "kelvin" in command:
                temp_var.set("Kelvin")
            convert_temperature()
        
        elif "convert weight" in command:
            weight_entry.delete(0, tk.END)
            weight_value = extract_value(command)
            if weight_value:
                weight_entry.insert(0, weight_value)
            if "kg" in command:
                weight_var.set("Kilograms")
            elif "Grams" in command:
                weight_var.set("Grams")
            elif "pounds" in command:
                weight_var.set("Pounds")
            elif "ounces" in command:
                weight_var.set("Ounces")
            convert_weight()
        
        elif "convert length" in command:
            length_entry.delete(0, tk.END)
            length_value = extract_value(command)
            if length_value:
                length_entry.insert(0, length_value)
            if "meters" in command:
                length_var.set("Metres")
            elif "km" in command:
                length_var.set("Kilometres")
            elif "inches" in command:
                length_var.set("Inches")
            elif "feet" in command:
                length_var.set("Feet")
            elif "yards" in command:
                length_var.set("Yards")
            elif "miles" in command:
                length_var.set("Miles")
            convert_length()

        elif "convert pressure" in command:
            pressure_entry.delete(0, tk.END)
            pressure_value = extract_value(command)
            if pressure_value:
                pressure_entry.insert(0, pressure_value)
            if "pascal" in command:
                pressure_var.set("Pascal")
            elif "bar" in command:
                pressure_var.set("Bar")
            elif "psi" in command:
                pressure_var.set("Pound per Square Inch")
            elif "standard atmosphere" in command:
                pressure_var.set("Std. Atmosphere")
            elif "torr" in command:
                pressure_var.set("Torr")
            convert_pressure()

        elif "convert time" in command:
            time_entry.delete(0, tk.END)
            time_value = extract_value(command)
            if time_value:
                time_entry.insert(0, time_value)
            if "hours" in command:
                time_var.set("Hours")
            elif "minutes" in command:
                time_var.set("Minutes")
            elif "seconds" in command:
                time_var.set("Seconds")
            elif "milliseconds" in command:
                time_var.set("Milliseconds")
            elif "days" in command:
                time_var.set("Days")
            elif "weeks" in command:
                time_var.set("Weeks")
            convert_time()
        
        else:
            result_label.config(text="Unknown command: " + command)
    
    except ValueError:
        messagebox.showerror("Invalid command", "Please speak a valid number and unit")

# Function to extract numeric value from the command string
def extract_value(command):
    words = command.split()
    for word in words:
        try:
            return float(word)
        except ValueError:
            continue
    return None


root = tk.Tk()
root.title("Voice Enabled Converter")
root.geometry("500x600")
bg_image = PhotoImage(file =r"C:\Users\syeds\Desktop\python project\bg.png")
my_label = tk.Label(root , image = bg_image)
my_label.place( relheight= 1, relwidth = 1)
root.resizable(False, False)
root.configure(bg="LightSteelBlue4")

down_png = ImageTk.PhotoImage(Image.open('down-4.png'))
mic_png = ImageTk.PhotoImage(Image.open('mic_png.png'))


style = ttk.Style()
style.configure('TFrame', background = "Blue" )
style.configure('TLabel', foreground="white" , font = ("David" , 10))
style.configure('TButton', background = "white" ,
                           font = ("David" , 9),
                           foreground = "Olive",
                           activebackground = "Lightgreen",
                           activeforeground = "Lightblue",
                           highlightbackground = "snow3",
                           height = 10,
                           width = 12,
                           border = 2.5,
                           corner_radius = 5,
                           cursor = 'hand1',
                           highcolour = "white"
                           )
style.configure('TEntry', background="Blue" , font = ("David" , 10))


notebook = ttk.Notebook(root )
notebook.pack ( pady=10, expand=True  )

frame_temp = ttk.Frame(notebook, padding=(20, 20, 20, 20))
frame_weight = ttk.Frame(notebook, padding=(20, 20, 20, 20))
frame_length = ttk.Frame(notebook, padding=(20, 20, 20, 20))
frame_pressure = ttk.Frame(notebook, padding=(20, 20, 20, 20))
frame_time = ttk.Frame(notebook, padding=(20, 20, 20, 20))

notebook.add(frame_temp, text='Temperature' )
notebook.add(frame_weight, text='Weight')
notebook.add(frame_length, text='Length')
notebook.add(frame_pressure, text='Pressure')
notebook.add(frame_time, text='Time')



# Temperature Conversion
temp_var = tk.StringVar(value="Celsius")
temp_label = ttk.Label(frame_temp, text="Enter temperature:"  , foreground=  "DodgerBlue4" , background="snow3" , font = ("Bookman Old Style" , 10))
temp_label.pack(pady=5)
temp_entry = tk.Entry(frame_temp , width=18 , borderwidth = 4 )
temp_entry.pack(pady = 5 )
temp_options = ["Celsius", "Fahrenheit", "Kelvin"]
temp_dropdown = tk.OptionMenu(frame_temp, temp_var, *temp_options)
temp_dropdown.config(bg = "dodger blue",
                     fg = "black",
                     activebackground = "deep sky blue",
                     activeforeground= "black",
                     font = ("Helvetica" , 10),
                     border = 1,
                     highlightthickness= 1,
                     highlightbackground= "sky blue",
                     pady= 6,
                     indicatoron= 0,
                     image= down_png,
                     compound=tk.RIGHT
)
temp_dropdown['menu'].config(
    bg = "dodger blue",
    fg = "black",
    activebackground= "deep sky blue",
    activeforeground = "maroon",
    font = ("Helvetica", 10),
    border = 0,
    activeborder = 5
)
temp_dropdown.pack(pady=5 )
temp_convert_button =ttk.Button(frame_temp, text = "convert", command = convert_temperature)
temp_convert_button.pack(pady=5)
temp_voice_button = tk.Button(frame_temp, text="Voice Command", 
                              command=recognize_voice,
                              background = "white" ,
                              font = ("David" , 9),
                              foreground = "Olive",
                              activebackground = "Lightgreen",
                              activeforeground = "Lightblue",
                              highlightbackground = "snow3",
                              height = 30,
                              width = 20,
                              border = 2.5,
                              cursor = 'hand1',
                              image = mic_png
                              )
temp_voice_button.pack(pady=10)

# Weight Conversion
weight_var = tk.StringVar(value="Kilograms")
weight_label = ttk.Label(frame_weight, text="Enter weight:"  , foreground=  "DodgerBlue4" , background="snow3" , font = ("Bookman Old Style" , 10))
weight_label.pack(pady=5)
weight_entry = tk.Entry(frame_weight , width=18 , borderwidth = 4)
weight_entry.pack(pady=5)
weight_options = ["Kilograms", "Grams", "Pounds", "Ounces"]
weight_dropdown = tk.OptionMenu(frame_weight, weight_var, *weight_options)
weight_dropdown.config(bg = "dodger blue",
                     fg = "black",
                     activebackground = "deep sky blue",
                     activeforeground= "black",
                     font = ("Helvetica" , 10),
                     border = 1,
                     highlightthickness= 1,
                     highlightbackground= "sky blue",
                     pady= 6,
                     indicatoron= 0,
                     image= down_png,
                     compound=tk.RIGHT
                     )
weight_dropdown['menu'].config(bg = "dodger blue",
    fg = "black",
    activebackground= "deep sky blue",
    activeforeground = "maroon",
    font = ("Helvetica", 10),
    border = 0
    )
weight_dropdown.pack(pady=5)
weight_convert_button = ttk.Button(frame_weight, text="Convert", command=convert_weight)
weight_convert_button.pack(pady=5)
weight_voice_button = tk.Button(frame_weight, text="Voice Command", command=recognize_voice ,
                                background = "white" ,
                              font = ("David" , 9),
                              foreground = "Olive",
                              activebackground = "Lightgreen",
                              activeforeground = "Lightblue",
                              highlightbackground = "snow3",
                              height = 30,
                              width = 20,
                              border = 2.5,
                              cursor = 'hand1',
                              image = mic_png)
weight_voice_button.pack(pady=10)
# Length Conversion
length_var = tk.StringVar(value="Metres")
length_label = ttk.Label(frame_length, text="Enter length:"  , foreground=  "DodgerBlue4" , background="snow3" , font = ("Bookman Old Style" , 10))
length_label.pack(pady=6)
length_entry = tk.Entry(frame_length , width=18 , borderwidth = 4)
length_entry.pack(pady=5)
length_options = ["Metres", "Kilometres", "Inches", "Feet", "Yards", "Miles" ]
length_dropdown = tk.OptionMenu(frame_length, length_var, *length_options)
length_dropdown.config(bg = "dodger blue",
                     fg = "black",
                     activebackground = "deep sky blue",
                     activeforeground= "black",
                     font = ("Helvetica" , 10),
                     border = 1,
                     highlightthickness= 1,
                     highlightbackground= "sky blue",
                     pady= 6,
                     indicatoron= 0,
                     image= down_png,
                     compound=tk.RIGHT
                     )
length_dropdown['menu'].config(bg = "dodger blue",
    fg = "black",
    activebackground= "deep sky blue",
    activeforeground = "maroon",
    font = ("Helvetica", 10),
    border = 0
    )
length_dropdown.pack(pady=5 )
length_convert_button = ttk.Button(frame_length, text="Convert", command=convert_length)
length_convert_button.pack(pady=5)
length_voice_button = tk.Button(frame_length, text="Voice Command", command= recognize_voice,
                                background = "white" ,
                              font = ("David" , 9),
                              foreground = "Olive",
                              activebackground = "Lightgreen",
                              activeforeground = "Lightblue",
                              highlightbackground = "snow3",
                              height = 30,
                              width = 20,
                              border = 2.5,
                              cursor = 'hand1',
                              image = mic_png)
length_voice_button.pack(pady=10)
# Pressure Conversion
pressure_var = tk.StringVar(value="Pascal")
pressure_label = ttk.Label(frame_pressure, text="Enter pressure:"  , foreground=  "DodgerBlue4" , background="snow3" , font = ("Bookman Old Style" , 10))
pressure_label.pack(pady=8)
pressure_entry = tk.Entry(frame_pressure , width=18 , borderwidth = 4)
pressure_entry.pack(pady=5)
pressure_options = ["Pascal", "Bar", "Pound per Square Inch", "Std. Atmosphere", "Torr"]
pressure_dropdown = tk.OptionMenu(frame_pressure, pressure_var, *pressure_options)
pressure_dropdown.config(bg = "dodger blue",
                     fg = "black",
                     activebackground = "deep sky blue",
                     activeforeground= "black",
                     font = ("Helvetica" , 10),
                     border = 1,
                     highlightthickness= 1,
                     highlightbackground= "sky blue",
                     pady= 6,
                     indicatoron= 0,
                     image= down_png,
                     compound=tk.RIGHT
                     )
pressure_dropdown['menu'].config(
    bg = "dodger blue",
    fg = "black",
    activebackground= "deep sky blue",
    activeforeground = "maroon",
    font = ("Helvetica", 10),
    border = 0
)
pressure_dropdown.pack(pady=5)
pressure_convert_button = ttk.Button(frame_pressure, text="Convert", command=convert_pressure)
pressure_convert_button.pack(pady=5)
pressure_voice_button = tk.Button(frame_pressure, text="Voice Command", command= recognize_voice,
                                  background = "white" ,
                              font = ("David" , 9),
                              foreground = "Olive",
                              activebackground = "Lightgreen",
                              activeforeground = "Lightblue",
                              highlightbackground = "snow3",
                              height = 30,
                              width = 20,
                              border = 2.5,
                              cursor = 'hand1',
                              image = mic_png)
pressure_voice_button.pack(pady=10)
# Time Conversion
time_var = tk.StringVar(value="Hours")
time_label = ttk.Label(frame_time, text="Enter time:"  , foreground=  "DodgerBlue4" , background="snow3" , font = ("Bookman Old Style" , 10))
time_label.pack(pady=8)
time_entry = tk.Entry(frame_time , width=18 , borderwidth = 4)
time_entry.pack(pady=5)
time_options = ["Hours", "Minutes", "Seconds", "Milliseconds", "Days", "Weeks"]
time_dropdown = tk.OptionMenu(frame_time, time_var, *time_options)
time_dropdown.config(bg = "dodger blue",
                     fg = "black",
                     activebackground = "deep sky blue",
                     activeforeground= "black",
                     font = ("Helvetica" , 10),
                     border = 1,
                     highlightthickness= 1,
                     highlightbackground= "sky blue",
                     pady= 6,
                     indicatoron= 0,
                     image= down_png,
                     compound=tk.RIGHT
                     )
time_dropdown['menu'].config(bg = "dodger blue",
    fg = "black",
    activebackground= "deep sky blue",
    activeforeground = "maroon",
    font = ("Helvetica", 10),
    border = 0
    )
time_dropdown.pack(pady=5)
time_convert_button = ttk.Button(frame_time, text="Convert", command=convert_time)
time_convert_button.pack(pady=5)
time_voice_button = tk.Button(frame_time, text="Voice Command", command=recognize_voice,
                              background = "white" ,
                              font = ("David" , 9),
                              foreground = "Olive",
                              activebackground = "Lightgreen",
                              activeforeground = "Lightblue",
                              highlightbackground = "snow3",
                              height = 30,
                              width = 20,
                              border = 2.5,
                              cursor = 'hand1',
                              image = mic_png)
time_voice_button.pack(pady=10)

# Result Label
result_label = ttk.Label(root, text="Conversion result will be shown here", foreground= "black", font=("Consolas", 12))
result_label.pack(pady=20)



root.mainloop()
