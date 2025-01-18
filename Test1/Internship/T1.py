import tkinter.messagebox as msgbox
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np

# Read data from Excel sheets into dataframes
df1 = pd.read_excel(r"C:\Users\kpbrb\PycharmProjects\Test1\Internship\2018-19.xlsx", sheet_name="Maize", engine='openpyxl')
df2 = pd.read_excel(r"C:\Users\kpbrb\PycharmProjects\Test1\Internship\2018-19.xlsx", sheet_name="Paddy", engine='openpyxl')
df3 = pd.read_excel(r"C:\Users\kpbrb\PycharmProjects\Test1\Internship\2018-19.xlsx", sheet_name="Cotton", engine='openpyxl')

# Set display options for pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Write dataframes to CSV files
df1.to_csv(r"C:\Users\kpbrb\PycharmProjects\Test1\Internship\2018-19-1.csv", index=None)
df2.to_csv(r"C:\Users\kpbrb\PycharmProjects\Test1\Internship\2018-19-2.csv", index=None)
df3.to_csv(r"C:\Users\kpbrb\PycharmProjects\Test1\Internship\2018-19-3.csv", index=None)

# Read CSV files into dataframes
d1 = pd.read_csv(r"C:\Users\kpbrb\PycharmProjects\Test1\Internship\2018-19-1.csv")
d2 = pd.read_csv(r"C:\Users\kpbrb\PycharmProjects\Test1\Internship\2018-19-2.csv")
d3 = pd.read_csv(r"C:\Users\kpbrb\PycharmProjects\Test1\Internship\2018-19-3.csv")



