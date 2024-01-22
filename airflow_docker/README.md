## __Running Airflow in Docker__
- [Official tutorial from Airflow page](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).
- docker-compose.yaml was copied from Airflow official page.
- mkdir -p ./dags ./logs ./plugins ./config
- __Initialize the database:__ docker compose up airflow-init
- __Running Airflow:__ docker compose up
- __In browser:__ localhost:8080