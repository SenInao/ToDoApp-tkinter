from data_handling import Database
import tkinter as tk
from tkinter import ttk

def draw_ToDos(page):
    db.todo_list = db.todo_list
    page = page.get()
    startval = len(db.todo_list[:3*(page-1)])
    endval = len(db.todo_list[:3*(page)])

    for i in range(startval,endval,1):
        if db.todo_list[i][3] == 1:
            color = "green"
        else:
            color = "black"

        ToDo_frame = ttk.Frame(window)

        title_todo = ttk.Label(ToDo_frame, text=db.todo_list[i][1], font="calibri 15 bold", foreground=color)
        title_todo.pack(expand=True, fill="x")

        content = ttk.Label(ToDo_frame, text=db.todo_list[i][2], font="calibri 10 bold", foreground=color)
        content.pack(expand=True, fill="x")

        check_off_button = ttk.Button(ToDo_frame, text="Check off", command=lambda i=i:check_off(db.todo_list[i]))
        check_off_button.pack()

        ToDo_frame.pack(expand=True, fill="x")

def draw_title():
    title_frame = ttk.Frame(window)
    title_label = ttk.Label(title_frame, text="Things To Do", font="calibri 24 bold")
    page_label = ttk.Label(title_frame, textvariable=page, font="calibri 9 bold")
    page_text_label = ttk.Label(title_frame, text="page: ", font="calibri 9 bold")

    title_label.pack()
    page_text_label.pack(side="left")
    page_label.pack(side="left")
    title_frame.pack()

def draw_scroll():
    scroll_panel = ttk.Frame(window)

    back = ttk.Button(scroll_panel, text="<--", command=previousPage)
    back.pack(side="left")

    forward = ttk.Button(scroll_panel, text="-->", command=nextPage)
    forward.pack(side="left")

    scroll_panel.pack()

def draw_actions():
    actions_panel = ttk.Frame(window)

    add = ttk.Button(actions_panel, text="Add", command=lambda:refresh("add"))
    add.pack(side="left")

    remove = ttk.Button(actions_panel, text="Remove", command=lambda:refresh("remove"))
    remove.pack(side="left")

    modify = ttk.Button(actions_panel, text="Modify", command=lambda:refresh("modify"))
    modify.pack(side="left")

    actions_panel.pack()

def draw_add():
    add_panel = ttk.Frame(window)

    title_todo = ttk.Label(add_panel, text="Title", font="calibri 14 bold")
    title_todo.pack()

    title_input = ttk.Entry(add_panel)
    title_input.pack()

    content = ttk.Label(add_panel, text="Content", font="calibri 14 bold")
    content.pack()

    content_input = tk.Text(add_panel,height=10, width=30 )
    content_input.pack()

    add_button = ttk.Button(add_panel, text="Add", command=lambda:add_button_press(title_input.get(), content_input.get("1.0",'end-1c')))
    add_button.pack()

    back = ttk.Button(add_panel, text="Back", command=lambda:refresh("home"))
    back.pack()

    add_panel.pack()

def draw_modify():
    modify_panel = ttk.Frame(window)

    title_todo1 = ttk.Label(modify_panel, text="Title", font="calibri 14 bold")
    title_todo1.pack()

    title1_input = ttk.Entry(modify_panel)
    title1_input.pack()

    title_todo = ttk.Label(modify_panel, text="New Title", font="calibri 14 bold")
    title_todo.pack()

    title_input = ttk.Entry(modify_panel)
    title_input.pack()

    content = ttk.Label(modify_panel, text="New Content", font="calibri 14 bold")
    content.pack()

    content_input = tk.Text(modify_panel,height=5, width=30 )
    content_input.pack()

    modify_button = ttk.Button(modify_panel, text="Modify", command=lambda:modify_button_press(title1_input.get(),title_input.get(),content_input.get("1.0",'end-1c')))
    modify_button.pack()

    back = ttk.Button(modify_panel, text="Back", command=lambda:refresh("home"))
    back.pack()

    modify_panel.pack()


def draw_remove():
    remove_panel = ttk.Frame(window)

    title_todo = ttk.Label(remove_panel, text="Title", font="calibri 14 bold")
    title_todo.pack()

    title_input = ttk.Entry(remove_panel)
    title_input.pack()

    remove_button = ttk.Button(remove_panel, text="Remove", command=lambda:remove_button_press(title_input.get()))
    remove_button.pack()

    back = ttk.Button(remove_panel, text="Back", command=lambda:refresh("home"))
    back.pack()

    remove_panel.pack()

def check_off(item):
    itembool = item[3]
    if itembool == 1:
        itembool = 0
    else:
        itembool = 1

    db.modifyToDo(item[0], item[1], item[2], itembool)
    refresh("home")

def refresh(panel):
    for child in window.winfo_children():
        child.destroy()

    draw_title()

    if panel == "home":
        draw_ToDos(page)
        draw_scroll()
        draw_actions()
    elif panel == "add":
        draw_add()
    elif panel == "remove":
        draw_remove()
    elif panel == "modify":
        draw_modify()

def modify_button_press(id, title_input, content_input):
    for item in db.todo_list:
        if item[1] == id:
            id = item[0]
            db.modifyToDo(id, title_input,content_input, 0)
            refresh("home")

def add_button_press(title_input, content_input):
    db.addToDo(title_input,content_input)
    refresh("home")

def remove_button_press(title):
    for item in db.todo_list:
        if item[1] == title:
            db.deleteToDo(item[0])
            refresh("home")
            break

def nextPage():
    page.set(page.get()+1)

    refresh("home")

def previousPage():
    if page.get() == 1:
        return
    page.set(page.get()-1)
    refresh("home")

WIDTH = 300
HEIGHT = 425

db = Database.get()

window = tk.Tk()
window.title("ToDo")
window.geometry(f"{WIDTH}x{HEIGHT}")

page = tk.IntVar(window, 1)

refresh("home")

window.mainloop()
db.close()
