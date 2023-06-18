from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = 'Run local server with https protocol'

    def add_arguments(self, parser):
        parser.add_argument('cert_file',
                            nargs='?',
                            default='cert.crt',
                            type=str)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\nServer start running...'))
        self.stdout.write(self.style.ERROR('\n!!!Don\'t run this command with stripe cli on!!!\n'))
        subprocess.Popen([
            'powershell',
            'python manage.py runserver_plus '
            f'--cert-file {options["cert_file"]}'
        ])
