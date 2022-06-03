from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=10)
    #put the data into database
    def register(self):
        self.save()

    def ifExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False

    @staticmethod
    def customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