def Table_format():
        c=Toplevel(root)
        c.geometry('800x800')
        c.title("Cultivation Details")
        c.iconbitmap("download.ico")
        tv = ttk.Treeview(c)
        style = ttk.Style()
        style.theme_use('clam')
        def fix_map(option):
                return [elm for elm in style.map('Treeview', query_opt=option)
                        if elm[:2] != ('!disabled', '!selected')]
        style.map('Treeview', foreground=fix_map('foreground'),
                  background=fix_map('background'))
        tv.tag_configure('bold', font=('', 0, 'bold'), foreground='red')

        tv['columns'] = ('SNo', 'Items', 'Cotton','Paddy','Maize')
        tv.column('#0', width=0, stretch=NO)
        tv.column('SNo', anchor=CENTER, width=120)
        tv.column('Items', anchor=CENTER, width=120)
        tv.column('Cotton', anchor=CENTER, width=120)
        tv.column('Paddy', anchor=CENTER, width=120)
        tv.column('Maize', anchor=CENTER, width=120)

        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('SNo', text='SNo', anchor=CENTER)
        tv.heading('Items', text='Items', anchor=CENTER)
        tv.heading('Cotton', text='Cotton', anchor=CENTER)
        tv.heading('Paddy', text='Paddy', anchor=CENTER)
        tv.heading('Maize', text='Maize', anchor=CENTER)
        x = c3.get()
        Tot_c=round((d3[x][1]) * float(var1.get()))+round((d3[x][2]) * float(var1.get()))+round((d3[x][3]) * float(var1.get()))+round((d3[x][4]) * float(var1.get()))+round(l[0])+round((d3[x][6]) * float(var1.get()))+round((d3[x][7]) * float(var1.get()))+round((d3[x][8]) * float(var1.get()))+round((d3[x][9]) * float(var1.get()))+round((d3[x][10]) * float(var1.get()))

        Tot_p = round((d2[x][1]) * float(var3.get())) + round((d2[x][2]) * float(var3.get())) + round(
                (d2[x][3]) * float(var3.get())) + round((d2[x][4]) * float(var3.get())) + round(l1[0]) + round(
                (d2[x][6]) * float(var3.get())) + round((d2[x][7]) * float(var3.get())) + round(
                (d2[x][8]) * float(var3.get())) + round((d2[x][9]) * float(var3.get())) + round(
                (d2[x][10]) * float(var3.get()))

        Tot_m = round((d1[x][1]) * float(var2.get())) + round((d1[x][2]) * float(var2.get())) + round(
                (d1[x][3]) * float(var2.get())) + round((d1[x][4]) * float(var2.get())) + round(l2[0]) + round(
                (d1[x][6]) * float(var2.get())) + round((d1[x][7]) * float(var2.get())) + round(
                (d1[x][8]) * float(var2.get())) + round((d1[x][9]) * float(var2.get())) + round(
                (d1[x][10]) * float(var2.get()))

        tv.insert(parent='', index=0, iid=0, text='',values=('1', 'Operational Cost', Tot_c,Tot_p, Tot_m))
        tv.insert(parent='', index=1, iid=1, text='',values=('2', 'Human Labour', round((d3[x][1]) * float(var1.get())),round((d2[x][1]) * float(var3.get())), round((d1[x][1]) * float(var2.get()))))
        tv.insert(parent='', index=2, iid=2, text='',values=('3', 'Animal Labour', round((d3[x][2]) * float(var1.get())),
                                  round((d2[x][2]) * float(var3.get())), round((d1[x][2]) * float(var2.get()))))
        tv.insert(parent='', index=3, iid=3, text='',
                          values=('4', 'Machine Labour', round((d3[x][3]) * float(var1.get())),
                                  round((d2[x][3]) * float(var3.get())), round((d1[x][3]) * float(var2.get()))))
        tv.insert(parent='', index=4, iid=4, text='', values=(
                '5', 'Seed', round((d3[x][4]) * float(var1.get())), round((d2[x][4]) * float(var3.get())),
                round((d1[x][4]) * float(var2.get()))))
        tv.insert(parent='', index=5, iid=5, text='',
                          values=('6', 'Fertilizer & Manure', round(l[0]), round(l1[0]), round(l2[0])))
        tv.insert(parent='', index=6, iid=6, text='',
                          values=('7', 'Insecticides', round((d3[x][6]) * float(var1.get())),
                                  round((d2[x][6]) * float(var3.get())), round((d1[x][6]) * float(var2.get()))))
        tv.insert(parent='', index=7, iid=7, text='',
                  values=('8', 'Irrigation Charges', round((d3[x][7]) * float(var1.get())),
                          round((d2[x][7]) * float(var3.get())), round((d1[x][7]) * float(var2.get()))))
        tv.insert(parent='', index=8, iid=8, text='',
                          values=('9', 'Crop Insurance', round((d3[x][8]) * float(var1.get())),
                                  round((d2[x][8]) * float(var3.get())), round((d1[x][8]) * float(var2.get()))))

        tv.insert(parent='', index=9, iid=9, text='',
                          values=('10', 'Miscellaneous', round((d3[x][9]) * float(var1.get())),
                                  round((d2[x][9]) * float(var3.get())), round((d1[x][9]) * float(var2.get()))))
        tv.insert(parent='', index=10, iid=10, text='',
                          values=('11', 'Interest on Working Capital ', round((d3[x][10]) * float(var1.get())),
                                  round((d2[x][10]) * float(var3.get())), round((d1[x][10]) * float(var2.get()))))
        tv.insert(parent='', index=11, iid=11, text='',
                          values=('12', 'Fixed Costs', round((d3[x][11]) * float(var1.get())),round((d2[x][11]) * float(var3.get())), round((d1[x][11]) * float(var2.get()))))
        tv.insert(parent='', index=12, iid=12, text='',
                  values=(
                  '', 'Total', round(Tot_c+round((d3[x][11]) * float(var1.get()))),round(Tot_p+round((d2[x][11]) * float(var3.get()))),
                  round(Tot_m+round((d1[x][11]) * float(var2.get())))))
        for row in tv.get_children()[-1:]:
                tv.item(row, tags='bold')
        tv.pack()
        if(var4.get()=="Normal"):
                y_m = ((d1[x][12] * float(var2.get()))) * 2100
                y_p = ((d2[x][12] * float(var3.get()))) * 2000
                y_c = ((d3[x][12] * float(var1.get()))) * 7000
                pl_c = y_c - (Tot_c + round((d3[x][11]) * float(var1.get())))
                pl_p = y_p - (Tot_p + round((d2[x][11]) * float(var3.get())))
                pl_m = y_m - (Tot_m + round((d1[x][11]) * float(var2.get())))
                if (pl_c > 0):
                        X1 = Label(c,
                                   text="Profit for Cotton" + '(' + str(var1.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_c), 0)), font=("bold", 16), foreground="Green").place(x=80, y=300)
                if (pl_c < 0):
                        X1 = Label(c,
                                   text="Loss for Cotton" + '(' + str(var1.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_c), 0)), font=("bold", 16), foreground="Red").place(x=80, y=300)
                if (pl_p > 0):
                        X2 = Label(c,
                                   text="Profit for Paddy" + '(' + str(var3.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_p), 0)), font=("bold", 16), foreground="Green").place(x=80, y=350)
                if (pl_p < 0):
                        X2 = Label(c,
                                   text="Loss for Paddy" + '(' + str(var3.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_p), 0)), font=("bold", 16),
                                   foreground="Red").place(x=80, y=350)
                if (pl_m > 0):
                        X3 = Label(c,
                                   text="Profit for Maize:" + '(' + str(var2.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_m), 0)), font=("bold", 16),
                                   foreground="Green").place(x=80, y=400)
                if (pl_m < 0):
                        X3 = Label(c,
                                   text="Loss for Maize" + '(' + str(var2.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_m), 0)), font=("bold", 16),
                                   foreground="Red").place(x=80, y=400)

                def bar():
                        w = 0.4
                        z1 = Tot_c + round((d3[x][11]) * float(var1.get()))
                        z2 = Tot_p + round((d2[x][11]) * float(var3.get()))
                        z3 = Tot_m + round((d1[x][11]) * float(var2.get()))
                        Total_1 = z1 + z2 + z3
                        Total_2 = y_c + y_m + y_p
                        x1 = ["Cotton", "Rice", "Maize", "Total"]
                        A1 = [z1, z2, z3, Total_1]
                        A2 = [y_c, y_p, y_m, Total_2]
                        n = 4
                        r = np.arange(n)
                        plt.bar(r, A1, w, label="COC")
                        plt.bar(r + w, A2, w, label="Returns")
                        plt.xticks(r + w / 2, x1)
                        plt.legend()
                        plt.title(Name.get() + " " + "FPO" + " " + District.get())
                        plt.show()
                        plt.clf()

                b4 = Button(root, text='Visualize', width=15, bg='brown', fg='white', command=bar).place(x=450, y=550)
        elif(var4.get()=="Below Normal"):
                y_m = ((d1[x][12]*0.7* float(var2.get()))) * 2100
                y_p = ((d2[x][12]*0.9* float(var3.get()))) * 2000
                y_c = ((d3[x][12] *0.7*float(var1.get()))) * 7000

                pl_c = y_c - (Tot_c + round((d3[x][11]) * float(var1.get())))
                pl_p = y_p - (Tot_p + round((d2[x][11]) * float(var3.get())))
                pl_m = y_m - (Tot_m + round((d1[x][11]) * float(var2.get())))
                if (pl_c > 0):
                        X1 = Label(c,
                                   text="Profit for Cotton" + '(' + str(var1.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(pl_c, 0)), font=("bold", 16), foreground="Green").place(x=80, y=300)
                if (pl_c < 0):
                        X1 = Label(c,
                                   text="Loss for Cotton" + '(' + str(var1.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_c), 0)), font=("bold", 16), foreground="Red").place(x=80, y=300)
                if (pl_p > 0):
                        X2 = Label(c,
                                   text="Profit for Paddy" + '(' + str(var3.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(pl_p, 0)), font=("bold", 16), foreground="Green").place(x=80, y=350)
                if (pl_p < 0):
                        X2 = Label(c,
                                   text="Loss for Paddy" + '(' + str(var3.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_p), 0)), font=("bold", 16),
                                   foreground="Red").place(x=80, y=350)
                if (pl_m > 0):
                        X3 = Label(c,
                                   text="Profit for Maize:" + '(' + str(var2.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(pl_m, 0)), font=("bold", 16),
                                   foreground="Green").place(x=80, y=400)
                if (pl_m < 0):
                        X3 = Label(c,
                                   text="Loss for Maize" + '(' + str(var2.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(pl_m, 0)), font=("bold", 16),
                                   foreground="Red").place(x=80, y=400)

                def bar():
                        w = 0.4
                        z1 = Tot_c + round((d3[x][11]) * float(var1.get()))
                        z2 = Tot_p + round((d2[x][11]) * float(var3.get()))
                        z3 = Tot_m + round((d1[x][11]) * float(var2.get()))
                        Total_1 = z1 + z2 + z3
                        Total_2 = y_c + y_m + y_p
                        x1 = ["Cotton", "Rice", "Maize", "Total"]
                        A1 = [z1, z2, z3, Total_1]
                        A2 = [y_c, y_p, y_m, Total_2]
                        n = 4
                        r = np.arange(n)
                        plt.bar(r, A1, w, label="COC")
                        plt.bar(r + w, A2, w, label="Returns")
                        plt.xticks(r + w / 2, x1)
                        plt.legend()
                        plt.title(Name.get() + " " + "FPO" + " " + District.get())
                        plt.show()
                        plt.clf()

                b4 = Button(root, text='Visualize', width=15, bg='brown', fg='white', command=bar).place(x=450, y=550)
        elif (var4.get() == "Above Normal"):
                y_m = ((d1[x][12] * 1.2 * float(var2.get()))) * 2100
                y_p = ((d2[x][12] * 1.1 * float(var3.get()))) * 2000
                y_c = ((d3[x][12] * 1.2 * float(var1.get()))) * 7000

                pl_c = y_c - (Tot_c + round((d3[x][11]) * float(var1.get())))
                pl_p = y_p - (Tot_p + round((d2[x][11]) * float(var3.get())))
                pl_m = y_m - (Tot_m + round((d1[x][11]) * float(var2.get())))
                if (pl_c > 0):
                        X1 = Label(c,
                                   text="Profit for Cotton" + '(' + str(var1.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_c), 0)), font=("bold", 16), foreground="Green").place(x=80, y=300)
                if (pl_c < 0):
                        X1 = Label(c,
                                   text="Loss for Cotton" + '(' + str(var1.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_c), 0)), font=("bold", 16), foreground="Red").place(x=80, y=300)
                if (pl_p > 0):
                        X2 = Label(c,
                                   text="Profit for Paddy" + '(' + str(var3.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_p), 0)), font=("bold", 16), foreground="Green").place(x=80, y=350)
                if (pl_p < 0):
                        X2 = Label(c,
                                   text="Loss for Paddy" + '(' + str(var3.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_p), 0)), font=("bold", 16),
                                   foreground="Red").place(x=80, y=350)
                if (pl_m > 0):
                        X3 = Label(c,
                                   text="Profit for Maize:" + '(' + str(var2.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_m), 0)), font=("bold", 16),
                                   foreground="Green").place(x=80, y=400)
                if (pl_m < 0):
                        X3 = Label(c,
                                   text="Loss for Maize" + '(' + str(var2.get()) + "ha" + ')' + ":" + "Rs" + str(
                                           round(abs(pl_m), 0)), font=("bold", 16),
                                   foreground="Red").place(x=80, y=400)

                def bar():
                        w = 0.4
                        z1 = Tot_c + round((d3[x][11]) * float(var1.get()))
                        z2 = Tot_p + round((d2[x][11]) * float(var3.get()))
                        z3 = Tot_m + round((d1[x][11]) * float(var2.get()))
                        Total_1 = z1 + z2 + z3
                        Total_2 = y_c + y_m + y_p
                        x1 = ["Cotton", "Rice", "Maize", "Total"]
                        A1 = [z1, z2, z3, Total_1]
                        A2 = [y_c, y_p, y_m, Total_2]
                        n = 4
                        r = np.arange(n)
                        plt.bar(r, A1, w, label="COC")
                        plt.bar(r + w, A2, w, label="Returns")
                        plt.xticks(r + w / 2, x1)
                        plt.legend()
                        plt.title(Name.get() + " " + "FPO" + " " + District.get())
                        plt.show()
                        plt.clf()

                b4 = Button(root, text='Visualize', width=15, bg='brown', fg='white', command=bar).place(x=450, y=550)
        else:
                msgbox.showinfo(title='FRC', message='Invalid Data')
