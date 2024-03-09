class Game:
    def __init__(self, title, introduction, platform):
        #game title
        self.title = title
        #game introduction
        self.introduction = introduction
        #which platform the game support, such as switch, steam
        self.platform = platform
        #characters in this game
        self.characters = [] 
        #negerated tags
        self.tags = []
        #the avarage rating of characters
        self.average_rating = 0.0

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, name):
        self.characters = [c for c in self.characters if name != name]

    def calculate_average_rating(self):
        total_rating = 0
        for c in self.characters:
            if c.get_ratings():
                total_rating += c.calculate_average_rating()
        self.average_rating = total_rating / len(self.characters)
        return self.average_rating

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def reset_tag(self):
        self.tag = []

    def get_info(self):
        return {
            'title': self.title,
            'introduction': self.introduction,
            'platform': self.platform,
            'average_rating': self.average_rating,
            'characters': [c.get_info() for c in self.characters],
            'tags': [t.name for t in self.tags]
        }