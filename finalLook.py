import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import newdatabase
import time

df = pd.read_csv('processed_ingredients.csv')
# Extract unique concerns from the comma-separated strings and remove the value 'Anyone'
all_concerns_new = []
for concerns in df['Concern'].dropna():
    individual_concerns = [c.strip() for c in concerns.split(",")]
    all_concerns_new.extend(individual_concerns)

# Remove 'Anyone' (case insensitive)
unique_concerns_new = sorted({c for c in all_concerns_new if c.lower() != 'anyone'})


## page to create the first page
class First_Page() :
    
    def next_page(self) :
        #self.first_img.destroy()
        self.name.destroy()
        self.enter.destroy()
        self.f_img.destroy()
        signup = SignUp(self.tkob)
        
        
    def __init__(self, tkob) :
        self.tkob = tkob
        self.first_img = Image.open('girl_bg_img.png')
        self.first_img = self.first_img.resize((950, 650))
        self.first_img = ImageTk.PhotoImage(self.first_img)

        self.f_img = Label(tkob, image=self.first_img)
        self.f_img.place(x=0, y=0)
        
        ## Display the name 
        self.name = Label(tkob, text="GLOW", font=('Times New Roman', 40, 'bold'), bg = "pink", fg = "black")
        self.name.place(x=200, y=130)
        self.name = Label(tkob, text="GENIUS", font=('Times New Roman', 40, 'bold'), bg = "pink", fg = "black")
        self.name.place(x=620, y=130)
        #self.name = Label(tkob, text="Get The Best Version of Your Skin..", font=('Times New Roman', 10, 'bold'), bg = "dimgrey", fg = "white")
        #self.name.place(x=700, y=220)
        
        self.enter = Button(tkob, text = "Enter\u27A1", font = ("Ariel", 20, "bold"), command = self.next_page)
        self.enter.place(x = 770, y = 570)



class SignUp():
    
    def authenticate_user(self) :
        username = self.user.entry1.get()
        password = self.password.entry2.get()
        userdata = newdatabase.db.authenticate_user(username, password)
        '''newdatabase.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        userdata = newdatabase .cursor.fetchone()'''
        if userdata :
            self.landingpage()
        else : 
            messagebox.showerror("Error", "Invalid username or password")
        #self.landingpage()
        
    def backPage(self) :
        self.l_img.destroy()
        self.lg.destroy()
        self.user.destroy()
        self.user.entry1.destroy()
        self.password.destroy()
        self.password.entry2.destroy()
        self.button.destroy()
        self.rbutton.destroy()
        self.fbutton.destroy()
        
        first_page = First_Page(self.tkob)

    def landingpage(self) :
        self.user.destroy()
        self.user.entry1.destroy()
        self.password.destroy()
        self.password.entry2.destroy()
        self.button.destroy()
        self.rbutton.destroy()

        landing_page = Landing_page(tkob)

    def registerpage(self) :
        self.user.destroy()
        self.user.entry1.destroy()
        self.password.destroy()
        self.password.entry2.destroy()
        self.button.destroy()
        self.rbutton.destroy()
        self.fbutton.destroy()

        register_page = Register(tkob)

    def display_password(self, event) :
        self.password.entry2.config(show = ".") 

    def change(self) :
        self.lg.destroy()
        self.user.destroy()
        self.user.entry1.destroy()
        self.password.destroy()
        self.password.entry2.destroy()
        self.button.destroy()
        self.rbutton.destroy()
        self.fbutton.destroy()

        new_password_page = ChangePassword(tkob)

    def __init__(self,tkob):
        self.tkob = tkob
        self.login_img = Image.open('loginpage_bgr.png')
        self.login_img = self.login_img.resize((950, 650))
        self.login_img = ImageTk.PhotoImage(self.login_img)

        self.l_img = Label(tkob, image=self.login_img)
        self.l_img.place(x=0, y=0)


        self.lg = Label(tkob, text="Login Here", font=('Comic Sans MS', 30, 'bold'))
        self.lg.place(x=380, y=10)


        self.user = Label(tkob, text = "Username" , font = ("Ariel", 15, "bold"))
        self.user.place(x =265, y = 125)
        self.user.entry1 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.user.entry1.place(x = 415, y = 125)

        self.password = Label(tkob, text = "Password", font = ("Ariel", 15, "bold"))
        self.password.place(x = 265, y = 185)
        self.password.entry2 = Entry(tkob, font = ("Ariel",15, "bold"))
        self.password.entry2.place(x = 415, y = 185)
        self.password.entry2.bind("<KeyRelease>", self.display_password)

        self.button = Button(tkob, text = "Login", font = ("Ariel", 15, "bold"), command = self.authenticate_user)
        self.button.place(x = 290, y = 275)

        self.rbutton = Button(tkob, text = "Register", font = ("Ariel", 15, "bold"), command = self.registerpage)
        self.rbutton.place(x = 500, y = 275)

        self.fbutton = Button(tkob, text = "Forgot Password", font = ("Ariel", 15, "bold"), command = self.change)
        self.fbutton.place(x = 360, y = 380)
        
        self.back_button = Button(tkob, text = "\u2B05", font = ("Ariel", 15, "bold"), command = self.backPage)
        self.back_button.place(x = 10, y = 10)



