sudo apt-get update
sudo apt-get install gcc libpq-dev -y
sudo apt-get install python-dev  python-pip -y
sudo apt-get install python3-dev python3-pip python3-venv python3-wheel -y
sudo apt-get install supervisor
sudo apt-get install nginx
sudo apt-get install python3-venv
sudo apt-get install libmysqlclient-dev
sudo apt install mysql-client-core-8.0

git clone https://github.com/jinxac/diary.git
source venv/bin/activate
cd diary


# [program:gunicorn]
# directory=/home/ubuntu/diary
# command=/home/ubuntu/venv/bin/gunicorn --workers=3 --bind unix:/home/ubuntu/diary/app.sock diary.wsgi:application
# autostart=true
# autorestart=true
# stderr_logfile=/var/log/gunicorn/err.log
# stdout_logfile=/var/log/gunicorn/out.log

# [group:guni]
# programs:gunicorn

sudo mkdir /var/log/gunicorn
sudo supervisorctl reread
sudo supervisorctl update

cd /etc/nginx/sites-available/
sudo touch django.conf

# server {
#   listen 80;
#   server_name add_server;

#     location /static/ {
#       expires 7d;
#       add_header Pragma public;
#       add_header Cache-Control "public";
#       alias /home/ubuntu/diary/diary/static/;
#     }

#   location / {
#     include proxy_params;
#     proxy_pass http://unix:/home/ubuntu/diary/app.sock;
#   }
# }


sudo nginx -t
sudo ln django.conf /etc/nginx/sites-enabled/

Modify settings.py with allowed hosts, debug and db
python3 manage.py migrate
python3 manage.py collectstatic