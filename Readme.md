# Python Dev Env Setup


## Create a virtual environement

[ref.](https://docs.python-guide.org/dev/virtualenvs)

- Install virualenv

virtualenv is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.


```bash
    pip install --upgrade pip
```

```bash
    pip install virtualenv
```

```bash
    virtualenv --version
```

- Create a virtual environment for a project

```bash
    cd project_folder
    virtualenv venv
```

virtualenv venv will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages. The name of the virtual environment (in this case, it was venv) can be anything; omitting the name will place the files in the current directory instead.

> ‘venv’ is the general convention used globally. As it is readily available in ignore files (eg: .gitignore’)

- Activate the environment

```bash
    source venv/bin/activate
```
- upgrade pip

```bash
    pip install --upgrade pip
```

You can then start installing packages using the `pip` command.

- Deactivate the environment

```
    deactivate
```

- Requirements management


Save your requirements:

```bash
    pip freeze > requirements.txt
```

Install projects requirements in a new environments:

```bash
    pip install -r requirements.txt
```

Uninstall:
```bash
    pip uninstall -r -y requirements.txt
```

## Manage environment variables

Python-decouple is a library that provides a simple way to manage configuration settings in your Python projects. Here's a step-by-step guide on how to use Python-decouple:

1. Installation

```bash
    pip install python-decouple
```

2. Create a configuration file

Create a configuration file for your project. You can use any format that `python-decouple` supports, such as `.env` files or `.ini` files.

For this example, create a file named .env in your project's root directory and add your configuration settings in this format:

```makefile
    DEBUG=True
    SECRET_KEY=mysecretkey
    DATABASE_URL=sqlite:///mydatabase.db
    EMAIL_HOST=smtp.example.com
    EMAIL_PORT=587
    API_KEY=arandomapikey123
```

3. Use the global `config` object:

```python
    from decouple import config

    DEBUG = config('DEBUG', default=False)
    SECRET_KEY = config('SECRET_KEY')
    DATABASE_URL = config('DATABASE_URL')
    EMAIL_HOST = config('EMAIL_HOST')
    EMAIL_PORT = config('EMAIL_PORT')
    API_KEY = config('API_KEY')
```

The `default` argument in `python-decouple` allows you to specify a default value to use for a configuration setting if the setting is not found in the configuration file (e.g., `.env` file). This is helpful to prevent exceptions or unexpected behavior in your application when a configuration setting is missing.

> In a real project, make sure to ignore the `.env` file in your `.gitignore`

> Note it sometimes can be useful to include a `sample.env` file with placeholder values and configuration instructions to your github repo.

## Set up a Git Repository and ignore `.env` (and `venv`)

1. Initialize a Git Repo:

Make sure you are in your project's root directory in the terminal and run the following command.

```bash
    git init
```

2. Create or edit `.gitignore`:

```bash
    touch .gitignore
```

Open the file, add `.env`, save and close the file.

> The `venv/` folder should already include a .gitignore file. Double check and repeat the steps if needed.

3. Verify the files are ignored:

Use the below command and make sure the files you want to ignore are not included.

```bash
    git status
```

4. Commit and push changes:

Create a repo on Github, then use the following commands:

```bash
    git remote add origin https://github.com/your-username/your-repo.git
    git branch -M main
    git add .
    git commit -m "first commit"
    git push -u origin main
``` 

To ensure that the remote URL points to the correct GitHub repository use:

```bash
    git remote -v
```

If needed, you can update the remote URL using:

```bash
    git remote set-url origin https://github.com/your-username/new-repo.git
```

___

> Dig deeper by containerizing your project by following these [best practices](https://snyk.io/blog/best-practices-containerizing-python-docker/).
___


## Clean up

1. Remove git Repo:

```bash
    rm -rf git
```

2. Remove `.env` files:

```bash
    rm .env
```

3. Remove Virtual Environment:

- Deactivate the virtual environment if it's currently activated:

```bash
    deactivate
```
- Delete the virtual environment directory:

```bash
    rm -r venv
```

4. Remove cached Python files (Optional):

- Python generates cached bytecode files (`.pyc`) during execution. You can remove these files if you want to clean them up:

```bash
    find . -name "*.pyc" -exec rm -f {} \;
```
-  If you want to clean up Python package caches, remove the  `__pycache__` directories:

```bash
    find . -type d -name "__pycache__" -exec rm -r {} \;
```

5. Clean Up Git Credentials (Optional):

```bash
    git credential reject
```
