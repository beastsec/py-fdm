# Base image.
FROM ubuntu:latest

# Labels.
LABEL maintainer="gabrielromero0499@gmail.com"
LABEL description="Donwload Manager Writted On Python3, This project is in the development phase."
LABEL version="0.1"

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

# Install default packages.
RUN apt install -y --no-install-recommends \
    python3 \
    python3-pip

# Set workdir.
WORKDIR /opt/py-fdm

# Add files.
COPY . .

# Install python libs.
RUN pip3 install -r requirements.txt && rm -rf requirements.txt

# Expose flask port.
EXPOSE 5000

# Run honeypot api service.
CMD [ "python3", "src/py-fdm/app.py" ]