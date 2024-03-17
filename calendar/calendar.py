# A code for calendar
import tkinter as tk
import time
import pandas as pd

# time
T = time.localtime()

# month
month = {
       '1': 31 , 
       '2': 28 , # ignore the 29th case
       '3': 31 , 
       '4': 30 , 
       '5': 31 , 
       '6': 30 , 
       '7': 31 , 
       '8': 31 , 
       '9': 30 , 
       '10': 31 , 
       '11': 30 , 
       '12': 31
       }

week = ["Monday", 
        "Tuesday", 
        "Wednesday", 
        "Thursday", 
        "Friday", 
        "Saturday", 
        "Sunday"]
  
# subpage function
def add():
    suba = tk.Toplevel()
    suba.title ("Add your schedule")
    suba.geometry("650x160+400+300")
    
    #subject
    sub_text = tk.Label(suba, text = "Title:")
    sub_text.grid(row = 2, column = 0)
    sub_in = tk.Entry(suba, width = 70)
    sub_in.grid(row = 2, column = 1, columnspan=10, padx = 10, pady = 10)
    
    #content
    con_text = tk.Label (suba, text = "Content:")
    con_text.grid(row = 3, column = 0)
    con_in = tk.Entry(suba, width = 70)
    con_in.grid(row = 3, column = 1, columnspan=10)   
    
    #time
    time_text = tk.Label (suba, text = "Time (d/m/yyyy):")
    time_text.grid(row = 4, column = 0, padx = 10, pady = 3)
    
    day_text = tk.Label (suba, text = "  ")
    day_text.grid(row = 4, column = 1)
    time_day_in = tk.Entry(suba)
    time_day_in.grid(row = 4, column = 2)
    
    month_text = tk.Label (suba, text = "  ")
    month_text.grid(row = 4, column = 3)
    time_month_in = tk.Entry(suba)
    time_month_in.insert(0,f"{T.tm_mon}")
    time_month_in.grid(row = 4, column = 4)
    
    year_text = tk.Label (suba, text = "  ")
    year_text.grid(row = 4, column = 5)
    time_year_in = tk.Entry(suba)
    time_year_in.insert(0,f"{T.tm_year}")
    time_year_in.grid(row = 4, column = 6)
    
    #defalyear = tk.Label(suba, text = ' (Default: current year) ')
    #defalyear.grid(row = 4, column = 7)
    
    # superior choice
    p_text = tk.Label(suba, text = "Enable Priority order:")
    p_text.grid(row = 5, column = 0)
    
    v = tk.IntVar()
    tk.Radiobutton(suba, text = "Yes", variable = v, value = 1).grid(row = 5, column = 2)
    tk.Radiobutton(suba, text = 'No' , variable = v, value = 2).grid(row = 5, column = 4)

    # Input data and quit function
    def con_suba (da1, mon1, ye1, sub1, cont1):
        #file check
        while True:
            try:
                df = pd.read_excel(f"{ye1}_{mon1}.xlsx")
                break
            except:
                head = {"day" : range(1,month[mon1]+1), 
                        "sub_f": None, "con_f": None, 
                        "sub_s" : None, "con_s": None,
                        "sub_t": None, "con_t": None}
                df = pd.DataFrame(head)
                df.to_excel(f"{ye1}_{mon1}.xlsx", index=True) #index = day - 1
                
        #data write in
        df.at[int(da1)-1, "sub_f"] = sub1
        df.at[int(da1)-1, "con_f"] = cont1
        df.to_excel(f"{ye1}_{mon1}.xlsx", index = False)

        #quit function
        quit_suba()
        top.destroy()
        main()

    # Quit function
    def quit_suba ():
        suba.destroy()
        suba.update()
        
    # Confirm botton
    tk.Button(suba, text = "Confirm", command = lambda: con_suba(da1 = time_day_in.get(), 
                                                                 mon1 = time_month_in.get(), 
                                                                 ye1 = time_year_in.get(),
                                                                 sub1 = sub_in.get(),
                                                                 cont1 = con_in.get())
              ).grid(row = 7, column = 2)
    
    # Cancel botton
    tk.Button(suba, text = "Cancel", command = quit_suba).grid(row = 7, column = 5)

