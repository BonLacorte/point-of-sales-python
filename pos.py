import csv
from os import path
from tkinter import *
import tkinter.messagebox
import pandas as pd
my_window = Tk()
my_window.title('Sample GUI')

def close():
    ays = tkinter.messagebox.askyesno("Exit", "Are you sure?")
    if ays > 0:
        my_window.destroy()
        


    

def calculate():
    
    #total
    gA1 = a1.get()
    gA2 = a2.get()
    gA3 = a3.get()
    
    gA4 = a4.get()
    gA5 = a5.get()
    gA6 = a6.get()
    
    gA7 = a7.get()
    gA8 = a8.get()
    gA9 = a9.get()
    
    gB1 = b1.get()
    gB2 = b2.get()
    gB3 = b3.get()
    
    gC1 = c1.get()
    gC2 = c2.get()
    gC3 = c3.get()
    
    
    
    
    
    if gA1.isdecimal() and gA2.isdecimal() and gA3.isdecimal() and gA4.isdecimal() and gA5.isdecimal() and gA6.isdecimal() and gA7.isdecimal() and gA8.isdecimal() and gA9.isdecimal() and gB1.isdecimal() and gB2.isdecimal() and gB3.isdecimal() and gC1.isdecimal() and gC2.isdecimal() and gC3.isdecimal():
        
        #get the discount
        gDiscount = discount.get()
        
        
        
        #dictionaries
        f = {"a1": 55, "a2": 30, "a3": 55, "a4": 100, "a5": 45, "a6": 60, "a7": 55, "a8": 70, "a9": 70, "b1": 35, "b2": 50, "b3": 25, "c1": 20, "c2": 35, "c3": 45}
        orders = {"a1":gA1, "a2":gA2, "a3":gA3, "a4":gA4, "a5":gA5, "a6":gA6, "a7":gA7, "a8":gA8, "a9":gA9, "b1":gB1, "b2":gB2, "b3":gB3, "c1":gC1, "c2":gC2, "c3":gC3}
        
        #print orders
        print("Total:   ",orders)
        
        #print unwanted (products w/ 0)
        unwanted = { key:value for (key,value) in orders.items() if value == 0}
        print("unwanted: ",unwanted)

        #print unwanted (products w/ 1 and above)
        wanted = dict(orders.items() - unwanted.items())
        print("Wanted:   ",wanted)
        
        #string variable for writing ordered products
        global ordered_w
        ordered_w = ''

        for i in sorted(wanted):   
            ordered_w += i + '=' + str(wanted[i]) + ' '
            
        print(type(ordered_w))
        #ordered meals passed to variable "ans"
        print(ordered_w)
        
        #total amount of customer's order
        tot_p = (int(gA1)*f["a1"])+(int(gA2)*f["a2"])+(int(gA3)*f["a3"]) + (int(gA4)*f["a4"])+(int(gA5)*f["a5"])+(int(gA6)*f["a6"]) + (int(gA7)*f["a7"])+(int(gA8)*f["a8"])+(int(gA9)*f["a9"]) + (int(gB1)*f["b1"])+(int(gB2)*f["b2"])+(int(gB3)*f["b3"]) + (int(gC1)*f["c1"])+(int(gC2)*f["c2"])+(int(gC3)*f["c3"])
        
        #computing total discount
        global pwd_w
        global sc_w
        global discount_w
        gPwd = pwd.get()
        gSc = sc.get()
        if (gPwd == 1):
            dc1 = 0.05
            pwd_w = 'pwd'
        else:
            dc1 = 0.00
            pwd_w = ''
        if (gSc == 1):
            dc2 = 0.20
            sc_w = 'sc'
        else:
            dc2 = 0.00
            dc1 = 0.00
            sc_w = ''
        
        discount_w = pwd_w + " " + sc_w    
        tdc = dc1 + dc2
        
        #total amount w/ discount calculation
        global totalWD_w
        totalWD_w = float(tot_p) - (float(tot_p)*tdc)
        print(totalWD_w)
        total_price.set(float(totalWD_w))
        
        #if (add_button['state'] == DISABLED):
        add_button = Button(my_window, text ="Add", command = add_transaction, state = "normal").grid(row=16, column=0)
        
        
    else:
        tkinter.messagebox.showinfo("Error", "Please input numbers only")
    
    
    


