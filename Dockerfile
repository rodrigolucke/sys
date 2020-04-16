FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/


# NODE
#RUN  apt-get update -yq \
 #   && apt-get install curl gnupg -yq \
  #  && curl -sL https://deb.nodesource.com/setup_8.x | bash \
   # && apt-get install nodejs -yq



#RUN pip install bootstrap-admin
#install mysqlclient
RUN pip install mysqlclient
#RUN python manage.py makemigrations blog

#RUN python manage.py migrate



#bootstrap-admin instalaçao

#RUN pip install django_admin_bootstrapped








