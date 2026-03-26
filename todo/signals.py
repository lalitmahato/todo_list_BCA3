from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
import time
from todo.models import Todo

@receiver(pre_save, sender=Todo)
def todo_pre_save(sender, instance, **kwargs):
    print(f"[PRE_SAVE] Todo about to be saved: {instance.title}")

@receiver(post_save, sender=Todo)
def todo_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"[POST_SAVE] New Todo created: {instance.title}")
    else:
        print(f"[POST_SAVE] Todo updated: {instance.title}")

@receiver(pre_delete, sender=Todo)
def todo_pre_delete(sender, instance, **kwargs):
    print(f"[PRE_DELETE] Todo about to be deleted: {instance.title}")

@receiver(post_delete, sender=Todo)
def todo_post_delete(sender, instance, **kwargs):
    print(f"[POST_DELETE] Todo deleted: {instance.title}")