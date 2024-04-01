from main.models import Key

def schedule_key_deletion():
    keys = Key.objects.all()
    for key in keys:
        key.time_remaining -= 1
        key.save()
        if key.time_remaining <= 0:
            key.delete()