from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Initialize app and configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/finance_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

# Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    date = db.Column(db.Date, nullable=False)

# API Routes
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the AI-Driven Financial Manager API!"})

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        new_user = User(name=data['name'], email=data['email'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully!", "user": data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/users/<int:user_id>/expenses', methods=['POST'])
def add_expense(user_id):
    data = request.get_json()
    try:
        new_expense = Expense(
            user_id=user_id,
            category=data['category'],
            amount=data['amount'],
            description=data.get('description'),
            date=data['date']
        )
        db.session.add(new_expense)
        db.session.commit()
        return jsonify({"message": "Expense added successfully!", "expense": data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/users/<int:user_id>/expenses', methods=['GET'])
def get_expenses(user_id):
    try:
        expenses = Expense.query.filter_by(user_id=user_id).all()
        expenses_list = [
            {
                "id": expense.id,
                "category": expense.category,
                "amount": expense.amount,
                "description": expense.description,
                "date": expense.date.strftime('%Y-%m-%d')
            } for expense in expenses
        ]
        return jsonify(expenses_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/users/<int:user_id>/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(user_id, expense_id):
    try:
        expense = Expense.query.filter_by(user_id=user_id, id=expense_id).first()
        if not expense:
            return jsonify({"error": "Expense not found."}), 404
        db.session.delete(expense)
        db.session.commit()
        return jsonify({"message": "Expense deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Error handling
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({"error": "An internal error occurred."}), 500

# Run server
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
