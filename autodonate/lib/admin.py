from django.contrib import admin

from autodonate.models import Item, Payment, PaymentProcess

admin.site.register(Item)
admin.site.register(Payment)
admin.site.register(PaymentProcess)