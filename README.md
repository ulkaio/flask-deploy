## flask-deploy
============

#### Check out the blog post: https://realpython.com/blog/python/kickstarting-flask-on-ubuntu-setup-and-deployment/ for further information.

##### Steps to setup:

###### To configure existing versions on PROD:
###### Simply do:
###### Follow steps @ https://realpython.com/blog/python/kickstarting-flask-on-ubuntu-setup-and-deployment/
###### 1) run: sudo apt-get install git  (to install git)
###### 1) sudo apt-get install fabric  (to install fabric)
###### 1) create linux user (adduser <your-user-here>; adduser <your-user-here> sudo)
###### 2) set the following in: /home/www/flask-deploy/fabfile.py ::
######   - server ip to: <your-server-ip-here> in flask_project/app.py
######   - user as <your-user-here>
######   - password to '<your-user-password-here>'
###### 3) configure scripts in config/ to point to the flask_project path @ /home/www/flask-deploy/flask_project
###### 5) make sure your in directory: /home/www/flask-deploy
###### 6) then run: sudo fab create, let it run for a bit, then access server ip
###### 7) Enjoy!