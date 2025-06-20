from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_303_SEE_OTHER # For redirects after POST
from typing import Optional # For optional form fields

# Assuming these imports are correct based on your project structure
from config.db import conn
from schemas.note import noteEntity, notesEntity # Ensure these are correctly defined if used elsewhere

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_notes(request: Request):
    """
    Renders the main page with existing notes.
    """
    # Fetch all documents from the 'notes' collection in the 'notes' database
    # The find({}) method returns a cursor, which we can iterate over
    docs = conn.notes.notes.find({})
    
    newDocs = []
    for doc in docs:
        # Convert ObjectId to string for JSON serialization and template rendering
        # Ensure 'important' field exists and handle its type correctly
        newDocs.append({
            "id": str(doc["_id"]), # Convert ObjectId to string
            "title": doc.get("title", "No Title"), # Use .get() for safer access
            "desc": doc.get("desc", "No Description"),
            "important": doc.get("important", False), # Default to False if not present
        })
    
    # print(newDocs) # Good for debugging, but remove in production
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/", response_class=RedirectResponse)
async def create_note(
    request: Request,
    title: str = Form(...), # Require title
    desc: str = Form(...),  # Require description
    important: Optional[str] = Form(None) # Optional, will be "on" if checked, None otherwise
):
    """
    Handles the submission of a new note.
    """
    # Create a dictionary from the form data
    note_data = {
        "title": title,
        "desc": desc,
        "important": True if important == "on" else False, # Convert "on" to True, None to False
    }

    # Insert the new note into the MongoDB collection
    # conn.notes is the database, .notes is the collection
    result = conn.notes.notes.insert_one(note_data)
    
    # Optional: print the inserted ID for debugging
    # print(f"Note inserted with ID: {result.inserted_id}")

    # Redirect to the home page to show the updated list of notes
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)