def Btotal():
        global l
        x = c3.get()
        if(var1.get()!=0.0 and var1.get()!=" " ):
                l = []
                MOP = (15 / 60) * 100 * float(var1.get())
                DAP = (60 / 46) * 100 * float(var1.get())
                z = ((18 * DAP) / 100) / float(var1.get())
                N1 = 30 - z
                N2 = (N1 / 46) * 100 * float(var1.get())

                Ni = round(N2, 1)
                P = round(DAP, 1)
                K = round(MOP, 1)

                #########
                U = (40 / 46) * 100 * float(var1.get())
                Ni1 = round(U, 1)
                P1 = round(0, 1)
                K1 = round(0, 1)

                #########
                U1 = (40 / 46) * 100 * float(var1.get())
                MOP1 = (15 / 60) * 100 * float(var1.get())

                Ni2 = round(U1, 1)
                P2 = round(0, 1)
                K2 = round(MOP1, 1)

                Ur = (Ni + Ni1 + Ni2) * Urea
                Da = (P + P1 + P2) * DAP_price
                Mo = (K + K1 + K2) * MOP_price
                T = Ur + Da + Mo

                HL1 = (d3[x][1]) * float(var1.get())
                AL1 = (d3[x][2]) * float(var1.get())
                ML1 = (d3[x][3]) * float(var1.get())
                Seed1 = (d3[x][4]) * float(var1.get())
                FM1 = T
                z1 = d3[x].replace(d3[x][5], FM1)
                l.append(z1[5])
                Insec1 = (d3[x][6]) * float(var1.get())
                Irri1 = (d3[x][7]) * float(var1.get())
                CI1 = (d3[x][8]) * float(var1.get())
                Misc1 = (d3[x][9]) * float(var1.get())
                WC1 = (d3[x][10]) * float(var1.get())
                FC1 = (d3[x][11]) * float(var1.get())
                Total1 = HL1 + AL1 + ML1 + Seed1 + FM1 + Insec1 + Irri1 + CI1 + Misc1 + WC1 + FC1

                L1 = Label(root,
                           text="Cost of Cultivation for Cotton:\t\t"+ "Rs\t" + str(round(Total1, 0))).place(x=80, y=400)

        else:
                msgbox.showinfo(title='FRC', message='Cotton Crop Area cannot be Zero or Empty')


