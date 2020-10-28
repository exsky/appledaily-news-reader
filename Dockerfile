FROM alpine
MAINTAINER SKY <sky@cht.com.tw>

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 make bash && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

WORKDIR /source
ADD . /source
RUN ["make", "install-pippkg"]

CMD ["make", "set_key", "run"]
