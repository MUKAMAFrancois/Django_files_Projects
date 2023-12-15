# Generated by Django 4.1.3 on 2023-04-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recapblog', '0004_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('business', 'BUSINESS'), ('tech', 'TECHNOLOGY'), ('sports', 'SPORTS'), ('health', 'HEALTH'), ('sciences', 'SCIENTIC'), ('travel', 'TRAVEL'), ('politics', 'POLITICS'), ('news', 'NEWS'), ('rest', 'OTHERS')], default='news', max_length=100),
        ),
    ]