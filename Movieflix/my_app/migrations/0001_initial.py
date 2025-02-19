# Generated by Django 5.0.7 on 2024-07-11 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='actors/')),
                ('bio', models.TextField()),
                ('nationality', models.CharField(max_length=100)),
                ('awards', models.TextField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('birthdate', models.DateField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.country')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='directors/')),
                ('bio', models.TextField()),
                ('nationality', models.CharField(max_length=100)),
                ('awards', models.TextField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.country')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('release_year', models.IntegerField()),
                ('poster', models.ImageField(upload_to='movies/')),
                ('trailer', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('actors', models.ManyToManyField(to='my_app.actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.director')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.genre')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.country')),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.state'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.state'),
        ),
        migrations.AddField(
            model_name='actor',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.state'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dp', models.ImageField(upload_to='users/')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Inactive')])),
                ('date_joined', models.DateField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.state')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
        ),
    ]
