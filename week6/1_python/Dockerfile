FROM python:3-slim

RUN mkdir -p /var/www/
COPY www/ /var/www/

RUN pip install flask
EXPOSE 5000/tcp

RUN useradd python-runner
USER python-runner

WORKDIR /var/www/
CMD ["python", "chall.py"]
