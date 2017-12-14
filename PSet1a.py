portion_down_payment=0.25
r=0.04
current_savings=0.0
months=0
annual_salary=float(input("Enter your starting salary:"))
portion_saved=float(input("Enter your portion of salary to be saved:"))
total_cost=float(input("Enter the total cost of your dream home:")) 
#The assignment does not call for a check if inputs are strings or negative/nonsense numbers. I may try to work this out later.
while current_savings<0.25*total_cost:
    current_savings =(1+r/12)*(current_savings+annual_salary*portion_saved/12)
    months= months+1
print("Number of months required to save for the 25% down payment on your home:", months)
if current_savings-0.25*total_cost>=0.01:
    print("You even have $"+ str(round(current_savings-0.25*total_cost,2))+" left over!")
input("Press Enter to exit")