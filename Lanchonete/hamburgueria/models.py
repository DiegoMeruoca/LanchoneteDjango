from django.db import models


class Cliente(models.Model):
    cpf_cliente = models.IntegerField(primary_key=True, verbose_name="CPF do cliente")
    nome_cliente = models.CharField(max_length=100, verbose_name="Nome do cliente")
    email_cliente = models.EmailField(max_length=254, verbose_name="E-mail do cliente")
    telefone_cliente = models.CharField(max_length=15, verbose_name="Telefone do cliente")
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField(max_length=10)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf_choices = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul (*)"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins")
    )
    uf = models.CharField(max_length=2, choices=uf_choices, default="SP")
    cep = models.CharField(max_length=9)

    def __str__(self):
        return self.nome_cliente


class Lanche(models.Model):
    nome_lanche = models.CharField(max_length=100, verbose_name="Nome do lanche")
    valor_lanche = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Valor do lanche")
    descricao = models.TextField(null=True, blank=True, verbose_name="Descrição")

    def __str__(self):
        return self.nome_lanche


class Acompanhamento(models.Model):
    nome_acompanhamento = models.CharField(max_length=100, verbose_name="Nome do acompanhamento")
    valor_acompanhamento = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Valor do acompanhamento")
    descricao = models.TextField(null=True, blank=True, verbose_name="Descrição")

    def __str__(self):
        return self.nome_acompanhamento


class Bebida(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da bebida")
    tipo = models.CharField(max_length=100, verbose_name="Tipo de bebida")
    marca = models.CharField(max_length=100, verbose_name="Marca da bebida")
    valor_bebida = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Valor da bebida")
    descricao = models.CharField(max_length=100, verbose_name="Descrição")

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    num_pedido = models.AutoField(primary_key=True)
    data = models.DateField()
    horario = models.TimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lanches = models.ManyToManyField("Lanche", blank=True)
    bebidas = models.ManyToManyField("Bebida", blank=True)
    acompanhamentos = models.ManyToManyField("Acompanhamento", blank=True)

    def __str__(self):
        return "Pedido numero: {} ".format(self.num_pedido)