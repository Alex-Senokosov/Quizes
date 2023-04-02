# Generated by Django 4.1.7 on 2023-04-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myQuize', '0005_rename_answer_1_myquize_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myquize',
            old_name='content',
            new_name='answer_1',
        ),
        migrations.RemoveField(
            model_name='myquize',
            name='cat',
        ),
        migrations.AddField(
            model_name='myquize',
            name='answer_2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='myquize',
            name='answer_3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='myquize',
            name='answer_correct',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='myquize',
            name='question',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='NotMyquize',
        ),
    ]