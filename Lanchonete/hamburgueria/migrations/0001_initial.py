# Generated by Django 3.0.2 on 2020-07-16 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanhamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_acompanhamento', models.CharField(max_length=100, verbose_name='Nome do acompanhamento')),
                ('valor_acompanhamento', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor do acompanhamento')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da bebida')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo de bebida')),
                ('marca', models.CharField(max_length=100, verbose_name='Marca da bebida')),
                ('valor_bebida', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor da bebida')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cpf_cliente', models.IntegerField(primary_key=True, serialize=False, verbose_name='CPF do cliente')),
                ('nome_cliente', models.CharField(max_length=100, verbose_name='Nome do cliente')),
                ('email_cliente', models.EmailField(max_length=254, verbose_name='E-mail do cliente')),
                ('telefone_cliente', models.CharField(max_length=15, verbose_name='Telefone do cliente')),
                ('logradouro', models.CharField(max_length=50)),
                ('numero', models.IntegerField(max_length=10)),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul (*)'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='SP', max_length=2)),
                ('cep', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Lanche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_lanche', models.CharField(max_length=100, verbose_name='Nome do lanche')),
                ('valor_lanche', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor do lanche')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('num_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('acompanhamentos', models.ManyToManyField(blank=True, to='hamburgueria.Acompanhamento')),
                ('bebidas', models.ManyToManyField(blank=True, to='hamburgueria.Bebida')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamburgueria.Cliente')),
                ('lanches', models.ManyToManyField(blank=True, to='hamburgueria.Lanche')),
            ],
        ),
    ]
