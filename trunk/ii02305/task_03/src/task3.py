from tkinter import Tk, Canvas, Button, Label, Entry, Checkbutton, BooleanVar
from tkinter import messagebox as mb
import numpy as np

FONT_CONSTANT = 'Arial'
BUTTON_CONSTANT = "<Button-1>"
TITLE_STR_NAME = "Задайте имя графа"
ERROR_STR_CONSTANT = "Ошибка"
SHOW_ERR_CONSTANT = "Вы ввели неверное имя вершины"
SIZE_CONSTANT = "400x400+0+0"
STR_LABEL_CONSTANT = "text"
tk = Tk()
tk.title("Graph")
tk.geometry("890x860+410+10")
tk.resizable(False, False)
tk.wm_attributes('-topmost', 1)

canvas = Canvas(tk, bg="#888", width=886, height=726)
canvas.place(x=0, y=130)

label = Label(tk)
label.place(x=370, y=100)
label[STR_LABEL_CONSTANT] = "Имя графа"

class Vertex:
    def init(self, canvas, color, name):
        self.vertex_count = vertex_count
        self.vert_name = name
        self.canvas = canvas
        self.color = color
        self.x = x_click
        self.y = y_click
        self.rename()
        self.id_vert = canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill=color, width=2)
        self.id_txt = self.canvas.create_text(self.x, self.y, anchor='center', text=self.vert_name,
                                              font=(FONT_CONSTANT, 10), fill="white")
        canvas.unbind(BUTTON_CONSTANT)

    def rename(self, new_name):
        self.vert_name = new_name
        self.canvas.itemconfigure(self.id_txt, text=new_name)

    def get_info(self):
        return self.vertex_count, self.vert_name[self.vertex_count - 1]

class Edge:
    def __init__(self, vertex1: Vertex, vertex2: Vertex, weight: int = 0):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.x1, self.y1 = vertex1.x, vertex1.y
        self.x2, self.y2 = vertex2.x, vertex2.y
        self.weight = weight
        self.create_edge()

    def create_edge(self):
        self.line = canvas.create_line(line_intersect_circle(self.x1, self.y1, self.x2, self.y2), width=2,
                                       arrow="last" if var1.get() else None)
        if self.weight != 0:
            self.rect = canvas.create_rectangle((self.x1 + self.x2) / 2 - 5,
                                                (self.y1 + self.y2) / 2 - 8,
                                                (self.x1 + self.x2) / 2 + 5,
                                                (self.y1 + self.y2) / 2 + 8,
                                                fill='white', width=0)
            self.text = canvas.create_text((self.x1 + self.x2) / 2,
                                           (self.y1 + self.y2) / 2,
                                           text=self.weight,
                                           font=(FONT_CONSTANT, 14), fill='black', )
        else:
            self.rect = None
            self.text = None

    def delete(self):
        canvas.delete(self.line)
        canvas.delete(self.rect)
        canvas.delete(self.text)

def on_wasd(event):
    x_click = event.x
    y_click = event.y

def create_matrix(matrix_type):
    matrix = [[0 for _ in range(len(edges))] for _ in range(len(vert_name))]
    for i in range(len(edges)):
        matrix[vert_name.index(edges[i].vertex1.vert_name)][i] = 1
        matrix[vert_name.index(edges[i].vertex2.vert_name)][i] = 1
    window = Tk()
    window.title(f"Матрица {matrix_type}")
    window.geometry(SIZE_CONSTANT)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            Label(window, text=matrix[i][j], font=(FONT_CONSTANT, 10), width=5, height=2, borderwidth=1, relief="solid").grid(
                row=i, column=j)
    window.mainloop()

def create_matrix_adjacency():
    create_matrix("смежности")

def create_matrix_incidence_window():
    create_matrix("инцидентности")

def quitfunc(root):
    root.destroy()

def change_graf_name(name, root):
    label[STR_LABEL_CONSTANT] = name
    quitfunc(root)

def graf_name():
    new_window = Tk()
    new_window.title(TITLE_STR_NAME)
    new_window.wm_attributes('-topmost', 1)
    new_window.resizable(False, False)
    labelgraph = Label(new_window)
    labelgraph[STR_LABEL_CONSTANT] = "Введите имя графа"
    labelgraph.grid(row=0, column=0, sticky="ew")
    entry = Entry(new_window)
    entry.grid(row=1, column=0)
    btngraf = Button(new_window, text="Ввод", command=lambda: change_graf_name(entry.get(), new_window))
    btngraf.grid(row=2, column=0, sticky="ew")
    if entry.get == label[STR_LABEL_CONSTANT]:
        new_window.destroy()
    new_window.mainloop()

def move_vertex2():
    canvas.bind(BUTTON_CONSTANT, select_vertex)

def select_vertex(event):
    x_click = event.x
    y_click = event.y
    for vert in vertex:
        if vert.x - 20 <= x_click <= vert.x + 20 and vert.y - 20 <= y_click <= vert.y + 20:
            sel_vert = vert
            canvas.bind("<B1-Motion>", move_vertex)
            canvas.bind("<ButtonRelease-1>", unselect_vertex)
            print(sel_vert.vert_name, x_click, y_click)
            break
