import tkinter as tk

root = tk.Tk()
root.title('Ok')
root.geometry('800x600')

results = tk.Label(root,text='Results will be here')
results.pack(padx=10,pady=10)

inputArea = tk.Entry(root)
inputArea.pack(padx=10,pady=10)

errors = tk.Label(root,text='Errors will be here')
errors.pack(side='left',padx=10,pady=10)

root.mainloop()

def gameLogic():
    hi