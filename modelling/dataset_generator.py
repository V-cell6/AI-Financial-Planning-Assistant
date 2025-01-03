import csv
import random
import math

def calculate_financial_health_score(monthly_food, monthly_transportation, monthly_liabilities, monthly_electric_bill, monthly_water_bill, monthly_income):

    total_expense = monthly_food + monthly_transportation + monthly_liabilities + monthly_electric_bill + monthly_water_bill
    
    food_percentage = 0.3 * ((monthly_food / 5000) * 100)
    transpo_percentage = 0.06 * ((monthly_transportation / 2000) * 100)
    lia_percentage = 0.04 * ((monthly_liabilities / 5000) * 100)
    ele_percentage = 0.3 * ((monthly_electric_bill / 2000) * 100)
    wat_percentage = 0.3 * ((monthly_water_bill / 2000) * 100)

    factor = food_percentage + transpo_percentage + lia_percentage + ele_percentage + wat_percentage
    factor /= 100


    score = (100 * (monthly_income - (factor*total_expense)) / monthly_income) / 10

    return score



def generate_dataset(filename, num_samples):
    income_range = (10000, 30000)  # Range of income in pesos

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow(['monthly_food', 'monthly_transportation', 'monthly_liabilities', 'monthly_electric_bill', 'monthly_water_bill', 'monthly_income', 'total_expense', 'financial_health_score'])

        for _ in range(num_samples):
            monthly_food = round(random.uniform(1000.0, 5000.0), 1)
            monthly_transportation = round(random.uniform(500.0, 2000.0), 1)
            monthly_liabilities = round(random.uniform(1000.0, 5000.0), 1)
            monthly_electric_bill = round(random.uniform(500.0, 2000.0), 1)
            monthly_water_bill = round(random.uniform(200.0, 1500.0), 1)
            monthly_income = round(random.uniform(*income_range), 1)



            # Calculate total expense
            expense_breakdown = {
                'monthly_food': monthly_food,
                'monthly_transportation': monthly_transportation,
                'monthly_liabilities': monthly_liabilities,
                'monthly_electric_bill': monthly_electric_bill,
                'monthly_water_bill': monthly_water_bill
            }
            total_expense = sum(value for key, value in expense_breakdown.items() if key != 'monthly_income')

            # Calculate financial health score
            financial_health_score = calculate_financial_health_score(monthly_food, monthly_transportation, monthly_liabilities, monthly_electric_bill, monthly_water_bill, monthly_income)

            writer.writerow([monthly_food, monthly_transportation, monthly_liabilities, monthly_electric_bill, monthly_water_bill, monthly_income, total_expense, financial_health_score])

    print(f"Dataset generated and saved as '{filename}'.")

# Generate a dataset with 100 samples
generate_dataset('financial_dataset.csv', 5000)
