from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")

def netmiko_send_commands_example(task):
    result = task.run(task=netmiko_send_command, command_string="show ip int bri | exc unass")

nr_filter = nr.filter(city="babolsar")
nr_filter2 = nr.filter( F(city="babolsar") | F(grade="enterprise") & F(as__le="65000") & F(city__contain="bol"))
results=nr_filter.run(task=netmiko_send_commands_example)
results2=nr_filter2.run(task=netmiko_send_commands_example)
print_result(results)

print_result(results2)
