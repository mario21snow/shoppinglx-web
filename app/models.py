from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
STATE_CHOICES = (
 ('Anadaman & Nicobar Island','Andaman & Nicobar Islands'),
 ('Andhra Pradesh','Andhra Pradesh'),
 ('Arunachal Pradesh','Aruanchal Pradesh'),
 ('Assam','Assam'),
 ('Bihar','Bihar'),
 ('Chandigarh','Chandigarh'),
 ('Chhattisgarh','Chhattisgarh'),
 ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
 ('Daman and Diu','Daman and Diu'),
 ('Delhi','Delhi'),
 ('Goa','Goa'),
 ('Gujarat','Gujarat'),
 ('Haryana','Haryana'),
 ('Himachal Pradesh','Himachal Pradesh'),
 ('Jammu & kashmir','Jammu & kashmir'),
 ('Jarkhand','Jarkhand'),
 ('Karanataka','Karanataka'),
 ( 'Kerala','Kerala'),
 ('Lakshadeep','Lakshadeep'),
 ('Madhya Pradeep','Madhya Pradeep'),
 ('Maharashtra','Maharashtra'),
 ('Meghalaya','Megehalaya'),
 ('Mizoram','Mizoram'),
 ('Nagaland','Nagaland'),
 ('Odisha','Odisha'),
 ('Punducherry','Punducherry'),
 ('Punjab','Punjab'),
 ('Rajasthan','Rajasthan'),
 ('Tamil Nadu','Tamil Nadu'),
 ('Telangana','Telanga'),
 ('Tripura','Tripura'),
 ('Uttarakhand','Uttarakhand'),
 ('Uttar Pradesh','Uttar Pradesh'),
 ('West Bengal','West Bengal'),
)
class Customer(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 name = models.CharField(max_length=200)
 locality = models.CharField(max_length=200)
 city = models.CharField(max_length=50)
 zipcode = models.IntegerField()
 state = models.CharField(choices=STATE_CHOICES, max_length=50)

 def __str__(self):
   return str(self.id)


CATEGORY_CHOICES = (
 ('M','Mobile'),
 ('L','Laptop'),
 ('TW','Top Wear'),
 ('BW','Bottom Wear'),
) 
class Product(models.Model):
 title = models.CharField(max_length=100)
 selling_price = models.FloatField()
 discounted_price = models.FloatField()
 description = models.TextField()
 brand = models.CharField(max_length=100)
 category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
 product_image = models.ImageField(upload_to='producting') 
  
 def __str__(self):
   return str(self.id)


class Cart(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)

 def __str__(self):
   return str(self.id)

 @property
 def total_cost(self):
   return self.quantity * self.product.discounted_price


STATUS_CHOICES = (
  ('Accepted','Accepted'),
  ('Packed','Packed'),
  ('On The Way','On The Way'),
  ('Delivered','Delivered'),
  ('Cancel','Cancel')
) 
 
class OrderPlaced(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
 product = models.ForeignKey (Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1) 
 ordered_date = models.DateTimeField(auto_now_add=True)
 status = models.CharField(max_length=50,
 choices=STATUS_CHOICES,default='Pending')  
 
 @property
 def total_cost(self):
   return self.quantity * self.product.discounted_price


    