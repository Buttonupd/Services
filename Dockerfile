FROM python:3.9-alpine
#set the working directory for the container

WORKDIR /code


#set the env variables
ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYCODE=1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev 
    
RUN pip install psycopg2-binary

RUN apk add zlib-dev jpeg-dev gcc musl-dev
#install pip for the docker image
RUN pip install --upgrade pip

#copy the requirement from local system to docker image inside /user/src/app/
COPY /requirements.txt /code
RUN pip install -r requirements.txt

#copy the complete project files after installing dependencies.
COPY . /code


ENTRYPOINT ["/code/entrypoint.sh"]
