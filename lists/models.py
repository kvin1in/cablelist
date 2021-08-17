from django.db import models


class Item(models.Model):
    trace_id = models.AutoField(primary_key=True)
    addr = models.CharField(max_length=30, verbose_name="Адрес расположения трассы")
    floor_num = models.CharField(max_length=15, verbose_name="Номер этажа")
    room_num = models.CharField(max_length=15, verbose_name="Номер комнаты")
    komm_name = models.CharField(max_length=25, verbose_name="Наименование коммутатора")
    port_num = models.CharField(max_length=15, verbose_name="Номер порта коммутатора")
    patch_panel = models.CharField(
        max_length=25, verbose_name="Обозначение идентификатора патч-панели"
    )
    roz_name = models.CharField(
        max_length=18, verbose_name="Номер или наименование розетки в комнате"
    )
    notes = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Прочие примечания и отметки",
    )

    def __str__(self):
        return self.addr
