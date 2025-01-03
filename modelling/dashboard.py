import csv
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import *
import time
import sys
from chat import get_response
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from predictScore import predictScore, get_insights

class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title("Financial Management System")
        self.window.geometry("1366x750")
        self.window.config(background="#cbd5e1")


        #Window Icon Photo
        icon = PhotoImage(file='images/icon.png')
        self.window.iconphoto(True, icon)

        #Sidebar
        self.sidebar = Frame(self.window, bg = "#0f172a")
        self.sidebar.place(x = 0, y = 0, width = 300, height = 750)

        #Logo
        self.logoImage = Image.open("images/logo.png")
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image=photo, bg="#0f172a")
        self.logo.image = photo
        self.logo.place(x = 45, y = 80, width = 200, height = 200)

        #User Name
        self.user = Label(self.sidebar,text="User", bg="#0f172a", font=("", 15, "bold"),
                          fg="white")
        self.user.place(x = 120, y = 260)

        #Main Frame
        self.mainFrame = Frame(self.window, bg = '#cbd5e1')
        self.mainFrame.place(x = 300, y = 0, width = 1096, height = 720)

        #Initial Frame
        self.showDashBoardPage()

        #Dashboard
        self.dashboardImage = Image.open('images/dashboard.png')
        photo = ImageTk.PhotoImage(self.dashboardImage)
        self.dashboard = Label(self.sidebar, image=photo, bg='#0f172a')
        self.dashboard.image = photo
        self.dashboard.place(x = 50, y = 330)

        self.dashboard_text = Button(self.sidebar, text='Dashboard', bg='#0f172a', fg='white',
                                    bd=0, font=("", 15, "bold"), cursor='hand2', activebackground='#0f172a', command=self.showDashBoardPage)
        self.dashboard_text.place(x=90, y=330)


        #Income
        self.dashboardImage1 = Image.open('images/income.png')
        photo1 = ImageTk.PhotoImage(self.dashboardImage1)
        self.dashboard1 = Label(self.sidebar, image=photo1, bg='#0f172a')
        self.dashboard1.image = photo1
        self.dashboard1.place(x = 50, y = 390)

        self.dashboard_text1 = Button(self.sidebar, text='Income', bg='#0f172a', fg='white',
                                    bd=0, font=("", 15, "bold"), cursor='hand2', 
                                    activebackground='#0f172a', command=self.showIncomePage)
        self.dashboard_text1.place(x = 90, y = 390)


        #Expenses
        self.dashboardImage2 = Image.open('images/expense.png')
        photo2 = ImageTk.PhotoImage(self.dashboardImage2)
        self.dashboard2 = Label(self.sidebar, image=photo2, bg='#0f172a')
        self.dashboard2.image = photo2
        self.dashboard2.place(x = 50, y = 450)

        self.dashboard_text2 = Button(self.sidebar, text='Expenses', bg='#0f172a', fg='white',
                                    bd=0, font=("", 15, "bold"), cursor='hand2', 
                                    activebackground='#0f172a', command=self.showExpensePage)
        self.dashboard_text2.place(x = 90, y = 450)

        #Signout
        self.dashboardImage3 = Image.open('images/signout.png')
        photo3 = ImageTk.PhotoImage(self.dashboardImage3)
        self.dashboard3 = Label(self.sidebar, image=photo3, bg='#0f172a')
        self.dashboard3.image = photo3
        self.dashboard3.place(x = 50, y = 650)

        self.dashboard_text3 = Button(self.sidebar, text='Logout', bg='#0f172a', fg='white',
                                    bd=0, font=("", 15, "bold"), cursor='hand2', activebackground='#0f172a', command=self.exit_page)
        self.dashboard_text3.place(x = 90, y = 650)
        

        #Time and Data
        self.datetimeImage = Image.open('images/date_time.png')
        photo4 = ImageTk.PhotoImage(self.datetimeImage)
        self.date_time_image = Label(self.sidebar, image=photo4, bg= '#0f172a')
        self.date_time_image.image = photo4
        self.date_time_image.place(x = 70, y = 35)

        self.date_time = Label(self.window)
        self.date_time.place(x = 115, y = 35)
        self.show_time()

        #Chatbot
        self.dashboardImage4 = Image.open('images/chatbot.png')
        photo5 = ImageTk.PhotoImage(self.dashboardImage4)
        self.dashboard4 = Label(self.sidebar, image=photo5, bg='#0f172a')
        self.dashboard4.image = photo5
        self.dashboard4.place(x = 50, y = 510)

        self.dashboard_text3 = Button(self.sidebar, text='Chat', bg='#0f172a', fg='white',
                                    bd=0, font=("", 15, "bold"), cursor='hand2', 
                                    activebackground='#0f172a', command=self.showChatbotPage)
        self.dashboard_text3.place(x = 90, y = 510)

    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f" {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0,
                                     bg='#0f172a', fg='white')
        self.date_time.after(100, self.show_time)

    def exit_page(self):
        sys.exit()

    def delete_page(self):
        for frame in self.mainFrame.winfo_children():
            frame.destroy()  

    def showDashBoardPage(self):
        self.delete_page()
        #Body
        self.heading = Label(self.mainFrame, text ='All Transactions', font=("", 30, "bold"), fg = "#111827",
                             bg = "#cbd5e1")
        self.heading.place(x = 20, y = 10)

        #Body Frame 1
        self.bodyFrame1 = Frame(self.mainFrame, bg = "white")
        self.bodyFrame1.place(x = 20, y = 65, width = 1025, height = 390)

        self.create_graph()

        #Body Frame 2
        self.bodyFrame2 = Frame(self.mainFrame, bg = "white")
        self.bodyFrame2.place(x = 20, y = 470, width = 320, height = 140)

        self.text = Label(self.bodyFrame2, text="Expenses", font=("", 15, "bold"), 
                          bg = "white")
        self.text.place(x = 20, y = 10)

        self.expense = Label(self.bodyFrame2, text="00.00", font=("", 40, "bold"), 
                          bg = "white")
        self.expense.place(relx = 0.5, rely = 0.53, anchor = CENTER)
 
        #Body Frame 3
        self.bodyFrame3 = Frame(self.mainFrame, bg = "white")
        self.bodyFrame3.place(x = 375, y = 470, width = 320, height = 140)

        self.text1 = Label(self.bodyFrame3, text="Income", font=("", 15, "bold"), 
                          bg = "white")
        self.text1.place(x = 20, y = 10)

        self.income = Label(self.bodyFrame3, text="00.00", font=("", 40, "bold"), 
                          bg = "white")
        self.income.place(relx = 0.5, rely = 0.53, anchor = CENTER)

        #Body Frame 4
        self.bodyFrame4 = Frame(self.mainFrame, bg = "white")
        self.bodyFrame4.place(x = 725, y = 470, width = 320, height = 140)

        self.text2 = Label(self.bodyFrame4, text="Financial Health Score", font=("", 15, "bold"), 
                          bg = "white")
        self.text2.place(x = 20, y = 10)

        self.score = Label(self.bodyFrame4, text="0", font=("", 40, "bold"), fg="red",
                          bg = "white")
        self.score.place(relx = 0.5, rely = 0.53, anchor = CENTER)

        #Body Frame 5
        self.bodyFrame5 = Frame(self.mainFrame, bg="white")
        self.bodyFrame5.place(x = 20, y = 625, width = 1025, height = 100)

        self.insight = Label(self.bodyFrame5, text="Insight: ", bg="white", font=("", 12, "bold"))
        self.insight.place(x = 20, y = 10)

        self.insightValue = Label(self.bodyFrame5, text="Insight: ", font=("", 15, "bold"),
                                  bg="white", fg="red")
        self.insightValue.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.load_data_from_csv()
        self.predict_score()

    def showIncomePage(self):
        self.delete_page()

        #Body
        self.heading = Label(self.mainFrame, text ='Income', font=("", 25, "bold"), fg = "#111827",
                                bg = "#cbd5e1")
        self.heading.place(x = 20, y = 20)

        #Header
        self.incomeHeader = Frame(self.mainFrame, bg="white")
        self.incomeHeader.place(x = 30, y = 70, height=75, width=1000)

        self.totalIncome = Label(self.incomeHeader, text="Total Income:", bg="white",
                                   fg="black", font=("", 20, "bold"))
        self.totalIncome.place(x = 350, y = 20)

        self.totalIncomeValue = Label(self.incomeHeader, text="0.00", bg="white",
                                   fg="red", font=("", 20, "bold"))
        self.totalIncomeValue.place(x = 540, y = 20)

        #IncomeFrame1
        self.incomeFrame1 = Frame(self.mainFrame, bg="white")
        self.incomeFrame1.place(x = 470, y = 220, height=200, width=520)

        self.salaryLabel = Label(self.incomeFrame1, text="Salary", bg="white", fg="#111827", font=("", 15, "bold"))
        self.salaryLabel.place(x = 140, y = 35)

        self.salaryLabelValue = Label(self.incomeFrame1, text="0.00", bg="white", fg="#111827", font=("", 45, "bold"))
        self.salaryLabelValue.place(x = 200, y = 60)

        self.incomeImage1 = Image.open('images/salary.png')
        photo11 = ImageTk.PhotoImage(self.incomeImage1)
        self.income1 = Label(self.incomeFrame1, image=photo11, bg='white')
        self.income1.image = photo11
        self.income1.place(x = 10, y = 35)

        #IncomeFrame2
        self.incomeFrame2 = Frame(self.mainFrame, bg="white")
        self.incomeFrame2.place(x = 470, y = 450, height=200, width=520)

        self.otherLabel = Label(self.incomeFrame2, text="Other", bg="white", fg="#111827", font=("", 15, "bold"))
        self.otherLabel.place(x = 140, y = 35)

        self.otherLabelValue = Label(self.incomeFrame2, text="0.00", bg="white", fg="#111827", font=("", 45, "bold"))
        self.otherLabelValue.place(x = 200, y = 60)

        self.incomeImage2 = Image.open('images/other.png')
        photo12 = ImageTk.PhotoImage(self.incomeImage2)
        self.income2 = Label(self.incomeFrame2, image=photo12, bg='white')
        self.income2.image = photo12
        self.income2.place(x = 30, y = 60)     

        # ------------------------------------------------------------------------------------------------------------------->

        self.expenseOption = Label(self.mainFrame, text="Record Your Income", bg="#cbd5e1", fg="black", font=("", 20, "bold"))
        self.expenseOption.place(x = 100, y = 190)

        self.expenseOption = Label(self.mainFrame, text="Select Option", bg="#cbd5e1", fg="black", font=("", 15, "bold"))
        self.expenseOption.place(x = 30, y = 240)

        #ComboBox
        expenseType = ["Salary", "Other"]
        self.incomeCombo = ttk.Combobox(self.mainFrame, width=30, values=expenseType, 
                                         font=("", 16, "bold"), justify='center', state='readonly')
        self.incomeCombo.place(x = 38, y = 280)

        self.incomeInput = Label(self.mainFrame, text="Amount", bg="#cbd5e1", fg="black", font=("", 15, "bold"))
        self.incomeInput.place(x = 30, y = 340)

        #Entry
        self.incomeEntry = Entry(self.mainFrame, font=("", 15, "bold"),
                                  borderwidth=1, justify="center")
        self.incomeEntry.place(x = 38, y = 380, height = 40, width=380)

        #Button
        self.addIncome = Button(self.mainFrame, text='Update Income', bg='#0f172a', fg='white',
                                    bd=0, font=("", 15, "bold"), cursor='hand2', 
                                    activebackground='#0f172a', command=self.update_income)
        self.addIncome.place(x = 120, y = 450, height=40, width=200)

        # ------------------------------------------------------------------------------------------------------------------->         
        self.load_data_from_csv_income()

    def showExpensePage(self):
        self.delete_page()

        #Body
        self.heading = Label(self.mainFrame, text ='Expenses', font=("", 25, "bold"), fg = "#111827",
                                bg = "#cbd5e1")
        self.heading.place(x = 20, y = 20)

        #Header
        self.expenseHeader = Frame(self.mainFrame, bg="white")
        self.expenseHeader.place(x = 30, y = 70, height=75, width=1000)

        self.totalExpense = Label(self.expenseHeader, text="Total: Expenses:", bg="white",
                                   fg="black", font=("", 20, "bold"))
        self.totalExpense.place(x = 350, y = 20)

        self.totalExpenseValue = Label(self.expenseHeader, text="0.00", bg="white",
                                   fg="red", font=("", 20, "bold"))
        self.totalExpenseValue.place(x = 580, y = 20)

        #ExpenseFrame1
        self.expenseFrame1 = Frame(self.mainFrame, bg="white")
        self.expenseFrame1.place(x = 450, y = 165, height=90, width=580)

        self.foodLabel = Label(self.expenseFrame1, text="Food", bg="white", fg="#111827", font=("", 12, "bold"))
        self.foodLabel.place(x = 80, y = 35)

        self.foodLabelValue = Label(self.expenseFrame1, text="0.00", bg="white", fg="#111827", font=("", 30, "bold"))
        self.foodLabelValue.place(x = 250, y = 20)

        self.expenseImage1 = Image.open('images/food.png')
        photo6 = ImageTk.PhotoImage(self.expenseImage1)
        self.expense1 = Label(self.expenseFrame1, image=photo6, bg='white')
        self.expense1.image = photo6
        self.expense1.place(x = 30, y = 25)

        #ExpenseFrame2
        self.expenseFrame2 = Frame(self.mainFrame, bg="white")
        self.expenseFrame2.place(x = 450, y = 270, height=90, width=580)

        self.transpoLabel = Label(self.expenseFrame2, text="Transportation", bg="white", fg="#111827", font=("", 12, "bold"))
        self.transpoLabel.place(x = 80, y = 35)

        self.transpoLabelValue = Label(self.expenseFrame2, text="0.00", bg="white", fg="#111827", font=("", 30, "bold"))
        self.transpoLabelValue.place(x = 250, y = 20)

        self.expenseImage2 = Image.open('images/transpo.png')
        photo7 = ImageTk.PhotoImage(self.expenseImage2)
        self.expense2 = Label(self.expenseFrame2, image=photo7, bg='white')
        self.expense2.image = photo7
        self.expense2.place(x = 30, y = 25)

        #ExpenseFrame3
        self.expenseFrame3 = Frame(self.mainFrame, bg="white")
        self.expenseFrame3.place(x = 450, y = 375, height=90, width=580)

        self.liaLabel = Label(self.expenseFrame3, text="Liabilities", bg="white", fg="#111827", font=("", 12, "bold"))
        self.liaLabel.place(x = 80, y = 35)

        self.liaLabelValue = Label(self.expenseFrame3, text="0.00", bg="white", fg="#111827", font=("", 30, "bold"))
        self.liaLabelValue.place(x = 250, y = 20)

        self.expenseImage3 = Image.open('images/lia.png')
        photo8 = ImageTk.PhotoImage(self.expenseImage3)
        self.expense3 = Label(self.expenseFrame3, image=photo8, bg='white')
        self.expense3.image = photo8
        self.expense3.place(x = 30, y = 25)        

        #ExpenseFrame4
        self.expenseFrame4 = Frame(self.mainFrame, bg="white")
        self.expenseFrame4.place(x = 450, y = 480, height=90, width=580)

        self.eleLabel = Label(self.expenseFrame4, text="Electric Bill", bg="white", fg="#111827", font=("", 12, "bold"))
        self.eleLabel.place(x = 80, y = 35)

        self.eleLabelValue = Label(self.expenseFrame4, text="0.00", bg="white", fg="#111827", font=("", 30, "bold"))
        self.eleLabelValue.place(x = 250, y = 20)

        self.expenseImage4 = Image.open('images/electric.png')
        photo9 = ImageTk.PhotoImage(self.expenseImage4)
        self.expense4 = Label(self.expenseFrame4, image=photo9, bg='white')
        self.expense4.image = photo9
        self.expense4.place(x = 30, y = 25)  

        #ExpenseFrame5
        self.expenseFrame5 = Frame(self.mainFrame, bg="white")
        self.expenseFrame5.place(x = 450, y = 585, height=90, width=580)

        self.watLabel = Label(self.expenseFrame5, text="Water Bill", bg="white", fg="#111827", font=("", 12, "bold"))
        self.watLabel.place(x = 80, y = 35)

        self.watLabelValue = Label(self.expenseFrame5, text="0.00", bg="white", fg="#111827", font=("", 30, "bold"))
        self.watLabelValue.place(x = 250, y = 20)

        self.expenseImage5 = Image.open('images/water.png')
        photo10 = ImageTk.PhotoImage(self.expenseImage5)
        self.expense5 = Label(self.expenseFrame5, image=photo10, bg='white')
        self.expense5.image = photo10
        self.expense5.place(x = 30, y = 25)

        # ------------------------------------------------------------------------------------------------------------------->

        self.expenseOption = Label(self.mainFrame, text="Record Your Expense", bg="#cbd5e1", fg="black", font=("", 20, "bold"))
        self.expenseOption.place(x = 100, y = 190)

        self.expenseOption = Label(self.mainFrame, text="Select Option", bg="#cbd5e1", fg="black", font=("", 15, "bold"))
        self.expenseOption.place(x = 30, y = 240)



        #ComboBox
        expenseType = ["Food", "Transportation", "Liabilities", "Electric Bill", "Water Bill"]
        self.expenseCombo = ttk.Combobox(self.mainFrame, width=30, values=expenseType, 
                                         font=("", 16, "bold"), justify='center', state='readonly')
        self.expenseCombo.place(x = 38, y = 280)

        self.expenseInput = Label(self.mainFrame, text="Expense Amount", bg="#cbd5e1", fg="black", font=("", 15, "bold"))
        self.expenseInput.place(x = 30, y = 340)

        #Entry
        self.expenseEntry = Entry(self.mainFrame, font=("", 15, "bold"),
                                  borderwidth=1, justify="center")
        self.expenseEntry.place(x = 38, y = 380, height = 40, width=380)

        #Button
        self.addExpense = Button(self.mainFrame, text='Update Expense', bg='#0f172a', fg='white',
                                    bd=0, font=("", 15, "bold"), cursor='hand2', 
                                    activebackground='#0f172a', command=self.update_expense)
        self.addExpense.place(x = 120, y = 450, height=40, width=200)

        # ------------------------------------------------------------------------------------------------------------------->        
        self.load_data_from_csv_expense()

    ####################################################################################################################
    #----------------------------------------------- Chatbot Page ----------------------------------------------------->
    ####################################################################################################################
    def showChatbotPage(self):
        self.delete_page()
        
        #Body
        self.chatbotImage = Image.open('images/sam.png')
        photo13 = ImageTk.PhotoImage(self.chatbotImage)
        self.headingImage = Label(self.mainFrame, bg = "#cbd5e1", image=photo13)
        self.headingImage.place(x = 400, y = 20)

        self.heading = Label(self.mainFrame, text ='Chat with Bro', font=("", 25, "bold"), fg = "#111827",
                                bg = "#cbd5e1")
        self.heading.image = photo13
        self.heading.place(x = 500, y = 30)

        #Chatbot Frame
        self.chatbot_frame = Frame(self.mainFrame, bg="#cbd5e1")
        self.chatbot_frame.place(x=20, y=80, width=1025, height=720)

        # Chatbox
        self.chatbox = Text(self.chatbot_frame, width=120, height=32, bg="#f8fafc")
        self.chatbox.tag_configure("user", foreground="blue")
        self.chatbox.tag_configure("bot", foreground="red")
        self.chatbox.config(state=DISABLED)
        self.chatbox.place(x = 10, y = 20)

        # Scrollbar
        self.scrollbar = Scrollbar(self.chatbot_frame)
        self.scrollbar.place(relheight=0.71, relx=0.97, y = 23)
        self.scrollbar.configure(command=self.chatbox.yview)

        # Chat Entry
        self.entry = Entry(self.chatbot_frame, width=55, borderwidth=1, font=("", 20))
        self.entry.bind("<Return>", self.send_message)
        self.entry.place(x = 10, y = 550)

        # Send Button
        self.send_button = Button(self.chatbot_frame, text="Send", command=self.send_message, 
                                  bg='#0f172a', fg='white')
        self.send_button.place(x = 872, y = 551, height=35, width=100)

    def send_message(self, event=None):
        message = self.entry.get()
        self.entry.delete(0, END)
        if message != '':
            self.chatbox.config(state=NORMAL)
            self.chatbox.insert(END, "You: " + message + '\n\n', "user")
            time.sleep(0.5)
            response = get_response(message)

            self.chatbox.insert(END, "Bro: " + response + '\n\n', "bot")

    ####################################################################################################################
    #----------------------------------------------- Show Graph ------------------------------------------------------->
    ####################################################################################################################
    def create_graph(self):
        df = pd.read_csv("dataset/financial_data.csv")

        plt.figure(figsize=(6, 4))
        plt.bar(["Monthly Income", "Total Expense"], [df["Monthly Income"][0], df["Total Expense"][0]], color=["#1e40af", "#115e59"])
        plt.xlabel("Categories")
        plt.ylabel("Amount (P)")
        plt.title("Monthly Income vs. Total Expense")

        canvas = FigureCanvasTkAgg(plt.gcf(), self.bodyFrame1)
        canvas.draw()
        canvas.get_tk_widget().pack()

    ####################################################################################################################
    #----------------------------------------------- Update Expense --------------------------------------------------->
    ####################################################################################################################
    def update_expense(self):
        selected_option = self.expenseCombo.get()
        expense_amount = float(self.expenseEntry.get())
            

        if selected_option == "Food":
            self.foodLabelValue.config(text=f"{expense_amount:.2f}")
        elif selected_option == "Transportation":
            self.transpoLabelValue.config(text=f"{expense_amount:.2f}")
        elif selected_option == "Liabilities":
            self.liaLabelValue.config(text=f"{expense_amount:.2f}")
        elif selected_option == "Electric Bill":
            self.eleLabelValue.config(text=f"{expense_amount:.2f}")
        elif selected_option == "Water Bill":
            self.watLabelValue.config(text=f"{expense_amount:.2f}")

        total_expense = (
        float(self.foodLabelValue["text"]) +
        float(self.transpoLabelValue["text"]) +
        float(self.liaLabelValue["text"]) +
        float(self.eleLabelValue["text"]) +
        float(self.watLabelValue["text"])
        )

        self.totalExpenseValue.config(text=f"{total_expense:.2f}")

    #----------------------------------------- Recording the Data to CSV file --------------------------->

        try:
            with open('dataset/dataset/financial_data.csv', 'r', newline='') as csvFileRead:
                reader = csv.DictReader(csvFileRead)
                data = list(reader)
                
            row = data[0]
            if selected_option == "Food":
                row['Food'] = f"{expense_amount:.2f}"
            elif selected_option == "Transportation":
                row['Transportation'] = f"{expense_amount:.2f}"
            elif selected_option == "Liabilities":
                row['Liabilities'] = f"{expense_amount:.2f}"
            elif selected_option == "Electric Bill":
                row['Electric Bill'] = f"{expense_amount:.2f}"
            elif selected_option == "Water Bill":
                row['Water Bill'] = f"{expense_amount:.2f}"

            row['Salary'] = row['Salary']
            row['Other'] = row['Other']
            row['Monthly Income'] = row['Monthly Income']
            row['Total Expense'] = f"{total_expense:.2f}"
                    
            with open('dataset/financial_data.csv', 'w', newline='') as csvfile:
                fieldnames = ["Food", "Transportation", "Liabilities", "Electric Bill", "Water Bill", "Salary", "Other", "Monthly Income", "Total Expense"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(row)

        except FileNotFoundError:
            print("CSV file not found!")
        except Exception as e:
            print("Error occurred while loading data:", str(e))

    ####################################################################################################################
    #--------------------------------------------- Display Data to Dashboard ------------------------------------------>
    ####################################################################################################################            
    def load_data_from_csv(self):
        try:
            with open('dataset/dataset/financial_data.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    total_expense = float(row['Total Expense'])
                    self.expense.config(text=f"{total_expense:.2f}")
                    monthly_income = float(row['Monthly Income'])
                    self.income.config(text=f"{monthly_income:.2f}")

        except FileNotFoundError:
            print("CSV file not found!")
        except Exception as e:
            print("Error occurred while loading data:", str(e))                    

    ####################################################################################################################
    #------------------------------------------ Load Data to Expense Page ---------------------------------------------->
    ####################################################################################################################
    def load_data_from_csv_expense(self):
        try:
            with open('dataset/dataset/financial_data.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.foodLabelValue.config(text=f"{float(row['Food']):.2f}")
                    self.transpoLabelValue.config(text=f"{float(row['Transportation']):.2f}")
                    self.liaLabelValue.config(text=f"{float(row['Liabilities']):.2f}") 
                    self.eleLabelValue.config(text=f"{float(row['Electric Bill']):.2f}")    
                    self.watLabelValue.config(text=f"{float(row['Water Bill']):.2f}")  
                    self.totalExpenseValue.config(text=f"{float(row['Total Expense']):.2f}")      

        except FileNotFoundError:
            print("CSV file not found!")
        except Exception as e:
            print("Error occurred while loading data:", str(e))

    ####################################################################################################################
    #------------------------------------------ Load Data to Income Page ---------------------------------------------->
    ####################################################################################################################
    def load_data_from_csv_income(self):
        try:
            with open('dataset/dataset/financial_data.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.salaryLabelValue.config(text=f"{float(row['Salary']):.2f}")
                    self.otherLabelValue.config(text=f"{float(row['Other']):.2f}")
                    self.totalIncomeValue.config(text=f"{float(row['Monthly Income']):.2f}")     

        except FileNotFoundError:
            print("CSV file not found!")
        except Exception as e:
            print("Error occurred while loading data:", str(e))


    ####################################################################################################################
    #----------------------------------------------- Update Income ---------------------------------------------------->
    ####################################################################################################################
    def update_income(self):
        selected_option = self.incomeCombo.get()
        income_amount = float(self.incomeEntry.get())
            

        if selected_option == "Salary":
            self.salaryLabelValue.config(text=f"{income_amount:.2f}")
        elif selected_option == "Other":
            self.otherLabelValue.config(text=f"{income_amount:.2f}")

        total_income = (
        float(self.salaryLabelValue["text"]) +
        float(self.otherLabelValue["text"])
        )

        self.totalIncomeValue.config(text=f"{total_income:.2f}")

        try:
            with open('dataset/dataset/financial_data.csv', 'r', newline='') as csvFileRead:
                reader = csv.DictReader(csvFileRead)
                data = list(reader)
                
            row = data[0]
            if selected_option == "Salary":
                row['Salary'] = f"{income_amount:.2f}"
            elif selected_option == "Other":
                row['Other'] = f"{income_amount:.2f}"

            row["Monthly Income"] = f"{total_income:.2f}"    

            row['Food'] = row['Food']
            row['Transportation'] = row['Transportation']
            row['Liabilities'] = row['Liabilities']
            row['Electric Bill'] = row['Electric Bill']
            row['Water Bill'] = row['Water Bill']
            row['Total Expense'] = row['Total Expense']
                    
            with open('dataset/financial_data.csv', 'w', newline='') as csvfile:
                fieldnames = ["Food", "Transportation", "Liabilities", "Electric Bill", "Water Bill", "Salary", "Other", "Monthly Income", "Total Expense"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(row)

        except FileNotFoundError:
            print("CSV file not found!")
        except Exception as e:
            print("Error occurred while loading data:", str(e))            

    ####################################################################################################################
    #-------------- The System Will Predict the Financial Health Score of the User based on Expenses ------------------>
    ####################################################################################################################
    def predict_score(self):
        try:
            with open('dataset/financial_data.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                data = list(reader)

            row = data[0]

            food = row["Food"]
            transpo = row["Transportation"]
            liabilities = row["Liabilities"]
            electricBill = row["Electric Bill"]
            waterBill = row["Water Bill"]
            monthlyIncome = row["Monthly Income"]
            totalExpense = row["Total Expense"]

            financialHealthScore = predictScore(food, transpo, liabilities, electricBill, waterBill, monthlyIncome, totalExpense)

            self.score.config(text=financialHealthScore)

            score = financialHealthScore

            insight = get_insights(score)

            self.insightValue.config(text=insight)

        except FileNotFoundError:
            print("CSV file not found!")
        except Exception as e:
            print("Error occurred while loading data:", str(e))   
    

def win():
    window = Tk()
    Dashboard(window)
    window.mainloop()

if __name__ == '__main__':
    win()