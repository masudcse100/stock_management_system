from django.db import models


# Create your models here.

class Categorie(models.Model):
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    cat_name = models.CharField(max_length=264)
    cat_brand = models.CharField(max_length=264)
    publish_date = models.DateTimeField(auto_now_add=True)
    # publish_date = models.DateTimeField()
    update_date = models.DateTimeField(auto_now=True)


    class Meta:
        # ordering = {'-publish_date',}
        ordering = ['-publish_date',]
    def __str__(self):
        return self.cat_name