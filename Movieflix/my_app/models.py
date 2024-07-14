from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Director(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='directors/')
    bio = models.TextField()
    nationality = models.CharField(max_length=100)
    awards = models.TextField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])

    def __str__(self):
        return self.name

class Actor(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='actors/')
    bio = models.TextField()
    nationality = models.CharField(max_length=100)
    awards = models.TextField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    birthdate = models.DateField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='movies/')
    trailer = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dp = models.ImageField(upload_to='users/')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    status = models.IntegerField(choices=[(0, 'Active'), (1, 'Inactive')])
    date_joined = models.DateField()

    def __str__(self):
        return self.name

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name} - {self.movie.title}'

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name} - {self.movie.title}'
