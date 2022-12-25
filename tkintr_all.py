from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror, showinfo
root = Tk()
root.title('TABE CONTROL')



###     LABLE_FREAM CREATE KRVA MATE
# lf = ttk.Labelframe(root , text = 'add ditales')
# lf.grid(root, row = 6 , column=6)



###     CREATE MANUE 
menubar = Menu(root)
root.config(menu=menubar)       ### ttk vadi method ne show krva mate jem grid vaprta m aama show krva mate aavdi aa method aave


#************************************   SIMPLE MENU BAR    *******************************************************#

# def func():
#     print('func called')
# menubar.add_command(label='save' , command=func)          ### MENU BAR MA LABLE CREATE KRYU
# menubar.add_command(label='save as' , command=func)       ### JYARE TENA PR CLICK THAI TYARE KYU ACTION PERFORM THAI A CREATE KRVANU
# menubar.add_command(label='delete' , command=func)


#***********************************    DROP DOWN MENU BAR  *********************************************************#

file_menu = Menu(menubar , tearoff=0)                ### MAIN MENU NU SUB MENU CREATE KRYU ,,, "tearoff" J SUBMENU NE BAR NA LAVVA DE
def func():
    print('func called')
file_menu.add_command(label='new file' , command=func)      ### SUB MENU MA LABLE ADD KRYA
file_menu.add_command(label='save file' , command=func)      ### SUB MENU MA LABLE ADD KRYA
file_menu.add_separator()                                    ### SUBMENU NA LABLE MA VACHHE LINE MUKVA 
file_menu.add_command(label='delete file' , command=func)      ### SUB MENU MA LABLE ADD KRYA
menubar.add_cascade(label = 'File' , menu = file_menu)        ### SIMPLE MAIN MENU MA BATADTU LABLE


edit_menu = Menu(menubar , tearoff=0)                                   ### MAIN MENU NU SUB MENU CREATE KRYU
def func():
    print('func called')
edit_menu.add_command(label='cut file' , command=func)      ### SUB MENU MA LABLE ADD KRYA
edit_menu.add_command(label='copy file' , command=func)      ### SUB MENU MA LABLE ADD KRYA
edit_menu.add_command(label='past file' , command=func)      ### SUB MENU MA LABLE ADD KRYA
menubar.add_cascade(label = 'EDIT' , menu = edit_menu)        ### SIMPLE MAIN MENU MA BATADTU LABLE



###     CREATE NOTE_BOOK
nb =   ttk.Notebook(root)      ###      NOTE_BOOK CREATE KRI JEMA TAB GOTHVVANI
page1 = ttk.Frame(nb)           ###     PELL TAB CREATE KRI
page2 = ttk.Frame(nb)           ###     BIJI TAB CREATE KRI
nb.add(page1 , text = "first page")     ###     PELLI TAB NE NOTE_BOOK MA ADD KRI
nb.add(page2 , text = 'second page') ###     BIJI TAB NE NOTE_BOOK MA ADD KRI
#nb.grid(row = 0 , column=0,padx = 9 , pady=9)   ###     NOTEBOOK NE SHOW KRI BUT AMA NOTE_BOOK JOTI HOI ATLI J JGYA LYE
nb.pack(expand=True , fill = 'both')    ###     "expand" J VADHANI JETLI SPACE HOI A BDHI COVER KRI LYE ,,, "fill" KAI SIDE EXPAND KRVANI A BATAVE 6 



###     LOOP USE NI CREATE LABLE

l = ['What is your name : ' ,'What is your age : ','What is your gender : ','Contry is : ','State : ','city : ']

for i in range(len(l)):
    cur_lable = 'lable' + str(i)
    cur_lable = ttk.Label(page1, text = l[i])       ###     ROOT NI BDLE J PAGE MA ADD KRVU HOI TE LAKHVANU
    cur_lable.grid(row = i , column=0,sticky=W,padx=3,pady=1)   ###     PADX = LEF/RIGHT ,,, PADY = UP/DOWEN

d = {
    'name' : StringVar(),
    'age' : StringVar(),
    'gender' : StringVar(),
    'country' : StringVar(),
    'state' : StringVar(),
    'city' : StringVar()
}
c = 0
for i,j in d.items():
    cur_entry = i + '_entry'
    cur_entry = ttk.Entry(page1, width= 15 ,textvariable= d[i])
    cur_entry.grid(row = c ,column=1,padx= 3 , pady=1)
    c += 1



### USE MEG BOX
def submit():
    l2 =[]
    for i,j in d.items():
        pr = ((d.get(i)).get())
        if pr == '':
            showerror('ERROR' , f'pls fill {i}')
            l2.clear()
            break
        else:
            if i == 'age':
                try:
                    pr = int(pr)
                except ValueError:
                    showerror('INVELID' , 'pls enter digit in age')
                    l2.clear()
                    break
                if pr < 18:
                    showerror('WARNING','you are enligibale for this')
                    l2.clear()
                    break
            else:
                l2.append(pr)
    if l2 == []:
        pass
    else:
        showinfo('INFO' , 'record store successfully')      ### POP UP MENU KHULI MSG BATAVE ---> "showinfo,showerror,showwarning"
        print(l2)
    
    
    
submit_btn = ttk.Button(page2 , text = 'Submit',command= submit)
submit_btn.grid(row = 7 , columnspan= 3 )



root.mainloop()