from django.contrib import admin
from django.utils.safestring import mark_safe

from movies.models import Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Reviews



""" Category """
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( "id","name")
    list_display_links = ("name",)

""" Actor """
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='50' height='50' ")

    get_image.short_description = "Изображенне"


""" Genre """
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


""" Inline in Movie"""
class ReviewInline(admin.TabularInline): # StackedInline
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")
class MoviShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='50' height='50' ")

    get_image.short_description = "Изображенне"


""" Movie Shots """
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='50' height='50' ")

    get_image.short_description = "Изображенне"


""" Movie """
class MovieAdmin(admin.ModelAdmin):
    list_display = ( "title","category", "draft")
    list_display_links = ("title",)
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [MoviShotsInline,ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", ("image", "get_image"))
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fess_in_world"),)
        }),
        ("Options", {
            "fields": (("slug", "draft"),)
        }),
    )



    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображенне"

""" Rating """
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "movie", "ip")


""" Review """
class RevieAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")



admin.site.register(Category, CategoryAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieShots, MovieShotsAdmin)
admin.site.register(RatingStar)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Reviews, RevieAdmin)



admin.site.site_title = "Movies"
admin.site.site_header = "Admin Panel Movies"