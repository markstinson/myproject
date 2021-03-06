from django.db import models

# Create your models here.

class Contact(models.Model):
    """docstring for Contact model """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    website_url = models.URLField(blank=True)

    def __unicode__(self):
    	""" it's effectively calling str(model_object) """
        return "{0} {1} <{2}>".format(
            self.first_name,
            self.last_name,
            self.email
        )

    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def useful_email(self):
        return '<a href="mailto:{0}">{0}</a>'.format(self.email)

    useful_email.allow_tags = True
    useful_email.admin_order_field = 'email'