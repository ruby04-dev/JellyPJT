# Generated by Django 3.2.18 on 2023-06-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0003_alter_diary_share'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='thumbnail',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]