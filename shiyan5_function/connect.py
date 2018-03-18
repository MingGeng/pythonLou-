#!/usr/bin/env python3

def connect(ip, ports):
	print('IP: ', ip)
	print('Ports: ', ports)
	ip = '10.10.10.1'
	ports.append(8000)

if __name__=='__main__':
	ip = '192.168.1.1'
	ports = [22, 443,8065]
	print('Before connect:')
	print('IP: ', ip)
	print('Ports: ', ports)
	print('In connect:')
	connect(ip, ports)
	print('After connect:')
	print('IP: ', ip)
	print('Ports: ', ports)
