import datetime
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    phone_number = models.CharField(default="NIL", max_length=11, blank=True, null=True)
    email_verified = models.BooleanField(default=False, null=False)
    phone_verified = models.BooleanField(default=False, null=False)
    referral_link = models.CharField(default="NIL", max_length=256, null=True)
    referred_by = models.CharField(default="Admin", max_length=256, null=False)
    session_id = models.CharField(default=datetime.datetime.now(),db_column='session_ID', max_length=256)
    wallet_balance = models.DecimalField(default='0.00', max_digits=10, decimal_places=2)
    
    # REQUIRED_FIELDS = ('user', 'email', 'phone_number', 'email_verified', 'phone_verified', 'wallet_balance')
    # USERNAME_FIELD = 'username'

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
          
    def get_username(self):
        return self.user.objects.get('username')
    
    def get_full_name(self):
        first_name = self.user.objects.get('first_name')
        last_name = self.user.objects.get('last_name')
        return f"{first_name} {last_name}"
