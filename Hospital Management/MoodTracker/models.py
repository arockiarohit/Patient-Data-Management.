from django.db import models
from django.utils import timezone

class information_db(models.Model):
    PatientName = models.CharField(max_length=50, null=True)
    Date = models.DateField(default=timezone.now)  
    Mood = models.CharField(max_length=50, null=True)
    StressLevel = models.IntegerField(default=0)
    SleepHours = models.IntegerField(default=0)
    Appetite = models.CharField(max_length=50, null=True)
    EnergyLevel = models.CharField(max_length=50, null=True)
    MedicationTaken = models.CharField(max_length=50, null=True)
    TherapyExercise = models.CharField(max_length=50, null=True)
    DailyGoalAchieved = models.CharField(max_length=50, null=True)
    Remarks = models.TextField(null=True)

    def __str__(self):
        return self.PatientName

class Patient_db(models.Model):
    PatientName = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    blood_group = models.CharField(max_length=3, null=True, blank=True)
    current_medications = models.TextField(null=True, blank=True)
    chronic_diseases = models.TextField(null=True, blank=True)
    previous_surgeries = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.PatientName

