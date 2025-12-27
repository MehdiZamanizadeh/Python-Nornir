from nornir import InitNornir
from nornir_utils.plugins.functions import print_result

nr=InitNornir(config_file='config.yaml')

def Access_Data(task):
    print(task.host['community'])
    print(task.host['OS_Type'])

results=nr.run(task=Access_Data)
print_result(results)
