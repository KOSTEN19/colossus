@echo off

echo "___________.__             .___.___.___           .___"
echo "\__    ___/|  |__   ____   |   |   |   |______  __| _/"
echo "  |    |   |  |  \_/ __ \  |   |   |   \_  __ \/ __ | "
echo "  |    |   |   Y  \  ___/  |   |   |   ||  | \/ /_/ | "
echo "  |____|   |___|  /\___  > |___|___|___||__|  \____ | "
echo "                \/     \/                          \/ "

python -m pip install --upgrade pip
pip install pycodestyle autopep8 unify docformatter

cd .\website

autopep8 --in-place --aggressive --aggressive __init__.py
autopep8 --in-place --aggressive --aggressive admin.py
autopep8 --in-place --aggressive --aggressive apps.py
autopep8 --in-place --aggressive --aggressive forms.py
autopep8 --in-place --aggressive --aggressive models.py
autopep8 --in-place --aggressive --aggressive tests.py
autopep8 --in-place --aggressive --aggressive views.py

echo [+] autopep8 done !

unify --in-place __init__.py
unify --in-place admin.py
unify --in-place apps.py
unify --in-place forms.py
unify --in-place models.py
unify --in-place tests.py
unify --in-place views.py

echo [+] unify done !

docformatter --in-place __init__.py
docformatter --in-place admin.py
docformatter --in-place apps.py
docformatter --in-place forms.py
docformatter --in-place models.py
docformatter --in-place tests.py
docformatter --in-place views.py

echo [+] docformatter done !

cd ..
cd .\mysite

echo [*] changing folder

autopep8 --in-place --aggressive --aggressive __init__.py
autopep8 --in-place --aggressive --aggressive asgi.py
autopep8 --in-place --aggressive --aggressive settings.py
autopep8 --in-place --aggressive --aggressive urls.py
autopep8 --in-place --aggressive --aggressive wsgi.py

echo [+] autopep8 done !

unify --in-place __init__.py
unify --in-place asgi.py
unify --in-place settings.py
unify --in-place urls.py
unify --in-place wsgi.py

echo [+] unify done !

docformatter --in-place __init__.py
docformatter --in-place asgi.py
docformatter --in-place settings.py
docformatter --in-place urls.py
docformatter --in-place wsgi.py

echo [+] docformatter done !

echo [+++] ALL DONE !

pause