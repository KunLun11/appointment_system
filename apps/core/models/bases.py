from django.db import models


class BaseModelID(models.Model):
    class Meta:
        abstract = True
        ordering = ("-id",)

    id = models.BigAutoField("ID", primary_key=True, editable=False)

    def __str__(self) -> str:
        return f"#{self.pk}"


class BaseModelIDTime(BaseModelID):
    class Meta:
        abstract = True
        ordering = ("-created_at",)

    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)


__all__ = [
    "BaseModelID",
    "BaseModelIDTime",
]
