# Import Python modules
import boto

# Create a connection to AWS S3
conn = boto.connect_s3()

# Open a bucket
mybucket = conn.get_bucket('pacheco-mybucket')

from boto.s3.key import Key

# Retriev the bucket Key
bucket_key = Key(mybucket)

# Create a new file (object) which in S3 is called a key.
bucket_key.key = 'test.txt'

# Get the contents of the key (file object)
contents = bucket_key.get_contents_as_string()

print "File Contents: \n %s." %  contents
