from django.contrib import admin
from . models import GoalStatus
from . models import ScrumyGoals
from . models import ScrumyHistory

# Register your models here.
admin.site.register(GoalStatus)
admin.site.register(ScrumyGoals)
admin.site.register(ScrumyHistory)
