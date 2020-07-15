# Generated by Django 3.0.8 on 2020-07-15 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport', models.CharField(choices=[('Car', 'Car'), ('Public', 'Public')], default='', max_length=50)),
                ('travell_locally_past_21dys', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('gathering_with_moreThan_10', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('contact_with_person_covid_positive', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caugh', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('shortness_of_breath', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('fever', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('body_pain', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('sore_throat', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('loss_of_taste', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('loss_of_smell', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caugh', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('shortness_of_breath', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('fever', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('body_pain', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('sore_throat', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('loss_of_taste', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('loss_of_smell', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('transport', models.CharField(blank=True, choices=[('Car', 'Car'), ('Public', 'Public')], default='', max_length=50)),
                ('travell_locally_past_21dys', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('gathering_with_moreThan_10', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('contact_with_person_covid_positive', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('medical_condition_risk_to_covid', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('medical_condition_in_family', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('understand_social_distancing', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('wear_mask', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('practice_safe_hygene', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('terms_and_conditions', models.CharField(blank=True, max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('comment', models.TextField(blank=True, default='', max_length=250)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hygiene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_condition_risk_to_covid', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('medical_condition_in_family', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('understand_social_distancing', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('wear_mask', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('practice_safe_hygene', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=50)),
                ('terms_and_conditions', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('comment', models.TextField(blank=True, default='', max_length=250)),
                ('Screening', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='riskAssesment.Screening')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]