import sys
import json
import csv

header = ["id", "name", "type", "hardware_model", "hardware_sn", "software_version", "software_last_update",
          "nic1_type", "nic1_mac", "nic1_ipv4", "nic2_type", "nic2_mac", "nic2_ipv4", "state"]

nic = {
    "type": None,
    "mac": None,
    "ipv4": None
}
info = {
    "id": None,  # 设备编号（数据库表自动编号，一般建议由雪花算法生成）
    "name": None,  # 设备名称
    "type": None,  # 设备类型
    "hardware": {  # 设备硬件信息，包括设备型号名称与序列号
        "model": None,  # 硬件型号
        "sn": None,  # 硬件序列号
    },
    "software": {  # 设备软件信息，包括软件版本及其更新时间
        "version": None,
        "last_update": None
    },
    "nic": [  # 设备接口卡，一个设备可以有多个网络接口，因此使用一个列表存储。简单起见，假设本类型设备最多拥有1个以太网接口与一个无线WiFi接口。
    ],
    "state": None  # 设备状态信息
}


def get_file_name(file_path: str):
    return file_path[:file_path.rfind('.')]


if sys.argv[1] == '-b':
    with open(sys.argv[2], 'r+') as csvf:
        devices = []
        for row in csv.reader(csvf):
            device = {
                'id': row[0],
                'name': row[1],
                'type': row[2],
                'hardware': {
                    'model': row[3],
                    'sn': row[4]
                },
                'software': {
                    'version': row[5],
                    'last_update': row[6]
                },
                'nic': [
                ],
                'state': row[13]
            }
            if len(row[7]) != 0:
                device['nic'].append({
                    "type": row[7],
                    "mac": row[8],
                    "ipv4": row[9]
                })
            if len(row[10]) != 0:
                device['nic'].append({
                    "type": row[10],
                    "mac": row[11],
                    "ipv4": row[12]
                })
            devices.append(device)
    with open(get_file_name(sys.argv[2]) + '.json', 'w+') as jsonf:
        json.dump(devices, jsonf)

elif sys.argv[1] == '-p':
    with open(sys.argv[2], 'r+') as jsonf:
        with open(get_file_name(sys.argv[2])+ '.csv', 'w+', newline='') as csvf:
            devices = []
            writer = csv.writer(csvf)
            for item in json.load(jsonf):
                device = [item['id'], item['name'], item['type'], item['hardware']['model'],
                          item['hardware']['sn'], item['software']['version'], item['software']['last_update']]
                for nic in item['nic']:
                    device.append(nic['type'])
                    device.append(nic['mac'])
                    device.append(nic['ipv4'])
                for i in range(13 - len(device)):
                    device.append('')
                device.append(item['state'])
                devices.append(device)
            writer.writerows(devices)

else:
    exit()
