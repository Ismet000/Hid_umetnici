# Generated by Django 4.2.13 on 2024-07-01 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('type', models.CharField(blank=True, choices=[('IMP', 'impressionism'), ('POP', 'pop art'), ('GRA', 'graffiti')], max_length=30, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('description', models.TextField(max_length=255)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='islozba/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='islozba.artist')),
                ('exhibition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='islozba.exhibition')),
            ],
        ),
    ]
