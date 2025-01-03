food = float(input("food:"))
transpo = float(input("transportation:"))
lia = float(input("liabilities:"))
ele = float(input("electric bill:"))
wat = float(input("water bill:"))
income = float(input("montly income:"))


expense = food + transpo + lia + ele + wat

monthly_food = 0.3
monthly_transportation = 0.2
monthly_liabilities = 0.3
monthly_electric_bill = 0.1
monthly_water_bill = 0.1

food_percentage = 0.3 * ((food / 5000) * 100)
transpo_percentage = 0.2 * ((transpo / 2000) * 100)
lia_percentage = 0.3 * ((lia / 5000) * 100)
ele_percentage = 0.1 * ((ele / 2000) * 100)
wat_percentage = 0.1 * ((wat / 2000) * 100)

factor = food_percentage + transpo_percentage + lia_percentage + ele_percentage + wat_percentage
factor /= 100


score = (100 * (income - (factor*expense)) / income) / 10


print("Total: ", factor)

print("Score: ", score)