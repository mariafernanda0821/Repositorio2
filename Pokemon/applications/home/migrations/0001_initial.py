# Generated by Django 3.1.6 on 2021-03-15 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad_name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.CreateModel(
            name='Moves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moves_name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regiones',
            },
        ),
        migrations.CreateModel(
            name='Sprites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('back_default', models.CharField(blank=True, default='null', max_length=200, null=True)),
                ('back_female', models.CharField(blank=True, default='null', max_length=200, null=True)),
                ('back_shiny', models.CharField(blank=True, default='null', max_length=200, null=True)),
                ('back_shiny_female', models.CharField(blank=True, default='null', max_length=200, null=True)),
                ('front_default', models.CharField(blank=True, default='null', max_length=200, null=True)),
                ('front_female', models.CharField(blank=True, default='null', max_length=200, null=True)),
                ('front_shiny', models.CharField(blank=True, default='null', max_length=200, null=True)),
                ('front_shiny_female', models.CharField(blank=True, default='null', max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Sprite',
                'verbose_name_plural': 'Sprites',
            },
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stats_SPEED', models.IntegerField()),
                ('stats_SPECIAL_DEFENSE', models.IntegerField()),
                ('stats_SPECIAL_ATTACK', models.IntegerField()),
                ('stats_DEFENSE', models.IntegerField()),
                ('stats_ATTACK', models.IntegerField()),
                ('stats_HP', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Stats',
                'verbose_name_plural': 'Stats de Pokemon',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types_name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'verbose_name': 'Tipos',
                'verbose_name_plural': 'Tipos de POkemon',
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_name', models.CharField(max_length=80, unique=True)),
                ('pokemon_capture_rate', models.CharField(blank=True, max_length=80, null=True)),
                ('pokemon_color', models.CharField(blank=True, max_length=80, null=True)),
                ('pokemon_flavor_text', models.TextField(blank=True)),
                ('pokemon_height', models.IntegerField(default=0)),
                ('pokemon_weight', models.IntegerField(default=0)),
                ('habilidad', models.ManyToManyField(to='home.Habilidades')),
                ('move', models.ManyToManyField(to='home.Moves')),
                ('sprites', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.sprites')),
                ('stats', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.stats')),
                ('types', models.ManyToManyField(to='home.Types')),
            ],
            options={
                'verbose_name': 'Pokemon',
                'verbose_name_plural': 'Pokemones',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=80, unique=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.region')),
            ],
            options={
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=80, unique=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.location')),
                ('pokemon', models.ManyToManyField(to='home.Pokemon')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
            },
        ),
    ]
