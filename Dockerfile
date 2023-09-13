FROM fastapi:origin
WORKDIR /server
COPY ./fastapi ./fastapi
WORKDIR /server/fastapi/
RUN pip install -r requirements.txt
CMD ["uvicorn","main:app","--reload","--host","0.0.0.0"]