from django.contrib import admin

from .models import Finch, Feeding, Photo, Toy

# Register your models here.
admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Photo)
admin.site.register(Toy)