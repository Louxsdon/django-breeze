import argparse
import shutil
import os
import glob
import fileinput
import subprocess
from pathlib import Path, PurePath
from django.conf import settings


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Manager:
    def args_parser(self):
        parser_des = """\
        Copy React or TypeScript files from templates 
        folder to current working directory.
        """
        parser = argparse.ArgumentParser(description=parser_des)
        parser.add_argument(
            "library", choices=["react", "vue3"], help="The Liberary to use"
        )
        parser.add_argument(
            "--typescript", action="store_true", help="Include if using TypeScript"
        )
        parser.add_argument(
            "--verbose",
            action="store_true",
            help="Display progress information",
            default=True,
        )

        self.args = parser.parse_args()
        return self.args

    def execute(self):
        args = self.args_parser()

        self.PROJECT_BASE_DIR = os.getcwd()

        self.copy_files()

    def copy_files(self):
        TEMPLATE_DIR = BASE_DIR / "templates"
        DESTINATION_DIR = os.getcwd()

        if self.args.library == "react":
            src_dir = TEMPLATE_DIR / "react"
        elif self.args.library == "vue3":
            src_dir = TEMPLATE_DIR / "vue3"
        else:
            print("You must provide library to use! suported libraries [react, vue3]")

        if self.args.typescript:
            src_dir += "_typescript"

        shutil.copytree(src_dir, DESTINATION_DIR, dirs_exist_ok=True)
        if self.args.verbose:
            self._verbose(f"Project files generated successfully!\n")

    def configs(self):
        # Modify settings variables
        self._verbose("Configuring project settings...")
        settings.INERTIA_LAYOUT = "index.html"
        settings.CSRF_HEADER_NAME = "HTTP_X_XSRF_TOKEN"
        settings.CSRF_COOKIE_NAME = "XSRF-TOKEN"

        if "django_vite" not in settings.INSTALLED_APPS:
            settings.INSTALLED_APPS += ["inertia", "django_vite"]
        if "inertia" not in settings.INSTALLED_APPS:
            settings.INSTALLED_APPS += ["inertia"]

        self._verbose("Settings modified successfully!\n")

    def project_configs(self):
        settings_files = glob.glob("**/settings.py", recursive=True)
        if settings_files:
            settings_file = settings_files[0]
            print(f"Found settings file: {settings_file}")

            # Add installed apps
            settings_file.INSTALLED_APPS.append("myAPp")

            # Add variables to settings.py file
            variables = {
                "STATIC_URL": "static/",
                "INERTIA_LAYOUT": "index.html",
                "CSRF_HEADER_NAME": "HTTP_X_XSRF_TOKEN",
                "CSRF_COOKIE_NAME": "XSRF-TOKEN",
                "DJANGO_VITE_ASSETS_PATH": 'BASE_DIR / "static" / "dist"',
                "DJANGO_VITE_DEV_MODE": "DEBUG",
            }

            added_variables = {key: False for key in variables}
            for line in fileinput.input(settings_file, inplace=True):
                for key, value in variables.items():
                    if line.startswith(key):
                        print(f'{key} = "{value}"')
                        added_variables[key] = True
                        break
                else:
                    print(line.rstrip())
            # Add variables that were not found in the file
            for key, value in variables.items():
                if not added_variables[key]:
                    with open(settings_file, "a") as f:
                        f.write(f'\n{key} = "{value}"\n')
        else:
            print("Could not find settings file in base directory.")

    def _verbose(self, message: str):
        """Display brief message of a process(es)

        Args:
            message (str): message to display
        """
        if self.args.verbose:
            print(message)


def execute_command(argv=None):
    """Run a ManagementUtility."""
    utility = Manager()
    utility.execute()
