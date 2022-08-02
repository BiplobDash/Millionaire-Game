# Millionaire Game Project
from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

mixer.init()
mixer.music.load("Image Folder/kbc.mp3")
mixer.music.play(-1)

def select(event):
    callButton.place_forget()

    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarLabelA.place_forget()
    progressbarLabelB.place_forget()
    progressbarLabelC.place_forget()
    progressbarLabelD.place_forget()

    b=event.widget
    value = b['text']

    for i in range(15):
        if value == correct_answer[i]:
            if value == correct_answer[14]:
                def Close():
                    window2.destroy()
                    window.destroy()

                def PlayAgain():
                    Life_Line_50_Button.config(state=NORMAL, image=Image_50)
                    Audience_Pole_Button.config(state=NORMAL, image=Audience_Pole)
                    PhoneAFriend_Button.config(state=NORMAL, image=PhoneAFriend_Image)

                    window2.destroy()
                    Question_Area.delete(1.0, END)
                    Question_Area.insert(my_questions[0])

                    optionButton1.config(text=option1[0])
                    optionButton2.config(text=option2[0])
                    optionButton3.config(text=option3[0])
                    optionButton4.config(text=option4[0])

                    Amount_Label.config(imgage=Amount_Image)

                mixer.music.stop()
                mixer.music.load("Image Folder/Kbcwon.mp3")
                mixer.music.play()

                window2 = Toplevel()
                window2.config(bg="black")
                window2.geometry('500x400+140+30')
                window2.title('You Won 0 Pounds')
                imgLabel = Label(window2, image=Center_Image, bd=0)
                imgLabel.pack(pady=30)

                winLabel = Label(window2, text="You Won", font=("Arial", 40, "bold"), bg="black", fg="white")
                winLabel.pack()

                playagainButton = Button(window2, text="Play Again", font=("Arial", 20, "bold"), bg="black", fg="white",
                                        activebackground="black", activeforeground="white", bd=0, cursor="hand2",
                                        command=PlayAgain)
                playagainButton.pack()

                closeButton = Button(window2, text="Close", font=("Arial", 20, "bold"), bg="black", fg="white",
                                     activebackground="black", activeforeground="white", bd=0, cursor="hand2",
                                     command=Close)
                closeButton.pack()

                happyImages = PhotoImage(file="Image Folder/happy.png")
                happyLabel = Label(window2, image=happyImages, bg="black")
                happyLabel.place(x=30, y=280)

                happyLabel1 = Label(window2, image=happyImages, bg="black")
                happyLabel1.place(x=400, y=280)

                window2.mainloop()
                break


            Question_Area.delete(1.0, END)
            Question_Area.insert(END, my_questions[i + 1])

            optionButton1.config(text=option1[i + 1])
            optionButton2.config(text=option2[i + 1])
            optionButton3.config(text=option3[i + 1])
            optionButton4.config(text=option4[i + 1])

            Amount_Label.config(image=Amount_Images[i])

        if value not in correct_answer:
            def Close():
                window1.destroy()
                window.destroy()

            def TryAgain():
                Life_Line_50_Button.config(state=NORMAL, image=Image_50)
                Audience_Pole_Button.config(state=NORMAL, image=Audience_Pole)
                PhoneAFriend_Button.config(state=NORMAL, image=PhoneAFriend_Image)

                window1.destroy()
                Question_Area.delete(1.0, END)
                Question_Area.insert(my_questions[0])

                optionButton1.config(text=option1[0])
                optionButton2.config(text=option2[0])
                optionButton3.config(text=option3[0])
                optionButton4.config(text=option4[0])

                Amount_Label.config(imgage=Amount_Image)


            window1 = Toplevel()
            window1.overrideredirect(True)
            window1.config(bg="black")
            window1.geometry('500x400+140+30')
            window1.title('You Won 0 Pounds')
            imgLabel = Label(window1, image=Center_Image, bd=0)
            imgLabel.pack(pady=30)

            loseLabel = Label(window1, text="You Lose", font=("Arial", 40, "bold"), bg="black", fg="white")
            loseLabel.pack()

            tryagainButton = Button(window1, text="Try Again", font=("Arial", 20, "bold"), bg="black", fg="white",
                                    activebackground="black", activeforeground="white", bd=0, cursor="hand2",
                                    command=TryAgain)
            tryagainButton.pack()

            closeButton = Button(window1, text="Close", font=("Arial", 20, "bold"), bg="black", fg="white",
                                    activebackground="black", activeforeground="white", bd=0, cursor="hand2",
                                 command=Close)
            closeButton.pack()

            sadImages = PhotoImage(file="Image Folder/sad.png")
            sadLabel = Label(window1, image=sadImages, bg="black")
            sadLabel.place(x=30, y=280)

            sadLabel1 = Label(window1, image=sadImages, bg="black")
            sadLabel1.place(x=400, y=280)

            window1.mainloop()
            break

