# Note Keeper

Note Keeper is a small web application built with Flask and SQLAlchemy that allows you to manage your personal notes. 

## Features
- Add new notes
- View all notes in descending order
- Update existing notes
- Delete notes
- Uses a SQLite database with SQLAlchemy ORM
- Securely manages environment variables using python-dotenv

## How to Run
1. Clone the repository
2. Create a virtual environment:
   `python -m venv venv`
3. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies:
   `pip install -r requirements.txt`
5. Run the app:
   `python app.py`
6. Open your browser and go to `http://127.0.0.1:5000/`
