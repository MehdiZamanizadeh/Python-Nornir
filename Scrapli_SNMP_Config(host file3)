from nornir import InitNornir
from nornir_scrapli.tasks import send_commands
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def configure_snmp_v2c(task):
    snmp = task.host.data.get("snmp")

    if not snmp:
        return

    configs = []

    # SNMP location & contact
    if "location" in snmp:
        configs.append(f"snmp-server location {snmp['location']}")

    if "contact" in snmp:
        configs.append(f"snmp-server contact {snmp['contact']}")

    # SNMP communities
    for community in snmp.get("communities", []):
        access = community["access"].upper()
        configs.append(
            f"snmp-server community {community['name']} {access}"
        )

    task.run(
        task=send_configs,
        configs=configs
    )

nr.run(task=configure_snmp_v2c)
