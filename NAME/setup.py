#!/usr/bin/env python3

import os

#vps_os = input('CentOS or Ubuntu: ')
#vps_memo = input('Amount of memory in megabytes or gigabytes: ')
#vps_proc = input('Number of processor cores: ')
#vps_band = input('Amount of bandwidth in gigabytes or terabytes: ')
#vps_disk = input('Amount of disk space in gigabytes: ')

email_addr = input('\nEnter your e-mail address: ')
vps_ip_addr = input('Enter the virtual private server\'s IP address: ')
vps_name = input('Enter the virtual private server\'s name: ')
os_username = input('Enter a string for your superuser\'s username: ')
os_password = input('Enter a string for your superuser\'s password: ')
defined_ssh_port = input('Enter an integer, between 1024 and 65535, for your virtual private server\'s new SSH port: ' )

os.system('sed -i "s/<email_addr>/{0}/g" bld/*.sh'.format(email_addr))
os.system('sed -i "s/<vps_ip_addr>/{0}/g" bld/*.sh'.format(vps_ip_addr))
os.system('sed -i "s/<vps_name>/{0}/g" bld/*.sh'.format(vps_name))
os.system('sed -i "s/<os_username>/{0}/g" bld/*.sh'.format(os_username))
os.system('sed -i "s/<os_password>/{0}/g" bld/*.sh'.format(os_password))
os.system('sed -i "s/<defined_ssh_port>/{0}/g" bld/*.sh'.format(defined_ssh_port))

#print('\n' + email_addr)
#print(vps_ip_addr)
#print(vps_name)
#print(os_username)
#print(os_password)
#print(defined_ssh_port)
