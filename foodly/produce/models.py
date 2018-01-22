from django.db import models

class Person(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    dob = models.DateField(blank=True, null=True)
    gender = models.PositiveIntegerField()  # 0 male, 1 female
    updated_at = models.DateTimeField(auto_now=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"{} {}".format(self.firstname, self.lastname)


class Farm(models.Model):
    owner = models.ManyToManyField(Person,
            related_name='farms',
            related_query_name='farm')
    estimated_size = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u"Estimated size={}".format(self.estimated_size)
