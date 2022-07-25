from django.contrib import admin
from .models import Partner, exchange_rate,Gambia_tax,Operator,operator_ndcs
from tables.models import Service,HPMNTable



admin.site.register(Service)
admin.site.register(HPMNTable)


admin.site.register(Partner)
admin.site.register(Operator)
admin.site.register(operator_ndcs)
admin.site.register(exchange_rate)
admin.site.register(Gambia_tax)




# Register your models here.

