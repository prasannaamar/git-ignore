import boto3
from botocore.exceptions import ClientError

# Create S3 client
s3 = boto3.client('s3')

# Bucket name must be globally unique
bucket_name = 'my-unique-demo-bucket-12345'

# AWS region
region = 'us-east-1'

try:
    # Create bucket
    if region == 'us-east-1':
        response = s3.create_bucket(
            Bucket=bucket_name
        )
    else:
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )

    print(f"Bucket '{bucket_name}' created successfully!")

except ClientError as e:
    print("Error:", e)
