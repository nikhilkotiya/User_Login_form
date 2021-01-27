from django.db import models

is_active = (
    ('True', 'True'),
    ('False', 'False')
)


class User(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True ,verbose_name='first_name')
    email = models.EmailField(null=True, blank=True ,verbose_name='email')
    last_name = models.CharField(max_length=20,null=True, blank=True,verbose_name='last_name')
    password = models.CharField(max_length=20,null=True,blank=True,verbose_name='password')
    username = models.CharField(max_length=20,verbose_name='username')
    confirm = models.CharField(max_length=20,null=True,blank=True,verbose_name='confirm')
    is_client = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.email

        