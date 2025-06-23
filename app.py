from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Episode, Guest, Appearance
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)
with app.app_context():
    from flask_migrate import Migrate
    migrate = Migrate(app, db)

# GET /episodes
@app.route('/episodes')
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([ep.to_dict() for ep in Episode.query.all()])

# GET /episodes/:id
@app.route('/episodes/<int:id>')
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [a.to_dict() for a in episode.appearances]
    })

# GET /guests
@app.route('/guests')
def get_guests():
    return jsonify([g.to_dict() for g in Guest.query.all()])

# POST /appearances
@app.route('/appearances', methods=['POST'])
def create_appearance():
    try:
        data = request.get_json()

        rating = int(data['rating'])

        if rating < 1 or rating > 5:
            return {"errors": ["Rating must be between 1 and 5"]}, 400

        episode = Episode.query.get(data['episode_id'])
        guest = Guest.query.get(data['guest_id'])

        if not episode or not guest:
            return {"errors": ["Invalid episode or guest ID"]}, 400

        appearance = Appearance(
            rating=rating,
            episode_id=episode.id,
            guest_id=guest.id
        )
        db.session.add(appearance)
        db.session.commit()

        return jsonify(appearance.to_dict()), 201

    except Exception as e:
        print(f"🔥 Error: {e}")
        return {"errors": [str(e)]}, 500


if __name__ == '__main__':
    app.run(debug=True)
