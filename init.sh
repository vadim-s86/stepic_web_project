sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/gunicorn_ask.conf /etc/gunicorn.d/gunicorn_ask
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
git config --global user.email "vadim.s86@ya.ru"
git config --global user.name "vadim-s86"
