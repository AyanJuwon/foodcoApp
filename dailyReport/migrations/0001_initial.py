# Generated by Django 3.2 on 2022-01-07 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_of_distribution', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pastries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[('meat_pie', 'Meat Pie'), ('chicken_pie', 'Chicken Pie'), ('doughnut', 'Doughnut')], max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterialRecieved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(choices=[('sugar', 'Sugar'), ('salt', 'Salt'), ('Flour', 'Flour')], max_length=255)),
                ('amount', models.FloatField()),
                ('price', models.FloatField()),
                ('transfer_cost', models.FloatField()),
                ('material_cost', models.FloatField()),
                ('time_of_day', models.DateField(auto_now_add=True, verbose_name='date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MorningEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=255)),
                ('time_of_day', models.CharField(choices=[('Morning', 'Morning'), ('Evening', 'Evening')], max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('raw_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dailyReport.rawmaterialrecieved')),
            ],
        ),
        migrations.CreateModel(
            name='EndOfDayReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_pastries', models.IntegerField()),
                ('no_of_pastries_sent', models.IntegerField()),
                ('no_of_pastries_not_sold', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('distribution', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dailyReport.disribution')),
            ],
        ),
    ]
