from django.db import models

class Ruta(models.Model):
    nombre = models.CharField(max_length=255, default='')

    def __str__(self):
        return '{}'.format(self.nombre)

class Operador(models.Model):
    cedula = models.CharField(blank=False, max_length=10, primary_key=True)
    nombres = models.CharField(max_length=255, default='')
    
    def __str__(self):
        return '{}'.format(self.nombres)

class Gasolina(models.Model):
    nivel = models.CharField(max_length=15, default='')

    def __str__(self):
        return '{}'.format(self.nivel)

class Despacho(models.Model):
    hora = models.CharField(max_length=15, default='')
    unidad = models.CharField(max_length=10, default='')
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    kilometraje = models.IntegerField(default=0)
    gasolina = models.ForeignKey(Gasolina, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=255, default='', blank=True)
    status = models.BooleanField(default=1)
    create_at = models.DateTimeField(auto_now=True)