def move_vertex(event):
    x_click = event.x
    y_click = event.y
    sel_vert.x = x_click
    sel_vert.y = y_click
    canvas.coords(sel_vert.id_vert, x_click - 20, y_click - 20, x_click + 20, y_click + 20)
    canvas.coords(sel_vert.id_txt, x_click, y_click)
    for edge in edges:
        if edge.vertex1 == sel_vert or edge.vertex2 == sel_vert:
            x1, y1 = (edge.vertex2.x, edge.vertex2.y) if edge.vertex1 == sel_vert else (edge.vertex1.x, edge.vertex1.y)
            canvas.coords(edge.line, line_intersect_circle(x_click, y_click, x1, y1))
            canvas.coords(edge.rect, (x_click + x1) / 2 - 5,
                          (y_click + y1) / 2 - 8,
                          (x_click + x1) / 2 + 5,
                          (y_click + y1) / 2 + 8)
            canvas.coords(edge.text, (x_click + x1) / 2, (y_click + y1) / 2)

def unselect_vertex(event):
    canvas.unbind("<B1-Motion>")
    canvas.unbind("<ButtonRelease-1>")

def save_data():
    #эта функция сохраняет значения вершин, ребер и весов графа
    pass

def give_color(numb):
    global color
    colors = ["blue", "red", "green", "white"]
    color = colors[numb-1] if numb <= 4 else "white"

call_count = 0

def menu_create_vetrex():
    call_count = 0
    canvas.bind(BUTTON_CONSTANT, on_wasd)
    vert_name.append("")
    new_window = Tk()
    new_window.geometry("230x100+0+0")
    new_window.wm_attributes('-topmost', 1)
    new_window.resizable(False, False)
    label = Label(new_window)
    label[STR_LABEL_CONSTANT] = "Введите имя вершины"
    entry = Entry(new_window)
    btncolor1 = Button(new_window, text="Синий", command=lambda: give_color(1), bg="blue")
    btncolor2 = Button(new_window, text="Красный", command=lambda: give_color(2), bg="red")
    btncolor3 = Button(new_window, text="Зелёный", command=lambda: give_color(3), bg="green")
    btncreate = Button(new_window, text="Создать\nвершину", command=lambda: create_vertex(new_window, entry))
    label.grid(row=0, column=0, sticky="ew")
    entry.grid(row=1, column=0, sticky="ewns")
    btncolor1.grid(row=0, column=1, sticky="ew")
    btncolor2.grid(row=1, column=1, sticky="ew")
    btncolor3.grid(row=2, column=1, sticky="ewn")
    btncreate.grid(row=2, column=0, sticky="ew")
    new_window.mainloop()
def find_delete_vertex(entry, root):
    vertex_count -= 1
    flag = 1
    while flag:
        for j, edge in enumerate(edges):
            if edge.vertex1.vert_name == entry or edge.vertex2.vert_name == entry:
                canvas.delete(edge.line)
                canvas.delete(edge.text)
                canvas.delete(edge.rect)
                edges.pop(j)
                edge_count -= 1
        for i, vert in enumerate(vertex):
            if vert.vert_name == entry:
                canvas.delete(vert.id_vert)
                canvas.delete(vert.id_txt)
                vertex.pop(i)
                vert_name.pop(i)
                root.destroy()
                flag = 0
                break
        else:
            mb.showerror(ERROR_STR_CONSTANT, SHOW_ERR_CONSTANT)
            break

def delete_vertex():
    create_window("Введите имя удаляемой вершины", find_delete_vertex)

def find_delete_edge(en1, en2, root):
    for i, edge in enumerate(edges):
        if edge.vertex1.vert_name == en1 and edge.vertex2.vert_name == en2:
            canvas.delete(edge.line)
            canvas.delete(edge.text)
            canvas.delete(edge.rect)
            edges.pop(i)
            edge_count -= 1
            root.destroy()
            break
    else:
        mb.showerror(ERROR_STR_CONSTANT, "Такого ребра не существует")

def menu_delete_edge():
    create_window("Введите имя вершин, между которыми \nудаляется ребро\nПервая вершина", find_delete_edge)

def menu_rename_vertex():
    create_vertex_window("Введите имя изменяемой вершины", rename)

def create_edge_window(title, command):
    new_window = Tk()
    new_window.title(TITLE_STR_NAME)
    new_window.wm_attributes('-topmost', 1)
    new_window.resizable(False, False)
    label1 = Label(new_window)
    label1[STR_LABEL_CONSTANT] = title
    label1.grid(row=0, column=0, sticky="ew")
    entry1 = Entry(new_window)
    entry1.grid(row=1, column=0, sticky="ew")
    btn = Button(new_window, text="Ввод", command=lambda: command(entry1.get(), new_window))
    btn.grid(row=2, column=0, sticky="ew")

def menu_create_edge():
    create_edge_window("Введите имя 1-ой вершины", create_edge)


sel_vert = None
vert_name = []
edges = []
vertex = []
color = "red"
x_click = 0
x_move = []
y_click = 0
y_move = []
vertex_count = 0
edge_count = 0
var1 = BooleanVar()
var1.set(False)
var2 = BooleanVar()
var2.set(False)

button_commands = [
    ("Задать имя графа", graf_name),
    ("Сохранить Значения", save_data),
    ("Создать вершину", menu_create_vetrex),
    ("Удалить вершину", delete_vertex),
    ("Переименовать вершину", menu_rename_vertex),
    ("Создать ребро", menu_create_edge),
    ("quit", exit),
    ("Удалить ребро", menu_delete_edge),
    ("Матрица инцендентности", create_matrix_incidence_window),
    ("Матрица смежности", create_matrix_adjacency)
]

for i, (text, command) in enumerate(button_commands):
    Button(tk, text=text, command=command).grid(row=i//4, column=i%4, stick="ew")

Checkbutton(tk, text="Ориентированность", onvalue=1, offvalue=0, variable=var1, bg="gray").grid(row=2, column=2, stick="ew")
Button(tk, text="Передвижение вершин", command=move_vertex2).grid(row=1, column=0, stick="ew")

tk.mainloop()
