def get_current_savings(guess,annual_salary): # Had problems needing to reinitializing varibles and def a function solved these probelms.
    r=0.04
    months=0
    current_savings=0.0
    semi_annual_raise=0.07
    while months<36:
        current_savings =(1+r/12)*(current_savings+annual_salary*guess/12)
        months= months+1
        if months%6==0: #Assuming the raise occurs at the end of the 6th month. Effective in the 7th month.
            annual_salary=(1+semi_annual_raise)*(annual_salary)
    return(current_savings)

annual_salary=float(input("Enter your starting salary:"))
total_cost=1000000
low=0.0
high=1.0
guess=(high+low)/2
num_guess=0
savings=0.0
if get_current_savings(1,annual_salary)<0.25*total_cost:
    print("It is not possible to pay the down payment in 3 years.")
else:
    while abs(0.25*total_cost - savings)>0.01: #Did not follow the exact instructions of the pset to get a more accurate result.
        savings=get_current_savings(guess,annual_salary)
        if savings>0.25*total_cost:
            high=guess
        else:
            low=guess
        guess=(high+low)/2
        num_guess+=1
    
    print("The best savings rate is:",round(guess,4))
    print("Steps in bisection search:",num_guess)
input("Press Enter to exit")