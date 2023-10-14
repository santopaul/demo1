from django.contrib import admin
from . models import portfolio_status,portfolio_work,people_about,home_portfolio_status,home_portfolio_work
# Register your models here.
admin.site.register(portfolio_status)
admin.site.register(portfolio_work)
admin.site.register(people_about)
admin.site.register(home_portfolio_status)
admin.site.register(home_portfolio_work)