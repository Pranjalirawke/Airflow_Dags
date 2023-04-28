import json
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.mongo.hooks.mongo import MongoHook
from pendulum import datetime


#SSHHook code 
def create_the_file():
    ssh = SSHHook(conn_id=<YOUR CONNECTION ID FROM THE UI>)
    ssh_client = None
    try:
        ssh_client = ssh.get_conn()
        ssh_client.load_system_host_keys()
        ssh_client.exec_command('touch file_name')
    finally:
        if ssh_client:
            ssh_client.close()
            

#MONGODB COnnection code            
def uploadtomongo(ti, **context):
    hook = MongoHook(mongo_conn_id='mongo_default')
    client = hook.get_conn()
    db = client.MyDB # Replace "MyDB" if you want to load data to a different database
    currency_collection=db.currency_collection
    print(f"Connected to MongoDB - {client.server_info()}")
    d=json.loads(context["result"])
    currency_collection.insert_one(d)

with DAG(
    dag_id="load_data_to_mongodb",
    schedule=None,
    start_date=datetime(2023, 04, 28),
    catchup=False,
    default_args={
        "retries": 0,
    }
):

    t1 = SimpleHttpOperator(
        task_id='get_currency',
        method='GET',
        endpoint='2023-04-28..2023-04-30',
        headers={"Content-Type": "application/json"},
        do_xcom_push=True
    )

    t2 = PythonOperator(
        task_id='upload-mongodb',
        python_callable=uploadtomongo,
        op_kwargs={"result": t1.output},
    )

    task_1 = BashOperator(
            task_id='shell_execute', 
            bash_command='echo "bashoperator" '
            bash_command_ssh='ssh ubuntu@control.brandsonroad.com'
            mongo_cmd = 'mongodump --forceTableScan --db led --gzip --archive=mongoBackup_`date +"%Y-%m-%d.gz"`'
            cmd01 = 'll'
            )
    
    
    t1 >> t2 >> task_1
    
    