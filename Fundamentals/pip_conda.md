**Conda** is an open-source, cross-platform package and environment management system. <br>
While <br>
**pip** primarily focuses on managing Python packages

**Important Conda commands**

* **conda create:** Creates a new Conda environment.

* **conda activate:** Activates a specific Conda environment.

* **conda deactivate:** Deactivates the currently active environment.

* **conda install:** Installs packages into the active environment.

* **conda list:** Lists all packages installed in the active environment.

* **conda search:** Searches for available packages in the Conda repositories.

* **conda search \<keyword>:** Searches the Conda repositories for packages related to the given keyword.

* **conda update:** Updates a package to its latest version.

* **conda remove:** Uninstalls a package from the active environment.

* **conda env list:** Lists all Conda environments on your system.

**Installing multiple packages at once**

```pip install django djangorestframework django-cors-headers```

* **Django:** This is the core web framework that provides the structure and tools for building your web application.

* **djangorestframework:** If you're building a RESTful API (a way for different applications to communicate with each other over the web), this library simplifies the process of creating and managing APIs in Django.

* **django-cors-headers:** Modern web applications often involve interactions between different domains (origins). This library helps you configure Cross-Origin Resource Sharing (CORS) in your Django project, ensuring secure communication between your front end and back end.

**Upgrading packages**

* pip install --upgrade django

**Controlling package versions**

* pip install django==1.23.5

**Requirements files: Reproducible environments**

* pip install -r requirements.txt

**Essential pip commands**

* pip list: Quickly view all installed packages and their versions.

* pip show <package>: Get detailed information about a specific package, including its dependencies and location.

* pip freeze: Generate a list of your installed packages suitable for a requirements.txt file, perfect for sharing your project's dependencies.

* pip check: Verify your environment for any dependency conflicts, helping prevent unexpected errors.