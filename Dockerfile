FROM tiangolo/uvicorn-gunicorn:python3.8

WORKDIR /sber

COPY ./requirements.txt /sber/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /sber/requirements.txt

COPY ./service.py /sber/

EXPOSE 8000

CMD ["uvicorn", "service:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
