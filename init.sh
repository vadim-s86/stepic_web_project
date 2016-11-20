sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/gunicorn2.conf /etc/gunicorn.d/gunicorn2.conf
sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
