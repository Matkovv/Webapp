from flask_sqlalchemy import SQLAlchemy
from Webapp import app

db = SQLAlchemy(app)

class Intention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

# Tworzenie bazy danych
with app.app_context():
    db.create_all()

    # Dodajemy przykładowe intencje
    if Intention.query.count() == 0:  # Tylko jeśli baza jest pusta
        intentions = [
            "Przyjmuję pozytywne energie.",
            "Z każdym dniem staję się lepszą wersją siebie.",
            "Dokonuję wyborów, które mnie uszczęśliwiają.",
            "Otwieram się na nowe doświadczenia.",
            "Przyciągam miłość i spokój.",
            "Mam siłę, by pokonywać wszelkie przeszkody.",
            "Wdzięczność otwiera nowe drzwi.",
        ]
        for text in intentions:
            intention = Intention(text=text)
            db.session.add(intention)
        db.session.commit()
