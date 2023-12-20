from django.db import models
from employee.manager import UserManager
from django.contrib.auth.models import User, AbstractBaseUser

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self) -> str:
        return self.first_name

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    employees = models.ManyToManyField(User, related_name='projects')

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)
    deadline = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User, related_name='tasks')

class Leave(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    employee = models.ForeignKey(User, on_delete=models.CASCADE)

class Salary(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
