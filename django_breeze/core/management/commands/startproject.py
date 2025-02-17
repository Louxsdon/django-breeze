import argparse
import sys
from pathlib import Path
from copier import run_copy

from django_breeze.core.management import BaseCommand

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
TEMPLATE_DIR = BASE_DIR / "stubs"


class StartProjectCommand(BaseCommand):
    """
    A command that delegates to the Django admin startproject command.
    """

    name = "startproject"
    description = "A command that delegates to the Django admin startproject command"

    def handle(self, args):
        run_copy(str(TEMPLATE_DIR), "./", unsafe=True)
