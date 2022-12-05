# Names: Christian Narcia, Jose Ruben Espinoza
#Summary: Cryptography Final, GPA Calcualtions with
#FHE Implementation with server and client.
# Client UI
##################################################
import time
from tkinter import *
from tkinter import messagebox


import client as cl
import socket
import threading
# pip install PyCryptodome



class ClientGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Client")
        self.window.geometry("640x480")
        self.window.configure(background = "black")
        self.window.resizable(False,False)

        # Add image file
        bg = PhotoImage(file="UI_background.png")

        # Show image using label
        wallpaper = Label(self.window, image=bg)
        wallpaper.place(x=0, y=0)

        #Frame
        titleFrame = Frame(self.window, width=30,height=20)
        titleFrame.pack(side=TOP)

        # Grades Frame
        inGrade = Label(self.window, text="Input Grades: ", font=('Helvetica 11 bold'), background='white', relief=FLAT)
        inGrade.pack()
        inGrade.place(x=37, y=32)
        gradeFrame = Frame(self.window, width=30, height=30, bg="#2363FF")
        gradeFrame.pack()
        gradeFrame.place(x=36, y=53)

        # Send Frame
        sendFrame = Frame(self.window, width=30, height=5)
        sendFrame.pack()
        sendFrame.place(x=550, y=420)


        title = Label(titleFrame, width=13, height=1, text= "Average GPA",font=('Helvetica 18 bold'))
        title.pack()

        self.gradeText = Text(gradeFrame,width=20, height=25, font=('Helvetica 10'))
        self.gradeText.pack()

        # Creates GPA LABEL Frame
        self.gpaUpdte = " -- "
        self.gpaFrame = Frame(self.window, width=30, height=5, background='white')
        self.gpaFrame.pack()
        self.gpaFrame.place(x=400, y=158)
        # Creates GPA Label on screen
        self.gpa_lbl()


        self.ThreadVar = {}
        self.count = 0

        # Send Button
        # self.sendBtn = Button(sendFrame, width=5, height= 1,text = "Send", font=("Helvetica 16 bold"), command=self.ValData)
        self.sendBtn = Button(sendFrame, width=5, height=1, text="Send", font=("Helvetica 16 bold"),
                              command=self.callVal)
        self.sendBtn.pack()

        self.window.mainloop()

    def gpa_lbl(self):
        #Places Creates "GPA" Label
        self.gpaLabel = Label(self.gpaFrame, width=4, height=1, text="GPA: ", font=('Helvetica 12 bold'), background='white')
        self.gpaLabel.pack(side=LEFT)

        # GPA Label
        self.gpaLabelNum = Label(self.gpaFrame, width=4, height=1,  text=self.gpaUpdte, font=('Helvetica 12'), background='white')
        self.gpaLabelNum.pack(side=LEFT)
        self.gpaFrame.place(x=400, y=158)

    def processing(self):
        self.proclbl = Label(self.gpaFrame, width=15, height=1, text="Processing...", fg='red',font=('Helvetica 12 bold'), background='white')
        self.proclbl.pack(side=LEFT)
        self.gpaFrame.place(x=370, y=158)


    def statusDisp(self):
        # updates to processing status
        self.gpaLabel.destroy()
        self.gpaLabelNum.destroy()
        self.processing()
        self.sendBtn.config(state=DISABLED)


    def show_GPA(self):
        #updates GPA
        try:
            self.gpaLabel.destroy()
            self.gpaLabelNum.destroy()
        except:
            pass
        self.proclbl.destroy()
        self.gpa_lbl()
        self.sendBtn.config(state=NORMAL)

    def callVal(self):
        self.ThreadVar["Thread{0}".format(self.count)] = threading.Thread(target=self.ValData).start()
        self.count +=1

    def ValData(self):
        # Validates input before sending data
        grades = []
        gradesS = ""
        tempNum = ''
        prob = False
        # clecks if blank
        if self.gradeText.get("1.0",END) != '\n':
            # loops through content
            for i in self.gradeText.get("1.0",END):
                # ignores spaces
                if i != ' ':
                    # every \n is a new number
                    if i == '\n':
                        if tempNum !='':
                            try:
                                int(tempNum)
                            except:
                                prob = self.err()
                                break
                            if int(tempNum)>100:
                                prob = self.err()
                                break
                            grades.append(int(tempNum))
                            gradesS = gradesS+" "+tempNum
                        tempNum = ''
                    if i!='\n':
                        tempNum = tempNum+i

            print(grades)
            if not prob:
                # Sends data
                self.connect(gradesS)


    def err(self):
        # Creates Pop-up error Message
        print("Check input")
        prob = True
        messagebox.showinfo("Error", "Check for invalid grades!")
        return prob

    # For local GPA testing
    # def calGPA(self, grades):
    #     self.statusDisp()
    #
    #     total = 0
    #     gpa = 0
    #     for i in grades:
    #         total = total + i
    #
    #     total = total/ len(grades)
    #     print(total)
    #
    #     if total >= 96:
    #         gpa = 4.0
    #     elif total >= 92:
    #         gpa = 3.7
    #     elif total >= 89:
    #         gpa = 3.3
    #     elif total >= 86:
    #         gpa = 3.0
    #     elif total >= 82:
    #         gpa = 2.7
    #     elif total >= 79:
    #         gpa = 2.3
    #     elif total >= 76:
    #         gpa = 2.0
    #     elif total >= 72:
    #         gpa = 1.7
    #     elif total >= 69:
    #         gpa = 1.3
    #     elif total >= 64:
    #         gpa = 1.0
    #     else:
    #         gpa = 0.0
    #
    #
    #     self.window.update()
    #     sleep(2)
    #     self.gpaUpdte = str(gpa)
    #     #updates GPA Value on window
    #     self.show_GPA()


    def connect(self, grades):
        addr = '34.133.176.136'
        port = 7878
        gpa = " -- "
        # disable sends and change to processing
        self.statusDisp()
        # Connect and send data
        try:
            # Connecting To Server
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((addr, port))
            client.send(grades.encode('utf-8'))
            print("Sent")

        except Exception as e:
            print(e)
            print("Failed to send message to server.")

        # Recieve section
        try:
            gpa = client.recv(1024).decode('utf-8')
            client.close()
        except Exception as e:
            print(e)
            print("Failed to recieve message.")

        # gpa = "3.0"
        # sleep(2)
        print(gpa)
        self.gpaUpdte = gpa
        self.show_GPA()

if __name__ == "__main__":
    ClientGUI()