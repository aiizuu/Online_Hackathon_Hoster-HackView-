# Generated by Django 3.0.5 on 2020-05-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0004_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='qa1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='questions',
            name='qa2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='questions',
            name='qa3',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='questions',
            name='qa4',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='questions',
            name='qa5',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='questions',
            name='qa6',
            field=models.TextField(),
        ),
    ]