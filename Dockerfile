FROM python:3.12-slim

WORKDIR /app

COPY . /app

EXPOSE 8080

ENV PORT="8080"
ENV NAME="David Shlomo Zim" 

CMD ["python", "-u", "app.py"]
