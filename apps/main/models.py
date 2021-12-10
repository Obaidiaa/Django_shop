from django.db import models

# models created with this base will inherit created_date and modified_date automatically
class ProductModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    product_name = models.CharField(max_length=100)
    product_skd = models.CharField(max_length=50,unique=True)
    product_price = models.DecimalField(max_digits=5,decimal_places=2)
    product_stock = models.DecimalField(max_digits=5,decimal_places=2)
    product_desc = models.CharField(max_length=240)

    # def json_to_form(self):
    #     data = self.

    # class Meta:
    #     abstract = True