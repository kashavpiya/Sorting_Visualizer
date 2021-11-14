from tkinter import *
from tkinter import ttk
import random
from colors import *
from algorithms.bubbleSort import bubbleSort
from algorithms.mergeSort import mergeSort

#Creating a window from the entire program
window = Tk()
window.title("Kashav and Quinn's Sorting Algorithm Visualizer")
window.maxsize(1000, 700)
window.config(bg = WHITE)

algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Merge Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

data = []


#This function is used to draw 'data' which will be filled with random values
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

#This function will generate random values to be put into data everytime it is required
def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])

#This function will set the speed of the visualization for sorting
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

#This function will choose the selected algorithm and start sorting
def sort():
    global data

    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        bubbleSort(data, drawData, timeTick)

    elif algo_menu.get() == 'Merge Sort':
        mergeSort(data, 0, len(data)-1, drawData, timeTick)
        
    

UI_frame = Frame(window, width = 900, height = 300, bg = WHITE)
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

l1 = Label(UI_frame, text = "Algorithm: ", bg=WHITE)
l1.grid(row = 0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row = 0, column = 1, padx = 5, pady = 5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row = 1, column= 0, padx = 10, pady =5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values = speed_list)
speed_menu.grid(row=1, column = 1, padx = 5, pady = 5)
speed_menu.current(0)

b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GREY)
b1.grid(row = 2, column = 1, padx = 5, pady = 5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GREY)
b3.grid(row = 2, column = 0, padx = 5, pady = 5)

canvas = Canvas(window, width =800, height = 400, bg = WHITE)
canvas.grid(row = 1, column=0, padx = 10, pady = 5)



window.mainloop()
