python manage.py makemigrations
python manage.py migrate

python manage.py makemigrations core
python manage.py migrate core
python manage.py sqlmigrate core 0001 

python manage.py makemigrations rental
python manage.py migrate rental
python manage.py sqlmigrate rental 0001

python manage.py makemigrations vehicles
python manage.py migrate vehicles
python manage.py sqlmigrate vehicles 0001

python manage.py makemigrations registration
python manage.py migrate registration
python manage.py sqlmigrate registration 0001

python manage.py createsuperuser

pause