from django.contrib import admin
from . import models


class VoterAdmin(admin.ModelAdmin):

    list_display   = ('user', 'email', 'choosen',)

    def email(self, obj):
        return obj.user.email

    email.admin_order_field = 'user__email'


admin.site.register(models.Voter, VoterAdmin)
admin.site.register(models.Candidate)
