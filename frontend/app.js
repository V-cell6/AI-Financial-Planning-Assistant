import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import Signup from './pages/Signup';
import Login from './pages/Login';
import Navbar from './components/Navbar';
import Footer from './components/Footer';

function App() {
    return (
        <Router>
            <div className="App">
                <Navbar />
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/dashboard" element={<Dashboard />} />
                    <Route path="/signup" element={<Signup />} />
                    <Route path="/login" element={<Login />} />
                </Routes>
                <Footer />
            </div>
        </Router>
    );
}

export default App;

// components/Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar-container">
                <Link to="/" className="navbar-logo">AI Finance</Link>
                <ul className="nav-menu">
                    <li><Link to="/" className="nav-links">Home</Link></li>
                    <li><Link to="/dashboard" className="nav-links">Dashboard</Link></li>
                    <li><Link to="/login" className="nav-links">Login</Link></li>
                    <li><Link to="/signup" className="nav-links nav-signup">Sign Up</Link></li>
                </ul>
            </div>
        </nav>
    );
}

export default Navbar;

/* A modern home page */
// pages/Home.js
import React from 'react';
import './Home.css';

function Home() {
    return (
        <div className="home-container">
            <header className="hero-section">
                <h1>Welcome to AI-Driven Personal Financial Manager</h1>
                <p>Take control of your finances with the power of AI.</p>
                <button className="cta-button">Get Started</button>
            </header>
            <section className="features">
                <div className="feature-item">
                    <img src="/images/expense-tracking.png" alt="Expense Tracking" />
                    <h3>Expense Tracking</h3>
                    <p>Automatically categorize and track your expenses.</p>
                </div>
                <div className="feature-item">
                    <img src="/images/budgeting.png" alt="Budgeting" />
                    <h3>Budget Management</h3>
                    <p>Set realistic budgets and achieve your financial goals.</p>
                </div>
                <div className="feature-item">
                    <img src="/images/insights.png" alt="Insights" />
                    <h3>Actionable Insights</h3>
                    <p>AI-powered insights to improve your savings.</p>
                </div>
            </section>
        </div>
    );
}

export default Home;

/* Styling the modern frontend */
// styles/Navbar.css
.navbar {
    background - color: #001f3f;
    padding: 1rem 2rem;
    display: flex;
    justify - content: space - between;
    align - items: center;
}

.navbar - logo {
    color: #fff;
    font - size: 1.5rem;
    font - weight: bold;
}

.nav - menu {
    list - style: none;
    display: flex;
    gap: 1.5rem;
}

.nav - links {
    color: #fff;
    text - decoration: none;
    font - size: 1.1rem;
}

.nav - signup {
    background - color: #ff851b;
    padding: 0.5rem 1rem;
    border - radius: 5px;
    color: #fff;
}

// styles/Home.css
.home - container {
    font - family: Arial, sans - serif;
    text - align: center;
    padding: 2rem;
}

.hero - section {
    background: url('/images/hero-bg.jpg') no - repeat center center / cover;
    color: #fff;
    padding: 4rem 2rem;
}

.cta - button {
    padding: 1rem 2rem;
    font - size: 1.2rem;
    background - color: #0074d9;
    color: #fff;
    border: none;
    border - radius: 5px;
    cursor: pointer;
}

.features {
    display: flex;
    gap: 2rem;
    justify - content: center;
    margin - top: 2rem;
}

.feature - item {
    width: 30 %;
    text - align: center;
}

.feature - item img {
    max - width: 100 %;
}

.feature - item h3 {
    color: #001f3f;
    margin: 1rem 0;
}
