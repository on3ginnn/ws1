from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("category/<int:catalog_id>/", views.category),
]


# from django.contrib.syndication.views import Feed


# class BeatFeed(Feed):
#     description_template = "category.html"

#     def get_object(self, request, beat_id):
#         print('fff')
#         return Beat.objects.get(pk=beat_id)

    # def title(self, obj):
    #     return "Police beat central: Crimes for beat %s" % obj.beat

    # def link(self, obj):
    #     print('fff')
    #     return obj.get_absolute_url()

    # def description(self, obj):
    #     return "Crimes recently reported in police beat %s" % obj.beat

    # def items(self, obj):
    #     return Crime.objects.filter(beat=obj).order_by("-crime_date")[:30]