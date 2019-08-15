import sys
import tkinter as tk

root = tk.Tk()
root.title("8 Queen!!")
root.geometry("300x400")

canvas = tk.Canvas(root, width = 300, height = 300, bg = "white")
canvas.place(x=0, y=0)
i=0
while i <260:
    i = i+37.5
    canvas.create_line(3,i,299,i,width=1)
    canvas.create_line(i,3,i,299)
    # canvas.pack()
# canvas.create_line(0,37.5,300,37.5)
# canvas.pack()

cnt=0
def click(event):
    global cnt
    cnt=cnt+1
    canvas.create_text(event.x,event.y, text="Q", font = ("",15))
    if cnt>=8:
        msg = tk.Message(root, text = "8つのクイーンを置きました！おめでとう！")
        msg.place(x=105,y=325)

canvas.bind("<Button-1>",click)



root.mainloop()
