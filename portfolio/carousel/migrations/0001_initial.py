# Generated by Django 3.1.4 on 2020-12-11 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('info', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=250)),
                ('id_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carousel.card')),
            ],
        ),
        migrations.CreateModel(
            name='CardTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carousel.card')),
                ('id_tab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carousel.tag')),
            ],
        ),
    ]
