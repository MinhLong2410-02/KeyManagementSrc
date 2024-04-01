from django.contrib.auth.management.commands.createsuperuser import Command as BaseCommand
from django.core.management import CommandError

class Command(BaseCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        # Override the default behavior by not setting email as required
        parser.add_argument(
            '--email', dest='email', default=None,
            help='Specifies the email for the superuser.',
        )
    def handle(self, *args, **options):
        options['email'] = None 
        super().handle(*args, **options)
