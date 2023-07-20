# Generated by Django 4.2.3 on 2023-07-20 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_anggal_publish_loan_tanggal_publish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('tgl_invoice', models.DateField(blank=True, null=True)),
                ('principal_amout', models.FloatField(default=0.0)),
                ('Loan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='loan_invoice', to='home.loan')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
