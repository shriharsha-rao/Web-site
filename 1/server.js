// User data storage
let users = JSON.parse(localStorage.getItem('users')) || [];
let loginHistory = JSON.parse(localStorage.getItem('loginHistory')) || [];

// DOM elements
const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');

// Get forms
const loginForm = document.querySelector('.form-box.login form');
const registerForm = document.querySelector('.form-box.register form');

// Registration functionality
if (registerForm) {
    registerForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const username = registerForm.querySelector('input[type="text"]').value;
        const email = registerForm.querySelector('input[type="email"]').value;
        const password = registerForm.querySelector('input[type="password"]').value;
        
        // Check if user already exists
        const existingUser = users.find(user => user.email === email || user.username === username);
        
        if (existingUser) {
            alert('User already exists with this email or username!');
            return;
        }
        
        // Add new user
        const newUser = {
            id: Date.now(),
            username: username,
            email: email,
            password: password, // In production, this should be hashed
            registrationDate: new Date().toISOString(),
            lastLogin: null
        };
        
        users.push(newUser);
        localStorage.setItem('users', JSON.stringify(users));
        
        alert('Registration successful! Please login.');
        
        // Switch to login form
        wrapper.classList.remove('active');
        
        // Clear form
        registerForm.reset();
    });
}

// Login functionality
if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const email = loginForm.querySelector('input[type="email"]').value;
        const password = loginForm.querySelector('input[type="password"]').value;
        
        // Find user
        const user = users.find(u => u.email === email && u.password === password);
        
        if (user) {
            // Update last login
            user.lastLogin = new Date().toISOString();
            localStorage.setItem('users', JSON.stringify(users));
            
            // Record login history
            const loginRecord = {
                userId: user.id,
                username: user.username,
                email: user.email,
                loginTime: new Date().toISOString(),
                ip: '127.0.0.1' // In production, get actual IP
            };
            
            loginHistory.push(loginRecord);
            localStorage.setItem('loginHistory', JSON.stringify(loginHistory));
            
            // Set session
            sessionStorage.setItem('loggedIn', 'true');
            sessionStorage.setItem('currentUser', JSON.stringify(user));
            
            // Redirect to index1.html
            window.location.href = 'index1.html';
        } else {
            alert('Invalid email or password!');
        }
    });
}

// Navigation between forms
registerLink.addEventListener('click', () => {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
});