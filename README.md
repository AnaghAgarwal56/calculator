# online-calculator
A stylish web-based calculator built with Flask, HTML, CSS, and JavaScript. Features include basic arithmetic operations, input management, calculation history with delete options, and a clean, responsive user interface.

PRO CALCULATOR - SETUP GUIDE

--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------

Create the following folder structure:

calculator/
│
├── app.py
└── templates/
    └── index.html

- app.py: Contains the backend logic using Flask
- templates/index.html: Contains the frontend user interface

--------------------------------------------------
INSTALLATION
--------------------------------------------------

Make sure Python is installed on your system.

Install Flask by running:

pip install flask

--------------------------------------------------
RUNNING THE APPLICATION
--------------------------------------------------

1. Open Command Prompt or Terminal

2. Navigate to the project folder:

cd path/to/calculator

3. Run the Flask application:

python app.py

--------------------------------------------------
ACCESSING THE APPLICATION
--------------------------------------------------

After running the server, you will see a message like:

Running on http://127.0.0.1:5000/

Copy this URL and paste it into your web browser.

--------------------------------------------------
FEATURES
--------------------------------------------------

- Basic arithmetic operations (Addition, Subtraction, Multiplication, Division)
- Clear input fields
- Clear full history
- Delete individual history entries
- Clean and responsive user interface

--------------------------------------------------
IMPORTANT NOTES
--------------------------------------------------

- Do not open index.html directly in the browser
- Always run the application using Flask (app.py)
- Ensure the folder name is "templates" (required by Flask)
- The server must be running to use the application

--------------------------------------------------
