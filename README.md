# Una Code Challenge

This is my solution for the description provided, I hope you like it :)

I am using ```Django 5.0.6``` and ``Django Rest Framework`` and default Django database  and data from the S3 container that you provided.

Dependencies can be seen in the file: ```requirements.txt```

## Endpoints

I created the following endpoints:
1. ``api/v1/levels/``
2. ``api/v1/levels/user_idUUID``
3. ``api/v1/levels/?user_id=UUID``
4. ``api/v1/levels/?start=2021-02-10T11&stop=2021-02-10T1``
4. ``api/v1/levels/?sorting=asc``
5. ``api/upload-csv/``
6. ``api/export-data/``



## Running Tests 
I use ```pytest``` and ```factory_boy``` for generated random the testing data. To run the tests use:

```bash
  pytest 
```

## Docker Deployment

To deploy this project run

```bash
  docker build -t unadjango . 
  docker run -it -p 8000:8000 unadjango

```