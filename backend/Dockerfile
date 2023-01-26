FROM python:3.9.7
ENV PYTHONUNBUFFERED 1

COPY ./requirments.txt .
RUN pip install -r requirments.txt
RUN ls
COPY . /app/
WORKDIR /app
COPY ./entrypoint.sh /

EXPOSE 8000
ENTRYPOINT ["sh", "/entrypoint.sh"]

