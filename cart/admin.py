from django.contrib import admin
from .models import OrderItem, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'ordered_price',
                    'start_date',
                    # 'refund_requested',
                    # 'refund_granted',
                    # 'shipping_address',
                    # 'billing_address',
                    # 'payment',
                    # 'coupon'
                    ]
    list_display_links = [
        'user',
        'ordered_price',
        # 'shipping_address',
        # 'billing_address',
        # 'payment',
        # 'coupon'
    ]
    list_filter = ['ordered',
                   'start_date',
                   'being_delivered',
                   'received',
                   'ordered_price',
                #    'refund_requested',
                #    'refund_granted'
    ]
    search_fields = [
        'user__username',
        # 'ref_code'
    ]
    # actions = [make_refund_accepted]


admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
# admin.site.register(Payment)
# admin.site.register(Coupon)
# admin.site.register(Refund)
# admin.site.register(Address, AddressAdmin)
# admin.site.register(UserProfile)
