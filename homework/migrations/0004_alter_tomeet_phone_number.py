# Generated by Django 4.1 on 2022-10-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_remove_tomeet_comment_alter_tomeet_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomeet',
            name='phone_number',
            field=models.IntegerField(default=True),
        ),
    ]
