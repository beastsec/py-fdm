# Base image.
FROM ubuntu:latest

# Labels.
LABEL authors="Gabriel Romero, Deiby Gerez"
LABEL maintainer="gabrielromero0499@gmail.com"
LABEL description="Donwload Manager Writted On Python3, This project is in the development phase."
LABEL version="0.1"

# Set vars.
ARG USER=fdm-data
ARG HOME=/opt/py-fdm

# Set env.
ENV DEBIAN_FRONTEND noninteractive
ENV TZ=America/Santo_Domingo
ENV LC_ALL=en_US.UTF-8
ENV PYTHONIOENCODING=UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LANG=en_US.UTF-8

# Update packages and install.
RUN apt -qq update && apt full-upgrade -y && apt install -y --no-install-recommends \
    apt-utils \
    dialog \
    locales

# Reconfigure locale.
RUN echo "en_US.UTF-8 UTF-8" | tee -a /etc/locale.gen
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales

# Set non-root User.
RUN groupadd -g 1000 ${USER}
RUN useradd -d ${HOME}} -s /bin/bash -m ${USER} -u 1000 -g 1000
USER ${USER}
ENV HOME ${HOME}

# Set fdm-data owner of /opt/py-fdm .
RUN chown ${USER}:${USER} ${HOME}

# Install default packages.
RUN apt install -y --no-install-recommends \
    python3 \
    python3-pip

# Set user.
USER ${USER}

# Set workdir.
WORKDIR ${HOME}/py-fdm

# Add files.
COPY . .

# Install python libs.
RUN pip3 install -r requirements.txt && rm -rf requirements.txt

# Expose flask port.
EXPOSE 5000

# Run honeypot api service.
CMD [ "python3", "src/py-fdm/app.py" ]