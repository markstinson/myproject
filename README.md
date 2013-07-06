myproject
=========

working through some django tutorials


Commands frequently used
------------------------

* `django-admin.py startproject myproject` -- create initial project base 
* `django-admin.py startapp contacts` -- create application base
* `python manage.py syncdb` -- make db file, inside myproject directory
* `python manage.py shell` -- to launch a project specific iPython shell
* `python manage.py runserver` -- defaults to local host
    * if inside virtual box, `python manage.py runserver 0.0.0.0:8000` so it can listen to all addresses. Your host OS browser would then point to `localhost:9000`