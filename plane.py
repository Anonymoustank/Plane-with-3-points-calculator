import tkinter

import math

root = tkinter.Tk()

root.title("Plane Calculator")
list = [] #will contain all entries

def create_gui():
    tkinter.Label(root, text="Enter Three Points:").grid(row=1, column=1)
    for a in range(2, 5): #Creates entries where you can put points and the label that go along with them
        tkinter.Label(root, text="(").grid(row=a, column=2)
        tkinter.Label(root, text=",").grid(row=a, column=4)
        tkinter.Label(root, text = ",").grid(row=a, column=6)
        tkinter.Label(root, text=")").grid(row=a, column=8)
        exec("point%s_x = tkinter.Entry(root)" % (a - 1), globals())
        exec("point%s_x.grid(row = %s, column = 3)" % (a - 1, a))
        exec("point%s_y = tkinter.Entry(root)" % (a - 1), globals())
        exec("point%s_y.grid(row = %s, column = 5)" % (a - 1, a))
        exec("point%s_z = tkinter.Entry(root)" % (a - 1), globals())
        exec("point%s_z.grid(row = %s, column = 7)" % (a - 1, a))
        exec("list.append(point%s_x)" % (a - 1))
        exec("list.append(point%s_y)" % (a - 1))
        exec("list.append(point%s_z)" % (a - 1))
    for a in list:
        a.insert(0, "0")

create_gui()

def square_root(list): #Computes expressions with square roots 
    for entry in list: #Iterates through the list containing the entries
        for text in entry.get(): #Iterates through all of the characters in the values in each entry
            if text == "√":
                entry_value = entry.get() #get method gets value from entry
                before_root = ""
                for z in entry.get():
                    if z == "√":
                        entry_value = entry_value.replace("√","")
                        break
                    else:
                        before_root = before_root + z
                        entry_value = entry_value.replace(z,"",1)
                entry_number = float(math.sqrt(float(entry_value))) #Square root of the radicand
                if before_root != '':
                    entry_number = entry_number * float(before_root) #Multiply number to the square root of radicand
                entry.delete(0,"end") #deletes whatever is in the entry
                entry.insert(0,entry_number) #puts the value that was calculated by the function within the entry

num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "√", "", " "] #acceptable values in the entries
def calculate():
    for a in list:
        if a.get() == "":
            a.insert(0, "0")

    for entry in list:
        for char in entry.get():
            if char not in num_list:
                error_window = tkinter.Tk()
                tkinter.Label(error_window, text="%s is not a valid character. Only numbers, decimal points, and square root symbols are valid." % char).grid(row=0, column=0)
                return False


    square_root(list)
    u1 = float(point2_x.get()) - float(point1_x.get()) #i component of vector 1
    u2 = float(point2_y.get()) - float(point1_y.get()) #j component 
    u3 = float(point2_z.get()) - float(point1_z.get()) #k component

    v1 = float(point3_x.get()) - float(point1_x.get()) #i component of vector 2
    v2 = float(point3_y.get()) - float(point1_y.get()) #j component
    v3 = float(point3_z.get()) - float(point1_z.get()) #k component

    #lines above create 2 vectors using the inputted points

    i = float((u2) * float(v3) - float(u3) * float(v2)) #i component of unit normal (x coefficient of plane)
    j = float((u3) * float(v1) - float(u1) * float(v3)) #j component of unit normal (y coefficient of plane)
    k = float((u1) * float(v2) - float(u2) * float(v1)) #k component of unit normal (z coefficient of plane)
    #3 lines above create the unit normal using the cross product formula

    negative_p = 0 - (i * float(point1_x.get())) - (j * float(point1_y.get())) - (k * float(point1_z.get())) #constant in plane formula
    p = abs(negative_p)

    if j >= 0:
        j_sign = "+" #signs that go in front of the coefficients
    else:
        j_sign = "-"
    
    if k >= 0:
        k_sign = "+"
    else:
        k_sign = "-"
    
    if negative_p < 0:
        p_sign = "-"
    else:
        p_sign = "+"

    j = abs(j)
    k = abs(k)

    if i == 0: #makes sure -0 is never printed
        i = abs(i)

    def convert_int(element):
        if element - int(element) == 0.0:
            return int(element)
        else:
            return element
    i = convert_int(i)
    j = convert_int(j)
    k = convert_int(k)
    p = convert_int(p)

    answer = tkinter.Tk()
    answer.title("Answer")
    tkinter.Label(answer, text="%sx %s %sy %s %sz %s %s = 0" % (i, j_sign, j, k_sign, k, p_sign, p)).grid(row=1, column=1)


tkinter.Button(root, text="Start Calculation", height = 1, width = 15, command = calculate).grid(row=5, column=1)
tkinter.Button(root, text="Reset Entries", height = 1, width = 15, command = create_gui).grid(row=6, column=1)

root.mainloop()