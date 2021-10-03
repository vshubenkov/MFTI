import tkinter as tk
import time

'''Константы'''
WIDTH = 800
HIGHT = 600

root = tk.Tk()
fr = tk.Frame(root)
root.geometry(str(WIDTH) + 'x' + str(HIGHT))
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
button_state = 0

def motion_move(event):
    print(event.x)

def press_button(event):
    global button_state
    button_state = 1
    index = 0
    while button_state:
        canv.update()
        index += 1
        print('press_button=', button_state, 'Время ожидание событие release_button=', index )
        time.sleep(1)

def release_button(event):
    global button_state
    button_state = 0
    print('release_button=', button_state)

canv.bind('<Motion>', motion_move)
canv.bind('<Button-1>', press_button)
canv.bind('<ButtonRelease-1>', release_button)

tk.mainloop()