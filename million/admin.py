from django.contrib import admin

# Register your models here.
from million.models import*
admin.site.register(Table)
admin.site.register(Roles)
admin.site.register(Departments)
admin.site.register(Users)
admin.site.register(Meal_Catgories)
admin.site.register(Statuses)
admin.site.register(ServicePercentage)
admin.site.register(Meals)
admin.site.register(Orders)
admin.site.register(Checks)
admin.site.register(Meals_to_order)



