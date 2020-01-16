# jwt_microservice

An example of using JWT as a microservice.

### Usage

1. Run `docker-compose -up -d` to run both services
1. Apply migrations on both: `docker exec -it {container_name} ./manage.py migrate`
1. Create users or superusers: `docker exec -it {container_name} ./manage.py createsuperuser`
1. You can create some data in `books_catalog`: `docker exec -it books_catalog_books_api_1 ./manage.py loaddata fixture.json` (assuming container name is `books_catalog_books_api_1`)
1. Authenticate yourself in `authenticator` service:
   ```
   curl --location --request POST '0.0.0.0:8000/auth/login' --header 'Content-Type: application/json' --data-raw '{"username": "user", "password": "some_password"}
   ```
1. Authorize books_catalog request with the token you've just obtained:
   ```
   curl --location --request GET '0.0.0.0:9000/books/book' --header 'Authorization: Bearer AN_EXAMPLE_USELESSJhbGciOiJSUzI1NiJ9.AN_EXAMPLE_USELESSoiYWNjZXNzIiwiZXhwIjoxNTc5MTU5MDE0LCJqdGkiOiJhYWRjNmVjNjQ4ZGE0OGZkYTE1NDgzNzZkZmM4NzRjMiIsInVzZXJfaWQiOjF9.AN_EXAMPLE_USELESSLK5q5uAGbkNtoSAXnqebeKnVMS6lbPcIPUzHHg3qkpbhdcyL3wijP6zA4-xGig-1lXKnxgzKehKAXkguAbTTmDEldmL5dDSG4_MuVgFE-qnAdJvj_aWVnPHJPUQmDRsdgqr2aexdI6GYIpZAPkK4wLiH6pBKC9CFfsJM8x1qWtFAOXIbeXouNAhUD7bb-KRrjignHx8spnJWa6laqeT_Gda_pvNxieapJ2Jo93mtsWJdaDoaW6HNBLmU5fXvc1RGKIv11v63XbPS4yYJVVx7Yma0It3__gHaSECgtLzWzw7d7l1LAK-J1sdl6ORzbY_IvStA'
   ```
