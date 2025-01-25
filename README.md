# Dashboard Implementation
This repository was forked from [the official Datahub project](https://github.com/datasnack/datahub) and does not have the latest update from the parent repository.

### Installation Steps:
1. Clone dh-ghana repository (the version where it's still locally built - you can clone it from [this fork](https://github.com/z1zzle/dh-ghana)).
2. Copy the .env.example to .env: ```cp .env.example .env```.
3. Make sure to configure **SECRET_KEY** and **DATAHUB_NAME** in .env file.
4. Run ```docker compose up -d``` and wait until [localhost:8000](http://localhost:8000/) is available.
5. Download latest .dump file from [the official release page](https://github.com/datasnack/dh-ghana/releases) to the directory ```data/```.
6. Run ```docker compose exec datahub python manage.py restore data/<dump file>```
7. Clone [this repository](https://github.com/z1zzle/datahub) in another directory.
8. Switch to ```latest_stable``` branch.
9. Run ```docker build -t datahub:latest .```.
10. Go back to dh-ghana directory and run:
   -  ```docker compose up -d```
   - ```docker compose exec datahub python manage.py preprocess_shape_dl_year``` - This process can take a while (6-10 minutes in my case) as it's a synchronous process. I'm really sorry for that!
   - When it's done, it should print out "Successfully precomputed stats!"
11. Go to ```http://localhost:8000/dashboard/``` to see the dashboard homepage.
