from datetime import datetime

from django.contrib import admin
from .models import Exhibition, Artist, Artwork


# Register your models here.

class ExhibitionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    # Уметниците може да ги прегледаат само изложбите на кои имаат свое дело

    def get_queryset(self, request):
        qs = super(ExhibitionAdmin, self).get_queryset(request)
        artist = Artist.objects.filter(user=request.user).first()
        if artist:
            aws = Artwork.objects.filter(artist=artist)
            exhibition_ids = aws.values_list('exhibition_id', flat=True)
            return qs.filter(id__in=exhibition_ids)

        if request.user.is_superuser:
            return qs.filter(date_fromgte=datetime.now())

        return qs

    # def has_view_permission(self, request, obj=None):
    #     return Exhibition.objects.filter(request.user.is_superuser, date_end__lt=datetime.now())


class ArtistAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser


class ArtworkAdmin(admin.ModelAdmin):
    exclude = ['artist', ]

    def has_add_permission(self, request):
        return Artist.objects.filter(user=request.user).first()

    def save_model(self, request, obj, form, change):
        obj.artist = Artist.objects.filter(user=request.user).first()
        return super(ArtworkAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return Artist.objects.filter(user=request.user).first()


admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Artwork, ArtworkAdmin)
