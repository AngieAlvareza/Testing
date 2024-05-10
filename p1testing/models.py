from django.db import models

# Create your models here.

class AuthorDb(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    fecha_nacimiento=models.DateField(verbose_name="Fecha Nacimiento", null=False, blank=False)
    fecha_fallecimiento=models.DateField(verbose_name="Fecha Fallecimiento", null = True, blank = True)
    profesion=models.CharField(verbose_name="Profesion", max_length=50)
    nacionalidad=models.CharField(verbose_name="Nacionalidad", max_length=50)

    class Meta:
        db_table = "Autores"
        verbose_name = "Autor"
        verbose_name = "Autores"
    def __str__(self) -> str:
        return self.nombre


class FraseDB(models.Model):
    cita = models.TextField(verbose_name="Cita", max_length=400)
    autor_fk = models.ForeignKey(AuthorDb, on_delete=models.CASCADE, related_name="frases")