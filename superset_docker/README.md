# Superset
- [Official resource Apache Superset](https://superset.apache.org/)
- [Installing Superset Locally Using Docker Compose](https://superset.apache.org/docs/installation/installing-superset-using-docker-compose)  

__Clone Superset's repo in your terminal with the following command:__    
git clone https://github.com/apache/superset.git 

__Navigate to the folder you created in step 1:__  
cd superset

__When working on master branch, run the following commands to run development mode using docker compose:__  
docker compose up  

__Log in to Superset__  
Your local Superset instance also includes a Postgres server to store your data and is already pre-loaded with some example datasets that ship with Superset. You can access Superset now via your web browser by visiting __http://localhost:8088__. Note that many browsers now default to https - if yours is one of them, please make sure it uses http.  

__Log in with the default username and password:__  
__username__: admin    
__password__: admin  