from tkinter import * #I started with importing the Tkinter classes

class survey: #I have defined a class with a constructor method
    def __init__ (self, name, age, sex, ethnicity, disabledstatus, q1, q2, q3):
        self.name=name #I am taking the values of every question to hold all the information and see the results later
        self.age=age
        self.sex=sex
        self.ethnicity=ethnicity
        self.disabledstatus=disabledstatus
        self.q1=q1
        self.q2=q2
        self.q3=q3
    def getInfo(self): #A method to return the information
        infoStr = self.name+ ", Aged "+str(self.age)+ ", Sex: "+str(self.sex)+ ", Ethnicity: "+str(self.ethnicity)+ ", Disabledstatus: "+str(self.disabledstatus)+ ", Have you enjoyed the sculpture?: "+str(self.q1)+ ", Are you curious as to how it works?: "+str(self.q2)+ ", Do you want to know more about science as a result of this experience?: "+ str(self.q3)
        return infoStr

surveys=[] #Declared a list for all the information I am gonna gather
surveys.append(survey("Name", 00, "Answer", "Answer", "Yes", "Yes", "Yes", "Yes"))
surveys.append(survey("Name", 00, "Answer", "Answer", "No", "Yes", "No", "No"))

for s in surveys:
    print(s.getInfo()) #This for loop is to get the information above

w=Tk() #I will use the variable "w" as an object in my coding so I have connected it with the class "Tk" here
w.title("Singing Sculpture Survey") #A title for the main window
w.geometry("800x600") #The size of the window
w.config(bg="#404040") #The bg color of the window using hexadecimal code representing a color

from tkinter import ttk #Imported ttk which is an instance of Tk
tabsurvey = ttk.Notebook(w) #Declared a reference called "tabsurvey"
tab1 = ttk.Frame(tabsurvey) #I have declared my first tab is for the survey completion
tab2 = ttk.Frame(tabsurvey) #I have declared my second tab is for the records

tabsurvey.add(tab1, text="Survey")
tabsurvey.add(tab2, text="Records")
tabsurvey.pack(expand=1, fill="both")
#I have created the tabs and called a pack() method to expand and fill the window appropriately

surveyslistbox = Listbox(tab2, width=155, height=50) #Created a survey list box in tab2 so we can see the surveyours responses
surveyslistbox.place(x=20, y=20) #The position of the list box
surveyslistbox.delete("0", "end") #To make the list box auto delete the information/records
for s in surveys:
    surveyslistbox.insert(END, s.getInfo()) #A for loop to get the information and insert it one after the other at the end

w=LabelFrame(tab1,bg="#404040",bd=5,width=1350,height=800)
w.place(x=10,y=10)

sLabel = Label(w, text="Sculpture Experience Survey") #I have created this instance to add a sentence in the window
sLabel.place(x=20, y=20) #The position of the sentence in the window
sLabel.config(bg="#404040") #I give it the same bg color as the window
sLabel.config(font=("Verdana", 18, "bold")) #I have added a font family and a font size for the sentence

tLabel = Label(w, text="Please complete our survey below as it's a part of our ongoing project.") #I have created this instance to add another sentence in the window
tLabel.place(x=20, y=60) #The position of the sentence in the window
tLabel.config(bg="#404040") #I give it the same bg color as the window and the previous sentence
tLabel.config(font=("Verdana", 12)) #I have added a font family and a font size for the sentence

nameLabel = Label(w, text="1. Full Name:") #I have created this instance to add a sentence where I ask the surveyors to write thier name
nameLabel.place(x = 20, y = 100) #The position
nameLabel.config(bg="#404040") #I give it the same bg color as the window and the previous sentences
nameLabel.config(font=("Verdana", 14)) #I have added a font family and a font size for the sentence

nameEntry = Entry(w, width=15) #Created a text entry field for the above
nameEntry.place(x=20, y= 130) #The position of the entry field

ageLabel = Label(w, text="2. Age:") #I have created this instance to add a sentence where I the surveyors to write thier age
ageLabel.place(x = 20, y=170) #The position
ageLabel.config(bg="#404040") #The color
ageLabel.config(font=("Verdana", 14)) #I have added a font family and a font size for the sentence

