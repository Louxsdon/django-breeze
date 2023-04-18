"""
Invokes django-breeze when the django_breeze module is run as a script.
Example: python -m django_breeze react
"""
from django_breeze.core import management

if __name__ == "__main__":
    management.execute_command()
