import matplotlib.pyplot as plt

Year = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
Money_Spend = [1000, 2000, 1500, 1800, 2500, 5000, 3000, 2500, 4750, 5000, 3333, 1099]

plt.plot(Year, Money_Spend)
plt.title('Money Spend Vs Year')
plt.xlabel('Year')
plt.ylabel('Money Spend')
plt.show()
