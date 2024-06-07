
# Home Library

The Home Library Project is a simple application to help you manage your personal book collection at home.

# Demo

[http://kreker.xyz](http://library.kreker.xyz/)

## Features

- **Add Books:** Easily add books to your library by providing details such as title, author, and publication information.
- **View Library:** View a list of all the books in your library along with their details.
- **Search:** Search for specific books based on title, author, or other criteria.
- **Remove Books:** Remove books from your TBR that you no longer plan to read.
- **Books of the Week (NYT):** Get recommendations for books of the week according to The New York Times bestseller list.

## Tech Stack

**Backend:** Django, Python, Gunicorn

**Frontend:** Nginx

**DB:** Postgres

**Rest:** Docker


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`POSTGRES_DB` - Specifies the name of the PostgreSQL database used for storing library data. Default value: `home-library`.

`POSTGRES_USER` - Specifies the username for connecting to the PostgreSQL database. Default value: `library-user`.

`POSTGRES_PASSWORD` - Specifies the password for connecting to the PostgreSQL database. Default value: `123`.

`PGHOST` - Specifies the hostname of the PostgreSQL database server. Default value used by Docker: `db`.

`PGPORT` - Specifies the port number of the PostgreSQL database server. Default value: `5432`.

`NYTimes_key` - API key for accessing The New York Times API to fetch data such as books of the week. You can generate yours after registering: https://developer.nytimes.com/.

`SECRET_KEY` - Secret key used by Django for cryptographic signing. You can easy generate one: https://djecrety.ir/

Please ensure that you set these environment variables appropriately, by using a configuration file like `.env`.



## Deployment

To deploy this project:

1. Make sure port 80 is available

2. Run

```bash
    git clone https://github.com/kreker783/Home-Library.git && cd Home-Library/library-code/
    docker compose up
```

3. Open your web browser and navigate to http://localhost.
