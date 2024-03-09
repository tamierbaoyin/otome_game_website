from django import forms
from .models import Game, Character, Rating, Comment
from django.core.validators import MinValueValidator, MaxValueValidator

class GameForm(forms.ModelForm):
    score = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                               widget=forms.NumberInput(attrs={'type': 'number', 'min': '1', 'max': '5'}))
    class Meta:
        model = Game
        fields = ['title', 'platform', 'introduction', 'image']

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'storyline', 'image', 'game']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']