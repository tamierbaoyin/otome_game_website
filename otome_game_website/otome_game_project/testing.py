from game import Game
from character import Character
from user import User

# Create a game
game = Game("Collar x Malice"," ", "Switch")

# Create characters for the game
aiji = Character("Aiji Yanagi"," ")
kei = Character("Kei Okazaki"," ")

# Add characters to the game
game.add_character(aiji)
game.add_character(kei)

# Create a user
user1 = User("Tamier","0426")

# User rates and comments on a character
user1.give_rating(aiji, 5)
aiji.add_rating(5)
user1.give_comments(aiji, "Loved the storyline and character development.")
aiji.add_comment("Loved the storyline and character development.")

# Calculate the average rating for Aiji Yanagi
print(f"Aiji's Average Rating: {aiji.calculate_average_rating()}")

# Print comments for Aiji Yanagi
print(f"Aiji's Comments: {aiji.comments}")