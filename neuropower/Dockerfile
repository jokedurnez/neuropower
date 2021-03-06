FROM oesteban/crn_nipype:freesurfer

# Update packages and install the minimal set of tools
RUN apt-get update && \
    apt-get install -y curl git xvfb bzip2 apt-utils

ENV LANG C.UTF-8

# Install conda
RUN conda install nose && \
    conda install numpy && \
    conda install scipy && \
    conda install pandas && \
    conda install matplotlib && \
    conda install xvfbwrapper

RUN mkdir /code

WORKDIR /code
ADD requirements.txt /code/

RUN conda install psycopg2 mpld3==0.2 scikit-learn==0.17.1 cycler==0.9.0 && \
  apt-get update && \
  apt-get install -y build-essential && \
  curl https://bootstrap.pypa.io/ez_setup.py -o - | python && \
  pip install -r requirements.txt && \
  apt-get install -y libglib2.0-0 && \
  apt-get install -y libfreetype6-dev libxft-dev && \
  conda install uwsgi && \
  conda install Jinja2

RUN conda install celery
RUN conda install SQLAlchemy
RUN pip install neuropower
RUN conda install django-celery
RUN pip install opbeat
#RUN conda install django
RUN pip install django
RUN pip install django-crispy-forms
RUN pip install django-secure
RUN pip install django-sslserver
RUN pip install psycopg2
RUN pip install django-picklefield
RUN pip install matplotlib
RUN pip install palettable
RUN pip install mpld3
RUN pip install jinja2
RUN pip install sklearn
RUN pip install nilearn
RUN pip install sqlalchemy
RUN pip install kombu
RUN pip install redis && \
    pip install celery[redis]
RUN pip install progressbar
RUN pip install neurodesign>0.0.6
RUN pip install reportlab
RUN pip install seaborn
RUN pip install pdfrw

RUN npm install colorsys

ADD colorsys.py /usr/local/miniconda/lib/python2.7/site-packages/


# Clear apt cache to reduce image size
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 3031