def de():
    subc = tk.Toplevel()
    subc.title ("Delete your schedule")

def main():
    global top
    # main interface
    top = tk.Tk()
    top.title ("Calendar")
    top.iconbitmap("calendar.ico")
    top.geometry("1130x780+180+12")
    
    #check the front page file
    while True:
        try:
            cur = pd.read_excel(f"{T.tm_year}_{T.tm_mon}.xlsx")
            break
        except:
            head = {"day" : range(1,month[str(T.tm_mon)]+1), 
                        "sub_f": None, "con_f": None, 
                        "sub_s" : None, "con_s": None,
                        "sub_t": None, "con_t": None}
            cur = pd.DataFrame(head)
            cur.to_excel(f"{T.tm_year}_{T.tm_mon}.xlsx", index=True) #index = day - 1
            
    # Top information
    time_r = f"Current time：{T.tm_year} / {T.tm_mon} / {T.tm_mday}"
    tk.Label(top, text = time_r, font=("Arial", 14)).grid(row = 0, column = 0, columnspan=2)

    frame_m = tk.Frame(top, borderwidth=1, width = 30, height = 10, relief = "solid")
    tk.Label(frame_m,text = week[0]).pack(padx=50, pady=5)
    frame_m.grid(row = 1, column = 0)

    frame_tu = tk.Frame(top, borderwidth=1, width = 30, height = 10, relief = "solid")
    tk.Label(frame_tu,text = week[1]).pack(padx=50, pady=5)
    frame_tu.grid(row = 1, column = 1)

    frame_w = tk.Frame(top, borderwidth=1, width = 30, height = 10, relief = "solid")
    tk.Label(frame_w,text = week[2]).pack(padx=45, pady=5)
    frame_w.grid(row = 1, column = 2)

    frame_th = tk.Frame(top, borderwidth=1, width = 30, height = 10, relief = "solid")
    tk.Label(frame_th,text = week[3]).pack(padx=50, pady=5)
    frame_th.grid(row = 1, column = 3)

    frame_f = tk.Frame(top, borderwidth=1, width = 30, height = 10, relief = "solid")
    tk.Label(frame_f,text = week[4]).pack(padx=58, pady=5)
    frame_f.grid(row = 1, column = 4)

    frame_sa = tk.Frame(top, borderwidth=1, width = 30, height = 10, relief = "solid")
    tk.Label(frame_sa,text = week[5]).pack(padx=50, pady=5)
    frame_sa.grid(row = 1, column = 5)
    
    frame_su = tk.Frame(top, borderwidth=1, width = 30, height = 10, relief = "solid")
    tk.Label(frame_su,text = week[6]).pack(padx=55, pady=5)
    frame_su.grid(row = 1, column = 6)
    
    #The two buttons
    tk.Button (top, text = "Add Schedule", borderwidth=5, relief="raised", command = add).grid(row = 0, column = 5)
    tk.Button (top, text = "Delete / Edit Schedule", borderwidth=5, relief="raised", command = de).grid(row = 0, column = 6)
    
    # generate the grid of days in current month
    dd = 0
    row_num = 2
    first_day = f"{T.tm_year}-{T.tm_mon}-01"
    time_struct = time.strptime(first_day,"%Y-%m-%d")
    startday = time_struct.tm_wday
    while dd < month[str(T.tm_mon)]:
        frame1 = tk.Frame(top,borderwidth=5, width=160, height=140, relief = "groove")
        frame1.grid(row = row_num, column = startday)
        
        # to get rid of the "NaN" text
        if pd.isnull(cur.at[dd,"sub_f"]):
            current = ""
        else:
            current = cur.at[dd,"sub_f"]
        
        #show the label
        tk.Label(frame1,text = current).place(x = 0, y = 20)
        startday += 1
        dd += 1
        number_label = tk.Label(frame1,text = str(dd))
        number_label.place(x=0 , y=0)
        if startday == 7:
            row_num += 1
            startday = 0
    
    #GUI output
    top.mainloop()

################################ code start from below ################################
if __name__ == "__main__":
    main()

