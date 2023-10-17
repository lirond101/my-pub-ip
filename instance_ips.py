import logging

logger = logging.getLogger()

SAMPLE_INSTANCE_DATA = {
    'Ips': [
        {'Id': '123',  
         'ReadTime': '2020-10-13T19:27:52.000Z', 
         'IpAddress': '54.214.201.8'
        },
        {'Id': '456',  
         'ReadTime': '2021-10-13T19:27:52.000Z', 
         'IpAddress': '54.214.201.9'
        },
        {'Id': '789',  
         'ReadTime': '2022-10-13T19:27:52.000Z', 
         'IpAddress': '54.214.201.10'
        }
    ]
}

class InstanceIps:

    def __init__(self, ips):
        self.ips = ips

    def ips_as_map(self):
        result = {
            'Ips': []
        }
        for ip in self.ips:
            result['Ips'].append({
                'read_id': ip['read_id'], 
                'read_time': ip['read_time'],
                'ip_address': ip['ip_address']
            })
        return result


    # def get_data(self):
    #     logger.debug("Before describe ip data %s", self.id)
    #     result = {'ip_data': []}
    #     try:
    #         response = self.ec2_client.describe_instances()
    #         if response['ResponseMetadata']['HTTPStatusCode'] != 200:
    #             return result
    #     except Exception as ex:
    #         logger.exception(ex)
    #         return result
