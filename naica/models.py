from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Poll(models.Model):
    """Represent table poll on database"""

    SEX_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Sin especificar'),
    ]

    sex = models.CharField(
        verbose_name='Sexo',
        max_length=1,
        choices=SEX_CHOICES,
        null=False,
        blank=False
    )
    age = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name='Edad',
        null=False,
        blank=False
    )
    financial_goals = models.BooleanField(
        verbose_name='Indica si cuentas con metas financieras:',
        default=False,
        null=False,
        blank=False
    )
    savings = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=Decimal(0.00),
        validators=[MinValueValidator(0)],
        verbose_name='Ahorro aproximado',
        null=False,
        blank=False
    )
    investment_knowledge = models.BooleanField(
        verbose_name='Indica si cuentas con conocimientos sobre inversiones',
        null=False,
        blank=False
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuestas'
