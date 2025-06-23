🎤 Late Show API

A RESTful Flask API that models guests appearing on a late-night talk show. This API allows you to fetch episodes, guests, and appearances, and supports creation and deletion of data. Built as part of a code challenge to demonstrate full-stack backend skills using Flask, SQLAlchemy, and Postman.

📁 Project Structure

late-show/
├── app.py # Main Flask application
├── models.py # SQLAlchemy models
├── seed.py # Seeds database from seed.csv
├── seed.csv # CSV data used for seeding
├── migrations/ # Flask-Migrate database versions
├── README.md # Project documentation
└── requirements.txt # Python dependencies

⚙️ Setup Instructions

1. Clone the Repository

```bash
git clone git@github.com:RoseofKendy/late-show.git
cd late-show

2. Create & Activate a Virtual Environment
bash
python3 -m venv venv
source venv/bin/activate

or 

pipenv shell

3. Install Dependencies
bash
pip install -r requirements.txt

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

5. Seed the Database
bash
python seed.py

6. Run the Server
bash
flask run
The API will be live at: http://localhost:5555
If not 
flask run --port=5555

📡 API Endpoints
GET /episodes
Returns a list of all episodes.

GET /episodes/<int:id>
Returns detailed info about a specific episode and its guest appearances.

GET /guests
Returns all guests.

POST /appearances
Creates a new appearance.

POST /appearances
Creates a new appearance.

🧪 Testing with Postman
Use the provided Postman collection to test your API:

Go to Postman → Import → Choose challenge-4-lateshow.postman_collection.json

Make sure your local server is running on http://localhost:5555

🛠 Technologies Used
Python 3
Flask
SQLAlchemy
Flask-Migrate
SQLite
Postman

🙌 Author
Made by Njue Sharon Kendi during Phase 4 at Moringa School.