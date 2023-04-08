# -*- coding: utf-8 -*-
"""
Завдання 5.5a

Доповнити скрипт із завдання 5.5 таким чином, щоб, залежно від вибраного
режиму, задавалися різні запитання у запиті про номер VLAN або список VLANів:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter the allowed VLANs:'

Плюсом буде вирішити завдання без використання умови if та циклу for, але
перший варіант рішення краще зробити так, як виходитиме.
"""

# access_template = """switchport mode access
# switchport access vlan {}
# switchport nonegotiate
# spanning-tree portfast
# spanning-tree bpduguard enable
# """

# trunk_template = """switchport trunk encapsulation dot1q
# switchport mode trunk
# switchport trunk allowed vlan {}
# """

interface_mode = input('Enter interface mode (access/trunk): ')
interface_type = input('Enter interface type and number: ')
vlan_mode = dict(access='Enter VLAN number: ', trunk='Enter the allowed VLANs: ')
vlans = input(vlan_mode[interface_mode])

mode = dict(

access = f"""switchport mode access
switchport access vlan {vlans}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
""",

trunk = f"""switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {vlans}
"""
)

print()
print(f'interface {interface_type}')
print(mode[interface_mode])
