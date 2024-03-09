from gensim import corpora, models
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

class TagGenerator:
    def __init__(self):
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text):
        """
        Tokenize, remove stopwords, and lemmatize text.
        """
        tokens = self.tokenizer.tokenize(text.lower())
        stopped_tokens = [i for i in tokens if not i in self.stop_words]
        lemma_tokens = [self.lemmatizer.lemmatize(i) for i in stopped_tokens]
        return lemma_tokens

    def filter_nouns_adjectives(self, words):
        """
        Filter nouns and adjectives from a list of words.
        """
        tagged_words = pos_tag(words)
        filtered_words = [word for word, tag in tagged_words if tag.startswith(('NN', 'JJ'))]
        return filtered_words

    def process_comments(self, comments):
        """
        Process a list of comments to extract topics/tags using LDA.
        """
        processed_comments = [self.preprocess_text(comment) for comment in comments]
        processed_comments = [self.filter_nouns_adjectives(comment) for comment in processed_comments]

        dictionary = corpora.Dictionary(processed_comments)
        corpus = [dictionary.doc2bow(text) for text in processed_comments]

        lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)

        topics = lda_model.print_topics(num_words=3)
        
        # Simplify topics to just lists of keywords for each topic
        tags = []
        for _, topic in topics:
            words = [word for word, _ in lda_model.show_topic(_, topn=3)]
            tags.extend(words)
        
        # Additional filtering to refine tags
        filtered_tags = [tag for tag in tags if tag not in self.stop_words and len(tag) > 3]
        
        return list(set(filtered_tags))
    
    def get_game_tags(self, game):
    # Aggregate tags from all comments related to characters of the game
        tags = []
        for character in game.characters.all():
            for comment in character.comments.all():
                tags.extend(self.process_comments(comment.text))
        
        return tags


comments = ["The unwavering devotion and his sweet moments make up most of the score, but this boy dragged me through hell and back by the hand and I’m still trying to catch my breath. If I could interpret some of his actions in a way, he’s got some very subtle yandere tendencies, and that’s something that I just don’t go for. It’s not favorite character type, so I might have a bit of a bias, but a character type/trope isn’t enough to completely ruin a route for me, especially if the route is well-written and enjoyable."]

tag_generator = TagGenerator()
tags = tag_generator.process_comments(comments)
print("Generated Tags:", tags)