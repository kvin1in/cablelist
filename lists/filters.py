import django_filters

from .models import Item


class OrderFilter(django_filters.FilterSet):
    addr = django_filters.ChoiceFilter(
        choices=list(set((o.addr, o.addr) for o in Item.objects.all()))
    )
    floor_num = django_filters.ChoiceFilter(
        choices=list(set((o.floor_num, o.floor_num) for o in Item.objects.all()))
    )
    room_num = django_filters.ChoiceFilter(
        choices=list(set((o.room_num, o.room_num) for o in Item.objects.all()))
    )

    class Meta:
        model = Item
        fields = ["addr", "floor_num", "room_num"]
