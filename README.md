# Dashboard Implementation
This repository was forked from [the official Datahub project](https://github.com/datasnack/datahub) and does not have the latest update from the parent repository.

## Installation Steps:
### Build Image:
1. Clone [this repository](https://github.com/z1zzle/datahub) in another directory.
2. Switch to ```last_stable``` branch.
3. Run ```docker build -t datahub:latest .```.

### Run Container:
4. Clone dh-ghana repository (the version where it's still locally built - you can clone it from [this fork](https://github.com/z1zzle/dh-ghana)).
5. Copy the .env.example to .env: ```cp .env.example .env```.
6. Make sure to configure **SECRET_KEY** and **DATAHUB_NAME** in .env file.
7. Run ```docker compose up -d``` and wait until [localhost:8000](http://localhost:8000/) is available.

### Import Data and Preprocess:
8. Download latest .dump file from [the official release page](https://github.com/datasnack/dh-ghana/releases) to the directory ```data/```.
9. Run ```docker compose exec datahub python manage.py restore data/<dump file>```
10. Run ```docker compose exec datahub python manage.py preprocess_shape_dl_year``` - This process can take a while (6-10 minutes in my case) as it's a synchronous process.
11. Go to ```http://localhost:8000/dashboard/``` to see the dashboard homepage.
