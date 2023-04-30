from django_breeze.core.management import BaseCommand
import argparse
import sys


class StartProjectCommand(BaseCommand):
    """
    A command that delegates to the Django admin startproject command.
    """

    name = "startproject"
    description = "A command that delegates to the Django admin startproject command"

    def add_arguments(self, parser):
        parser.add_argument(
            "project_args",
            help="Django admin startproject command arguments.",
            nargs=argparse.REMAINDER,
        )

    def handle(self, args):
        from django.core.management import execute_from_command_line

        execute_from_command_line(["django-admin"] + [args.command] + args.project_args)
