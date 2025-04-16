import os
try:

    os.system('data.py')
    os.system('prom.py')
except:
    pass
import psutil
import subprocess
import pygetwindow as gw
import pyautogui
import webbrowser
from googletrans import Translator
from datetime import date
import speech_recognition as sr
import pyttsx3
import pyautogui
import time
from bs4 import BeautifulSoup
import requests
import csv

with open('data.csv', mode='r') as file:
    reader = csv.reader(file)

    # خواندن یک رکورد خاص (مثلاً اولین رکورد)
    for i, row in enumerate(reader):
        if i == 1:  # انتخاب رکورد سوم (اعداد از ۰ شروع می‌شوند)
            country = row[0]
            name = row[1]
            gmail = row[2]
            gender = int(row[3])
            city = row[4]
            psg = row[5]
            break

engine = pyttsx3.init()
engine.setProperty('rate',150)
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[gender].id)
recognizer = sr.Recognizer()

try:
    last_date = open('time.txt')
    last_date = last_date.read()
    today = date.today()
    if last_date != today:
        with open('time.txt','w') as file:
            file.write(today)
            file.close
            engine.say('Hi how are you ')
except:
    pass




edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

def text_calculator(expression):

  
    result = eval(expression)
    return result


def close_app_by_name(process_name):
    # جستجو در لیست فرآیندها
    for process in psutil.process_iter(['pid', 'name']):
        if process_name.lower() in process.info['name'].lower():  # مطابقت با نام فرآیند
            process_id = process.info['pid']
            psutil.Process(process_id).terminate()  # پایان دادن به فرآیند
            engine.say(f"{process_name} closed!")
            return
    engine.say(f"i didnt find{process_name} ")

# باز کردن فایل CSV


while True:
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    
        try:
            command = recognizer.recognize_google(audio, language="en-US")
            text = command
            

            
            if 'the' in text:
                text = text.replace('the','')
            if 'hello' in text:
                engine.say('hi')
            if 'hi' in text:
                engine.say('hi')
            if 'goodbye' in text:
                break
            if 'bye' in text:
                break
            if 'what is your name' in text:
                engine.say('im your freind crase')
            if 'play my song' in text:
                playlist_path = r"C:\Users\shaha\Music\Playlists\my favs.m3u8"
                os.startfile(playlist_path)
            if 'Open' in text:
                from AppOpener import open
                
                if 'fifa' in text:
                    open('FiFa19')
                else:
                    text = text.replace('open','')
                    open(text)
                
            if 'go to' in text:
                webbrowser.get('edge').open_new_tab("https://www.%s.com"%(text))

            if 'close' in text:
                from AppOpener import close
                if 'fifa' in text:
                    close_app_by_name('FiFa19')
                text = text.replace('close','')
                if ' ' in text:
                    text = text.replace(' ','')
                close_app_by_name(text)
            if 'volume down' in text:
                    pyautogui.press("volumedown")
                    time.sleep(0.2)
            if 'volume up':
                    pyautogui.press("volumeup")
                    time.sleep(0.1)
            if 'calculate' in text:
                if 'plus' in text:
                    text = text.replace('plus','+')
                if 'mines' in text:
                    text = text.replcae('mines','-')
                if 'mines' in text:
                    text = text.replcae('mines','-')
                text = text.replace('calculate','')
                expression = text
                engine.say(text_calculator(expression))
            if 'restart pc' in text:
                os.system("shutdown /r /t 1")
            if 'shutdown pc' in text:
                os.system("shutdown /s /t 1")
            if 'say news' in text:


                    # URL سایت "آخرین خبر"
                    url = "https://akharinkhabar.ir/"

                    # ارسال درخواست با Header مناسب
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                    }
                    response = requests.get(url, headers=headers)

                    # تحلیل HTML صفحه
                    soup = BeautifulSoup(response.content, "html.parser")

                    # استخراج تیتر خبری از کلاس مشخص‌شده
                    news_items = soup.find_all("header", class_="square_news_title__MC_t4")

                    # نمایش تیتر خبرها
                    if news_items:
                        print("تیترهای خبری:")
                        for i, item in enumerate(news_items[:5]):  # محدود به ۵ خبر
                            print(f"{i+1}. {item.text.strip()}")
                    else:
                        print("هیچ خبری یافت نشد. لطفاً ساختار سایت را بررسی کنید.")
                
            if 'log in to' in text:
                text = text.replace('log in to','')
          
                data = {
                    'username': gmail,
                    'password': psg
                }

                # ارسال درخواست
                response = requests.post('https://%s.com/login'%(text), data=data)
                

                # بررسی پاسخ
                if response.ok:
                    engine.say("i did it")
                else:
                    engine.say("i couldnt beacuse: ", response.text)
            if 'make acount on' in text:
                # باز کردن فایل CSV
                    text = text.replace('make acount on','')

                    # اطلاعات حساب جدید
                    data = {
                        'username': gmail,
                        'email': gmail,
                        'password': psg,
                        'confirm_password': psg
                    }

                    # ارسال درخواست به URL مربوط به ثبت‌نام
                    response = requests.post('https://%s.com/signup'%(text), data=data)

                    # بررسی پاسخ
                    if response.status_code == 200:
                        print("اکانت با موفقیت ساخته شد!")
                    else:
                        print("مشکلی وجود دارد:", response.text)
                                                    

          
        except sr.UnknownValueError:
            engine.setProperty('rate', 120)
        except sr.RequestError as e:
            print(f"your call have disconection: {e}")

    engine.runAndWait()        
