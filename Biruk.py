from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import random 

def countFreq(arr):   
    mp = dict()
    for i in range(len(arr)):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    return mp
        
        
def task(min_n, max_n, n):
    #generate array
    arr =[]
    for i in range(int(n)):
        arr.append(random.randint(int(min_n), int(max_n)))
    #plot array
    plt.plot(arr)    
    plt.show()
    
    arr.sort()
    mp = countFreq(arr)
    
    #
    table = Frame(window)
    table.grid(column=1, row=7, sticky='w')
    canvas = Canvas(table, width=170)
    scrollbar = Scrollbar(table, orient=VERTICAL, command=canvas.yview)
    scrollable_frame = Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="w")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.grid(row=7, column=1, sticky="w")
    scrollbar.grid(row=7, column=1, sticky="nse")

    table.grid_rowconfigure(0, weight=1)
    table.grid_columnconfigure(0, weight=1)
    #table title
    Label(scrollable_frame, text="Cislo", borderwidth=2, relief="solid", width=10, bg="lightgray").grid(row=0, column=1, sticky="nsew")
    Label(scrollable_frame, text="Frekvencia", borderwidth=2, relief="solid", width=10, bg="lightgray").grid(row=0, column=2, sticky="nsew")
    #inserting content into table
    for i, (key, value) in enumerate(mp.items(), start=1):
        Label(scrollable_frame, text=str(key), borderwidth=1, relief="solid", width=10).grid(row=i, column=1, sticky="nsew")
        Label(scrollable_frame, text=str(value), borderwidth=1, relief="solid", width=10).grid(row=i, column=2, sticky="nsew")


window = Tk() 
window.title('Zadanie #1') 
window.geometry("500x500") 

img = Image.open("kpii.jpg")
image = img.resize((500,98))
image = ImageTk.PhotoImage(image)
panel = Label(window, image=image)
panel.image = image
panel.grid(column=1, row=0, columnspan = 7, sticky=W+E)

m_label=Label(text="Programovacie techniky")
m_label.grid(column=3, row=1, sticky='w')

meno = Label(text="Uladzislau Biruk")
meno.grid(column=3, row=2, sticky='w')

hint_min=Label(text="Dajte minimum: ")
hint_min.grid(column=1, row=3, sticky='w')
min_n=Entry(validate='all', width=10) 
min_n.grid(column=2, row=3, sticky='w')

hint_max=Label(text="Dajte maximum: ")
hint_max.grid(column=1, row=4, sticky='w')
max_n=Entry(validate='all', width=10) 
max_n.grid(column=2, row=4, sticky='w')

hint_n=Label(text="Dajte mnozstvo cisel: ")
hint_n.grid(column=1, row=5, sticky='w')
n=Entry(validate='all', width=10) 
n.grid(column=2, row=5, sticky='w')

plot_button = Button(text = "Start",
                    command = lambda : task(min_n.get(), max_n.get(), n.get())) 
plot_button.grid(column=2, row=6, sticky='w')
window.mainloop()
