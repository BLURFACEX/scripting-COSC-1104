import boto3
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import time

# Constants
CPU_THRESHOLD = 80.0  # CPU usage percentage threshold
MEMORY_THRESHOLD = 75.0  # Memory usage percentage threshold
CHECK_INTERVAL = 60  # Time in seconds between checks

# AWS Boto3 client setup
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
ec2 = boto3.client('ec2', region_name='us-east-1')

def get_cpu_usage(instance_id):
    """Fetches CPU usage data for a specified EC2 instance."""
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=datetime.utcnow() - timedelta(minutes=5),
        EndTime=datetime.utcnow(),
        Period=300,
        Statistics=['Average']
    )
    cpu_usage = response['Datapoints'][0]['Average'] if response['Datapoints'] else 0
    return cpu_usage

def send_email_alert(instance_id, metric, value):
    """Sends an email alert if usage exceeds the defined threshold."""
    msg = MIMEText(f'Alert: {metric} usage for instance {instance_id} is at {value}%')
    msg['Subject'] = f'{metric} Usage Alert'
    msg['From'] = 'alert@example.com'
    msg['To'] = 'recipient@example.com'
    
    with smtplib.SMTP('smtp.example.com') as server:
        server.login("username", "password")
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
    print(f"Alert email sent for {metric} usage on instance {instance_id}")

def monitor_instance(instance_id):
    """Monitors CPU and memory usage for an EC2 instance."""
    cpu_usage = get_cpu_usage(instance_id)
    print(f"Instance {instance_id} - CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        send_email_alert(instance_id, 'CPU', cpu_usage)
        
def main():
    # Replace with your instance ID(s)
    instance_ids = ['i-0123456789abcdef0']
    while True:
        for instance_id in instance_ids:
            monitor_instance(instance_id)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
