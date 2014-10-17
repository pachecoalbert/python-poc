#!/usr/bin/python
"""
# -----------------------------------------------------------------------------

File name: sqs.py
Date created: October 17, 2014
Created by: Al Pacheco

Usage: sqs.py <bukcet_name> <dir_to_copy>

Program Description: To Do


Revisions:
Date            Revised by                      Comments
----------  ----------------        -----------------------------------------------
20140817    Al Pacheco                    Script Created


# -----------------------------------------------------------------------------
"""

# Import Python modules
import boto
import sys
import os
import boto.sqs


# -----------------------------------------------------------------------------
#                                                           FUNCTIONS
# -----------------------------------------------------------------------------

def initiate_sqs_connection(sqs_region):
    # Create a connection to AWS SQS
    try:
        sqs_conn = boto.sqs.connect_to_region(sqs_region)
    except Exception, e:
        print "\t Unable to establish SQS Connection. ERROR %s" % e
        exit(1)
    return sqs_conn

def create_sqs_q(sqs_queue,visibility_timeout,sqs_conn):

    # Check if the SQS queue already exists
    sqs_q = sqs_conn.lookup(sqs_queue)

    if sqs_q:
        # SQS already exits, set visibilty timeout if necessary
        print '\t The SQS queue, %s, already exists' % sqs_queue

        # If a visibility timeout is provided then set it
        if visibility_timeout != 'NULL':
            print '\t The SQS queue visibility_timeout to: %s '% visibility_timeout

            try:
                sqs_q = sqs_conn.get_queue(sqs_queue)
                sqs_q.set_attribute('VisibilityTimeout',visibility_timeout)
            except Exception, e:
                print "\t  Failed to set SQS queue visibilty timeout. ERROR %s" % e
    else:
        # SQS queue doesn't exist so create it

        # If a visibility timeout is provided then set it
        try:
            if visibility_timeout != 'NULL':
                sqs_q = sqs_conn.create_queue(sqs_queue, visibility_timeout)
            else:
                sqs_q = sqs_conn.create_queue(sqs_queue)
        except Exception, e:
            print "\t  Failed to set SQS queue visibilty timeout. ERROR %s" % e
        else:
            print "The SQS Queue, (%s), has been created" % sqs_queue

    return sqs_q


# function to print file upload status
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def copy_file_to_s3(file_name,bucket):
    # print 'Uploading %s to Amazon S3 bucket %s' % (file_name, bucket)
    bucket_key = Key(bucket)
    bucket_key.key = file_name
    #print "file_name %s" % file_name
    #print "bucket %s" % bucket

    try:
        bucket_key.set_contents_from_filename(file_name,cb=percent_cb, num_cb=10)
    except:
        raise "Failed to upload file", e

def copy_dir_to_s3(directory,s3_bucket):
    # Set the root dir
    root_dir = directory

    for dir_name, subdir_list, file_list in os.walk(root_dir):
        #print 'Found directory: %s' % dir_name

        for file_name in file_list:
            local_file = os.path.join(dir_name + '/'+ file_name)
            #print "\n\t File long name: %s" % local_file
            #print '\n\t File: %s ' % file_name
            print "\n\t Copying local file: %s to s3 bucket: %s" % (local_file,s3_bucket),

            try:
                copy_file_to_s3(local_file,s3_bucket)
            except:
                print "Failed to copy local file: %s to s3 bucket: %s" % (local_file,s3_bucket)
                exit(1)
    print"\n"


# -----------------------------------------------------------------------------
#                                                           MAIN
# -----------------------------------------------------------------------------

# Check to if required arguments have been provided
if len(sys.argv) < 2 :
    print 'Usage: ', sys.argv[0], ' <sqs_queue> [<visibility_timeout>] '
    print'\t <sqs_queue> = SQS queue name.'
    print'\t <visibility_timeout> = Optional: set the queue visibility timeout.\n'
    exit(1)

# Debug argv
"""
argv_len = len(sys.argv)
for arg in  sys.argv:
    print "Value of argv = %s" % arg
#    print "Index %s: , Value: %s" % i, sys.argv[i]
"""

# Assign command line arguments to local variables
sqs_queue = sys.argv[1]

try:
    visibility_timeout = sys.argv[2]
except:
    visibility_timeout = 'NULL'

print "\t sqs_queue = %s" % sqs_queue
print "\t visibility_timeout = %s" % visibility_timeout



# Initiate SQS connections
my_sqs_conn = initiate_sqs_connection('us-east-1')

# Create the sqs queue
myq = create_sqs_q(sqs_queue,visibility_timeout,my_sqs_conn)

exit(0)


copy_dir_to_s3(dir_to_copy,mybucket)


exit(0)

"""
**************
SCRATCH PAD
**************

# Create a bucket
mybucket = conn.create_bucket('pacheco-mybucket')


from boto.s3.key import Key

# Retriev the bucket Key
bucket_key = Key(mybucket)

# Create a new file (object) which in S3 is called a key.
bucket_key.key = 'test.txt'

# Add content to the new key (file object)
bucket_key.set_contents_from_string('This is a test of S3')

"""
