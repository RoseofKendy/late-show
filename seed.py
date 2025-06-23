import csv
import random
from app import app, db
from models import Episode, Guest, Appearance

def seed_from_csv():
    with open('seed.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        episode_counter = 1  # For assigning episode numbers
        guest_cache = {}     # To avoid duplicate guests

        for row in reader:
            date = row['Show'].strip()
            occupation = row['GoogleKnowlege_Occupation'].strip()
            guest_list = [name.strip() for name in row['Raw_Guest_List'].split(',') if name.strip()]

            # Create episode
            episode = Episode(
                date=date,
                number=episode_counter
            )
            db.session.add(episode)
            db.session.flush()  # Get episode.id

            # Create guest(s) and appearances
            for guest_name in guest_list:
                if guest_name not in guest_cache:
                    guest = Guest(
                        name=guest_name,
                        occupation=occupation if occupation != 'NA' else 'Unknown'
                    )
                    db.session.add(guest)
                    db.session.flush()
                    guest_cache[guest_name] = guest.id
                else:
                    guest = Guest.query.get(guest_cache[guest_name])

                appearance = Appearance(
                    rating=random.randint(1, 5),
                    episode_id=episode.id,
                    guest_id=guest.id
                )
                db.session.add(appearance)

            episode_counter += 1

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        seed_from_csv()
        db.session.commit()
        print("🌱 Database seeded from seed.csv successfully!")
