# Generated by Django 4.2.3 on 2023-09-02 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcreatorApp', '0004_remove_keyword_id_keyword_keyword_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keyword',
            old_name='keyword_id',
            new_name='id',
        ),
    ]