def add_transaction():
    
    #get cashier user all of the info from the screen
    global cashier_w
    gCashier = cashier_choice.get()
    if (gCashier == 0):
        cashier_w = 'Angelo'
    if (gCashier == 1):
        cashier_w = 'Bon'
    if (gCashier == 2):
        cashier_w = 'Cali'
    print(cashier_w)
    
    #get all three pieces info for date recorded
    gDay = day.get()
    gMonth = month.get()
    gYear = year.get()
    #combine the three pieces to create full date
    transaction_date = gDay + "." + gMonth + "." + gYear
    print(transaction_date)
    
    print(pwd_w)
    print(sc_w)
    print(discount_w)
    print(ordered_w)
    print(totalWD_w)
    
    ask = tkinter.messagebox.askyesno("Exit", "Are you sure?")
    if ask > 0:
        try:
            #opens the file and writes the new data to the file
            if path.exists('McDollibeePOS.csv'):
                fp = open ('McDollibeePOS.csv', 'a', newline='')
                fprint = csv.writer(fp)
                fprint.writerow([cashier_w,transaction_date,ordered_w,discount_w,str(totalWD_w)])
            #create new .csv file
            else:
                fp = open ('McDollibeePOS.csv', 'w', newline='')
                fprint = csv.writer(fp)
                fprint.writerow(["Cashier Name","Date of Transaction","Ordered Products", "Discounts", "Total Amount"])
                fprint.writerow([cashier_w,transaction_date,ordered_w,discount_w,str(totalWD_w)])
        except Exception as err:
            print("Error: ", err)
        finally:
            fp.close()
            
    add_button = Button(my_window, text ="Add", command = add_transaction, state = "disabled").grid(row=16, column=0)
    
    

#Clear

#Variables that will be derived

rem = StringVar()
cashier_choice = IntVar()
day = StringVar()
month = StringVar()
year = StringVar()

a1 = StringVar(value = "0")
a2 = StringVar(value = "0")
a3 = StringVar(value = "0")

a4 = StringVar(value = "0")
a5 = StringVar(value = "0")
a6 = StringVar(value = "0")

a7 = StringVar(value = "0")
a8 = StringVar(value = "0")
a9 = StringVar(value = "0")

b1 = StringVar(value = "0")
b2 = StringVar(value = "0")
b3 = StringVar(value = "0")

c1 = StringVar(value = "0")
c2 = StringVar(value = "0")
c3 = StringVar(value = "0")

discount = IntVar()

total_price = StringVar()

pwd = IntVar()
sc = IntVar()


#Row 0
Label(my_window, text="McDollibee POS ").grid(row=0, column=2)


#Row 1
Label(my_window, text="Cashier Name: ").grid(row=1, column=0)
Radiobutton(my_window, text = "Angelo", variable = cashier_choice, value = 1).grid(row=1,column=1)
Radiobutton(my_window, text = "Bon", variable = cashier_choice, value = 2).grid(row=1,column=2)
Radiobutton(my_window, text = "Cali", variable = cashier_choice, value = 3).grid(row=1,column=3)

#Row 2
Label(my_window, text="Date: ").grid(row=2, column=0)

list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
droplist = OptionMenu(my_window, day, *list1)
day.set('1')
droplist.grid(row=2,column=1)

list2 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
droplist = OptionMenu(my_window, month, *list2)
month.set('January')
droplist.grid(row=2,column=3)

list3 = ['2020', '2021', '2022', '2023', '2024', '2025']
droplist = OptionMenu(my_window, year, *list3)
year.set('2022')
droplist.grid(row=2,column=5)

#Row 3

#Row 4
Label(my_window, text="Meal ").grid(row=3, column=0)

