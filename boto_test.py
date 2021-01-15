import os
import boto
import boto3
from boto.s3.key import Key
import boto.s3.connection


folder_name = 's3_folders'
download_folder = os.path.join(os.getcwd(), folder_name)
print(os.getcwd())
if os.path.isdir(download_folder):
    pass
else:
    os.mkdir(download_folder)


AWS_ACCESS_KEY_ID = 'AKIAXRUJHASABRVOZPHG'
AWS_SECRET_ACCESS_KEY = '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'
Bucketname = 'aktana-novartis-cdf' 

session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
client = session.client(service_name = 's3',endpoint_url='https://aktana-novartis-cdf.s3.amazonaws.com')

print(client.list_objects(Bucket = Bucketname) )
# exit()  
response = client.list_objects_v2(Bucket='aktana-novartis-cdf')

for content in response['Contents']:
    obj_dict = client.get_object(Bucket=Bucketname, Key=content['Key'])
    print(content['Key'], obj_dict['LastModified'])
    # client.download_file(Bucketname, content['Key'], download_folder)
    if content['Key'].split('.')[-1] == 'csv':
        file = str(os.path.join(download_folder, content['Key'].split('/')[-1]))
        client.download_file(Bucketname, content['Key'], file)
    




