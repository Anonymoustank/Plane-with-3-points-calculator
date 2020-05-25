import tkinter

root = tkinter.Tk()

root.title("Plane Calculator")

tkinter.Label(root, text="Enter Three Points:").grid(row=1, column=1)

for a in range(2, 5):
    tkinter.Label(root, text="(").grid(row=a, column=2)
    tkinter.Label(root, text=",").grid(row=a, column=4)
    tkinter.Label(root, text = ",").grid(row=a, column=6)
    tkinter.Label(root, text=")").grid(row=a, column=8)
    exec("point%s_x = tkinter.Entry(root)" % (a - 1))
    exec("point%s_x.grid(row = %s, column = 3)" % (a - 1, a))
    exec("point%s_y = tkinter.Entry(root)" % (a - 1))
    exec("point%s_y.grid(row = %s, column = 5)" % (a - 1, a))
    exec("point%s_z = tkinter.Entry(root)" % (a - 1))
    exec("point%s_z.grid(row = %s, column = 7)" % (a - 1, a))


def calculate():
    u1 = float(point2_x.get()) - float(point1_x.get())
    u2 = float(point2_y.get()) - float(point1_y.get())
    u3 = float(point2_z.get()) - float(point1_z.get())

    v1 = float(point3_x.get()) - float(point1_x.get())
    v2 = float(point3_y.get()) - float(point1_y.get())
    v3 = float(point3_z.get()) - float(point1_z.get())

    i = float((u2) * float(v3) - float(u3) * float(v2))
    j = float((u3) * float(v1) - float(u1) * float(v3))
    k = float((u1) * float(v2) - float(u2) * float(v1))

    negative_p = 0 - (i * float(point1_x.get())) - (j * float(point1_y.get())) - (k * float(point1_z.get()))
    p = abs(negative_p)

    print("%sx, %sy, %sz, -%s" % (i, j, k, p))

tkinter.Button(root, text="Calculate", command = calculate).grid(row=5, column=1)

root.mainloop()