class Register() :

    def add_user(self) :
        user_name = self.username.en1.get()
        e_mail = self.email.en2.get()
        pass_word = self.password.en3.get()
        mob_ile = self.mobile.en4.get()
        newdatabase.db.add_user(user_name, e_mail, pass_word, mob_ile)
    

    def register(self) :
        self.add_user()
        self.R.destroy()
        self.username.destroy()
        self.username.en1.destroy()
        self.email.destroy()
        self.email.en2.destroy()
        self.password.destroy()
        self.password.en3.destroy()
        self.mobile.destroy()
        self.mobile.en4.destroy()
        self.rbutton.destroy()

        l_page = Landing_page(tkob)

    def backPage(self) :
        self.username.destroy()
        self.username.en1.destroy()
        self.email.destroy()
        self.email.en2.destroy()
        self.password.destroy()
        self.password.en3.destroy()
        self.mobile.destroy()
        self.mobile.en4.destroy()
        self.rbutton.destroy()


        s_page = SignUp(tkob)

    def display_password(self, event) :
        self.password.en3.config(show = ".")


    def __init__(self, tkob) :
        self.tkob = tkob
        self.sign_img = Image.open('loginpage_bgr.png')
        self.sign_img = self.sign_img.resize((950, 650))
        self.sign_img = ImageTk.PhotoImage(self.sign_img)

        self.s_img = Label(tkob, image=self.sign_img)
        self.s_img.place(x=0, y=0)

        self.R = Label(tkob, text="Register Yourself", font=('Comic Sans MS', 30, 'bold'))
        self.R.place(x=350, y=10)

        self.username = Label(tkob, text = "UserName", font = ("Ariel", 15, "bold"))
        self.username.place(x = 275, y = 150)
        self.username.en1 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.username.en1.place(x = 500, y = 150)

        self.email = Label(tkob, text = "Email", font = ("Ariel", 15, "bold"))
        self.email.place(x = 275, y = 200)
        self.email.en2 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.email.en2.place(x = 500, y = 200)



        self.password = Label(tkob, text = "Password", font = ("Ariel", 15, "bold"))
        self.password.place(x = 275, y = 250)
        self.password.en3 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.password.en3.place(x = 500, y = 250)
        self.password.en3.bind("<KeyRelease>", self.display_password)


        self.mobile = Label(tkob, text = "Mobile No", font = ("Ariel", 15, "bold"))
        self.mobile.place(x = 275, y = 300)
        self.mobile.en4 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.mobile.en4.place(x = 500, y = 300)

        self.rbutton = Button(tkob, text = "Create an Account", font = ("Ariel", 15, "bold"), command = self.register)
        self.rbutton.place(x = 400, y = 400)

        self.back_button = Button(tkob, text = "\u2B05", font = ("Ariel", 15, "bold"), command = self.backPage)
        self.back_button.place(x = 10, y = 10)


