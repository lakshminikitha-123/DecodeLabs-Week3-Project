# AI Recommendation Logic - DecodeLabs Project 3

items = {
    "Technology": ["Laptop", "Python Course", "AI Newsletter"],
    "Sports": ["Football", "Fitness Tracker", "Sports Magazine"],
    "Music": ["Guitar", "Spotify Playlist", "Music Theory Course"],
    "Books": ["Atomic Habits", "Deep Work", "The Psychology of Money"],
    "Movies": ["Inception", "Interstellar", "The Martian"]
}

print("=== AI Recommendation System ===")
print("Available Interests:")
for category in items:
    print("-", category)

user_interest = input("\nEnter your interest: ").strip().title()

if user_interest in items:
    print("\nRecommended Items:")
    for item in items[user_interest]:
        print("✓", item)
else:
    print("\nNo exact match found. Please choose a listed interest.")
