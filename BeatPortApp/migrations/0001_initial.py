# Generated by Django 3.2.6 on 2021-09-03 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AfroHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'AFRO HOUSE',
            },
        ),
        migrations.CreateModel(
            name='BassClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'BASS / CLUB',
            },
        ),
        migrations.CreateModel(
            name='BassHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'BASS / HOUSE',
            },
        ),
        migrations.CreateModel(
            name='BreaksBreakBeatUKBass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'BREAKS / BREAKBEAT / UK BASS',
            },
        ),
        migrations.CreateModel(
            name='DanceElectroPop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'DANCE / ELECTRO POP',
            },
        ),
        migrations.CreateModel(
            name='DeepDubstepGrime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': '140 / DEEP DUBSTEP / GRIME',
            },
        ),
        migrations.CreateModel(
            name='DeepHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'DEEP HOUSE',
            },
        ),
        migrations.CreateModel(
            name='DJTools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'DJ TOOLS',
            },
        ),
        migrations.CreateModel(
            name='DrumAndBass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'DRUM & BASS',
            },
        ),
        migrations.CreateModel(
            name='Dubstep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'DUBSTEP',
            },
        ),
        migrations.CreateModel(
            name='ElectroClassicDetroitModern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'ELECTRO (CLASSIC / DETROIT / MODERN)',
            },
        ),
        migrations.CreateModel(
            name='Electronica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'ELECTRONICA',
            },
        ),
        migrations.CreateModel(
            name='FunkyHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'FUNKY HOUSE',
            },
        ),
        migrations.CreateModel(
            name='HardDanceHardcore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'HARD DANCE / HARDCORE',
            },
        ),
        migrations.CreateModel(
            name='HardTechno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'HARD TECHNO',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'HOUSE',
            },
        ),
        migrations.CreateModel(
            name='IndieDance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'INDIE DANCE',
            },
        ),
        migrations.CreateModel(
            name='JackinHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'JACKIN HOUSE',
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('remixers', models.CharField(blank=True, max_length=200)),
                ('video_id', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(blank=True, max_length=200)),
                ('release_date', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'MAIN',
            },
        ),
    ]