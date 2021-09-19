import random
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Osom")

user_score = 0
comp_score = 0
user_input = ""
comp_input = ""

'''USER CHOICE'''

def put_num(choice):
    osom = {'air' : 0, 'batu':1, 'burung':2}
    return osom[choice]

def num_put(choice):
    osom={0:'air',1:'batu',2:'burung'}
    return osom[number]

''' AI CHOICE '''

def ran_comp_choice():
    return random.choice(['air','batu','burung'])

''' TEXT AREA '''
def result(player,pc):
    global user_score
    global comp_score
    user = put_num(player)
    comp = put_num(pc)
    if(user==comp):
        print("Tie")
    elif((user-comp)% 3==1):
        print("You win")
        user_score+=1
    else:
        print("Comp wins")
        comp_score+=1

text_area = tk.Text(master=window,height=12,width=30,bg="#FFFF99")
text_area.grid(column=0,row=4)
answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=user_input,cc=comp_input,u=user_score,c=comp_score)
text_area.insert(tk.END,answer)


''' DEFINE METHOD'''

def air():
    global user_choice
    global comp_choice
    user_choice='air'
    comp_choice=ran_comp_choice()
    result(user_choice,comp_choice)

def batu():
    global user_choice
    global comp_choice
    user_choice='batu'
    comp_choice=ran_comp_choice()
    result(user_choice,comp_choice)

def burung():
    global user_choice
    global comp_choice
    user_choice='burung'
    comp_choice=ran_comp_choice()
    result(user_choice,comp_choice)


button1 = tk.Button(text="       Air       ",bg="skyblue",command=air)
button1.grid(column=0,row=1)
button2 = tk.Button(text="       Batu      ",bg="pink",command=batu)
button2.grid(column=0,row=2)
button3 = tk.Button(text="     Burung     ",bg="lightgreen",command=burung)
button3.grid(column=0,row=3)


window.mainloop()