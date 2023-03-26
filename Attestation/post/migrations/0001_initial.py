# Generated by Django 4.1.7 on 2023-03-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('headline', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]