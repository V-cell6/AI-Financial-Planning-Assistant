# FinSageAI

## 🚀 Overview

The **FinSageAI - AI-Financial Planning Assistant** is a cutting-edge application designed to help users gain control over their finances. Leveraging artificial intelligence and data analytics, this project provides:

- Automated expense tracking
- Budget management
- Financial insights and recommendations

Whether you’re planning to save for a big purchase or manage day-to-day expenses, this tool is your personal financial assistant.

---

## 🎯 Features

- **Expense Categorization**: Automatically categorize expenses using AI.
- **Budget Monitoring**: Set and monitor financial goals.
- **Actionable Insights**: Get personalized recommendations to improve savings.
- **Visualization**: Beautiful charts and graphs to track your financial health.
- **Security**: Data privacy with encryption.

---

## 🛠️ Tech Stack

- **Frontend**: React, Bootstrap
- **Backend**: Flask, Python
- **Database**: PostgreSQL
- **AI/ML**: TensorFlow, Scikit-learn
- **APIs**: OpenAI GPT API, Plaid API (for financial data)

---

## 📂 Repository Structure

```plaintext
AI-Driven-Personal-Financial-Manager/
├── frontend/         # React application files
├── backend/          # Flask server and API
├── modelling/        # AI models and relevant python files for financial predictions
├── dataset/          # Sample data and preprocessed data
├── README.md         # Project overview (you are here!)
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8+
- Node.js 14+
- PostgreSQL
- Virtual Environment (optional)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/V-cell6/AI-Financial-Planning-Assistant.git
   cd AI-Financial-Planning-Assistant
   ```

2. **Backend Setup**:

   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python app.py
   ```

3. **Frontend Setup**:

   ```bash
   cd ../frontend
   npm install
   npm start
   ```

4. **Database Setup**:

   - Create a PostgreSQL database and update credentials in `backend/config.py`.

---

## 📊 Usage

1. Navigate to the frontend interface: `http://localhost:3000`
2. Sign up and connect your bank account (via Plaid API).
3. Start tracking your expenses and view insights.

---

## 🧪 Testing

Run the backend and frontend tests using:

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd ../frontend
npm test
```




