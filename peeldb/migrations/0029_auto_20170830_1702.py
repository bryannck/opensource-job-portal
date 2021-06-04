# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 17:02
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeldb", "0028_auto_20170823_1037"),
    ]

    operations = [
        migrations.RenameField(
            model_name="searchresult",
            old_name="location",
            new_name="other_location",
        ),
        migrations.AddField(
            model_name="searchresult",
            name="locations",
            field=models.ManyToManyField(
                related_name="location_search", to="peeldb.City"
            ),
        ),
        migrations.AddField(
            model_name="searchresult",
            name="other_skill",
            field=models.CharField(default="", max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="searchresult",
            name="search_text",
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.RemoveField(
            model_name="searchresult",
            name="job_post",
        ),
        migrations.AddField(
            model_name="searchresult",
            name="job_post",
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.RemoveField(
            model_name="searchresult",
            name="skills",
        ),
        migrations.AddField(
            model_name="searchresult",
            name="skills",
            field=models.ManyToManyField(
                related_name="skill_search", to="peeldb.Skill"
            ),
        ),
    ]
