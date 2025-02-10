from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    emblem = models.CharField(max_length=20)
    color = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.user.username == "Guest":
            self.user.email = ""
            self.user.set_unusable_password()
        else:
            if not self.user.email or not self.user.has_usable_password:
                raise ValidationError("Regular users must have an email and password.")
            super().save(*args, **kwargs)
        
#    def guest_validation(self):       
#        if self.user.username != 'Guest' and (not self.user.email or not self.user.password):
#            raise ValidationError('User must have email and password')
#        elif self.user.username == "Guest" and (self.user.email or self.user.password):
#            raise ValidationError("'Guest' cannot have email or password")
        