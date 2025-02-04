from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)       # Patient's name
    room_number = models.IntegerField()           # Patient's room number

    def __str__(self):
        return f"{self.name} (Room {self.room_number})"

# Call Request Model
class CallRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # Link to Patient
    created_at = models.DateTimeField(auto_now_add=True)            # Timestamp when the call was made
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Completed', 'Completed')],  # Status options
        default='Pending'                                             # Default status
    )

    def __str__(self):
        return f"Call Request from {self.patient.name}"
