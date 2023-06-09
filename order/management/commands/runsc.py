import subprocess

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Run stripe cli for local server which takes one positional argument: '  \
            'stripe_webhook_url where you can write name of listening url'

    def add_arguments(self, parser):
        parser.add_argument('stripe_webhook_url',
                            nargs='?',
                            default='127.0.0.1:8000/payment/webhook/',
                            type=str)
        parser.add_argument('--nm',
                            action='store_true')

    def handle(self, *args, **options):
        if not options['nm']:
            self.stdout.write(self.style.SUCCESS('\nStripe cli start listening to '
                                                 f'{options["stripe_webhook_url"]}...\n'))

        subprocess.Popen([
            'powershell',
            f'stripe listen --forward-to {options["stripe_webhook_url"]}'])