def Kharif_Total_maize():
        global l2
        x = c3.get()
        if (var2.get() != 0.0  and var2.get() != " " ):
                l2 = []
                MOP = (25 / 60) * 100 * float(var2.get())
                DAP = (60 / 46) * 100 * float(var2.get())
                z = ((18 * DAP) / 100) / float(var2.get())
                N1 = (200 / 3) - z
                N2 = (N1 / 46) * 100 * float(var2.get())
                Ni = round(N2, 1)
                P = round(DAP, 1)
                K = round(MOP, 1)
                U = ((200 / 3) / 46) * 100 * float(var2.get())
                Ni1 = round(U, 1)
                P1 = round(0, 1)
                K1 = round(0, 1)
                U1 = ((200 / 3) / 46) * 100 * float(var2.get())
                MOP1 = (25 / 60) * 100 * float(var2.get())
                Ni2 = round(U1, 1)
                P2 = round(0, 1)
                K2 = round(MOP1, 1)
                Ur = (Ni + Ni1 + Ni2) * Urea
                Da = (P + P1 + P2) * DAP_price
                Mo = (K + K1 + K2) * MOP_price
                T = Ur + Da + Mo
                x = c3.get()
                HL2 = (d1[x][1]) * float(var2.get())
                AL2 = (d1[x][2]) * float(var2.get())
                ML2 = (d1[x][3]) * float(var2.get())
                Seed2 = (d1[x][4]) * float(var2.get())
                FM2 = T
                z2 = d1[x].replace(d1[x][5], FM2)
                l2.append(z2[5])
                Insec2 = (d1[x][6]) * float(var2.get())
                Irri2 = (d1[x][7]) * float(var2.get())
                CI2 = (d1[x][8]) * float(var2.get())
                Misc2 = (d1[x][9]) * float(var2.get())
                WC2 = (d1[x][10]) * float(var2.get())
                FC2 = (d1[x][11]) * float(var2.get())
                Total2 = HL2 + AL2 + ML2 + Seed2 + FM2 + Insec2 + Irri2 + CI2 + Misc2 + WC2 + FC2
                L2 = Label(root,
                           text="Cost of Cultivation for Maize:\t\t"+ "Rs\t" + str(round(Total2, 0)) ).place(x=80, y=450)

        else:
                msgbox.showinfo(title='FRC', message='Maize Crop Area cannot be Zero or Empty')

