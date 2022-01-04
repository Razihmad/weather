This project is all about getting the temprature of the city of the user and sending a mail to the user email id which contain the temprature of that city.
To run this project first you have to fork this or clone this project on your local computer and then run the command pip freeze -r requirements.txt to install all the packages,
that are being used to run this project.
create a .env file in the same folder where template folder is where you can keep your secret things in the given manner
SECRET_KEY=<secret key here>
DEBUG=1
appid=<your api id here>
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=<email host here>
EMAIL_USE_TLS=True
EMAIL_PORT=<email port here
EMAIL_HOST_USER=<email user here
EMAIL_HOST_PASSWORD=<email password here>

then you can type python manage.py runserve to run the project.
or you can directyl visit on https://weather-api02.herokuapp.com/ link to check this out.
