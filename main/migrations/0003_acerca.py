# Generated by Django 3.1.5 on 2021-05-24 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210523_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acerca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_programa', models.CharField(max_length=30)),
                ('contenido', models.CharField(max_length=200)),
                ('inicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.inicio')),
            ],
        ),
    ]