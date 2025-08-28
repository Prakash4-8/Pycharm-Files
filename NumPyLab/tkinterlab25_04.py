from matplotlib import pyplot as plt

rainfall= [120,120,160,140,100,60,80,120,140,160,110,120]
months=[ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',' July', 'Aug', "Sept", 'Oct', 'Nov', 'Dec']

plt.bar( months, rainfall, align= 'center', color= 'Orange')
plt.show


plt.bar(range(len(rainfall)), rainfall,align='center',  color='Blue')
plt.xticks(range(len(rainfall)), months, rotation= 'vertical')
plt.show()
