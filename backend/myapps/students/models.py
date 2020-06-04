from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=140)
    course = models.CharField(max_length=140)
    rating = models.IntegerField()

    class Meta:
        ordering = ['-name', ]
        verbose_name = "student"
        verbose_name_plural = "students"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('students:student_detail', kwargs={'pk': self.pk})
