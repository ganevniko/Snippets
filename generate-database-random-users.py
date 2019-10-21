import pandas as pd
from randomuser import RandomUser

first=[]
last=[]
username=[]
phone=[]
gender=[]
email=[]

N=50

for i in range(N):
    user = RandomUser()
    
    first.append(user.get_first_name())
    last.append(user.get_last_name())
    username.append(user.get_username())
    phone.append(user.get_phone())
    gender.append(user.get_gender())
    email.append(user.get_email())
    
df=pd.DataFrame(columns=['First_Name','Last_Name','Gender','Username','Phone','Email'])
df['First_Name']=first
df['Last_Name']=last
df['Gender']=gender
df['Username']=username
df['Phone']=phone
df['Email']=email

df
