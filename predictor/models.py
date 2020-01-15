from django.db import models

# Create your models here.


class approvals(models.Model):
    Obtainmarks = models.FloatField()
    Time = models.FloatField()
    grade = models.CharField(max_length=100)

    def __str__(self):
        return f"User Grade {self.grade} User Score {self.Obtainmarks} User total time {self.Time}"
