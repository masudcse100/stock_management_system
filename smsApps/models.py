from django.db import models
# from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Categorie(models.Model):
    active = 1
    inactive = 0
    status = (
        (active, ('Active')),
        (inactive, ('Inactive')),
    )

    active  = models.IntegerField(default=0, choices=status)
    cat_name = models.CharField(max_length=264)
    cat_brand = models.CharField(max_length=264)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    class Meta:
        # ordering = {'-publish_date',}
        ordering = ['-publish_date',]
    def __str__(self):
        return self.cat_name