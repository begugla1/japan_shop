import random
import subprocess

from django.core.management.base import BaseCommand


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
            self.stdout.write(self.style.SUCCESS('\nCelery start running '
                                                 f'with settings of {options["main_app"]}\n'))

        command_tail = '--pool=solo' if not options['nw'] else ''
        subprocess.Popen([
            'zsh',
            f'celery -A {options["main_app"]} worker --loglevel=INFO '
            f'--concurrency=10 -n worker-{random.randint(1, 1000000)}.%h {command_tail}'
            ])


