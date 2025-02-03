'''
this file will efine how data is stored, thing like patient information, call requests and etc
'''

from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255) #255 is max, example: Viya Atambayeva
    room_number = models.IntegerField() #ex: room 406 

    def __str__(self): #display
        return f"{self.name} (Room {self.room_number})"

class CallRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Completed', 'Completed')],
        default='Pending'
    )

    def __str__(self):
        return f"Call Request from {self.patient.name}"
