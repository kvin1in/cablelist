from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "addr",
        "floor_num",
        "room_num",
        "komm_name",
        "port_num",
        "patch_panel",
        "roz_name",
    )
    search_fields = ("addr", "floor_num")
    list_filter = ("room_num", "floor_num", "patch_panel")
    empty_value_display = "-пусто-"


# при регистрации модели Item источником конфигурации для неё назначаем класс PostAdmin
admin.site.register(Item, ItemAdmin)
