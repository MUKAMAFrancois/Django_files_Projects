# Generated by Django 4.1.3 on 2023-03-22 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp1', '0003_alter_post_options_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='posting',
        ),
    ]
