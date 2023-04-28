import json
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
#from airflow.providers.mongo.hooks.mongo import MongoHook
from pendulum import datetime


#SSHHook code 
def create_the_file():
    ssh = SSHHook(conn_id=<YOUR CONNECTION ID FROM THE UI>)
    ssh_client = None
    try:
        ssh_client = ssh.get_conn()
        ssh_client.load_system_host_keys()
        #ssh_client.exec_command('touch file_name')
    finally:
        if ssh_client:
            ssh_client.close()
            
task_1 = BashOperator(
            task_id='shell_execute', 
            bash_command='echo "bashoperator" '
            bash_command_ssh='ssh ubuntu@control.brandsonroad.com'
            mongo_cmd = 'echo "mongodump --forceTableScan --db led --gzip --archive=mongoBackup_`date +"%Y-%m-%d.gz"`"'
            cmd01 = 'll'
            )
    
    
task_1
    
    