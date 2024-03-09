class Character:
    def __init__(self, name, storyline):
        self.name = name
        self.storyline = storyline
        self.ratings = []
        self.comments = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def add_comment(self, comment):
        self.comments.append(comment)

    def calculate_average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0
    
    def get_ratings(self):
        return self._ratings

    def get_info(self):
        return {
            'character_id': self.character_id,
            'name': self.name,
            'storyline': self.storyline,
            'average_rating': self.calculate_average_rating(),
            'comments': self.comments
        }