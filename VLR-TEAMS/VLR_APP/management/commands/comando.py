
from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    help = 'Añadir equipos a la base de datos'

    def add_arguments(self, parser):

        parser.add_argument('--add', action="store_true" ,help='Añade equipos desde Liquipedia')


    def handle(self, *args, **options):
        
        if options['add']:
            None