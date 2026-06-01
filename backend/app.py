from flask import Flask, jsonify, render_template_string
from backend.notes.routes import notes_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(notes_bp, url_prefix='/api/notes')

    spec = {
        "openapi": "3.0.0",
        "info": {"title": "Notes API", "version": "1.0.0"},
        "paths": {
            "/api/notes/": {
                "get": {
                    "summary": "List notes",
                    "responses": {"200": {"description": "A list of notes"}}
                },
                "post": {
                    "summary": "Create note",
                    "responses": {"201": {"description": "Note created"}}
                }
            },
            "/api/notes/{note_id}": {
                "get": {
                    "summary": "Get note by id",
                    "parameters": [{"name": "note_id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "responses": {"200": {"description": "Note found"}, "404": {"description": "Note not found"}}
                }
            }
        }
    }

    @app.route('/swagger.json')
    def swagger_json():
        return jsonify(spec)

    @app.route('/apidocs')
    def apidocs():
        html = '''
        <!doctype html>
        <html>
        <head>
          <meta charset="utf-8" />
          <title>Swagger UI</title>
          <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.18.3/swagger-ui.css" />
        </head>
        <body>
          <div id="swagger-ui"></div>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.18.3/swagger-ui-bundle.js"></script>
          <script>
            window.ui = SwaggerUIBundle({ url: '/swagger.json', dom_id: '#swagger-ui' })
          </script>
        </body>
        </html>
        '''
        return render_template_string(html)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
