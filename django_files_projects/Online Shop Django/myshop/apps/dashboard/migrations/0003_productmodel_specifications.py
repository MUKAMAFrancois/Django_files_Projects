# Generated by Django 4.1.3 on 2023-08-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_productmodel_category_delete_categorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='specifications',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]