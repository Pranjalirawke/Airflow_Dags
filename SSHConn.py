from airflow.contrib.hooks import SSHHook
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from pendulum import datetime

sshHook = SSHHook(conn_id=<YOUR CONNECTION ID FROM THE UI>)

t1 = SSHExecuteOperator(
     task_id="task1",
     bash_command= echo "task1",
     ssh_hook=sshHook,
     dag=dag)

@dag(start_date=datetime(2023, 04, 28), schedule=None, catchup=False)

def bash_script_example_dag():
    execute_my_script = BashOperator(
        task_id="execute_my_script",
        # Note the space at the end of the command!
  
        bash_command="$AIRFLOW_HOME/include/BASH01.sh "
        
        # since the env argument is not specified, this instance of the
        # BashOperator has access to the environment variables of the Airflow
        # instance like AIRFLOW_HOME
    )

    execute_my_script


bash_script_example_dag()