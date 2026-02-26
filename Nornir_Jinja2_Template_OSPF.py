import logging
import os
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.tasks.data import load_yaml

nr = InitNornir(config_file="config.yaml")

def load_data(task):
  hosts_data = task.run(task=load_yaml, file=f"C:/Users/Thinkpad/AppData/Local/Programs/Python/Python313/Nornir/host_vars/{task.host}.yaml")
  task.host["hdata"] = hosts_data.result

def template_sample(task):
    template_path = os.path.dirname(__file__)
    template = task.run(
        task=template_file,
        path=template_path,
        template="ios-template-ospf.j2",
        severity_level=logging.DEBUG,
    )
    task.host["config"]=template.result
    configurations=task.host["config"].splitlines()
    task.run(task=netmiko_send_config, config_commands=configurations)

nr.run(task=load_data)
results = nr.run(task=template_sample)
print_result(results)