def lifeLine50():

    Life_Line_50_Button.config(image=Image_50x, state=DISABLED)

    if Question_Area.get(1.0, "end-1c") == my_questions[0]:
        optionButton1.config(text="")
        optionButton4.config(text="")

    if Question_Area.get(1.0, "end-1c") == my_questions[1]:
        optionButton2.config(text="")
        optionButton3.config(text="")

    if Question_Area.get(1.0, "end-1c") == my_questions[2]:
        optionButton1.config(text="")
        optionButton2.config(text="")

    if Question_Area.get(1.0, "end-1c") == my_questions[3]:
        optionButton2.config(text="")
        optionButton4.config(text="")

    if Question_Area.get(1.0, "end-1c") == my_questions[4]:
        optionButton3.config(text="")
        optionButton4.config(text="")

    if Question_Area.get(1.0, "end-1c") == my_questions[5]:
        optionButton2.config(text="")
        optionButton4.config(text="")

    if Question_Area.get(1.0, "end-1c") == my_questions[6]:
        optionButton2.config(text="")
        optionButton3.config(text="")

    if Question_Area.get(1.0, "end-1c") == my_questions[7]:
        optionButton2.config(text="")
        optionButton3.config(text="")


def audiencePoleLifeLine():
    Audience_Pole_Button.config(image=Audience_Polex, state=DISABLED)


    progressbarA.place(x=580, y=190)
    progressbarB.place(x=620, y=190)
    progressbarC.place(x=660, y=190)
    progressbarD.place(x=700, y=190)

    progressbarLabelA.place(x=580, y=320)
    progressbarLabelB.place(x=620, y=320)
    progressbarLabelC.place(x=660, y=320)
    progressbarLabelD.place(x=700, y=320)

    if Question_Area.get(1.0, "end-1c") == my_questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=70)

    if Question_Area.get(1.0, "end-1c") == my_questions[1]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=30)
        progressbarD.config(value=70)

    if Question_Area.get(1.0, "end-1c") == my_questions[2]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=70)

    if Question_Area.get(1.0, "end-1c") == my_questions[3]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=30)
        progressbarD.config(value=70)

    if Question_Area.get(1.0, "end-1c") == my_questions[4]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=50)
        progressbarD.config(value=70)

    if Question_Area.get(1.0, "end-1c") == my_questions[5]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=70)
        progressbarD.config(value=30)

    if Question_Area.get(1.0, "end-1c") == my_questions[6]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=30)
        progressbarD.config(value=70)


def PhoneLifeLine():
    mixer.music.load('Image Folder/calling.mp3')
    mixer.music.play()
    callButton.place(x=70, y=260)
    PhoneAFriend_Button.config(image=PhoneAFriend_Imagex, state=DISABLED)

def phoneclick():
    for i in range(15):
        if Question_Area.get(1.0, "end-1c") == my_questions[i]:
            engine.say(f"The Answer is {correct_answer[i]}")
            engine.runAndWait()

correct_answer = ["93 million", "Moth", "Isaac Newton", "Lesotho",
                  "Peru", "C", "Van Rossum", "1989", "100 billion",
                  "Baghdad", "Six iron", "Johannes Kepler","Trees", "1949", "1815"]









my_questions = ["The Earth is approximately how many miles away from the Sun?",
                "Which insect shorted out an early supercomputer and inspired the term 'computer bug'?",
                "Which of the following men does not have a chemical element named for him?",
                "Which of the following landlocked countries is entirely contained within another country?",
                "In the children’s book series, where is Paddington Bear originally from?",
                " Python is written in which language?",
                "Python was developed by",
                "Python was developed in which year?",
                "According to the Population Reference Bureau, what is the approximate number of people who have ever lived on earth?",
                "Now used to refer to a cat, the word 'tabby' is derived from the name of a district of what world capital?",
                "What club did astronaut Alan Shepard use to make his famous golf shot on the moon?",
                "What scientist first determined that human sight results from images projected onto the retina?",
                "If you planted the seeds of Quercus robur, what would grow?",
                "When did Mao Zedong come to power?",
                "What year did the War of 1812 end?"
                ]

