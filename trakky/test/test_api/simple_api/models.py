from django.db import models
import uuid

def generate_sequential_uuid():
    # This function generates sequential UUIDs starting from 1
    return uuid.UUID(int=uuid.uuid1().int & (2**122 - 1) | (1 << 122))

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_sequential_uuid, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
