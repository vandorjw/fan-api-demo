FROM registry.access.redhat.com/ubi8/python-39

# build args
ARG DEBUG=False
ARG ALLOWED_HOSTS=*
ARG SECRET_KEY=0
ARG DATABASE_URL="sqlite:///db.sqlite"

# runtime args
ENV APP_CONFIG=gunicorn.conf.py
ENV APP_MODULE=config.wsgi

# Add application sources to a directory that the assemble script expects them
# and set permissions so that the container runs without root access
USER 0
COPY ./src /tmp/src
RUN /usr/bin/fix-permissions /tmp/src
USER 1001

# Install the dependencies
RUN /usr/libexec/s2i/assemble

# Set the default command for the resulting image
CMD /usr/libexec/s2i/run