# Generated by Django 2.1.1 on 2018-09-12 10:53

from django.db import migrations, models
import members.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Användarnamn')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='E-postadress')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='Förnamn')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='Efternamn')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Telefonnummer')),
                ('address', models.CharField(blank=True, max_length=50, verbose_name='Adress')),
                ('zip_code', models.CharField(blank=True, max_length=5, verbose_name='Postkod')),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='Postanstalt')),
                ('country', models.CharField(blank=True, default='Finland', max_length=30, verbose_name='Land')),
                ('membership_type', models.IntegerField(choices=[(1, 'Gulnäbb'), (2, 'Ordinarie medlem'), (3, 'Stödjande medlem'), (4, 'Seniormedlem')], default=1, verbose_name='Medlemskap')),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'medlem',
                'verbose_name_plural': 'medlemmar',
                'ordering': ('id',),
            },
            managers=[
                ('objects', members.models.MemberManager()),
            ],
        ),
    ]
