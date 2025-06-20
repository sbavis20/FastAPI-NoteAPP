prN0tes: A Simple Note-Taking Application
prN0tes is a minimalist web application built with FastAPI and MongoDB for efficient note management. It allows users to quickly add new notes with titles and descriptions, and mark them as important. The notes are then displayed dynamically on the homepage.

Features
Create Notes: Easily add new notes with a title and description.
Mark as Important: Prioritize notes by marking them as "Important."
Dynamic Display: View all your notes listed on the homepage, with important notes visually highlighted.
Responsive Design: Built with Bootstrap 5, ensuring a pleasant experience across various devices.
MongoDB Integration: Persistently stores notes in a MongoDB database.
Technologies Used
FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
MongoDB: A popular NoSQL database for flexible data storage.
Jinja2: A modern and designer-friendly templating language for Python.
Bootstrap 5: The latest version of the world's most popular front-end open source toolkit, for responsive and stylish UI components.
Pymongo: The official PyMongo driver for MongoDB.
Project Structure
.
├── main.py              # Main FastAPI application entry point (assuming this is where your note router is included)
├── app
│   ├── note.py          # FastAPI router for note-related endpoints
│   ├── schemas
│   │   └── note.py      # Pydantic models for note data (if you have them, currently not explicitly used in the provided code)
│   └── config
│       └── db.py        # Database connection setup
└── templates
    └── index.html       # Jinja2 template for the main page
Note: The provided .py file seems to be note.py from the app directory. Ensure your main.py correctly imports and includes this router.

Setup and Installation
Follow these steps to get prN0tes up and running on your local machine.

Prerequisites
Python 3.7+
MongoDB: Make sure you have a MongoDB instance running. You can install it locally or use a cloud service like MongoDB Atlas.
1. Clone the Repository
Bash

git clone https://github.com/your-username/prN0tes.git
cd prN0tes
2. Create a Virtual Environment (Recommended)
Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
Bash

pip install fastapi "uvicorn[standard]" python-multipart Jinja2 pymongo
4. Configure MongoDB Connection
In app/config/db.py (or wherever your database connection is handled), ensure your MongoDB connection string is correctly set up. For example:

Python

# app/config/db.py
from pymongo import MongoClient

# Replace with your MongoDB connection string
# For a local MongoDB instance:
conn = MongoClient("mongodb://localhost:27017/")

# For MongoDB Atlas or other cloud services:
# conn = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority")

# Access the 'notes' database (it will be created if it doesn't exist)
db = conn.notes
Important: Replace <username>, <password>, <cluster-url>, and <dbname> with your actual MongoDB Atlas credentials if you're using it.

5. Run the Application
Assuming your main FastAPI application is in main.py and it includes the note router:

Python

uvicorn main:app --reload
If your main application is in app/note.py and you want to run it directly for testing (less common for larger apps but possible for small ones):

Bash

uvicorn app.note:note --reload
Note: The provided note.py defines an APIRouter instance named note. If this is intended to be the main application, you would typically define app = FastAPI() in a main.py and then include this router using app.include_router(note). The uvicorn command should point to your FastAPI instance. For this README, I'll assume your main.py aggregates your routers.

The application will now be running at http://127.0.0.1:8000. Open this URL in your web browser.

Usage
Open your browser and navigate to http://127.0.0.1:8000.
Add a New Note:
Enter a "Note Title" in the first input field.
Enter a "Note Description" in the textarea.
Optionally, check the "Mark as Important" checkbox.
Click the "Add Note" button.
View Your Notes: Your newly added note will appear below the form. Important notes will be highlighted with a yellow background and an "Important" tag.
