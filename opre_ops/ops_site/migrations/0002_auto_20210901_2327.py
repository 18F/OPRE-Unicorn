# Generated by Django 3.2.6 on 2021-09-01 23:27

from django.db import migrations
from csv import DictReader
from ops_site.models import Agency
from pathlib import Path

def seed_agencies(apps, schema_editor):
    filename = os.path.abspath("ops_site/test_data/agencies.csv")
    with open(filename) as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            agency = Agency(name=csv_dict_reader.get("name"), nickname=csv_dict_reader.get("nickname"))
            agency.save()

class Migration(migrations.Migration):

    dependencies = [
        ('ops_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_agencies)
    ]
