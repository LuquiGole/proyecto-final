# Generated by Django 4.1.1 on 2022-10-10 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="autor",
            options={"verbose_name_plural": "Autores"},
        ),
        migrations.AlterModelOptions(
            name="seccion",
            options={"verbose_name_plural": "Secciones"},
        ),
    ]
