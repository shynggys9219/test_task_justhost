from django.db import models
from traitlets import default

# Create your models here.

class VPS(models.Model):
    SERVER_STATUSES = [("STARTED","Started"), ("BLOCKED","Blocked"), ("STOPPED","Stopped")]
    
    # в задаче не совсем ясно было, uid является основным ключом или нет, я использовал его как основно
    # если так не должно быть, можно закомментировать это поле и разкомментировать следующее
    uid = models.IntegerField(primary_key=True)
    # uid = models.IntegerField()
    cpu = models.IntegerField()
    ram = models.IntegerField()
    hdd = models.IntegerField()
    status = models.CharField(max_length=15, choices=SERVER_STATUSES, blank=True)
    
    def __str__(self) -> str:
        return f"UID: {self.uid}, Status: {self.status}"
    
