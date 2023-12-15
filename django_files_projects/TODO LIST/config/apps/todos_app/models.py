from django.db import models
from django.contrib.auth.models import User


categories = (
    ('job', 'Job Issues'),
    ('school', 'School'),
    ('family', 'Family'),
    ('daily_acts', 'Daily Routine'),
    ('vacation', 'Vacation & Weekends'),
    ('business', 'My Business'),
    ('others', 'Others')
)

class TodoModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=233)
    category = models.CharField(max_length=80, choices=categories, default='daily_acts')
    due_date = models.DateField(auto_now=True)
    description =models.TextField()
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering=('due_date',)

    def __str__(self):
        return self.title
