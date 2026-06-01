from flask import Blueprint, jsonify, request, abort
from pydantic import BaseModel, ValidationError

notes_bp = Blueprint('notes', __name__)

NOTES = [
    {"id": 1, "title": "Exemplo", "content": "Nota de exemplo"}
]

class NoteModel(BaseModel):
    title: str
    content: str


@notes_bp.route('/', methods=['GET'])
def list_notes():
    """
    List notes
    ---
    responses:
      200:
        description: A list of notes
        schema:
          type: array
          items:
            type: object
            properties:
              id: {type: integer}
              title: {type: string}
              content: {type: string}
    """
    return jsonify(NOTES)


@notes_bp.route('/<int:note_id>', methods=['GET'])
def get_note(note_id):
    """
    Get note by id
    ---
    parameters:
      - name: note_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Note found
      404:
        description: Note not found
    """
    for n in NOTES:
        if n['id'] == note_id:
            return jsonify(n)
    abort(404)


@notes_bp.route('/', methods=['POST'])
def create_note():
    """
    Create a note
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        schema:
          properties:
            title:
              type: string
            content:
              type: string
    responses:
      201:
        description: Note created
      400:
        description: Validation error
    """
    try:
        data = request.get_json()
        note = NoteModel(**data)
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except Exception:
        return jsonify({'error': 'Invalid JSON body'}), 400

    new_id = max([n['id'] for n in NOTES]) + 1 if NOTES else 1
    new_note = {"id": new_id, "title": note.title, "content": note.content}
    NOTES.append(new_note)
    return jsonify(new_note), 201
