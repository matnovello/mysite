# Generated by Django 3.2 on 2021-04-22 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_question_question_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
    ]
