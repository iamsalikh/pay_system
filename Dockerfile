# какой язык программирования
FROM python:latest


# копирование всех файлов во внутрь контейнера
COPY . /code


# назначить основную папку
WORKDIR /code

# установка библиотек
RUN pip install -r requirements.txt

# запуск проекта
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0"]

