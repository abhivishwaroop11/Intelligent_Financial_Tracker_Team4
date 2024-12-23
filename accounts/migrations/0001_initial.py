# Generated by Django 5.1.3 on 2024-12-19 14:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Utilities', 'Utilities'), ('Entertainment', 'Entertainment'), ('Others', 'Others')], default='Others', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_budget', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('entertainment_budget', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('utilities_budget', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('others_budget', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
