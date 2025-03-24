from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=25)

    class Meta:
        db_table = 'usuarios' #forzar a django a usar esta tabla

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    TIPO_CHOICES = [
        ('Ingreso', 'Ingreso'),
        ('Gasto', 'Gasto'),
    ]
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
    
class Transaccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('Ingreso', 'Ingreso'), ('Gasto', 'Gasto')])
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.monto} ({self.fecha})"
