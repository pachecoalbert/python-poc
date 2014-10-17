#!/usr/bin/python
"""
# -----------------------------------------------------------------------------

File name: s3.py
Date created: October 10, 2014
Created by: Al Pacheco

Usage: s3.py <bukcet_name> <dir_to_copy>

Program Description: This program is used to create a s3 bucket in Amazon Web Services.
If the bucket already exists an error will be returned.

Revisions:
    Date            Revised by                      Comments
    ----------  ----------------        -----------------------------------------------
    20140810    Al Pacheco                    Script Created


# -----------------------------------------------------------------------------
"""

# Import Python modules
import boto
import sys
import os
from boto.s3.key import Key

# -----------------------------------------------------------------------------
#                                                           FUNCTIONS
# -----------------------------------------------------------------------------

def initiate_s3_connection():
    # Create a connection to AWS S3
    try:
        s3_conn = boto.connect_s3()
    except boto.s3.connection.HostRequiredError, e:
        print "Unable to establish s3 connections \n %s" %e
        exit(1)
    return s3_conn

def create_bucket(bucket_name,s3_conn):

    s3bucket = s3_conn.lookup(bucket_name)
    if s3bucket:
        print 'The bucket, %s, already exists' % bucket_name
    else:

        try:
            s3bucket = s3_conn.create_bucket(bucket_name)
        except s3_conn.provider.storage_create_error, e:
            print 'The bucket name, %s, is already used by another AWS user.  \nPlease choose another name.' % bucket_name
            exit(1)
        else:
            print "The bucket, %s, has been created!\n" % bucket_name
    return s3bucket

# function to print file upload status
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def copy_file_to_s3(file_name,bucket):
    print 'Uploading %s to Amazon S3 bucket %s' % (file_name, bucket)
    bucket_key = Key(bucket)
    bucket_key.key = file_name
    bucket_key.set_contents_from_filename(file_name,cb=percent_cb, num_cb=10)

def copy_dir_to_s3(directory,s3_bucket):
    # Set the root dir
    root_dir = directory

    for dir_name, subdir_list, file_list in os.walk(root_dir):
        #print 'Found directory: %s' % dir_name

        for file_name in file_list:
            local_file = os.path.join(dir_name + '/'+ file_name)
            #print "\t File long name: %s" % local_file
            #print '\t File: %s ' % file_name
            print "\t Copying local file: %s to s3 bucket: %s" % (local_file,s3_bucket)

            try:
                copy_file_to_s3(local_file,s3_bucket)
            except:
                print "Failed to copy local file: %s to s3 bucket: %s" % (local_file,s3_bucket)
                exit(1)


# -----------------------------------------------------------------------------
#                                                           MAIN
# -----------------------------------------------------------------------------

# Check to if required arguments have been provided
if len(sys.argv) < 3 :
    print 'Usage: ', sys.argv[0], ' <bucket_name> <file_to_copy>'
    print'\t <bucket_name> = Unique s3 bucket name.'
    print'\t <file_to_copy> = File to copy to s3 bucket.\n'
    exit(1)

# Debug argv
"""
argv_len = len(sys.argv)
for arg in  sys.argv:
    print "Value of argv = %s" % arg
#    print "Index %s: , Value: %s" % i, sys.argv[i]
"""

# Assign command line arguments to local variables
bucket_name = sys.argv[1]
dir_to_copy = sys.argv[2]

print "bucket_name = %s" % bucket_name
print "dir_to_copy = %s" % dir_to_copy

# Initiate s3 connections
my_s3_conn = initiate_s3_connection()

# Create the bucket
mybucket = create_bucket(bucket_name,my_s3_conn)

# Upload file to s3 bucket
#TEMP_REM copy_file_to_s3(file_to_copy,mybucket)

# Copy folder to s3
# Note: the dir must be the relative path and NOT include ./
# EG /dir/dir_to_copy
# cd to /dir and pass dir_to_copy
copy_dir_to_s3(dir_to_copy,mybucket)


exit(0)

"""
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
