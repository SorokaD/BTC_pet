# Почемуто не работает вариант Марата на локальной машине. Нужно разбираться с ошибкой apk
#FROM python:3.11-alpine3.18 

# почемуто работает, в отличии от варианта Марата, именно в комбинации: "python:3.9-alpine3.12"
FROM python:3.9-alpine3.12    

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/app

RUN mkdir -p /msdata/log

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN su -l root

RUN apk --no-cache update

RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install --no-cache-dir -r requirements.txt; \
	apk del .build-deps;

#TimeZone
RUN apk add --no-cache tzdata

ENV TZ=Asia/Bishkek

RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENTRYPOINT ["uwsgi", "uwsgi.ini"]
