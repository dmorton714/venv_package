# **Python Package Installer**

This project provides a script to create a Python virtual environment and install specified packages interactively. The user is prompted to confirm whether they want each package to be installed.


## **Project Structure*

```
/your_project_directory
    |-- shell.md  
    |-- package.py

```



* `shell.md`: A shell script to create and activate a virtual environment, upgrade `pip`, and run the Python script to install packages. Rename this to whatevery you want an use the extension `.sh` ex: `your_file.sh`
* `install_packages.py`: A Python script to check for the presence of specified packages and install them if they are not already installed.


## **Prerequisites**

* Python 3.x must be installed on your system.

* Ensure you have `pip` installed.

## **Setup and Usage**


### **1. Clone the Repository**

```
git clone https://github.com/dmorton714/venv_package.git
cd your-repo
```

### **2. Make the Shell Script Executable**

```
chmod +x your_file.sh
```

### **3. Run the Shell Script**

Change the file path in the `your_file.sh` file to where you want to store  `package.py`

### **4. Run the Shell Script**

Move the `your_file.sh` to the following folder:
- **Mac** /usr/local/bin

- **Windows** C:\Program Files\scripts

### **5. Run the Shell Script**

```
source your_file.sh
```


### **What the Script Does**



1. **Create a Virtual Environment**:
    * The script creates a virtual environment named `venv` in the project directory.
2. **Activate the Virtual Environment**:
    * The script activates the virtual environment.
3. **Upgrade <code>pip</code></strong>:
    * The script upgrades <code>pip</code> to the latest version.
4. <strong>Run the Python Script</strong>:
    * The script runs <code>install_packages.py</code> to check and install the required packages based on user input.


### <strong>Example Output</strong>

When you run the shell script, you will see output similar to the following:

```
Creating virtual environment...
Activating virtual environment...
Upgrading pip...
pip is upgraded to the latest version.
Do you want to install pandas in your project? (y/n): y
'pandas' not found. Installing...
'pandas' has been installed.
Do you want to install numpy in your project? (y/n): n
Skipping installation of numpy.
Please enter 'y' or 'n'.
...
```

## **Customizing the Package List**

You can customize the list of packages to be checked and installed by editing the `install_packages.py` file. Modify the `packages` list to include the packages you need:

```python
packages = ["pandas", "numpy", "plotly", "requests", "matplotlib", "scikit-learn"]
```
