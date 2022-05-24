import json
import requests

dict = """{
        "type": "uplink",
        "meta": {
            "network": "358b679dd88d47948f6e108677b4b79a",
            "packet_hash": "4f5f09b3e40ca6a4394c64c03e0ee660",
            "application": "0000000000000000",
            "device_addr": "1730bd23",
            "time": 1653076504.095,
            "device": "e0ede7150c1d0976",
            "packet_id": "66ff3377c23adb39b11cb6d56e569ef5",
            "gateway": "b0fd0b70001c0000"
        },
        "params": {
            "payload": "VQr8/Pz8AQAAAAAAAAAAIgUgFlUANgI6Fg==",
            "port": 10,
            "duplicate": False,
            "radio": {
                "gps_time": 1337111721986,
                "hardware": {
                    "status": 1,
                    "chain": 0,
                    "tmst": 2233043716,
                    "snr": -16,
                    "rssi": -115,
                    "channel": 2,
                    "gps": {
                        "lat": -23.462099075317383,
                        "lng": -46.78153991699219,
                        "alt": 901
                    }
                },
                "datarate": 0,
                "modulation": {
                    "bandwidth": 125000,
                    "type": "LORA",
                    "spreading": 12,
                    "coderate": "4/5"
                },
                "delay": 0.0403132438659668,
                "time": 1653076504.0201912,
                "freq": 915.6,
                "size": 38
            },
            "counter_up": 12,
            "lora": {
                "header": {
                    "class_b": False,
                    "confirmed": True,
                    "adr": False,
                    "ack": False,
                    "adr_ack_req": False,
                    "version": 0,
                    "type": 4
                },
            "mac_commands": []
            },
            "rx_time": 1653076504.0201912,
            "encrypted_payload": "Jro0dGF7FVld69CpsCjBCfzI78Q7qzrdrA=="
        }
        }"""

simple_json = """
        {
        "type": "uplink",
        "meta": {
            "network": "358b679dd88d47948f6e108677b4b79a",
            "packet_hash": "4f5f09b3e40ca6a4394c64c03e0ee660",
            "application": "0000000000000000",
            "device_addr": "1730bd23",
            "time": 1653076504.095,
            "device": "e0ede7150c1d0976",
            "packet_id": "66ff3377c23adb39b11cb6d56e569ef5",
            "gateway": "b0fd0b70001c0000"
        },
        "params": {
            "payload": "VQr8/Pz8AQAAAAAAAAAAIgUgFlUANgI6Fg==",
            "port": 10,
            "duplicate": false,
            "radio": {
                "gps_time": 1337111721986,
                "hardware": {
                    "status": 1,
                    "chain": 0,
                    "tmst": 2233043716,
                    "snr": -16,
                    "rssi": -115,
                    "channel": 2,
                    "gps": {
                        "lat": -23.462099075317383,
                        "lng": -46.78153991699219,
                        "alt": 901
                    }
                },
                "datarate": 0,
                "modulation": {
                    "bandwidth": 125000,
                    "type": "LORA",
                    "spreading": 12,
                    "coderate": "4/5"
                },
                "delay": 0.0403132438659668,
                "time": 1653076504.0201912,
                "freq": 915.6,
                "size": 38
            },
            "counter_up": 12,
            "lora": {
                "header": {
                    "class_b": false,
                    "confirmed": true,
                    "adr": false,
                    "ack": false,
                    "adr_ack_req": false,
                    "version": 0,
                    "type": 4
                },
            "mac_commands": []
            },
            "rx_time": 1653076504.0201912,
            "encrypted_payload": "Jro0dGF7FVld69CpsCjBCfzI78Q7qzrdrA=="
        }
        
        }
        """
dict2 = dict.replace("False", "false")
dict3 = dict2.replace("True", "true")
dict4 = dict3.replace(" ", "")
print(type(json.loads(dict3)))
aux = json.loads(dict3)
print(json.loads(simple_json))
#print(json.loads(dict))
j = eval(dict)
#print(j)
teste = "teste"
d = {"key": "value"}
response = requests.post('http://192.168.100.6:5050/api/v1/{}'.format(d), json=dict3, headers={"Authorization": "CachorroZika"})

print(response.text)
