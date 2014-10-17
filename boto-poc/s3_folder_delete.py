#!/usr/bin/python
"""
# -----------------------------------------------------------------------------

File name: s3_folder_delete.py
Date created: October 10, 2014
Created by: Al Pacheco

Usage: s3_folder_delete.py <bukcet_name> <override>

Program Description: This progra is used to delte an AWS s3 bucket, including all of its
contents.


Revisions:
Date            Revised by                      Comments
----------  ----------------        -----------------------------------------------
20140811   Al Pacheco                    Script Created


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


def is_protected():
    flag = "DO-NOT-DELETE"

def initiate_s3_connection():
    # Create a connection to AWS S3
    try:
        s3_conn = boto.connect_s3()
    except boto.s3.connection.HostRequiredError, e:
        print "\t Unable to establish s3 connections \n %s" %e
        exit(1)
    return s3_conn

# This function will delete an empty bucket
def delete_root_bucket(bucket_name,s3_conn):
      # This function deltes an s3 bucket.  The bucket
      # MUST be empty
    try:
        s3_conn.delete_bucket(bucket_name)
    except Exception, e:
        print "\t Unable to delete root buket key. ERROR %s" % e

# This function will delte an s3 bucket and its contents
def delete_bucket(bucket_name,s3_conn):
    # if the file 'DO-NOT-DELETE' exists then the folder is protected and
    # will NOT be deleted unless the 'override' is set to true.

    flag = "DO-NOT-DELETE"      # name of file that protects folder

    # Lookup the s3 bucket
    s3bucket = s3_conn.lookup(bucket_name)
    if s3bucket:
        # Lookup key object
        s3key = s3bucket.lookup(flag)

        if  s3key:
            if override == 'true':
                print "\t This bukcet (%s) is protected but will be deleded since override provided!" % bucket_name
                delete_bucket = True
            else:
                print "\t This bukcet (%s) is protected!" % bucket_name
                print "\t If you would like to delete this then set the override = true"
                exit(1)
#        else:

        print '\t Deleting Bucket, (%s),! ' % bucket_name
        try:
            s3bucket = s3_conn.get_bucket(bucket_name)
            for key in s3bucket.list():
                key.delete()
                print "\t This will delete file (key): %s" % key
        except Exception, e:
            print "\t Unable to delte buket key. ERROR %s" % e
            exit(1)
        else:
            print "\t The bucket, %s, and all its contents have been deleted!" % bucket_name        # Now delte the bucket

        # Now delete empty bucket
        try:
            delete_root_bucket(bucket_name,s3_conn)
        except Exception, e:
            print "\t Unable to delte root buket. ERROR %s" % e
            exit(1)

    else:
        print '\t Bucket (%s) does not exist.  Exiting!' % bucket_name
        exit(1)


# -----------------------------------------------------------------------------
#                                                           MAIN
# -----------------------------------------------------------------------------

# Check to if required arguments have been provided
if len(sys.argv) < 2 :
    print 'Usage: ', sys.argv[0], ' <bucket_name> [<override>]'
    print'\t <bucket_name> = Unique s3 bucket name.'
    print'\t <override> = Forces the deltetion of a protected buckett.\n'
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
try:
    override = sys.argv[2]
except:
    override = ''


#print "bucket_name = %s" % bucket_name
#print "override = %s" % override

# Initiate s3 connections
my_s3_conn = initiate_s3_connection()

# Delete the bucket
delete_bucket(bucket_name,my_s3_conn)




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
