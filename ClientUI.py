# Names: Christian Narcia, Jose Ruben Espinoza
#Summary: Cryptography Final, GPA Calcualtions with
#FHE Implementation with server and client.
# Client UI
##################################################

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
        # window.configure(background='grey')
        self.window.resizable(False,False)

        #Frame
        titleFrame = Frame(self.window, width=30,height=20)
        titleFrame.pack(side=TOP)

        # Grades Frame
        gradeFrame = Frame(self.window, width=30, height=30)
        gradeFrame.pack(side=LEFT)

        # Send Frame
        sendFrame = Frame(self.window, width=30, height=5)
        sendFrame.pack(anchor=E,side=BOTTOM)


        title = Label(titleFrame, width=10, height=1, text= "Find GPA",font=('Helvetica 18 bold'))
        title.pack()

        self.gradeText = Text(gradeFrame,width=20, height=25, font=('Helvetica 10'))
        self.gradeText.pack(padx=10)

        # Creates GPA LABEL Frame
        self.gpaUpdte = " -- "
        self.gpaFrame = Frame(self.window, width=30, height=5)
        self.gpaFrame.pack()
        self.gpaFrame.place(x=400, y=150)
        # Creates GPA Label on screen
        self.gpa_lbl()


        self.ThreadVar = {}
        self.count = 0

        # Send Button
        # self.sendBtn = Button(sendFrame, width=5, height= 1,text = "Send", font=("Helvetica 16 bold"), command=self.ValData)
        self.sendBtn = Button(sendFrame, width=5, height=1, text="Send", font=("Helvetica 16 bold"),
                              command=self.callVal)
        self.sendBtn.pack(padx=20, pady=20)

        self.window.mainloop()

    def gpa_lbl(self):
        #Places Creates "GPA" Label
        self.gpaLabel = Label(self.gpaFrame, width=4, height=1, text="GPA: ", font=('Helvetica 12 bold'))
        self.gpaLabel.pack(side=LEFT)

        # GPA Label
        self.gpaLabelNum = Label(self.gpaFrame, width=4, height=1,  text=self.gpaUpdte, font=('Helvetica 12'))
        self.gpaLabelNum.pack(side=LEFT)

    def processing(self):
        self.proclbl = Label(self.gpaFrame, width=15, height=1, text="Processing...", fg='red',font=('Helvetica 12 bold'))
        self.proclbl.pack(side=LEFT)

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
        # disable sends and change to processing
        self.statusDisp()

        try:
            # Connecting To Server
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('127.0.0.1', 7878))
            # send data:
            client.send(grades.encode())
            client.close()
        except:
            print("Failed to connect to server.")

        #temp
        gpa= "0.0"
        # wait for server
        # gpa = client.recv(1024).decode()
        # client.close()
        #store gpa for displaying
        self.gpaUpdte = gpa
        self.show_GPA()



if __name__ == "__main__":
    ClientGUI()