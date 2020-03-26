# Generated by Django 3.0.4 on 2020-03-26 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='demo.Book'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('books', models.ManyToManyField(to='demo.Book')),
            ],
        ),
    ]