option1 = ["9.3 million", "Moth",
           "Albert Einstein", "Lesotho",
           "India", "C", "Van Rossum",
           "1972", "5o billion", "Baghdad",
           "Nine iron", "Galileo", "Trees", "1947", "1813"]


option2 = ["39 million", "Roach",
           "Niels Bohr", "Burkina Faso",
           "Peru", "C++",
           "James Gosling",
           "1995", "100 billion",
           "New Delhi", "Sand wedge",
           "Copernicus", "Flowers", "1948", "1815"]

option3 = ["93 million", "Fly",
           "Isaac Newton", "Mongolia",
           "Canada", "Java",
           "Dennis Ritchie", "1989",
           "1 trillion", "Cairo",
           "Six iron", "Johannes Kepler",
           "Vegetables", "1949", "1817"]

option4 = ["193 million", "Japanese beetle",
           "Enrico Fermi", "Luxembourg",
           "Iceland", "None of the above",
           "Bjarne Stroustrup", "1981",
           "5 trillion", "Moscow",
           "Seven iron", "Isaac Newton", "Grain", "1950", "1821"]











# WINDOW SETUP
window = Tk()
window.geometry('1270x652+0+0')
window.title("Who Wants To Be a Millionaire Created By BiPLoB DAsH")
window.config(bg="black")

# CREATE FRAME
Left_Frame = Frame(window, bg="black", padx=90)
Left_Frame.grid(row=0, column=0)

Top_Frame = Frame(Left_Frame, bg="black", pady=15)
Top_Frame.grid()

Center_Frame = Frame(Left_Frame, bg="black", pady=15)
Center_Frame.grid(row=1, column=0)

Bottom_Frame = Frame(Left_Frame)
Bottom_Frame.grid(row=2, column=0)

Right_Frame = Frame(window, pady=25, padx=50, bg="black")
Right_Frame.grid(row=0, column=1)


# TOP PHOTO SETUP
Image_50 = PhotoImage(file="Image Folder/50-50.png")
Image_50x = PhotoImage(file="Image Folder/50-50-X.png")
Audience_Pole = PhotoImage(file="Image Folder/audiencePole.png")
Audience_Polex = PhotoImage(file="Image Folder/audiencePoleX.png")
PhoneAFriend_Image = PhotoImage(file="Image Folder/phoneAFriend.png")
PhoneAFriend_Imagex = PhotoImage(file="Image Folder/phoneAFriendX.png")

# TOP BUTTON CREATED
# Life Line Button
Life_Line_50_Button = Button(Top_Frame, image= Image_50, bg="black", bd=0, activebackground="black", width=180, height=80, command=lifeLine50)
Life_Line_50_Button.grid(row=0, column=0)

# Audience Pole Button
Audience_Pole_Button = Button(Top_Frame, image= Audience_Pole, bg="black", bd=0, activebackground="black", width=180, height=80,
                              command=audiencePoleLifeLine)
Audience_Pole_Button.grid(row=0, column=1)

# Phone A Friend Button
PhoneAFriend_Button = Button(Top_Frame, image= PhoneAFriend_Image, bg="black", bd=0, activebackground="black", width=180, height=80,
                             command=PhoneLifeLine)
PhoneAFriend_Button.grid(row=0, column=2)

callimage = PhotoImage(file="Image Folder/phone.png")
callButton = Button(window, image=callimage, bd=0, bg="black", activebackground="black", cursor='hand2', command=phoneclick)


# CENTER PHOTO SETUP
Center_Image = PhotoImage(file="Image Folder/center.png")

# Center Label
Center_Label = Label(Center_Frame, image = Center_Image, bg="black", width=300, height=200)
Center_Label.grid(row=0, column=0)


