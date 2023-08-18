from django.core.management import BaseCommand

from catalog.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Seidov', 'first_name': 'Selim'},
            {'last_name': 'Seidov', 'first_name': 'Salih'},
            {'last_name': 'Nepesov', 'first_name': 'Pigam'},
            {'last_name': 'Jallyew', 'first_name': 'Serdar'},
        ]

    #    for student_item in student_list:
    #        Student.objects.create(**student_item)

        students_for_create = []
        for student_item in student_list:
            students_for_create.append(
                Student(**student_item)
            )

        Student.objects.bulk_create(students_for_create)

