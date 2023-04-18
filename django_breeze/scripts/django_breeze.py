import re
import sys
from django_breeze.core.management import execute_command


def run():
    sys.argv[0] = re.sub(r"(-script\.pyw|\.exe)?$", "", sys.argv[0])
    sys.exit(execute_command())


if __name__ == "__main__":
    run()
