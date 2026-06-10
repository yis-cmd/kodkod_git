from typing import TypedDict
from fastapi import FastAPI, HTTPException

class Note(TypedDict):
	id:str 
	text:str

class Task(TypedDict):
	id:str
	text:str
	end_date:str

notes:dict[int, Note] = {}
tasks:dict[int, Task] = {}

app = FastAPI()

@app.get("/")
def get_all_notes():
	return notes

@app.get("/notes/{note_id}")
def get_note_by_id(note_id:int):
	try:
		return notes[note_id]
	except KeyError:
		raise HTTPException(404)

@app.post("/notes/{note_id}")
def add_note(note_id:int, text:str):
	global notes
	if note_id in notes:
		raise HTTPException(409)
	notes |= {note_id:{"id":note_id,"text":text}}

@app.put("/notes/{note_id}")
def update_note(note_id:int, text:str):
	if note_id not in notes:
		raise HTTPException(404)
	notes[note_id] = text

@app.delete("/notes/{note_id}")
def delete_note(note_id:int):
	if note_id not in notes:
		raise HTTPException(404)
	notes.pop(note_id)
	return {"deleted": note_id}