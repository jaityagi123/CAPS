import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
from tkinter import ttk
import string
from googletrans import Translator
from playsound import playsound
import speech_recognition as sr  
from googletrans import Translator  
from gtts import gTTS  
import os
def func(language):
    r = sr.Recognizer()
    isl_gif=['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
            'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money',
            'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry', 'flower is beautiful',
            'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch', 'happy journey',
            'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing', 
             'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
            'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
            'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
            'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'shall I help you',
            'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
            'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your job',
            'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay',
            'where is the bathroom', 'where is the police station', 'you are wrong','address','agra','ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
    'bihar','bihar','bridge','cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile','dasara',
    'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujrat', 'hello',
    'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
    'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
    'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
    'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
    'voice', 'wednesday', 'weight','please wait for sometime','what is your mobile number','what are you doing','are you busy']
    
    
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1 
        i=0
        while True:
            print("I am Listening")
            audio = r.listen(source)
            try:
                b=r.recognize_google(audio)
                translator = Translator()
                a = translator.translate(b, dest='en').text
                a = a.lower()
                print("You said:", b)
                print('Translated text:', a.lower())
                for c in string.punctuation:
                    a = a.replace(c,"")
                    
                if (a.lower() == 'goodbye' or a.lower() == 'good bye' or a.lower() == 'bye'):
                    print("Oops! Time to say goodbye")
                    break
                
                elif (a.lower() in isl_gif):
                    class ImageLabel(tk.Label):
                        def load(self, im):
                            if isinstance(im, str):
                                im = Image.open(im)
                            self.loc = 0
                            self.frames = []

                            try:
                                for i in count(1):
                                    self.frames.append(ImageTk.PhotoImage(im.copy()))
                                    im.seek(i)
                            except EOFError:
                                pass

                            try:
                                self.delay = im.info['duration']
                            except:
                                self.delay = 100

                            if len(self.frames) == 1:
                                self.config(image=self.frames[0])
                            else:
                                self.next_frame()

                        def unload(self):
                            self.config(image=None)
                            self.frames = None

                        def next_frame(self):
                            if self.frames:
                                self.loc += 1
                                self.loc %= len(self.frames)
                                self.config(image=self.frames[self.loc])
                                self.after(self.delay, self.next_frame)
                    
                    root = tk.Tk()
                    lbl = ImageLabel(root)
                    lbl.pack()
                    lbl.load(f'ISL_Gifs/'.format(a.lower()))
                    root.after(3000, root.destroy)
                    root.mainloop()
                    
                else:
                    for i in range(len(a)):
                        if (a[i] in arr):
                            ImageAddress = 'letters/' + a[i] + '.jpg'
                            ImageItself = Image.open(ImageAddress)
                            ImageNumpyFormat = np.asarray(ImageItself)
                            plt.imshow(ImageNumpyFormat)
                            plt.draw()
                            plt.pause(0.8)
                        else:
                            continue

            except:
                print(" ")
            plt.close()

def main():
    root = tk.Tk()
    root.title("HEARING IMPAIRMENT ASSISTANT")

    # Load the image
    image_path = "signlang.png"
    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

    # Frame for holding buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)


    # Drop-down menu for selecting language
    language_label = ttk.Label(button_frame, text="Select Language:")
    language_label.pack(side=tk.LEFT)

    language_var = tk.StringVar()
    languages = ["Hindi", "Bengali", "Spanish", "German"]  # Add more languages as needed

    language_menu = ttk.Combobox(button_frame, textvariable=language_var, values=languages)
    language_menu.pack(side=tk.LEFT, padx=10)

    # Button for starting live voice recognition
    live_voice_button = ttk.Button(button_frame, text="Live Voice", command=lambda: func(language_var.get()))
    live_voice_button.pack(side=tk.LEFT, padx=10)

    # Button for quitting the application
    quit_button = ttk.Button(button_frame, text="Quit", command=root.destroy)
    quit_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
