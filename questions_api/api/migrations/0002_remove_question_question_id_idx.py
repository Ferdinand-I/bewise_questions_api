# Generated by Django 4.2.1 on 2023-05-28 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='question',
            name='question_id_idx',
        ),
    ]