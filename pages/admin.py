from django.contrib import admin
from pages.models import TeamMembers

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','title', 'is_part_of_team')
    list_editable = ('is_part_of_team', )


admin.site.register(TeamMembers, TeamAdmin)