from tkinter import filedialog
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import socket
#import getpass
import os
import time
import pandas as pd
from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image

mGui = Tk()
mGui.geometry("800x400")
mGui.title('WhatsApp Bot')
mGui.configure(bg='#66CDAA')

photo = PhotoImage(file = r"foto.png")
Label(mGui, image=photo).place(x=480, y=20)

Label(mGui,background='#66CDAA', text = "Vendos kohen mes dergimit te mesazheve: ", fg='white', font=('Calibri', 14, 'bold')).place(x=20, y=10)
x = Entry(mGui, justify=CENTER, font = ('courier', 14, 'bold'))
x.place(x=20, y=60)

def getInput():
    a = x.get()
    global params
    params = [a]

submit_time_button = Button(mGui, bg='#33FF33', text = "Submit",bd = '4', fg='black',font=('Calibri', 12 , 'bold'),command=getInput,)
submit_time_button.place(x=20, y=110)

mesazh = Label(
    text = "Vendosni pathin e dokumentit: ",
    bg = '#66CDAA',
    fg='white', 
    font=('Calibri', 14, 'bold')
)

def photo_path():
    global filepath
    filepath = filedialog.askopenfilename()


mesazh.place(x=20,y=160)
photo_browse_button = Button(mGui, bg='#33FF33', text = "Browse",bd = '4', fg='black',font=('Calibri', 12 , 'bold'),command=photo_path)
photo_browse_button.place(x=20,y=210)

mesazh1 = Label(
    text = "Vendosni pathin e excel-it: ",
    bg = '#66CDAA',
    fg='white', 
    font=('Calibri', 14, 'bold')
)

mesazh1.place(x=20,y=260)

copyright = Label(
    text = 'By Iseld Muca',
    bg = '#66CDAA',
    fg = 'white',
    font=('Calibri', 11, 'bold')
)

copyright.place(
    relx = 0.0,
    rely = 1.0,
    anchor = 'sw'
)
def excel_path():
    global numrat_telefonit
    numrat_telefonit = filedialog.askopenfilename()

buton = Button(mGui, bg='#33FF33', text = "Browse",bd = '4', fg='black',font=('Calibri', 12 , 'bold'),command=excel_path)
buton.place(x=20,y=310)

exit_button = Button(mGui, bg='#33FF33', text = "START",bd = '4', fg='black',font=('Calibri', 12 , 'bold'),command=mGui.destroy)
exit_button.place(x=580,y=350)
mGui.mainloop()

#user = getpass.getuser()

data = pd.read_csv(numrat_telefonit)
data_dict = data.to_dict('list')
numrat = data_dict['numrat']
moblie_no_list = zip(numrat,)

no_of_message=1

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://web.whatsapp.com")
time.sleep(60) #sekondat me prit per me skanu qr kodin

def send_whatsapp_msg(phone_no,image):
    mesazhi = "Pershendetje , une jam Nirvana Myrtja perfaqesuese e shitjeve tek Sihana Cosmetics  e cila perfshine nje  linjë produktesh te certifikuara  kozmetike  dhe trajtuse per problematikat e lekures dhe flokeve .Disa nga brendet tona jane Silky, Esterel  dhe Esencial . Sihana Cosmetics  po bashkepunon   me disa biznese te cilet kane zbritjen e tyre per cdo produkte  15 % ulje, zbritje e  cila vlen per  gjitha bizneset .Me  poshte po ju bashkengjisim disa file me  produktet dhe pershkrimin perkates   , te cilat i pershtaten biznesit  tuaj si  qender  estetike apo  parukeri . Ju falenderoj per kohen , nese jeni te interesuar do te mbetemi ne kontakte edhe duke zhvilluar nje takim nga afer."
    driver.get("https://web.whatsapp.com/send?phone="+str(phone_no)+"&text="+mesazhi)
    time.sleep(10)
    shkruaj = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    shkruaj.click()
    time.sleep(10)
    try:
        driver.switch_to.alert()
    except Exception as e:
        pass

    try:
        time.sleep(10)
        attachment_box = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div')# butoni attachment
        attachment_box.click()
        time.sleep(10)
        image_box = driver.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')#Butoni per te vendos pathin
        time.sleep(3)
        image_box.send_keys(filepath)
        time.sleep(15)
        send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')#Butoni send
        send_button.click()
        time.sleep(15)
        global no_of_message
        for x in range(no_of_message):

            send_button.send_keys(image)
            send_button.send_keys("\n")
            time.sleep(params) #Koha ndermjet mesazheve

    except Exception as e:
        print("Telefone Invalido:"+str(phone_no))
for moblie_no in moblie_no_list:
    try:
        send_whatsapp_msg(moblie_no,filepath)

    except Exception as e:
        time.sleep(20)
        is_connected()