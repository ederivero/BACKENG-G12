# Generated by Django 4.2.2 on 2023-06-15 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(unique=True)),
                ('estante', models.TextField()),
                ('piso', models.TextField()),
            ],
            options={
                'db_table': 'categorias',
                'unique_together': {('estante', 'piso')},
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('fechaPublicacion', models.DateField(db_column='fecha_publicacion')),
                ('unidades', models.IntegerField(default=0)),
                ('sinopsis', models.TextField()),
                ('categoria', models.ForeignKey(db_column='categoria_id', on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='gestion.categoria')),
            ],
            options={
                'db_table': 'libros',
            },
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('nacionalidad', models.TextField()),
                ('foto', models.ImageField(upload_to='')),
                ('libros', models.ManyToManyField(to='gestion.libro')),
            ],
            options={
                'db_table': 'autores',
                'unique_together': {('nombre', 'nacionalidad')},
            },
        ),
    ]