class ChangePassword() :

    def change_password(self) :
        new_password = self.new_password.p1.get()
        email = self.mail.m1.get()
        newdatabase.update_password(new_password, email)

    def display(self, event) :
        self.new_password.p1.config(show = ".")
    
    def check_email(self) :
        mail = self.mail.m1.get()
        newdatabase.cursor.execute("SELECT * FROM users WHERE email = ?", (mail,))
        userdata = newdatabase .cursor.fetchone()
        if userdata :
            self.change_password()
            sign = SignUp(tkob)
        else : 
            messagebox.showerror("Error","Email doesn't exist")

    
    def back_page(self) :
        self.L.destroy()
        self.mail.destroy()
        self.mail.m1.destroy()
        self.new_password.destroy()
        self.new_password.p1.destroy()
        self.change.destroy()
        self.bg_label.destroy()

        #change_password_page = ChangePassword(self.tkob)
        go_back = SignUp(tkob)



    def __init__(self, tkob) :
        self.tkob = tkob
        self.forgot_img = Image.open('loginpage_bgr.png')
        self.forgot_img = self.forgot_img.resize((950, 650))
        self.forgot_img = ImageTk.PhotoImage(self.forgot_img)


        ##Adding changes
        self.bg_label = tk.Label(tkob, image = self.forgot_img)
        self.bg_label.image = self.forgot_img
        self.bg_label.place(x = 0, y = 0)

        self.L = Label(tkob, text="Change Password", font=('Comic Sans MS', 30, 'bold'))
        self.L.place(x=350, y=10)

        self.mail = Label(tkob, text = "Email", font = ("Ariel", 15, "bold"))
        self.mail.place(x = 275, y = 200)
        self.mail.m1 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.mail.m1.place(x = 500, y = 200)

        self.new_password = Label(tkob, text = "New Password", font = ("Ariel", 15, "bold"))
        self.new_password.place(x = 275, y = 250)
        self.new_password.p1 = Entry(tkob, font = ("Ariel", 15, "bold"))
        self.new_password.p1.place(x = 500, y = 250)
        self.new_password.p1.bind("<KeyRelease>", self.display)

        self.change = Button(tkob, text = "Confirm Password", font = ("Ariel", 15, "bold"), command = self.check_email)
        self.change.place(x = 400, y = 350)

        self.back_button = Button(tkob, text = "\u2B05", font = ("Ariel", 15, "bold"), command = self.back_page)
        self.back_button.place(x = 10, y = 10)

        


class Landing_page():
    
    def next_page(self):
        skinconcern = self.skin_concern_dropdown.get()
        #skinconcern = self.skin_concern_dropdown.get()

        self.name.destroy()
        self.tag.destroy()
        self.bg_img.destroy()
        self.skin_concern_label.destroy()
        self.skin_concern_dropdown.destroy()
        self.suggest.destroy()
        self.back_button.destroy()

        sug = Suggest(tkob, skinconcern)

    def signup(self) :
        self.name.destroy()
        self.tag.destroy()
        self.bg_img.destroy()
        #self.skin_type_label.destroy()
        #self.skin_type_dropdown.destroy()
        self.suggest.destroy()
        self.back_button.destroy()

        sign = SignUp(tkob)

    def __init__(self, tkob):
        self.tkob = tkob
        self.bgr_img = Image.open('bgr_img.png')
        self.bgr_img = self.bgr_img.resize((950, 650))
        self.bgr_img = ImageTk.PhotoImage(self.bgr_img)

        self.bg_img = Label(tkob, image=self.bgr_img)
        self.bg_img.place(x=0, y=0)

        self.name = Label(tkob, text="Glow Genius", font=('Roman', 50, 'bold'))
        self.name.place(x=300, y=10)
        
        self.tag = Label(tkob, text = " - get the best version of your skin..", font = ('Courier New' ,13))
        self.tag.place(x=550, y=100)

        self.skin_concern_label = Label(tkob, text="Skin Concern:", font=('Courier New', 15, 'bold'))
        self.skin_concern_label.place(x=400, y=180)

        
        self.skin_concern_dropdown = ttk.Combobox(tkob, font=('Courier New', 10) )
        self.skin_concern_dropdown['values'] = unique_concerns_new 
        self.skin_concern_dropdown.place(x=400, y=230)
  
        '''self.skin_concern_label = Label(tkob, text="Skin Concern:", font=('Courier New', 15,'bold'))
        self.skin_concern_label.place(x=500, y=180)

        self.skin_concern_dropdown = ttk.Combobox(tkob, font=('Courier New', 10))
        self.skin_concern_dropdown['values'] = ['acne', 'hyperpigmentation', 'uneven texture', 'eczema', 'melasma', 'enlarged pores','dark circles', 'None']
        self.skin_concern_dropdown.place(x=665, y=180)'''

        self.suggest = Button(tkob,text = "Suggest" , font = ('Times New Roman',15,'bold'),command = self.next_page)
        self.suggest.place(x = 425 , y = 400)

        self.back_button = Button(tkob, text = "\u2B05", font = ("Ariel", 15, "bold"), command = self.signup)
        self.back_button.place(x = 10, y = 10)
        