# RIGHT PHOTO SETUP
Amount_Image = PhotoImage(file="Image Folder/Picture0.png")
Amount_Image1 = PhotoImage(file="Image Folder/Picture1.png")
Amount_Image2 = PhotoImage(file="Image Folder/Picture2.png")
Amount_Image3 = PhotoImage(file="Image Folder/Picture3.png")
Amount_Image4 = PhotoImage(file="Image Folder/Picture4.png")
Amount_Image5 = PhotoImage(file="Image Folder/Picture5.png")
Amount_Image6 = PhotoImage(file="Image Folder/Picture6.png")
Amount_Image7 = PhotoImage(file="Image Folder/Picture7.png")
Amount_Image8 = PhotoImage(file="Image Folder/Picture8.png")
Amount_Image9 = PhotoImage(file="Image Folder/Picture9.png")
Amount_Image10 = PhotoImage(file="Image Folder/Picture10.png")
Amount_Image11 = PhotoImage(file="Image Folder/Picture11.png")
Amount_Image12 = PhotoImage(file="Image Folder/Picture12.png")
Amount_Image13 = PhotoImage(file="Image Folder/Picture13.png")
Amount_Image14 = PhotoImage(file="Image Folder/Picture14.png")
Amount_Image15 = PhotoImage(file="Image Folder/Picture15.png")

Amount_Images = [Amount_Image1, Amount_Image2, Amount_Image3, Amount_Image4, Amount_Image5, Amount_Image6,
                 Amount_Image7, Amount_Image8, Amount_Image9, Amount_Image10, Amount_Image11, Amount_Image12,
                 Amount_Image13, Amount_Image14, Amount_Image15]

# Right Label
Amount_Label = Label(Right_Frame, image = Amount_Image, bg="black")
Amount_Label.grid(row=0, column=0)


# BOTTOM PHOTO SETUP
Layout_Image = PhotoImage(file="Image Folder/lay.png")

# Bottom Label
Layout_Label = Label(Bottom_Frame, image= Layout_Image, bg="black")
Layout_Label.grid(row=0, column=0)


# QUESTION AREA
Question_Area = Text(Bottom_Frame, font=("Arial", 14, "bold"), width=40, height=2, wrap="word", bg="black", fg="white", bd=0)
Question_Area.place(x=70, y=10)
Question_Area.insert(END, my_questions[0])

labelA = Label(Bottom_Frame, text="A:", bg="black", fg="white", font=("Arial", 16, "bold"))
labelA.place(x=60, y=110)
optionButton1 = Button(Bottom_Frame, text=option1[0], font=("Arial", 13, "bold"), bg="black", fg="white", bd=0, activebackground="black",
                       activeforeground="white", cursor="hand2", padx=9, pady=9)
optionButton1.place(x=100, y=100)

labelB = Label(Bottom_Frame, text="B:", bg="black", fg="white", font=("Arial", 16, "bold"))
labelB.place(x=330, y=110)
optionButton2 = Button(Bottom_Frame, text=option2[0], font=("Arial", 13, "bold"), bg="black", fg="white", bd=0, activebackground="black",
                       activeforeground="white", cursor="hand2", padx=9, pady=9)
optionButton2.place(x=370, y=100)

labelC = Label(Bottom_Frame, text="C:", bg="black", fg="white", font=("Arial", 16, "bold"))
labelC.place(x=60, y=190)
optionButton3 = Button(Bottom_Frame, text=option3[0], font=("Arial", 13, "bold"), bg="black", fg="white", bd=0, activebackground="black",
                       activeforeground="white", cursor="hand2", padx=9, pady=9)
optionButton3.place(x=100, y=180)

labelD = Label(Bottom_Frame, text="D:", bg="black", fg="white", font=("Arial", 16, "bold"))
labelD.place(x=330, y=190)
optionButton4 = Button(Bottom_Frame, text=option4[0], font=("Arial", 13, "bold"), bg="black", fg="white", bd=0, activebackground="black",
                       activeforeground="white", cursor="hand2", padx=9, pady=9)
optionButton4.place(x=370, y=180)


progressbarA = Progressbar(window, orient=VERTICAL, length=120)
progressbarB = Progressbar(window, orient=VERTICAL, length=120)
progressbarC = Progressbar(window, orient=VERTICAL, length=120)
progressbarD = Progressbar(window, orient=VERTICAL, length=120)


progressbarLabelA = Label(window, text="A", font=("Arial", 20, "bold"), bg="black", fg="white")
progressbarLabelB = Label(window, text="B", font=("Arial", 20, "bold"), bg="black", fg="white")
progressbarLabelC = Label(window, text="C", font=("Arial", 20, "bold"), bg="black", fg="white")
progressbarLabelD = Label(window, text="D", font=("Arial", 20, "bold"), bg="black", fg="white")


optionButton1.bind("<Button-1>", select)
optionButton2.bind("<Button-1>", select)
optionButton3.bind("<Button-1>", select)
optionButton4.bind("<Button-1>", select)




window.mainloop()