#!/usr/bin/env python
import os
import sys

manage_path = os.path.abspath(os.path.dirname(__file__))
project_path = os.path.abspath(os.path.join(manage_path, ".."))
libs_path = os.path.join(project_path, "libs")
sys.path.insert(0, project_path)
sys.path.insert(0, libs_path)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
