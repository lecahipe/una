FROM python:3.11

# install dependencies
WORKDIR /una
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . .

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "unaDjango/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]