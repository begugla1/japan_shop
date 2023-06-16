from django.core.management.base import BaseCommand
import subprocess
import random


class Command(BaseCommand):
    help = 'Command running celery api which takes one optional positional argument\n ' \
           ' where you can write name of your Django main_app'

    def add_arguments(self, parser):
        parser.add_argument('main_app',
                            nargs='?',
                            default='app',
                            type=str
                            )

        parser.add_argument('--nm',
                            action='store_true')

        parser.add_argument('--nw',
                            action='store_true',
                            )

    def handle(self, *args, **options):
        if not options['nm']:
            self.stdout.write(self.style.SUCCESS('Celery start running...'))

        command_tail = '--pool=solo' if not options['nw'] else ''
        subprocess.Popen([
            'powershell',
            f'celery -A {options["main_app"]} worker --loglevel=INFO '
            f'--concurrency=10 -n worker-{random.randint(1, 1000000)}.%h {command_tail}'
            ])


