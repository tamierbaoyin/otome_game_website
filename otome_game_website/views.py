from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.urls import reverse

# Create your views here.
from .models import Game, Character, Rating, Comment, Tag
from .forms import RatingForm, CommentForm
from .otome_game_project.tagGenerator import TagGenerator

#@api_view(['GET'])
def game_detail(request):
    game = Game.objects.first()  
    characters = game.characters.all() 

    overall_rating = Rating.objects.filter(character__game=game).aggregate(average=Avg('score'))['average']
    tags = game.tags.all()
    
    # Get tags for the game 
    # game_tags = get_game_tags(game)
    
    return render(request, 'otome_game_website/game_detail.html', {
        'game': game,
        'characters': characters,
        'overall_rating': overall_rating,
        'tags': tags,
        # 'game_tags': game_tags
    })
    


def character_detail(request, name):
    character = get_object_or_404(Character, id=name)
    rating_form = RatingForm()
    comment_form = CommentForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            if 'rate' in request.POST:
                rating_form = RatingForm(request.POST)
                if rating_form.is_valid():
                    rating = rating_form.save(commit=False)
                    rating.user = request.user
                    rating.character = character
                    rating.save()
                    return redirect(request.path_info)  # Refresh the page to clear the form
            elif 'comment' in request.POST:
                comment_form = CommentForm(request.POST)
                if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.user = request.user
                    comment.character = character
                    comment.save()
                    
                    newTag = TagGenerator()
                    
                    tags = newTag.process_comments([comment.text])
                    game = Game.objects.first()
                    # Save generated tags to the database
                    for tag_name in tags:
                        tag, created = Tag.objects.get_or_create(name=tag_name)
                        if tag not in game.tags.all():
                            game.tags.add(tag)
                    return redirect(request.path_info)  # Refresh the page to clear the form
                    
            else:
                return redirect('%s?next=%s' % (reverse('login'), request.path_info))

        
    
    # Calculate overall rating
    overall_rating_result = character.ratings.aggregate(average=Avg('score'))
    overall_rating = overall_rating_result['average'] if overall_rating_result['average'] is not None else "No ratings yet"

    
    return render(request, 'otome_game_website/character_detail.html', {
        'character': character,
        'rating_form': rating_form,
        'comment_form': comment_form,
        'overall_rating': overall_rating,
        'comments': character.comments.all(),
    })
    