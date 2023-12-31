# Generated by Django 4.2.6 on 2023-10-06 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=200)),
                ('nome_produtora', models.CharField(max_length=50)),
                ('ano', models.DateTimeField(verbose_name='Data Publicada')),
                ('pais', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('quantidade', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
