from django.db import models

class HitParadeManager(models.Manager):


    def get_or_none(self, **kwargs):

        try:
            return self.get(**kwargs)
        except (self.model.DoesNotExist, self.model.MultipleObjectsReturned) as e:
            return None
