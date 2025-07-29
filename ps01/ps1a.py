## 6.100A PSet 1: Part A
## Name: Wissem Jderi
## Time Spent: 10 minutes
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Please enter your yearly salary: "))
portion_saved = float(input("Enter how much of your salary you will save: "))
cost_of_dream_home = float(input("How much does your dream house cost? "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
down_payment = cost_of_dream_home * 0.25
monthly_saved = (yearly_salary * portion_saved) / 12
amount_saved = 0
months = 0
while amount_saved <= down_payment:

    amount_saved += amount_saved * (0.05 / 12)

    amount_saved += monthly_saved

    ###############################################################################################
    ## Determine how many months it would take to get the down payment for your dream home below ##
    ###############################################################################################
    months += 1
print(months)
