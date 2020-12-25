from django.contrib import admin
from .models import Card, Tag, Link, CardTag


def card(modeladmin, request, queryset):
    card.short_description = "Carousel and Cards"


class CardAdmin(admin.ModelAdmin):

    lisit_dispaly = ['title', 'info', 'description', 'image']
    ordering = ['title']
    actions = [card]


class LinkAdmin(admin.ModelAdmin):

    lisit_dispaly = ['name', 'url']
    ordering = ['name']
    actions = [card]


class TagAdmin(admin.ModelAdmin):

    lisit_dispaly = ['name']
    ordering = ['name']
    actions = [card]


class CardTagAdmin(admin.ModelAdmin):
    lisit_dispaly = ['id_tag', 'id_card']
    actions = [card]


admin.site.register(Card, CardAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(CardTag, CardTagAdmin)
