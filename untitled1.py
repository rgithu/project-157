from tkinter import *
from PIL import ImageTk,Image

root=Tk()

root.geometry("600x500")
root.title("Endless Pokemon  game")

root.configure(background="orange")
abra=ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender=ImageTk.PhotoImage(Image.open("charmender.jpg"))
iyvasour=ImageTk.PhotoImage(Image.open("iyvasour.jpg"))
jigglypuff=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra=ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth=ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras=ImageTk.PhotoImage(Image.open("paras.jpg"))
persion=ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratata=ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle=ImageTk.PhotoImage(Image.open("squirtle.jpg"))

player1=Label(root,text="Player 1",bg="royal blue",fg="white")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player2=Label(root,text="Player 2",bg="royal blue",fg="white")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)

player1_label_score=Label(root,bg="royal blue",fg="white")
player1_label_score.place(relx=0.1,rely=0.4,anchor=CENTER)

player2_label_score=Label(root,bg="royal blue",fg="white")
player2_label_score.place(relx=0.9,rely=0.4,anchor=CENTER)

random_pokemon_label=Label(root,bg="orange",fg="white")
random_pokemon_label.place(relx=0.5,rely=0.5,anchor=CENTER)

random_power_list = [30,60,50,100,70,70,60,90,40,70,200,40,50]
random_pokemon_list = [abra,bulbasour,charmender,iyvasour,jigglypuff,kadabra,meowth,nidoking,paras
                       ,persion,pikachu,ratata,squirtle]
random_power_list2 = [30,60,50,100,70,70,60,90,40,70,200,40,50]

player1_score = 0
def player1():
    global player1_score
    random_pokemon_label["text"] = "Player 1 pokemon Random Number : " + str(random_power_list)
    player1_score = player1_score + random_power_list
    player_1_score_label["text"] = str( player1_score)
    
player_1_btn = Button(root, image = random_pokemon_label, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6 , anchor =  CENTER)
    
player2_score = 0
def player2():
    global player2_score
    random_no2 = random.randint(1,6)
    random_pokemon_label["text"] = "Player 2 pokemon Random Number : " + str(random_power_list2)
    player2_score = player2_score + random_power_list
    player_2_score_label["text"] = str( player2_score)
    


player_2_btn = Button(root, image = random_pokemon_list, command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6 , anchor =  CENTER)
root.mainloop()