#Row 5
Entry(my_window, textvariable=a1, width=4, border=2).grid(row=5,column=0)
Label(my_window, text="55 - (A1)1pc Chicken ").grid(row=5, column=1)

Entry(my_window, textvariable=a2, width=4, border=2).grid(row=5,column=2)
Label(my_window, text="30 - (A2)2pcs Burger Steak").grid(row=5, column=3)

Entry(my_window, textvariable=a3, width=4, border=2).grid(row=5,column=4)
Label(my_window, text="55 - (A3)3pcs Shanghai ").grid(row=5, column=5)

#Row 6
Entry(my_window, textvariable=a4, width=4, border=2).grid(row=6,column=0)
Label(my_window, text="100 - (A4)2pc Chicken ").grid(row=6, column=1)

Entry(my_window, textvariable=a5, width=4, border=2).grid(row=6,column=2)
Label(my_window, text="45 - (A5)Spaghetti ").grid(row=6, column=3)

Entry(my_window, textvariable=a6, width=4, border=2).grid(row=6,column=4)
Label(my_window, text="60 - (A6)Sisig ").grid(row=6, column=5)

#Row 7
Entry(my_window, textvariable=a7, width=4, border=2).grid(row=7,column=0)
Label(my_window, text="55 - (A7)Beef Tapsilog ").grid(row=7, column=1)

Entry(my_window, textvariable=a8, width=4, border=2).grid(row=7,column=2)
Label(my_window, text="70 - (A8)Kare-Kare").grid(row=7, column=3)

Entry(my_window, textvariable=a9, width=4, border=2).grid(row=7,column=4)
Label(my_window, text="70 - (A9)Chicken Adobo ").grid(row=7, column=5)

#Row 8

#Row 9
Label(my_window, text="Snacks ").grid(row=9, column=0)
Label(my_window, text="Drinks ").grid(row=9, column=3)


#Row 10
Entry(my_window, textvariable=b1, width=4, border=2,).grid(row=10,column=0)
Label(my_window, text="35 - (B1)Burger ").grid(row=10, column=1)

Entry(my_window, textvariable=c1, width=4, border=2).grid(row=10,column=2)
Label(my_window, text="20 - (C1)Softdrinks ").grid(row=10, column=3)

#Row 11
Entry(my_window, textvariable=b2, width=4, border=2).grid(row=11,column=0)
Label(my_window, text="50 - (B2)Fries ").grid(row=11, column=1)

Entry(my_window, textvariable=c2, width=4, border=2).grid(row=11,column=2)
Label(my_window, text="35 - (C2)Cokefloat ").grid(row=11, column=3)

#Row 12
Entry(my_window, textvariable=b3, width=4, border=2).grid(row=12,column=0)
Label(my_window, text="25 - (B3)Turon ").grid(row=12, column=1)

Entry(my_window, textvariable=c3, width=4, border=2).grid(row=12,column=2)
Label(my_window, text="45 - (C3)Milktea ").grid(row=12, column=3)

#Row 13
Label(my_window, text="Discount ").grid(row=13, column=0)

#Row 14
Label(my_window, text="Discount ").grid(row=14, column=0)
Checkbutton(my_window, text="PWD", variable=pwd, command = calculate).grid(row=14, column=0)
Checkbutton(my_window, text="Senior Citizen", variable=sc, command = calculate).grid(row=14, column=1)

#Row 15
Label(my_window, text="Total amount: ").grid(row=15, column=0)
Entry(my_window, textvariable=total_price, state="disabled", width=8, border=2).grid(row=15,column=1)

#Row 16
add_button = Button(my_window, text ="Add", command = add_transaction, state = "disabled").grid(row=16, column=0)
calc_button = Button(my_window, text ="Calculate", command = calculate).grid(row=16, column=1)
clear_button = Button(my_window, text ="Clear", command = calculate).grid(row=16, column=2)
close_button = Button(my_window, text ="Close", command = close).grid(row=16, column=3)


my_window.mainloop()