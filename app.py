from flask import Flask , render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///notes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(255) , nullable = False)
    created_at = db.Column(db.DateTime , default = datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    notes = Note.query.order_by(Note.id.desc()).all()
    return render_template("index.html", notes=notes)



@app.route("/add" , methods=["POST"])
def add_note():
    content = request.form.get("content")
    if content.strip():
        new_note = Note(content=content)
        db.session.add(new_note)
        db.session.commit()
    return redirect("/")



@app.route("/delete/<int:id>")
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)