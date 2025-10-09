from django.core.management import BaseCommand
from django.utils.autoreload import run_with_reloader
import atexit
import subprocess
import sys


class Command(BaseCommand):
    """
    Basic management command which will execute a process using the same
    autoreload mechanism used by the runserver command. Processes run with
    this command will be reloaded when changes are made to source files.
    
    A simple alternative to the Watchdog/watchmedo utility. Will also
    detects changes made to shared files/directories in a VM - Watchdog 
    doesn't do this well.
    
    TODO: Allow specification of signal used to restart the process
          (i.e. SIGTERM/SIGKILL)
    
    Examples:
      ./manage.py autoreload -- celery -A <project_name> worker -l info
    """

    help = "Run and auto-reload a process using the default django autoreloader"

    def handle(self, *args, **options):
        self.command = options['command']
        run_with_reloader(self.run_process)

    def add_arguments(self, parser):
        parser.add_argument('command', nargs='+')

    def run_process(self):
        process = subprocess.Popen(self.command)
        atexit.register(process.terminate)
        sys.exit(process.wait())