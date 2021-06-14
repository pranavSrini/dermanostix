# dermanostix
DERMANOSTIX

This is an AI tool to identify and classify skin lesions.

INSTRUCTIONS

Download IntelliJ's PyCharm, which can be found here: https://www.jetbrains.com/pycharm/download/

Create a new project in PyCharm(File -> New Project). Name it whatever you wish.

Open the Terminal in PyCharm (in the bottom left)

Type git init and press Enter. Then type git remote add origin https://github.com/theReality2-0/dermanostix.git and hit Enter. Finally, type git pull origin master and press Enter. This will copy and paste all of the code into your new project.

Enter pip install flask opencv-python-headless numpy torch torchvision into Terminal.

If you are on Windows, type set FLASK_APP=app.py and hit Enter. Otherwise, type export FLASK_APP=app.py and hit Enter.

If you are on Windows, enter set FLASK_ENV=development. Otherwise, enter export FLASK_ENV=development.

Type flask run and press Enter. It will print many things, of which one is a url, starting with 127.0.0.1. Click on that to go to the web app.
