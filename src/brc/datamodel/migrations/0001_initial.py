# Generated by Django 2.0.8 on 2018-09-06 09:35

from django.db import migrations, models
import django.db.models.deletion
import uuid
import vng_api_common.fields
import vng_api_common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Besluit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('identificatie', models.CharField(help_text='Identificatie van het besluit binnen de organisatie die het besluit heeft vastgesteld.', max_length=50, validators=[vng_api_common.validators.AlphanumericExcludingDiacritic()], verbose_name='identificatie')),
                ('verantwoordelijke_organisatie', vng_api_common.fields.RSINField(help_text='Het RSIN van de Niet-natuurlijk persoon zijnde de organisatie die het besluit heeft vastgesteld.', max_length=9, verbose_name='verantwoordelijke organisatie')),
                ('besluittype', models.URLField(help_text='Aanduiding van de aard van het BESLUIT. Referentie naar het BESLUITTYPE in de zaaktypecatalogus.', verbose_name='besluittype')),
                ('zaak', models.URLField(blank=True, help_text='Referentie naar de ZAAK waarvan dit besluit uitkomst is', verbose_name='zaak')),
                ('datum', models.DateTimeField(help_text='De beslisdatum (AWB) van het besluit.', validators=[vng_api_common.validators.UntilNowValidator()], verbose_name='datum')),
                ('toelichting', models.TextField(blank=True, help_text='Toelichting bij het besluit.', max_length=1000, verbose_name='toelichting')),
                ('bestuursorgaan', models.CharField(blank=True, help_text='Een orgaan van een rechtspersoon krachtens publiekrecht ingesteld of een persoon of college, met enig openbaar gezag bekleed onder wiens verantwoordelijkheid het besluit vastgesteld is.', max_length=50, verbose_name='bestuursorgaan')),
                ('ingangsdatum', models.DateField(help_text='Ingangsdatum van de werkingsperiode van het besluit.', verbose_name='ingangsdatum')),
                ('vervaldatum', models.DateField(blank=True, help_text='Datum waarop de werkingsperiode van het besluit eindigt.', null=True, verbose_name='vervaldatum')),
                ('publicatiedatum', models.DateField(blank=True, help_text='Datum waarop het besluit gepubliceerd wordt.', null=True, verbose_name='publicatiedatum')),
                ('verzenddatum', models.DateField(blank=True, help_text='Datum waarop het besluit verzonden is.', null=True, verbose_name='verzenddatum')),
                ('uiterlijke_reactiedatum', models.DateField(blank=True, help_text='De datum tot wanneer verweer tegen het besluit mogelijk is.', null=True, verbose_name='uiterlijke reactiedatum')),
            ],
            options={
                'verbose_name': 'besluit',
                'verbose_name_plural': 'besluiten',
            },
        ),
        migrations.CreateModel(
            name='BesluitInformatieObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('informatieobject', models.URLField(help_text='URL-referentie naar het informatieobject waarin (een deel van) het besluit beschreven is.', verbose_name='informatieobject')),
                ('besluit', models.ForeignKey(help_text='URL-referentie naar het BESLUIT.', on_delete=django.db.models.deletion.CASCADE, to='datamodel.Besluit')),
            ],
            options={
                'verbose_name': 'besluitinformatieobject',
                'verbose_name_plural': 'besluitinformatieobjecten',
            },
        ),
        migrations.AlterUniqueTogether(
            name='besluit',
            unique_together={('identificatie', 'verantwoordelijke_organisatie')},
        ),
        migrations.AlterUniqueTogether(
            name='besluitinformatieobject',
            unique_together={('besluit', 'informatieobject')},
        ),
    ]
