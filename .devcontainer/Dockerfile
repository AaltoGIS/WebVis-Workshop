FROM osgeo/gdal:ubuntu-small-latest

RUN apt-get update && apt-get -y install python3-pip --fix-missing

# set working dir and copy its content to docker side
WORKDIR app/
COPY ./app .

# install req file content
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 8501
