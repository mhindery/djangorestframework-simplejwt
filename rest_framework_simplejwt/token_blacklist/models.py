from django.conf import settings
from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class OutstandingToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    jti = models.UUIDField(unique=True)
    token = models.TextField()

    created_at = models.DateTimeField()
    expires_at = models.DateTimeField()

    class Meta:
        ordering = ('user',)

    def __str__(self):
        return 'Token for {} ({})'.format(
            self.user,
            self.jti,
        )


@python_2_unicode_compatible
class BlacklistedToken(models.Model):
    token = models.OneToOneField(OutstandingToken, on_delete=models.CASCADE)

    blacklisted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Blacklisted token for {}'.format(self.token.user)