class Suggest():
    def backpage(self) :
        #self.bgr2_img.destroy()
        self.scrollable_text.destroy()
        self.bg2_img.destroy()
        
        landing = Landing_page(tkob)


    def __init__(self,tkob, skinconcern):
        self.tkob = tkob
        self.skinconcern = skinconcern
        
        self.bgr2_img = Image.open('suggest_img.png')
        self.bgr2_img = self.bgr2_img.resize((950, 650))
        self.bgr2_img = ImageTk.PhotoImage(self.bgr2_img)

        self.bg2_img = Label(tkob, image=self.bgr2_img)
        ##Keeping reference
        self.bg2_img.image = self.bgr2_img
        self.bg2_img.place(x = 0, y = 0)
            

        '''def get_ingredient(user_skintype, user_concern) :
            #newdatabase.cursor.execute(f"SELECT concerns.ingredient FROM concerns JOIN skintypes ON concerns.ingredient = skintypes.ingredient WHERE concern = '{user_concern}' AND skintype = '{user_skintype}' ")
            ingredients = newdatabase.db.get_ingredients_by_type_and_concern(user_skintype, user_concern) #fetching single result
            print(ingredients)
            return [ingredient for ingredient in ingredients]'''
        
        # Correcting the column names in the function to match the dataset

        '''def search_ingredient(df, concern_input):
            # Convert concern_input to lowercase for case insensitive search
            concern_input_lower = concern_input.lower()
            
            # Create a boolean mask if the concern substring is contained in the Concern column
            mask = df['Concern'].str.lower().str.contains(concern_input_lower, na=False)
            
            # Filter the dataframe based on the mask and return the ingredients column
            return df.loc[mask, 'Ingredient']'''
         
        def search_ingredient(df, concern_input):
            # Convert concern_input to lowercase for case-insensitive search
            concern_input_lower = concern_input.lower()
                
            # Create a boolean mask if the concern substring is contained in the Concern column
            mask = df['Concern'].str.lower().str.contains(concern_input_lower, na=False)
                
            # Return the relevant columns for matching rows
            return df.loc[mask, ['Ingredient', 'short_description', 'what_does_it_do']]   

        # Test the function with an example concern
        '''example_concern = 'hydration'  # Replace with desired skin concern
        result = search_ingredient(df, example_concern)
        print("Ingredients corresponding to concern '" + example_concern + "':")
        print(result)'''

        
        
        # Ingredients Section
        #ingredients_text = "Recommended Ingredients:\n"
        ingredients = search_ingredient(df, skinconcern)
        
        self.back_button = Button(tkob, text = "\u2B05", font = ("Ariel", 15, "bold"), command = self.backpage)
        self.back_button.place(x = 10, y = 10)


        # Scrollable Text Section
        self.scrollable_text = Text(tkob, wrap='word', font=("Arial", 12), height=17, width=70, bg = "lightgrey", highlightthickness = 0)
        self.scrollable_text.place(x=200, y=150)
        
        # Add the results to the Text widget
        # Configure tags for bold text
        self.scrollable_text.tag_configure('bold', font=("Arial", 12, "bold"))
        self.scrollable_text.insert('1.0', "Recommended Ingredients:\n\n", "bold")
        for _, row in ingredients.iterrows():
            self.scrollable_text.insert("end", f"\n\n")
            self.scrollable_text.insert('end', "  Ingredient :", 'bold')
            self.scrollable_text.insert('end', f"{row['Ingredient']}\n\n")
            
            self.scrollable_text.insert('end', "  Short Description : ", 'bold')
            self.scrollable_text.insert('end', f"{row['short_description']}\n\n")
            
            self.scrollable_text.insert('end', "  What Does It Do : ", 'bold')
            self.scrollable_text.insert('end', f"{row['what_does_it_do']}\n\n")

        # Make the text read-only
        self.scrollable_text.config(state='disabled')

        # Scrollbar
        scrollbar = Scrollbar(tkob, orient='vertical', command=self.scrollable_text.yview)
        scrollbar.place(x = 840, y = 150, height = 350)
        self.scrollable_text.config(yscrollcommand=scrollbar.set)
            
        


tkob = tk.Tk()
tkob.title("Glow Genius")
tkob.iconbitmap('icon.ico')
firstPage = First_Page(tkob)
#signup = SignUp(tkob)
tkob.geometry('950x650+250+30')
tkob.resizable(False,False)
#landing_page = Landing_page(tkob)
tkob.mainloop()


