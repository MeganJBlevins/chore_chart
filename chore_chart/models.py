from django.db import models
from django.contrib.auth.models import User

class Chore(models.Model):
    chore_name = models.CharField(max_length=264, unique=True)
    description = models.CharField(max_length=264, null=True)
    value = models.DecimalField(decimal_places=2,max_digits=4)  
    image = models.CharField(max_length=128, null=True)
    
    def __str__(self):
        return self.chore_name

class UserProfileInfo(models.Model):
    image_choices = [
        ('monster', 'Monster'),
        ('princess', 'Princess'),
        ('unicorn', 'Unicorn'),
        ('dinosaur', 'Dinosaur'),
        ('car', 'Car'),
    ]
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    profile_image = models.CharField(max_length=10, choices=image_choices, default='princess')
    bank = models.IntegerField(default=0)
    goal = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username



 # class Completed(models.Model):
 #    chore_id = models.ForeignKey(Chore)

 #    def __str__(self):
 #        return self.str(chore_id)


# class CompletedChore(models.Model)
#     chore_id = models.ForeignKey(Chore)
#     user_id = models.ForeignKey(User)
#     completed_date = models.DateField()

#      def __str__(self):
#         return self.str(completed_date)
