# Create Your Own Email Bot | Python Project | Email Automation Bot |

import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener=sr.Recognizer()
engine=pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listenig...!')
            voice=listener.listen(source)
            info=listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver,subject,message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('daffofil@gmail.com','111111111')
    email=EmailMessage()
    email['From']='farukmd494494@gmail.com'
    email['To']= receiver
    email['Subject']= subject
    email.set_content(message)
    server.send_message(email)

email_list={
    'dude': 'COOL_DUDE_EMAIL',
    'bts': 'diamond@bts.com',
    'pink': 'jennie@blackpink.com',
    'lisa': 'lisa@blackpink.com',
    'irene': 'irene@redvelvet.com',
    'diu': 'daffodil@gmail.com'
}

def get_email_info():
    talk('to whome you want to send email')
    name=get_info()
    receiver=email_list[name]
    print(receiver)
    talk('what is the subject of your email?')
    subject=get_info()
    talk('tell me the text of your email?')
    message=get_info()
    send_email(receiver,subject,message)
    talk('your mail is sent!')
    talk('do you want to send more email?')
    send_more=get_info()
    if 'yes' in send_more():
        get_email_info()


get_email_info()
