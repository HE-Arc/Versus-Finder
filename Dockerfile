FROM java:8

ADD ./dockerSrc ./

RUN apt update && apt upgrade -y
RUN apt install wget -y
RUN chmod +x ./index.sh
RUN chmod +x ./setup/katalon.sh

ENV DISPLAY :99
ENV DISPLAY_CONFIGURATION 1024x768x24

RUN ./index.sh

WORKDIR /

ENTRYPOINT ["tail", "-f", "/dev/null"]