from django.db import models
import json
import json

def safe_request_info(request):
    cleaned = {}
    for key, value in vars(request).items():
        try:
            json.dumps(value)  # test if serializable
            cleaned[key] = value
        except TypeError:
            cleaned[key] = str(value)  # fallback to string
    return cleaned

# Create your models here.
class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0.0)
    def __str__(self) -> str:
        return f"Current balance is {self.current_balance}"
class HistoryTracker(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE)
    amount = models.FloatField()
    expense_type = models.CharField(choices=(('CREDIT', 'Credit'), ('DEBIT', 'Debit')), max_length=200)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"The amount is {self.amount} for {self.description} expense type is {self.expense_type} and it is created at {self.created_at}"
#models.py

class RequestLogs(models.Model):
    request_info = models.TextField()
    request_type = models.CharField(max_length = 100)
    request_method = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)