ageEntry = Entry(w, width=10) #Created a text entry field for the above
ageEntry.place(x=20, y= 200) #The position of the entry field

var = IntVar() #A class to store integer values

sexLabel = Label(w, text="3. Sex:") #I have created this instance to add a sentence where I ask the surveyors to write thier sex
sexLabel.place(x = 20, y=250) #The position
sexLabel.config(bg="#404040") #The color
sexLabel.config(font=("Verdana", 14)) #I have added a font family and a font size for the sentence

def enable_other():
    otherEntry.config(state='normal' if var.get()==3 else 'disabled') #Created a definition to enable the other entry option below when the surveyors choose the "other" radiobutton

rb1 = Radiobutton(w, text = "Male", variable = var, value=1, bg="#404040", command=enable_other)
rb1.place(x=20, y=280) #The first radio button with the value, bg (background) color and position

rb2 = Radiobutton(w, text = "Female", variable = var, value=2, bg="#404040", command=enable_other)
rb2.place(x=20, y=300) #The second radio button with the value, bg color and position

rb3 = Radiobutton(w, text = "Other, please specify", variable = var, value=3, bg="#404040", command=enable_other)
rb3.place(x=20, y=320) #The third radio button with the value, bg color and position

otherEntry = Entry(w, width=15, state='disabled')
otherEntry.place(x=40, y=350) #The entry field for the "other" radiobutton

ethnicityLabel = Label(w, text="4. Ethnicity: ") #I have created this instance to add a sentence where I ask the surveyors to write thier ethnicity
ethnicityLabel.place(x = 20, y=400) #The position
ethnicityLabel.config(bg="#404040") #The color
ethnicityLabel.config(font=("Verdana", 14)) #I have added a font family and a font size for the sentence

var2 = IntVar() #A class to store integer values

def enable_other2():
    otherEntry2.config(state='normal' if var2.get()==6 else 'disabled') #Created a definition to enable the other entry option below when the surveyors choose the "other" radiobutton

rb1 = Radiobutton(w, text = "White", variable = var2, value=1, bg="#404040", command=enable_other2)
rb1.place(x=20, y=430) #The first radio button with the value, bg (background) color and position

rb2 = Radiobutton(w, text = "Black", variable = var2, value=2, bg="#404040", command=enable_other2)
rb2.place(x=20, y=450) #The second radio button with the value, bg color and position

rb3 = Radiobutton(w, text = "Mixed", variable = var2, value=3, bg="#404040", command=enable_other2)
rb3.place(x=20, y=470) #The third radio button with the value, bg color and position

rb4 = Radiobutton(w, text = "Arab", variable = var2, value=4, bg="#404040", command=enable_other2)
rb4.place(x=20, y=490) #The forth radio button with the value, bg color and position

rb5 = Radiobutton(w, text = "Asian", variable = var2, value=5, bg="#404040", command=enable_other2)
rb5.place(x=20, y=510) #The fifth radio button with the value, bg color and position

rb6 = Radiobutton(w, text = "Other, please specify", variable = var2, value=6, bg="#404040", command=enable_other2)
rb6.place(x=20, y=530) #The sixth radio button with the value, bg color and position

otherEntry2 = Entry(w, width=15, state='disabled')
otherEntry2.place(x=40, y=560) #The entry field for the "other" radiobutton

disabledstatusLabel = Label(w, text="5. Do you identify as a person with a disability?") #I have created this instance to add a sentence where I ask the surveyors to write thier ethnicity
disabledstatusLabel.place(x = 20, y=620) #The position
disabledstatusLabel.config(bg="#404040") #The color
disabledstatusLabel.config(font=("Verdana", 14)) #I have added a font family and a font size for the sentence

var3 = IntVar() #A class to store integer values

rb1 = Radiobutton(w, text = "Yes", variable = var3, value=1, bg="#404040")
rb1.place(x=20, y=650) #The first radio button with the value, bg (background) color and position

rb2 = Radiobutton(w, text = "No", variable = var3, value=2, bg="#404040")
rb2.place(x=20, y=670) #The second radio button with the value, bg color and position

