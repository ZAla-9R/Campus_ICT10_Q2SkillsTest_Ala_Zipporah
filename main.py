clubs = {
    "Band club": {
        "name": "Band club",
        "description": "A band club is a group of students who share a passion for music and come together to practice, perform, and appreciate various musical styles.",
        "meeting": "Every Wednesday 3:30-5:00 PM",
        "location": "Room 406",
        "moderator": "Mr. Ciriaco",
        "members": 20,
        "category": "Music"
    },
    "Science Club": {
        "name": "Science Club",
        "description": "Explore experiments, research, and science competitions.",
        "meeting": "Every Monday 4:00-5:00 PM",
        "location": "Lab 2",
        "moderator": "Mr. Calpo",
        "members": 25,
        "category": "Science and Acedemic"
    },
    "Math Club": {
        "name": "Math Club",
        "description": "A club for students who enjoy solving mathematical problems and exploring mathematical concepts.",
        "meeting": "Fridays 3:00-4:30 PM",
        "location": "Room 502",
        "moderator": "Mr. Ferma",
        "members": 18,
        "category": "Academic"
    }
}

def get_club_info(club_name):
    return clubs.get(club_name, None)

# Example usage (for testing)
if __name__ == "__main__":
    test = get_club_info("Band club")
    print(test)