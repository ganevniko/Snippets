import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('seaborn')

#creating data base
#--------------------------------------------------------------------------

names,salaries,loans,paid = [],[],[],[]

for i in range(12):

    name = input('Name :')
    names.append(name)
    salary=input('Salary :')
    salaries.append(salary)
    loan = input('Loan :')
    loans.append(loan)
    p=input('Paid? ')
    paid.append(p)

df=pd.DataFrame(columns=['Name','Salary','Loan','Paid?'])
df['Name']=names
df['Salary']=salaries
df['Loan']=loans
df['Paid?']=paid

print(df)

#Visualizing
#--------------------------------------------------------------------------

df.Salary=df.Salary.astype(int)
df.Loan=df.Loan.astype(int)

dy=df[df['Paid?']=='Yes']
dn=df[df['Paid?']=='No']

plt.figure(figsize = (9,4))
plt.scatter(dy['Salary'],dy['Loan'],marker = 'x',color ='g', s = 200, label = 'Paid')
plt.scatter(dn['Salary'],dn['Loan'],marker = 'o',color ='r', s = 200, label = 'Unpaid')
plt.xlabel('Salary',fontsize = 15)
plt.ylabel('Loan',fontsize = 15)
plt.legend(frameon=True, framealpha=0.3).get_frame().set_facecolor('k')
plt.title('Who repaid his loan?', fontsize = 20)
