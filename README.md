# E-Commerce
Need Python3.7+ to run this project

## Project Setup

### Run in Local Environment
create a virtual environment to the root directory and then run the following commands.
```shell
source venv/bin/activate  # venv is the virtual env name
pip install -r requirements.txt
python manage.py runserver
```

### Run in Docker
```shell
docker-compose build
docker-compose up
```

## Database Restore in Docker
```shell
docker exec -it e-commerce_db_1 psql -U postgres -c "DROP SCHEMA public CASCADE;"
docker exec -it e-commerce_db_1 psql -U postgres -c "CREATE SCHEMA public"
cat <file_path> | docker exec -i itbutton-web_db_1 psql -U postgres
```
## Necessary Commands
```shell
# run shell
docker exec -it e-commerce_web_1 sh -c "python manage.py shell_plus"
# migration commands
docker exec -it e-commerce_web_1 sh -c "python manage.py makemigrations"
docker exec -it e-commerce_web_1 sh -c "python manage.py migrate"
# create super user
docker exec -it e-commerce_web_1 sh -c "python manage.py createsuperuser"
```

## Re Index
```shell
docker exec -it e-commerce_web_1 sh -c "python manage.py search_index --rebuild -f"  # reindex
docker exec -it e-commerce_web_1 sh -c "python manage.py search_index --delete -f" # delete index
docker exec -it e-commerce_web_1 sh -c "python manage.py search_index --populate -f" # populate data
```