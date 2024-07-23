import subprocess
import sys


'''
The function attempts to import the packages. If the package is already
installed, the import succeeds, and it prints a message indicating that
the package is already installed.

If the package is not installed, the function prints a message indicating
that the package is not found and will be installed.

After successfully installing the package, it prints a message indicating
that the package has been installed.
'''


def install_package(package_name):
    try:
        __import__(package_name)
        print(f"'{package_name}' is already installed.")
    except ImportError:
        print(f"'{package_name}' not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name]) # noqa
        print(f"'{package_name}' has been installed.")


# List of packages to check/install
packages = ["pandas", "numpy", "plotly", "requests", "matplotlib", "scikit-learn"] # noqa

# logic for the user input to install packages
for package in packages:
    while True:
        response = input(f"Do you want to install {package} in your project? (y/n): ").strip().lower() # noqa
        if response == 'y':
            install_package(package)
            break
        elif response == 'n':
            print(f"Skipping installation of {package}.")
            break
        else:
            print("Please enter 'y' or 'n'.")
