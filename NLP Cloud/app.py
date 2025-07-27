from http.client import responses
from tkinter import *
from tkinter import messagebox
from mydb import Database
from myAPi import  API


class App:
    """
       NLP Desktop Application using Tkinter.

       This class handles the GUI components and interactions for:
       - User login and registration
       - Sentiment analysis
       - Named Entity Recognition (NER)
       - Emotion prediction

       It uses external modules for database operations (`mydb.Database`)
       and NLP APIs (`myAPI.API`).
       """
    def __init__(self):
        """
                Initialize the main application window, database, and API client.
                Launches the login interface on startup.
                """
        self.responses_NER = ""
        self.dbo = Database()
        self.apio=API()
        self.root=Tk()
        self.root.title("NLP_app")
        self.root.iconbitmap('resource/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')
        self.login_gui()
        self.root.mainloop()


    def clear(self):
        """
               Clear all packed widgets from the root window.
               Useful for refreshing the interface between views.
               """
        for i in self.root.pack_slaves():
            i.destroy()


    def login_gui(self):
        """
                Display the login interface for existing users.
                Allows users to enter email and password to log in,
                or navigate to the registration screen.
                """
        self.clear()

        heading=Label(self.root,text="NLPApp",bg="#34495E",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=("verdana",24,'bold'))

        label1=Label(self.root,text="Enter Email_id")
        label1.pack(pady=(10,10))

        self.email=Entry(self.root,width=50)
        self.email.pack(pady=(5,10),ipady=4)


        label2=Label(self.root,text="Enter password")
        label2.pack(pady=(10,10))

        self.password_input=Entry(self.root,width=50,show="*")
        self.password_input.pack(pady=(5,10),ipady=4)

        login_button=Button(self.root,text='Login',width=30,height=2,command=self.perfrom_log_in)
        login_button.pack(pady=(10,10))

        label3=Button(self.root,text="Not a member ?",command=self.register_gui)
        label3.pack(pady=(20,10))

        register=Button(self.root,text="Register Now",command=self.register_gui)
        register.pack(pady=(10,10))


    def register_gui(self):
        """
                Display the registration interface for new users.
                Collects name, email, and password and allows users to register.
                """
        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#34495E", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, 'bold'))



        label0 = Label(self.root, text="Enter Name")
        label0.pack(pady=(10, 10))
        self.name = Entry(self.root, width=50)
        self.name.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text="Enter Email_id")
        label1.pack(pady=(10, 10))
        self.email = Entry(self.root, width=50)
        self.email.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text="Enter password")
        label2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=50, show="*")
        self.password_input.pack(pady=(5, 10), ipady=4)

        register = Button(self.root, text="Register",width=30,height=2,command=self.perfrom_registration)
        register.pack(pady=(10, 10))

        already_member = Button(self.root, text="Already a member",command=self.login_gui)
        already_member.pack(pady=(10, 10))

        login_now = Button(self.root, text="Login now",command=self.login_gui)
        login_now.pack(pady=(10, 10))


    def perfrom_registration(self):
        """
                Process registration by capturing user inputs and adding them to the database.
                If successful, redirects to login; otherwise shows an error.
                """
        email=self.email.get()
        password= self.password_input.get()
        name=self.name.get()

        response=self.dbo.add_data(name, email, password)
        if response:
            messagebox.showinfo('Success',"reg successful")
            self.login_gui()
        else:

            messagebox.showerror('Error',"Already a member")
            self.login_gui()

    def perfrom_log_in(self):
        """
                Verify user credentials against the database.
                If valid, navigates to the home menu.
                """
        email = self.email.get()
        password = self.password_input.get()
        response=self.dbo.check_data(email,password)
        if response:
            messagebox.showinfo('Success',"Login successful")
            self.home_gui()
        else:

            messagebox.showerror('Error',"Email/password error ")
            self.login_gui()

    def home_gui(self):
        """
               Display the main application home screen.
               Provides navigation to Sentiment Analysis, NER, and Emotion Prediction.
               """
        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#34495E", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, 'bold'))

        Sentiment_Analysis = Button(self.root, text="Sentiment Analysis", width=30, height=2,
                                    command=self.Sentiment_Analysis)
        Sentiment_Analysis.pack(pady=(10, 10))

        Name_Entity_Recognition = Button(self.root, text="Name Entity Recognition", width=30, height=2,
                                         command=self.Name_Entity_Recognition)
        Name_Entity_Recognition.pack(pady=(10, 10))

        Emotion_Prediction = Button(self.root, text="Emotion Prediction", width=30, height=2,
                                    command=self.Emotion_Prediction)
        Emotion_Prediction.pack(pady=(10, 10))

        log_out = Button(self.root, text="log_out", command=self.login_gui)
        log_out.pack(pady=(10, 10))


    def Sentiment_Analysis (self):
        """
               Display the GUI for Sentiment Analysis.
               Allows user to enter input text and get sentiment prediction.
               """
        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#34495E", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, 'bold'))

        heading2 = Label(self.root, text="Sentiment Analysis", bg="#34495E", fg="white")
        heading2.pack(pady=(10, 20))
        heading2.configure(font=("verdana", 20))

        label1 = Label(self.root, text="Enter the Test")
        label1.pack(pady=(10, 10))
        self.sentiment_analysis_input= Entry(self.root, width=50)
        self.sentiment_analysis_input.pack(pady=(5, 10), ipady=4)

        Sentiment_button = Button(self.root, text="Analysis Sentiment", command=self.do_sentiment_analysis)
        Sentiment_button.pack(pady=(10, 10))

        # Placeholder for result label (initially empty)
        self.sentiment_analysis_result_var = StringVar()
        self.sentiment_analysis_result = Label(self.root, textvariable=self.sentiment_analysis_result_var, bg="#34495E", fg='white')
        self.sentiment_analysis_result.pack(pady=(10, 10))


        goBack_button = Button(self.root, text="Go Back", command=self.home_gui)
        goBack_button.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        """
                Handle the sentiment analysis logic.
                Calls the API and updates the UI with the sentiment result.
                """
        input_text = self.sentiment_analysis_input.get()
        try:
            self.responses_sentiment_analysis =self.apio.sentiment_api(input_text)
            print(self.responses_sentiment_analysis)

            # Show result in the label
            self.sentiment_analysis_result_var.set(str(self.responses_sentiment_analysis))

        except Exception as e:
            self.sentiment_analysis_result_var.set(f"Error: {e}")






    def Name_Entity_Recognition(self):
        """
                Display the GUI for Named Entity Recognition (NER).
                Takes input and target, and provides results from the API.
                """
        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#34495E", fg="white", font=("verdana", 24, 'bold'))
        heading.pack(pady=(30, 30))

        heading2 = Label(self.root, text="Name Entity Recognition", bg="#34495E", fg="white", font=("verdana", 20))
        heading2.pack(pady=(10, 20))

        label1 = Label(self.root, text="Enter the Text")
        label1.pack(pady=(10, 10))
        self.Name_Entity_Recognition_input = Entry(self.root, width=50)
        self.Name_Entity_Recognition_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text="Enter the Target")
        label2.pack(pady=(10, 10))
        self.Name_Entity_Recognition_input_Target = Entry(self.root, width=50)
        self.Name_Entity_Recognition_input_Target.pack(pady=(5, 10), ipady=4)

        Sentiment_button = Button(self.root, text="Analyze NER", command=self.do_Name_Entity_Recognition)
        Sentiment_button.pack(pady=(10, 10))

        # Placeholder for result label (initially empty)
        self.NER_result_var = StringVar()
        self.NER_result = Label(self.root, textvariable=self.NER_result_var, bg="#34495E", fg='white')
        self.NER_result.pack(pady=(10, 10))

        goBack_button = Button(self.root, text="Go Back", command=self.home_gui)
        goBack_button.pack(pady=(10, 10))

    def do_Name_Entity_Recognition(self):
        """
                Handle the NER logic.
                Calls the API with user inputs and updates the result label.
                """
        input_text = self.Name_Entity_Recognition_input.get()
        input_target = self.Name_Entity_Recognition_input_Target.get()

        try:
            self.responses_NER = self.apio.Name_Entity_Recognition_api(input_text, input_target)
            print(self.responses_NER)

            # Show result in the label
            self.NER_result_var.set(str(self.responses_NER))

        except Exception as e:
            self.NER_result_var.set(f"Error: {e}")

    def  Emotion_Prediction(self):
        """
                Display the GUI for Emotion Prediction.
                Allows user to enter input text and get predicted emotion.
                """
        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#34495E", fg="white", font=("verdana", 24, 'bold'))
        heading.pack(pady=(30, 30))

        heading2 = Label(self.root, text="Emotion Prediction", bg="#34495E", fg="white", font=("verdana", 20))
        heading2.pack(pady=(10, 20))

        label1 = Label(self.root, text="Enter the Text")
        label1.pack(pady=(10, 10))
        self.Emotion_Prediction_input = Entry(self.root, width=50)
        self.Emotion_Prediction_input.pack(pady=(5, 10), ipady=4)

        Emotion_Prediction_button = Button(self.root, text="Analyze Emotion", command=self.do_Emotion_Prediction)
        Emotion_Prediction_button.pack(pady=(10, 10))

        # Placeholder for result label (initially empty)
        self.Emotion_Prediction_result_var = StringVar()
        self.Emotion_Prediction_result = Label(self.root, textvariable=self.self.Emotion_Prediction_result_var, bg="#34495E", fg='white')
        self.Emotion_Prediction_result.pack(pady=(10, 10))

        goBack_button = Button(self.root, text="Go Back", command=self.home_gui)
        goBack_button.pack(pady=(10, 10))

    def do_Emotion_Prediction(self):
        """
                Handle the emotion prediction logic.
                Calls the API with input text and updates the result label.
                """
        input_text = self.Emotion_Prediction_input.get()

        try:
            self.responses_Emotion_Prediction = self.apio.Emotion_Prediction_api(input_text)
            print(self.responses_Emotion_Prediction)

            # Show result in the label
            self.Emotion_Prediction_result_var.set(str(self.responses_Emotion_Prediction))

        except Exception as e:
            self.Emotion_Prediction_result_var.set(f"Error: {e}")


nlp=App()
