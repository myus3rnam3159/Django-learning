from django.db import models

#Các class được tạo dưới dây đều kế thừa lớp models.Model
class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    #Override phương thức của Model
    #Django sẽ thể hiện tên vaccine tương ứng với object
    #Chỉ cần thay đổi trong một class thì các class kế thừa Model cũng bị ảnh hưởng
    def __str__(self):
        return self.name