def Kharif_Total_paddy():
        global l1
        x = c3.get()
        if (var3.get() != 0.0 and var3.get() != " " ):
                l1 = []
                MOP = (45 / 60) * 100 * float(var3.get())
                DAP = (90 / 46) * 100 * float(var3.get())
                z = ((18 * DAP) / 100) / float(var3.get())
                N1 = 60 - z
                N2 = (N1 / 46) * 100 * float(var3.get())
                Ni = round(N2, 1)
                P = round(DAP, 1)
                K = round(MOP, 1)
                U = (60 / 46) * 100 * float(var3.get())
                Ni1 = round(U, 1)
                P1 = round(0, 1)
                K1 = round(0, 1)
                U1 = (60 / 46) * 100 * float(var3.get())
                MOP1 = (45 / 60) * 100 * float(var3.get())
                Ni2 = round(U1, 1)
                P2 = round(0, 1)
                K2 = round(MOP1, 1)
                Ur = (Ni + Ni1 + Ni2) * Urea
                Da = (P + P1 + P2) * DAP_price
                Mo = (K + K1 + K2) * MOP_price
                T = Ur + Da + Mo
                x = c3.get()
                HL3 = (d2[x][1]) * float(var3.get())
                AL3 = (d2[x][2]) * float(var3.get())
                ML3 = (d2[x][3]) * float(var3.get())
                Seed3 = (d2[x][4]) * float(var3.get())
                FM3 = T
                z3 = d2[x].replace(d2[x][5], FM3)
                l1.append(z3[5])
                Insec3 = (d2[x][6]) * float(var3.get())
                Irri3 = (d2[x][7]) * float(var3.get())
                CI3 = (d2[x][8]) * float(var3.get())
                Misc3 = (d2[x][9]) * float(var3.get())
                WC3 = (d2[x][10]) * float(var3.get())
                FC3 = (d2[x][11]) * float(var3.get())
                Total3 = HL3 + AL3 + ML3 + Seed3+ FM3 + Insec3 + Irri3 + CI3 + Misc3 + WC3 + FC3
                L3 = Label(root,
                           text="Cost of Cultivation for Paddy\t\t"+ "Rs\t" + str(round(Total3, 0))).place(x=80, y=500)
        else:
                msgbox.showinfo(title='FRC', message='Paddy Crop Area cannot be Zero or Empty')
