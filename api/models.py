from django.db import models

# # TRY - from 
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
# from django.conf import settings
# from datetime import date

# class User(AbstractUser):
#   username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#   email = models.EmailField(_('email address'), unique = True)
# #   native_name = models.CharField(max_length = 5)
# #   phone_no = models.CharField(max_length = 10)
#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#   def __str__(self):
#       return "{}".format(self.email)

# class Event(models.Model):
#     title = pass 
#     organization = pass
#     location = pass
#     datetime = models.DateTimeField()
#     description = models.TextField()
#     tags = pass