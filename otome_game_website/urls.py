from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/', views.game_detail, name='game_detail'),
    path('character/<str:name>/', views.character_detail, name='character_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='otome_game_website/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]