# GUI tkinter Part#######################################################################################################################
root = Tk()
c3 = StringVar()
root.geometry('700x800')
root.title("FRC")
Name = StringVar()
District = StringVar()
var1 = DoubleVar()
var2 = DoubleVar()
var3 = DoubleVar()
var4 = StringVar()
Urea=5.52
DAP_price=22.5
MOP_price=17.77
global L1,L2,L3
global Total1,Total2,Total3,Z1

def clear():
    Name.set("")
    District.set("")
    var1.set("")
    var2.set("")
    var3.set("")
    c3.set("Select")



def COC():
        Btotal()
        Kharif_Total_maize()
        Kharif_Total_paddy()
        b5 = Button(root, text='Details', width=15, bg='brown', fg='white', command=Table_format).place(x=450, y=450)


l0 = Label(root, text="FERTIGURU", font=("bold", 20), foreground="Red",
           background="#FFFDD0").place(x=240, y=20)
l1 = Label(root, text="Name of the FPO", width=20, font=("bold", 10)).place(x=80, y=80)
e1 = Entry(root, textvar=Name).place(x=300, y=80)
l2 = Label(root, text="District Name", width=20, font=("bold", 10)).place(x=80, y=130)
e2 = Entry(root, textvar=District).place(x=300, y=130)

