$makemigrations = 'python manage.py makemigrations notes'
$migrate = 'python manage.py migrate'


Invoke-Expression $makemigrations
Invoke-Expression $migrate