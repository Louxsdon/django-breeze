from django_breeze.core.management import BaseCommand
import argparse
import sys


class StartAppCommand(BaseCommand):
    """
    A command that delegates to the Django admin startapp command.
    """

    name = "startapp"
    description = "A command that delegates to the Django admin startapp command"

    def add_arguments(self, parser):
        parser.add_argument(
            "app_args",
            help="Django admin startapp command arguments.",
            nargs=argparse.REMAINDER,
        )

    def handle(self, args):
        from django.core.management import execute_from_command_line

        execute_from_command_line(["django-admin"] + [args.command] + args.app_args)
