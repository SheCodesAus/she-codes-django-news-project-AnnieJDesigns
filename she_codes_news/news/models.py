from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        USER, on_delete= models.CASCADE,
        related_name="stories"
    )
    content = models.TextField()

    class Meta:
        ordering = ['-pub_date']

    #Add image field
    image_field = models.URLField(max_length=200, null=True)


    
    



