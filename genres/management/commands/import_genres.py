import csv
from django.core.management.base import BaseCommand
from genres.models import Genre


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo csv com a lista de gêneros.',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']

                self.stdout.write(self.style.NOTICE(name))

                Genre.objects.create(
                    name=name,
                )

        self.stdout.write(self.style.SUCCESS('Gêneros cadastrados com sucesso!'))
