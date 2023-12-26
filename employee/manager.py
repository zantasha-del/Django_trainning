from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, first_name,last_name,address,date_of_birth, phone, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
           email = self.normalize_email(email),
           first_name = first_name,
           last_name = last_name,
           address= address,
           phone= phone,
           date_of_birth = date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password=password, **extra_fields)

    