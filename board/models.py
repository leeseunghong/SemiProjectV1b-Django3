from django.db import models
from datetime import datetime
from member.models import Member

# on_delete : CASCADE, DO_NOTHING
class board(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    userid=models.ForeignKey(Member, on_delete=models.CASCADE,
                             db_column='userid')
    regdate=models.DateTimeField(default=datetime.now)
    views=models.IntegerField(default=0)
    contents=models.TextField(null=False, blank=False)


    class Meta:
        db_table = 'board'
        ordering = ['-regdate']

    def __str__(self):
        return self.title