"""
Django management command to wait for the database to be
ready before starting the application.
This is useful in Docker environments where the database
may take some time to start up.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database to be ready."""

    def handle(self, *args, **options):
        """Handle the command."""
        self.stdout.write("Waiting for database...")

        # Here you would typically implement logic to
        # check if the database is ready.
        # For example, you could use a loop that tries
        # to connect to the database
        # and breaks when successful. This is a placeholder
        # for that logic.
        db_up = False
        while db_up is False:
            try:
                # Attempt to connect to the database
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is ready!"))
