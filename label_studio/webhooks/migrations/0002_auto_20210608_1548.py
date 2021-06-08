# Generated by Django 3.1.4 on 2021-06-08 15:48

import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20210310_2044'),
        ('webhooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook',
            name='headers',
            field=models.JSONField(default=dict, validators=[core.validators.JSONSchemaValidator({'additionalProperties': False, 'maxProperties': 10, 'patternProperties': {'^[a-zA-Z0-9-]+$': {'type': 'string'}}, 'type': 'object'})], verbose_name='request extra headers of webhook'),
        ),
        migrations.AddField(
            model_name='webhook',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is webhook active'),
        ),
        migrations.AddField(
            model_name='webhook',
            name='send_for_all_actions',
            field=models.BooleanField(default=True, verbose_name='Use webhook for all actions'),
        ),
        migrations.AlterField(
            model_name='webhook',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webhooks', to='organizations.organization'),
        ),
        migrations.AlterField(
            model_name='webhook',
            name='send_payload',
            field=models.BooleanField(default=True, verbose_name='does webhook send the payload'),
        ),
    ]
