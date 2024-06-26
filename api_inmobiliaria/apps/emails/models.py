from django.db import models
from django.utils import timezone
from uuid import uuid4


class Token(models.Model):
    """
    This model represents a token that is used in various user-related email
    communication, the token is a unique identifier that ensures the security and
    validity of the processes initiated.
    """

    uuid = models.UUIDField(db_column="uuid", default=uuid4, primary_key=True)
    token = models.CharField(
        db_column="token",
        max_length=255,
        db_index=True,
        unique=True,
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        db_column="date_joined", auto_now_add=True
    )

    class Meta:
        db_table = "token"
        verbose_name = "Token"
        verbose_name_plural = "Tokens"
        ordering = ["-date_joined"]

    def is_expired(self) -> bool:
        """
        Check if the token is expired.
        """

        from apps.emails.domain.constants import TOKEN_EXPIRATION

        time_limit = self.date_joined + TOKEN_EXPIRATION
        current_datetime = timezone.now()

        return not current_datetime < time_limit

    def __str__(self) -> str:

        return self.token
