# Generated by Django 4.2 on 2023-05-02 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='spirit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baptism_water', models.CharField(choices=[('oui', 'oui'), ('non', 'non')], max_length=3)),
                ('date', models.DateField(default=None, null=True)),
                ('baptism_spirit', models.CharField(choices=[('oui', 'oui'), ('non', 'non')], max_length=3)),
                ('commite', models.CharField(choices=[('ORDRE ET ACCEUIL', 'ORDRE ET ACCEUIL'), ('COMMITE SOCIAL', 'COMMITE SOCIAL')], max_length=16)),
                ('jeunesse', models.CharField(choices=[('ESTER', 'ESTHER'), ('EMMANUEL', 'EMMANUEL'), ('JOSUE', 'JOSUE'), ('OSE', 'OSE')], max_length=8)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulaires.person')),
            ],
        ),
        migrations.CreateModel(
            name='scolaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau', models.CharField(choices=[('JE CONTINUE LES COURS', 'JE CONTINUE LES COURS'), ('CP1', 'CP1'), ('CP2', 'CP2'), ('CE1', 'CE1'), ('CE2', 'CE2'), ('CM1', 'CM1'), ('CM2', 'CM2'), ('SIXIEME', 'SIXIEME'), ('CINQUIEME', 'CINQUIEME'), ('QUATRIEME', 'QUATRIEME'), ('TROISIEME', 'TROISIEME'), ('SECOND', 'SECOND'), ('PREMIERE', 'PREMIERE'), ('TERMINAL', 'TERMINAL'), ('LICENCE 1', 'LICENCE 1'), ('LICENCE 2', 'LICENCE 2'), ('LICENCE 3', 'LICENCE 3'), ('MASTER 1', 'MASTER 1'), ('MASTER 2', 'MASTER 2'), ('DOCTORAT', 'DOCTORAT')], max_length=21)),
                ('diplomes', models.CharField(choices=[('CEPE', 'CEPE'), ('BEPEC', 'BEPEC'), ('BACCALAUREAT', 'BACCALAUREAT'), ('BTS', 'BTS'), ('LICENCE 3', 'LICENCE 3'), ('MASTER', 'MASTER'), ('DOCTORAT', 'DOCTORAT'), ('DUT', 'DUT')], max_length=12)),
                ('series', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G')], max_length=12)),
                ('filiere', models.CharField(max_length=36)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulaires.person')),
            ],
        ),
    ]
