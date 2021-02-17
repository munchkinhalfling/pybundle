def reqs(params):
    return {
        "location": "requirements.txt",
        "content": """
# requirements.txt
# This file defines the dependencies for this program (one per line).
# See https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format
# Use 'pyb add <package>' to add to this file and 'pyb install' to install all dependencies.
"""
    }