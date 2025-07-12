#Write a Python script using boto3 to deploy a trained model artifact from S3 to an EC2 instance and trigger a Flask API service.

import boto3
import paramiko

def deploy_model(s3_bucket, s3_key, ec2_dns, key_file_path):
    # Download the model
    s3 = boto3.client('s3')
    s3.download_file(s3_bucket, s3_key, 'model.pkl')

    # SSH to EC2
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ec2_dns, username='ec2-user', key_filename=key_file_path)

    # Transfer model file
    sftp = ssh.open_sftp()
    sftp.put('model.pkl', '/home/ec2-user/model.pkl')
    sftp.close()

    # Start Flask app
    stdin, stdout, stderr = ssh.exec_command('sudo systemctl restart flask-api.service')
    print(stdout.read().decode())
    ssh.close()

deploy_model("my-ml-bucket", "models/model.pkl", "ec2-3-22-44.compute.amazonaws.com", "/path/to/key.pem")
