from pathlib import Path
import os
import shutil
from typing import List


BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATE_DIR = BASE_DIR / "templates"


class TemplateFilesHandler:
    """Responsible for handling template files"""

    def get_templates(self) -> List:
        """Get list of all available templates

        Returns:
            List: List of template files
        """
        templates = os.listdir(TEMPLATE_DIR)
        return templates

    def get_template_dir(self, template_name: str) -> Path:
        """Get the template file's directory

        Args:
            template_name (str): Name of the template file

        Returns:
            Path: Returns the path to the template directory
        """
        return TEMPLATE_DIR / template_name.lower()

    def create_project_files(self, args) -> None:
        """Create a new project fles base on the selected framework

        Args:
            args: Argparser arguments
        """
        DESTINATION_DIR = os.getcwd()

        src_dir = self.get_template_dir(args.framework)

        print(src_dir)

        if args.typescript:
            src_dir = str(src_dir) + "_typescript"

        # Check if the source directory exists in the destination directory
        for name in os.listdir(src_dir):
            if name == ".gitignore":
                continue
            dest = os.path.join(DESTINATION_DIR, name)

            if os.path.exists(dest):
                print(f"File or directory '{dest}' already exists. Skipping.")
                return

        # copy template files
        copy_files(src_dir, DESTINATION_DIR)

        print("\nProject files generated successfully!\n")


def copy_files(src, dest):
    """Copy files and directories from template directory to destination directory

    Args:
        src (Path): Source directory
        dest (Path): Destination directory
    """

    for item in os.listdir(src):
        src_dir = os.path.join(src, item)
        dest_dir = os.path.join(dest, item)
        if os.path.isdir(src_dir):
            shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
        else:
            shutil.copy2(src_dir, dest_dir)
