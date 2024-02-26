from django.db import models

# Create your models here.

class Product(models.Model):
    product_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.product_type}'
    
    class Meta:
        verbose_name_plural = 'products'


class Riders(models.Model):
    rider_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.rider_type}'
    
    class Meta:
        verbose_name_plural = 'riders'


class Client(models.Model):
    gender_choices = [("Male", "Male"), ("Female", "Female")]
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    birthdate = models.DateField()
    age = models.IntegerField(default=None, null=True, blank=True)
    gender = models.CharField(max_length=50, default=None, null=True, blank=True, choices=gender_choices)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        if self.middle_name:
            return f'{self.last_name.upper()}, {self.first_name.title()} {"".join(m[0].upper() for m in self.middle_name.strip().split(" "))}.'
        # DELACRUZ, Juan
        return f"{self.last_name.upper()}, {self.first_name.title()}"
    
    class Meta:
        verbose_name_plural = 'clients'


class Beneficiary(models.Model):
    type_choices = [("Trustee", "Trustee"), ("Primary", "Primary")]
    relationship_choices = [
        ("Mother", "Mother"),
        ("Father", "Father"),
        ("Sister", "Sister"),
        ("Brother", "Brother"),
        ("Son", "Son"),
        ("Daughter", "Daugther"),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(default=None)
    relationship = models.CharField(max_length=50, choices=relationship_choices)
    percentage = models.FloatField(default=None)
    birthdate = models.DateField()
    type = models.CharField(max_length=50, choices=type_choices)
    is_irrevocable = models.BooleanField(default=False)

    def __str__(self):
        if self.middle_name:
            return f'{self.last_name.upper()}, {self.first_name.title()} {"".join(m[0].upper() for m in self.middle_name.strip().split(" "))}.'
        # DELACRUZ, Juan
        return f"{self.last_name.upper()}, {self.first_name.title()}"
    
    class Meta:
        verbose_name_plural = 'beneficiaries'


class InsurancePlan(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True,)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rider1 = models.ForeignKey(Riders, on_delete=models.CASCADE, blank=True, null=True, related_name="rider1")
    rider2 = models.ForeignKey(Riders, on_delete=models.CASCADE, blank=True, null=True, related_name="rider2")
    rider3 = models.ForeignKey(Riders, on_delete=models.CASCADE, blank=True, null=True, related_name="rider3")
    rider4 = models.ForeignKey(Riders, on_delete=models.CASCADE, blank=True, null=True, related_name="rider4")
    rider5 = models.ForeignKey(Riders, on_delete=models.CASCADE, blank=True, null=True, related_name="rider5")
    rider1_amount = models.FloatField(default=None, blank=True, null=True)
    rider2_amount = models.FloatField(default=None, blank=True, null=True)
    rider3_amount = models.FloatField(default=None, blank=True, null=True)
    rider4_amount = models.FloatField(default=None, blank=True, null=True)
    rider5_amount = models.FloatField(default=None, blank=True, null=True)
    face_amount = models.FloatField(default=None)
    policy_number = models.CharField(max_length=10)
    # number_of_years = models.IntegerField(default=None)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.client.last_name} {self.client.first_name} {self.client.middle_name}'
    
    class Meta:
        verbose_name_plural = 'insurance plans'