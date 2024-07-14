from django.contrib import admin

from .models import Country, State, City, Genre, Director, Actor, Movie, User, Review, Watchlist

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    search_fields = ('name',)
    list_filter = ('country',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state')
    search_fields = ('name',)
    list_filter = ('state',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nationality', 'gender', 'country', 'state', 'city')
    search_fields = ('name', 'nationality')
    list_filter = ('gender', 'country', 'state', 'city')

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nationality', 'gender', 'birthdate', 'country', 'state', 'city')
    search_fields = ('name', 'nationality')
    list_filter = ('gender', 'country', 'state', 'city')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year', 'genre', 'director')
    search_fields = ('title', 'description')
    list_filter = ('release_year', 'genre', 'director')
    filter_horizontal = ('actors',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'gender', 'status', 'date_joined', 'country', 'state', 'city')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('gender', 'status', 'country', 'state', 'city')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'user', 'rating', 'created_at')
    search_fields = ('comment',)
    list_filter = ('rating', 'created_at')

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie', 'added_at')
    list_filter = ('added_at',)
