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
    def __init__(self) -> None:
        # project_name = os.environ.get('DJANGO_SETTINGS_MODULE')
        # project_name = getattr(settings, 'ROOT_URLCONF')
        # DJANGO_BASE_DIR = settings.BASE_DIR
        # import re
        # project_name = re.sub(r'\.urls$', '', settings.ROOT_URLCONF)
        settings_dir = os.path.dirname(os.path.abspath(__file__))
        project_name = os.path.basename(settings_dir)
        print(project_name)

    def args_parser(self):
        parser_des = """\
        Copy React or TypeScript files from templates 
        folder to current working directory.
        """
        parser = argparse.ArgumentParser(description=parser_des)
        parser.add_argument("project_name", type=str, help="Name of the django project")
        parser.add_argument(
            "framework", choices=["react", "vue"], help="The framework to use"
        )
        parser.add_argument(
            "--typescript", action="store_true", help="Include if using TypeScript"
        )
        parser.add_argument(
            "--fresh",
            action="store_true",
            help="If the existing destination directory should be overide.",
        )
        parser.add_argument(
            "--verbose",
            action="store_true",
            help="Display progress information",
            default=True,
        )

        self.args = parser.parse_args()
        return self.args

    def execute_command(self):
        args = self.args_parser()

        self.PROJECT_BASE_DIR = os.getcwd()

        # check django project name and existence settings
        self.PROJECT_DIR = Path(args.project_name)
        self.PROJECT_DIR = Path(args.project_name)
        self.PROJECT_DIR = Path(args.project_name)

        print((self.PROJECT_BASE_DIR))
        print((self.PROJECT_DIR))
        # copy neccessary project files
        self.copy_files()
        # self.configs()

    def copy_files(self):
        # install packages
        # self.install_packages()

        TEMPLATE_DIR = BASE_DIR / "templates"
        DESTINATION_DIR = os.getcwd()

        if self.args.framework == "react":
            src_dir = TEMPLATE_DIR / "react"
        elif self.args.framework == "vue":
            src_dir = TEMPLATE_DIR / "vue"
        else:
            print("You must provide framework to use! suported frameworks [react, vue]")

        if self.args.typescript:
            src_dir += "_typescript"

        # if not os.path.exists(DESTINATION_DIR):
        #     os.makedirs(DESTINATION_DIR)
        try:
            shutil.copytree(src_dir, DESTINATION_DIR, dirs_exist_ok=self.args.fresh)
            if self.args.verbose:
                self._verbose(
                    f"Files created successfully. Source Directory is: {DESTINATION_DIR}\n"
                )
        except FileExistsError as e:
            print(
                f"Directory '{DESTINATION_DIR}' already exist! Use --fresh to overide the existing folder"
            )
            return

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

    def install_packages(
        self,
    ):
        """Install required Pypi packages for this project"""
        # Install pip packages
        packages = ["django-vite", "django-inertia"]
        print("\nInstalling required packages please wait...")
        for package in packages:
            subprocess.run(["pip", "install", package], stdout=subprocess.PIPE)
            self._verbose(f"Installed package {package}")
        print("Packages installed successfully!\n")

    def _verbose(self, message: str):
        """Display brief message of a process(es)

        Args:
            message (str): message to display
        """
        if self.args.verbose:
            print(message)
