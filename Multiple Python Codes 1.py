#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator
# 
# 

# In[1]:


Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)
if(BMI>0):
    if(BMI<=16):
        print("you are severely underweight")
    elif(BMI<=18.5):
        print("you are underweight")
    elif(BMI<=25):
        print("you are Healthy")
    elif(BMI<=30):
        print("you are overweight")
    else: print("you are severely overweight")
else:("enter valid details")


# # Farenheit to Celcius Calculator

# In[2]:


def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c
x = int(input("Enter Temperature in Celcius to convert it into Farenheit = "))
print(convert(x))


# # Encryption and Decryption using Python

# In[3]:


from tkinter import messagebox, simpledialog, Tk

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

root = Tk()
while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
        
    elif task == 'decrypt':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('Plaintext of the secret message is:', decrypted)
    else:
        break
root.mainloop() 


# In[ ]:


'''Our code needs user input to be an even number of characters. 
The program first checks the number of characters entered by the user,
if the character length is odd, the program will add x at the end to make the count even.'''


# # Chat Bot

# In[6]:


from nltk.chat.util import Chat, reflections
#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Aman Kharwal created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['New Delhi, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]

#default message at the start of chat
print("Hi, I'm the clever programmer and I like to chat.\nPlease type lowercase English language to start a conversation.\nType quit to leave.")
#Create Chat Bot
chat = Chat(pairs, reflections)
#Start conversation
chat.converse()


# # Scraping Data From Website

# In[10]:


get_ipython().system('pip install bs4')


# In[11]:


from bs4 import BeautifulSoup
import requests


# In[12]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[13]:


print(soup)


# In[14]:


soup.find('table')


# In[15]:


soup.find_all('table')[1]


# In[16]:


soup.find('table', class_ = 'wikitable sortable')


# In[17]:


table = soup.find_all('table')[1]


# In[18]:



print(table)


# In[19]:


world_titles = table.find_all('th')


# In[20]:


world_titles


# In[21]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[22]:


import pandas as pd


# In[23]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[24]:


column_data = table.find_all('tr')


# In[25]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[26]:


df

