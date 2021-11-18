# Import needed modules. Boto3 for communicating with AWS + uuid to generate random 128 bit objects as ids
import boto3
import uuid
from os import listdir

# Variable to create a s3 client
s3_client = boto3.client("s3", region_name="us-east-1")

# Function upload_objects(): Uploads each object in the uploadFolder into the targetBucket
def upload_objects():
    try:
        # Asking the user for bucket and folder name
        targetBucket = input("Enter the Bucket you would like to upload to: ") # Target bucket name
        uploadFolder = input("Enter the Folder you would like to upload: ") # Local folder for upload starting with C:\ or other drive name

        # Identify each file by traversing through the folder
        for file in listdir(uploadFolder):
            with open(uploadFolder + "\\" + file, "rb") as data:
                s3_client.upload_fileobj(data, targetBucket, str(uuid.uuid1()))

    except Exception as err:
        print(err)

# Initiate the main function
if __name__ == "__main__":
    upload_objects()