import pickle
import warnings


with open('financialScorePredict.pkl', 'rb') as file:

    model = pickle.load(file)

warnings.filterwarnings("ignore", category=UserWarning, message="X does not have valid feature names, but RandomForestRegressor was fitted with feature names")    

def get_insights(score):

    score = round(score)

    insights = {
        1: "Critical financial situation. Immediate action is required to avoid serious consequences.",
        2: "Very poor financial health. Major improvements are needed.",
        3: "Poor financial health. Focus on reducing debt and increasing savings.",
        4: "Below-average financial health. Consider making necessary adjustments.",
        5: "Moderate financial health. There is room for improvement in managing your finances.",
        6: "Fair financial health. Continue to work on enhancing your financial situation.",
        7: "Good financial health. You are doing a decent job in managing your finances.",
        8: "Very good financial health. Keep up the good work!",
        9: "Excellent financial health! You are managing your finances exceptionally well.",
        10: "Outstanding financial health! Congratulations on achieving financial success!",
    }
    return insights.get(score, "Invalid score")


def predictScore (food, transpo, lia, ele, wat, income, expense):
    data = []

    row = [food, transpo, lia, ele, wat, income, expense]
    data.append(row)

    predictions = model.predict(data)
    prediction = predictions[0]

    prediction = round((prediction),1)

    return prediction