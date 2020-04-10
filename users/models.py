from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_unicode_patch(self):
    return '%s %s' % (self.first_name, self.last_name)