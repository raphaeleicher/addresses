from tabnanny import verbose
from django.db import models
from django.urls import reverse


class Salutation(models.Model):
    salutation = models.CharField(max_length=50)

    class Meta:
        verbose_name = "salutation"
        verbose_name_plural = "salutations"

    def __str__(self):
        return self.salutation

    def get_absolute_url(self):
        return reverse("salutation-detail", kwargs={"pk": self.pk})


class LastName(models.Model):
    last_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "last name"
        verbose_name_plural = "last names"

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse("last-name-detail", kwargs={"pk": self.pk})


class GivenName(models.Model):
    given_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "given name"
        verbose_name_plural = "given names"

    def __str__(self):
        return self.given_name

    def get_absolute_url(self):
        return reverse("given-name-detail", kwargs={"pk": self.pk})


class Street(models.Model):
    street_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "street"
        verbose_name_plural = "streets"

    def __str__(self):
        return self.street_name

    def get_absolute_url(self):
        return reverse("street-detail", kwargs={"pk": self.pk})


class Address(models.Model):
    given_name = models.ForeignKey(
        GivenName,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    last_name = models.ForeignKey(
        LastName,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    street = models.ForeignKey(
        Street,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    street_nr = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
