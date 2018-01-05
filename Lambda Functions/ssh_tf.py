from __future__ import print_function
import boto3
import paramiko
import StringIO

def lambda_handler(event, context):
    key = """-----BEGIN RSA PRIVATE KEY-----
    YOUR KEY
-----END RSA PRIVATE KEY-----"""

    pkey = paramiko.RSAKey.from_private_key(StringIO.StringIO(key))
    image_name = event['params']['querystring']['image_name']
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    event = {"IP" : ""}
    host=event["IP"]
    print("Connecting")
    c.connect( hostname = host, username = "ec2-user", pkey=pkey)
    print("Connected")
    command = "python tf.py " + image_name
    commands = [command]
    for command in commands:
        print("Executing {}".format(command))
        stdin , stdout, stderr = c.exec_command(command)
        result_string = stdout.read()
        print(result_string)
        print(stderr.read())
    c.close()
    result = result_string.strip().split("=")
    return {'result' : result[1]}