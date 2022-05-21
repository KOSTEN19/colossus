#!/bin/bash

echo "___________.__             .___.___.___           .___"
echo "\__    ___/|  |__   ____   |   |   |   |______  __| _/"
echo "  |    |   |  |  \_/ __ \  |   |   |   \_  __ \/ __ | "
echo "  |    |   |   Y  \  ___/  |   |   |   ||  | \/ /_/ | "
echo "  |____|   |___|  /\___  > |___|___|___||__|  \____ | "
echo "                \/     \/                          \/ "


python -m pip install --upgrade pip
pip install pycodestyle autopep8 unify docformatter


autopep8 --in-place --aggressive --aggressive ./website/__init__.py
autopep8 --in-place --aggressive --aggressive ./website/admin.py
autopep8 --in-place --aggressive --aggressive ./website/apps.py
autopep8 --in-place --aggressive --aggressive ./website/forms.py
autopep8 --in-place --aggressive --aggressive ./website/models.py
autopep8 --in-place --aggressive --aggressive ./website/tests.py
autopep8 --in-place --aggressive --aggressive ./website/views.py

echo "[+] autopep8 done !"

unify --in-place ./website/__init__.py
unify --in-place ./website/admin.py
unify --in-place ./website/apps.py
unify --in-place ./website/forms.py
unify --in-place ./website/models.py
unify --in-place ./website/tests.py
unify --in-place ./website/views.py

echo "[+] unify done !"

docformatter --in-place ./website/__init__.py
docformatter --in-place ./website/admin.py
docformatter --in-place ./website/apps.py
docformatter --in-place ./website/forms.py
docformatter --in-place ./website/models.py
docformatter --in-place ./website/tests.py
docformatter --in-place ./website/views.py

echo "[+] docformatter done !"


echo "[*] changing folder"

autopep8 --in-place --aggressive --aggressive ./mysite/__init__.py
autopep8 --in-place --aggressive --aggressive ./mysite/asgi.py
autopep8 --in-place --aggressive --aggressive ./mysite/settings.py
autopep8 --in-place --aggressive --aggressive ./mysite/urls.py
autopep8 --in-place --aggressive --aggressive ./mysite/wsgi.py

echo "[+] autopep8 done !"

unify --in-place ./mysite/__init__.py
unify --in-place ./mysite/asgi.py
unify --in-place ./mysite/settings.py
unify --in-place ./mysite/urls.py
unify --in-place ./mysite/wsgi.py

echo "[+] unify done !"

docformatter --in-place ./mysite/__init__.py
docformatter --in-place ./mysite/asgi.py
docformatter --in-place ./mysite/settings.py
docformatter --in-place ./mysite/urls.py
docformatter --in-place ./mysite/wsgi.py

echo "[+] docformatter done !"

echo "[+++] ALL DONE !"
