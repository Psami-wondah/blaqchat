from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone



# class User(AbstractUser):
#     username = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)

class Chat(models.Model):
    initiator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="initiator_chat")
    acceptor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="acceptor_name")
    short_id = models.CharField(max_length=255, default=uuid.uuid4, unique=True)

    def _str_(self) -> str:
        return str(self.room_name)
    
    def get_messages(self):
        pass

class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.TextField()
    created_at = models.DateTimeField( default=timezone.now)

    def _str_(self) -> str:
        return f"{self.chat.room_name}-{self.sender.username}"