from django.contrib import admin
import venues.models as v_m

# Register your models here.
class VenueAdmin(admin.ModelAdmin):
    pass

admin.site.register(v_m.Venue, VenueAdmin)