l6_1 = Label(root, text="Crop Area(ha) of Cotton:", width=20, font=("bold", 10)).place(x=80, y=180)
e6_1 = Entry(root, textvar=var1).place(x=300, y=180)

l6_2 = Label(root, text="Crop Area(ha) of Maize:", width=20, font=("bold", 10)).place(x= 80, y=230)
e6_2 = Entry(root, textvar=var2).place(x=300, y=230)

l6_3 = Label(root, text="Crop Area(ha) of Paddy:", width=20, font=("bold", 10)).place(x=80, y=280)
e6_3 = Entry(root, textvar=var3).place(x=300, y=280)


l7 = Label(root, text="State Name:", width=20, font=("bold", 10)).place(x=80, y=320)
list3 = []
for col in d1.columns:
        list3.append(col)
list3.sort()
list3.remove("Items")
droplist2 = OptionMenu(root, c3, *list3)
droplist2.config(width=15)
c3.set('Select')
droplist2.place(x=300, y=320)
b3 = Button(root, text='Clear', width=15, bg='brown', fg='white', command=clear).place(x=250, y=550)
root.configure(background='#C1E1D2')

b2 = Button(root, text='Total Cost', width=15, bg='brown', fg='white',command=COC).place(x=80, y=550)
l5 = Label(root, text="Climate Forecast:", width=20, font=("bold", 10)).place(x=80, y=360)
Radiobutton(root, text="Normal", variable=var4, value="Normal").place(x=280, y=360)
Radiobutton(root, text="Above Normal", variable=var4, value="Above Normal").place(x=380, y=360)
Radiobutton(root, text="Below Normal", variable=var4, value="Below Normal").place(x=500, y=360)
def display_msg():
    msgbox.showinfo(title='FRC', message='🙂Thank You For Using Our Calculator🙂')
    root.destroy()
root.configure(background='#C1E1D2')
root.iconbitmap("download.ico")

image1 = Image.open("images.png")
test1 = ImageTk.PhotoImage(image1)
label1 = Label(image=test1)
label1.image = test1
label1.place(x=500, y=150)

root.protocol('WM_DELETE_WINDOW', display_msg)
root.mainloop()
###################################################################################################################