rb3 = Radiobutton(w, text = "Prefer not to say", variable = var3, value=3, bg="#404040")
rb3.place(x=20, y=690) #The third radio button with the value, bg color and position

q1Label = Label(w, text="6. Have you enjoyed the sculpture?") #I have created this instance to add a sentence where I ask the surveyors to write thier opinion on wether they have enjoyed the sculpture or not
q1Label.place(x = 500, y = 100) #The position
q1Label.config(bg="#404040") #I give it the same bg color as the window and the previous sentences
q1Label.config(font=("Verdana", 14)) #I have added a font family and a font size for the sentenceenjoyed the sculpture

var4 = IntVar() #A class to store integer values

rb1 = Radiobutton(w, text = "Yes", variable = var4, value=1, bg="#404040", command=enable_other)
rb1.place(x=500, y=130) #The first radio button with the value, bg (background) color and position

rb2 = Radiobutton(w, text = "No", variable = var4, value=2, bg="#404040", command=enable_other)
rb2.place(x=500, y=150) #The second radio button with the value, bg color and position

q2Label = Label(w, text="7. Are you curious as to how it works?") #I have created this instance to add a sentence where I ask the surveyors to write thier opinion on wether they are curious as to how it works or not
q2Label.place(x = 500, y = 200) #The position
q2Label.config(bg="#404040") #I give it the same bg color as the window and the previous sentences
q2Label.config(font=("Verdana", 14)) #I have added a font family and a font size for the sentence

var5 = IntVar() #A class to store integer values

rb1 = Radiobutton(w, text = "Yes", variable = var5, value=1, bg="#404040", command=enable_other)
rb1.place(x=500, y=230) #The first radio button with the value, bg (background) color and position

rb2 = Radiobutton(w, text = "No", variable = var5, value=2, bg="#404040", command=enable_other)
rb2.place(x=500, y=250) #The second radio button with the value, bg color and position

q3Label = Label(w, text="8. Do you want to know more about science as a result of this experience?") #I have created this instance to add a sentence where I ask the surveyors to write thier opinion on wether they want to know more about science as a result of this experience or not
q3Label.place(x = 500, y = 300) #The position
q3Label.config(bg="#404040") #I give it the same bg color as the window and the previous sentences
q3Label.config(font=("Verdana", 14)) #I have added a font family and a font size for the sentence

var6 = IntVar() #A class to store integer values

rb1 = Radiobutton(w, text = "Yes", variable = var6, value=1, bg="#404040", command=enable_other)
rb1.place(x=500, y=330) #The first radio button with the value, bg (background) color and position

rb2 = Radiobutton(w, text = "No", variable = var6, value=2, bg="#404040", command=enable_other)
rb2.place(x=500, y=350) #The second radio button with the value, bg color and position

tLabel = Label(w, text= "Thank you for your contribution to the success of our project!") #I have created this instance to add a thank you sentence
tLabel.place(x = 500, y = 630) #The position
tLabel.config(bg="#404040") #I give it the same bg color as the window and the previous sentences
tLabel.config(font=("Verdana", 14)) #I have added a font family and a font size for the sentence

submitButton = Button(w, text = "Submit") #Created a submit button so the surveyors can click on it when they finish
submitButton.place(x=850, y=670) #The position of the submit button
submitButton.config(bg="white") #The color

def submitButtoncallback(): #I have created a call back function  with instructions, so when someone click on the submit button it takes the information and add it to tab2
    name=nameEntry.get()
    ageStr=ageEntry.get()
    age=int(ageStr)
    sex=var.get()
    if sex == 3:
        sex = otherEntry.get()
    ethnicity=var2.get()
    if ethnicity == 6:
        ethnicity = otherEntry2.get()
    disabledstatus=var3.get()
    q1=var4.get()
    q2=var5.get()
    q3=var6.get()
    surveys.append(survey(name, age, sex, ethnicity, disabledstatus, q1, q2, q3))
    surveyslistbox.delete("0", "end")
    for s in surveys:
        surveyslistbox.insert(END, s.getInfo())

submitButton.config(command=submitButtoncallback) #Added the command for the submit button

w.mainloop() #This allows my GUI come to life and keeps the window running until someone close it