from django.db import models
from gallery.models import Book
from account.models import User
# Create your models here.


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    
    ordered = models.BooleanField(default=False, verbose_name='سفارش شده')
    item = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='محصول')
    quantity = models.IntegerField(default=1, verbose_name='تعداد')

    def __str__(self):
        return f"{self.quantity} تا {self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.get_book_offer_price()

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.percent!=0:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

    class Meta:
        verbose_name = 'آیتم سفارشی'
        verbose_name_plural = 'آیتم های سفارشی'



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    
    items = models.ManyToManyField(OrderItem, verbose_name='محصول')
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ شروع')
    ordered_date = models.DateTimeField(verbose_name='تاریخ سفارش')
    ordered = models.BooleanField(default=False, verbose_name='سفارش شده')
    
    # coupon = models.ForeignKey(
    #     'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    
    being_delivered = models.BooleanField(default=False, verbose_name='ارسال')
    received = models.BooleanField(default=False, verbose_name='دریافت')
    # refund_requested = models.BooleanField(default=False, verbose_name='refund_requested')
    # refund_granted = models.BooleanField(default=False, verbose_name='refund_granted')

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات کاربران'

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        # if self.coupon:
        #     total -= self.coupon.amount
        return total


# class Coupon(models.Model):
#     code = models.CharField(max_length=15)
#     amount = models.FloatField()

#     def __str__(self):
#         return self.code


# class Refund(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     reason = models.TextField()
#     accepted = models.BooleanField(default=False)
#     email = models.EmailField()

#     def __str__(self):
#         return f"{self.pk}"


# def userprofile_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         userprofile = UserProfile.objects.create(user=instance)


# post_save.connect(userprofile_receiver, sender=User)
