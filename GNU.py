### START CODE
from csv import DictWriter
import os
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk


root = Tk()
root.title('GUI')



### CREATE LABELS
name_lable = ttk.Label(root , text='Enter Your Name : ')
age_lable = ttk.Label(root , text='Enter Your Age :')
email_lable = ttk.Label(root , text = 'Enter Your Email :')
gender_leble = ttk.Label(root , text = 'Select Your Gender')



### SHOW KRVA MATE ,,, METHOD ,,,---> pack,grid
name_lable.grid(row=0, column=0 , sticky=W)         ### W FOR WEST
age_lable.grid(row=2,column=0, sticky=W)
email_lable.grid(row=1,column=0, sticky=W)
gender_leble.grid(row=3 , column=0 , sticky=W)



### ENTRY BOX / TAXT BOX FOR USER ENTER
name_var = StringVar()   ### USER A ENTER KRELI VALUE STORE KRVA MATE TEMPORORY VARIABL BANAVYO 6
name_enterybox = ttk.Entry(root , width = 15, textvariable = name_var)
name_enterybox.grid(row = 0 , column = 1 )
name_enterybox.focus()          ### BY DEFAULT CURSOR NU FOCUSE AA BOX PR RAKHVA MATE ,,, BAKI MANUALI CLICK KRVU PADE KYAY NA AAVE CURSOR

email_var = StringVar()   ### USER A ENTER KRELI VALUE STORE KRVA MATE TEMPORORY  VARIABL BANAVYO 6
email_enterybox = ttk.Entry(root , width = 15, textvariable = email_var)
email_enterybox.grid(row = 1 , column = 1 )

age_var = StringVar()   ### AGE MATE """INTVAT""" DATA TYPE PN LAISAKIYE
age_enterybox = ttk.Entry(root , width = 15, textvariable = age_var)
age_enterybox.grid(row = 2 , column =  1 )



### CREATE A COMBO BOX
gender_var = StringVar()        ### J GENDER SELECT KRE TENI VALUE TEMPORARY VARIABLE MA STORE KRI 6
gender_combobox = ttk.Combobox(root , width = 12 , textvariable = gender_var , state='readonly')    ### "state" THI NAKKI KRVANU K USER TEMA ENTER KRI SAKSE K KHALI SELECT J ,,, AHI KHALI SELECT
gender_combobox['values'] = ('male' , 'femal' , 'other')        ### BOX MA J VALUE AAPDE USER NE SELECT KRVA MATE DEVI 6 A
gender_combobox.current(0)          ### COMBO BOX MA BY DEFAULD UPPE J VALUE BATADVI HOI TE VALUE NO INDEX NUMBER UPPR MA TUPPLE MA JYA HOI TYA
gender_combobox.grid(row = 3 , column = 1)



### CREATE RADIO BUTTON
usertype_var = StringVar()
usertype1 = ttk.Radiobutton(root , text='Student' , value='Student' , variable = usertype_var)      ### "value" J VALUE AAPDE TEMPORARY VARIABLE MA ADD KRVA MAGTA HOI TE TYA ENTER KRVAANI TE KAYAY USER NE BATADVA MATE NATHI
usertype1.grid(row = 4 , column = 0)

usertype2 = ttk.Radiobutton(root , text='Teacher' , value='Teacher' , variable = usertype_var)      ### "variable" J 6 A  SAME J RESE BECAUSE JYARE USER BIJU SELECT KRE TO PELLU UNSELECT THAI JAI
usertype2.grid(row = 4 , column = 1)



### CREATE A CHECK BUTTON
check_button_var = IntVar()         ### AAMA JO USER TICK KRE TO "1" STORE THAI BAKI "0"
check_button = ttk.Checkbutton(root , text = 'check if you want to subscribe to our newslatter' , variable = check_button_var)
check_button.grid(row = 5 , columnspan = 3)         ### "columnspan" J PELLI J COLUMN NE MOTI NA KRE BUT JO JAGYA GHATE TO NEXT COLUMN USE KRI LYE "text" BATADVA MATE



### CREATE SUBMIT BUTTON
### BUTTON MA J ACTION THAI A NAME NU FUNCTION BANAVVANU 
### ACTION CALL THAI JYARE BUTTON PR CLICK KRE 
def action():                          ### FUCTION NU NAME KAI PN RAKHI SAKIYE
    username = name_var.get()       ### NVA VARIABLE MA J VALUE ENTER KRI HOI A STORE KRVANI TEMPORORY MATHI LAI NE
    userage = age_var.get()
    usermail = email_var.get()
    usergender = gender_var.get()
    usertype = usertype_var.get()
    if check_button_var.get() == 0:
        subscribed = 'no'
    else:
        subscribed = 'yes'

    # print(f" user name is {username} and age is {userage} and Email id is {usermail} , {username} is {usertype} and {usergender} , news latter subscription = {subscribed} ")

    # with open('F:/hey/extra/file.txt' , 'a') as f:
    #     f.write(f' {username},{userage},{usermail},{usergender},{usertype},{subscribed} \n')

    ### WRITE TO CSV FILE
    with open('F:/hey/extra/file.csv', 'a' ,newline='') as f:
        dict_writer = DictWriter(f , fieldnames=['name\t','age\t','email\t','type\t','gender\t','subscription'])
        if os.stat('F:/hey/extra/file.csv').st_size == 0:
            dict_writer.writeheader()
        dict_writer.writerows([{'name\t' : username,'age\t' : userage ,'email\t' : usermail , 'type\t' : usertype , 'gender\t' : usergender , 'subscription' : subscribed}])

    name_enterybox.delete(0 , END)      ### ENTRY BOX MA J USR A LAKHYU HOI TE CLEAR KRVA MATE
    age_enterybox.delete(0,END)
    email_enterybox.delete(0,END)

    name_lable.configure(foreground='green')    ### J LABLE AAPYU 6 TENO COLOUR CHANGE KRVA MATE ,,, AAPDNE MAN THAI A COLOUR ADD KRI SAKIYE TENA MATE TENI HACS VALUE GOOGLE MATHI LAI LEVANI



### CREATE A BUTTON
submit_butten = ttk.Button(root , text = 'Submit' , command = action)   ### BUTTON NO COLOUR CHANGE KRAVO HOI TO SIMPLE METHOD USE KRVANI 'ttk' VADI NAI
submit_butten.grid(row = 6 , column = 0 )







root.mainloop()

