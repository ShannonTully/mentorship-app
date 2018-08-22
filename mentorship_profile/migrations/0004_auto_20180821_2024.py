# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-21 20:24
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship_profile', '0003_auto_20180801_0238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='area_of_expertise',
        ),
        migrations.AddField(
            model_name='mentor',
            name='areas_of_interest',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('portfolio_code_review', 'Portfolio / Code Reviews'), ('job_search_interviews', 'Job Search and Interviews'), ('industry_trends', 'Industry Trends, Skills, Technologies'), ('leadership_management', 'Leadership / Management'), ('business_entrepreneurship', 'Business, Entrepreneurship'), ('career_growth', 'Career Growth')], default='unknown', max_length=30),
        ),
    ]
