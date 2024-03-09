class User:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
        self.ratings = {}  # key: character name, value: rating
        self.comments = {}  # key: characte name, value: comment

    def give_rating(self, character_name, rating):
        self.ratings[character_name] = rating

    def give_comments(self, character_name, comment):
        self.comments[character_name] = comment

    def get_ratings(self):
        return self.ratings

    def get_comments(self):
        return self.comments