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

#All attributes available 
#get_cell()
#get_city()
#get_dob()
#get_email()
#get_first_name()
#get_full_name()
#get_gender()
#get_id()
#get_id_number()
#get_id_type()
#get_info()
#get_last_name()
#get_login_md5()
#get_login_salt()
#get_login_sha1()
#get_login_sha256()
#get_nat()
#get_password()
#get_phone()
#get_picture()
#get_postcode()
#get_registered()
#get_state()
#get_street()
#get_username()
#get_zipcode()
