from tkinter import *
from tkinter import ttk #ComboBox ko lekr aati hai yeh
from googletrans import Translator,LANGUAGES
import pyttsx3 
def Translate_Text():
    Input_Text = input_text.get(1.0,END)
    Input_Lang = input_lang.get()
    Output_Lang = output_lang.get()
    main = Translator()
    translated_text = main.translate(text=Input_Text,src=Input_Lang,dest=Output_Lang)
    output_text.delete(1.0,END)
    output_text.insert(END,translated_text.text)
    
def Text_to_Speech():
    # Install: pip install pyttsx3
    InputText = input_text.get(1.0,END)
    engine = pyttsx3.init()
    engine.say(InputText)
    engine.runAndWait()


root = Tk()
root.title("-:Translator & Text-to-Speech App:-")
root.geometry("700x600") #widthxheight
root.config(bg='#333333')

heading = Label(root,text="-:Translator & Text-to-Speech App:-",font=("protest strike",28,'bold'),fg='white',bg='#333333')
heading.place(width=700,height=80)

heading = Label(root,text="Enter Your Text:-",font=("protest strike",16,'bold'),fg='light grey',bg='#333333')
heading.place(x=-245,y=60,width=700,height=50)
input_text = Text(root,font=("protest strike",15),fg='black',bg='white')
input_text.place(x=20,y=105,width=655,height=150)
photo = PhotoImage(file='E:/DUET Material/3rd Semester/OOP/Translator & Text to Speech/speakericon.png')
photo.configure(height=39,width=40)
button = Button(root, image = photo,command=Text_to_Speech)
button.place(height=39,width=45,x=21,y=215)

languages = list(LANGUAGES.values())
input_lang = ttk.Combobox(root,value=languages,font=("roboto",12))
input_lang.set('english')
input_lang.place(x=50,y=270,width=180,height=35)

button = Button(root,text="->      Translate     ->",font=("roboto",13),bg='white',command=Translate_Text)
button.place(x=245,y=270,width=200,height=35)

output_lang = ttk.Combobox(root,value=languages,font=("roboto",12))
output_lang.set('urdu')
output_lang.place(x=460,y=270,width=180,height=35)

output_heading = Label(root,text="Translation:-",font=("protest strike",16,'bold'),fg='light grey',bg='#333333')
output_heading.place(x=-268,y=320,width=700,height=50)
output_text = Text(root,font=("protest strike",15),fg='black',bg='light grey')
output_text.place(x=20,y=370,width=655,height=150)

root.mainloop()



