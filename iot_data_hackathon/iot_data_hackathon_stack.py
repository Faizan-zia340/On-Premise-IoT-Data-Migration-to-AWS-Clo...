from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_ec2 as ec2,
    aws_s3 as s3,
)
from constructs import Construct

class IotDataHackathonStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1. VPC Setup with custom CIDR to avoid conflicts
        vpc = ec2.Vpc(self, "IoT-VPC",
            max_azs=2,
            nat_gateways=1,
            ip_addresses=ec2.IpAddresses.cidr("10.1.0.0/16")
        )

        # 2. PostgreSQL Server (EC2 Instance)
        # Latest Amazon Linux 2023 AMI
        ami = ec2.MachineImage.latest_amazon_linux2023()

        ec2_instance = ec2.Instance(self, "PostgreSQL-Server",
            instance_type=ec2.InstanceType("t3.medium"),
            machine_image=ami,
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )

        # 3. S3 Bucket for Data (Fixed RemovalPolicy)
        data_bucket = s3.Bucket(self, "IoTHackathonDataBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # Output the Public IP for your records
        from aws_cdk import CfnOutput
        CfnOutput(self, "InstancePublicIP", value=ec2_instance.instance_public_ip)