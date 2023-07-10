# Generated by Django 4.2.3 on 2023-07-08 07:42

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
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('weight', models.CharField(choices=[('L', 'Light'), ('M', 'Medium'), ('H', 'Heavy')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_name', models.CharField(max_length=250)),
                ('receiver_familyname', models.CharField(max_length=250)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('sending_date', models.DateTimeField(blank=True, null=True)),
                ('receiving_date', models.DateTimeField(blank=True, null=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.package')),
                ('receiver_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_shipments', to='shipment.address')),
                ('sender_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_shipments', to='shipment.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.city'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL),
        ),
    ]