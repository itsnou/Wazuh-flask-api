**Depending on how you have the PATH configured, you should proceed to use 'python', in my case it is 'python', but in other cases it can be 'python3', 'python2'.
(Same for pip)**

- Install virtual env:
    * pip install virtual env
- Create the virtual environment with virtual env:
    * virtualenv -p python env
- Activate virtualenv:
    * ./env/Scripts/activate (On windows)
- Install flask:
    * pip install flask
- Install swagger:
    * pip install flask-swagger-ui
- Downgrade Jinja2:
    * pip uninstall Jinja2
    * pip install Jinja2==2.11.3