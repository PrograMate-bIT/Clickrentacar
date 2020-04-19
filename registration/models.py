from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename


# Create your models here.
class Profile(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="id", null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ci = models.IntegerField(verbose_name="ci", null=True, blank=True)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(verbose_name="telefono", null=True, blank=True)
    birthDate = models.DateField(verbose_name="fechaNacimiento", null=True, blank=True)
    adress = models.CharField(verbose_name="calle", max_length=50, blank=False, null=True)

    class Meta:
        ordering = ['user__username']


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        # print("Se acaba de crear un usuario y su perfil enlazado")
