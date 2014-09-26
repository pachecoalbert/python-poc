python-poc
==========

-- Install SetupTools
sudo curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python



-- Install boto

sudo easy_install boto

-- Intall Paramiko for SSH2 secure connections
git clone https://github.com/paramiko/paramiko
cd paramiko
sudo python setup.py install

-- Setup euca2ools

git clone https://github.com/eucalyptus/euca2ools.git
cd euca2ools/


sudo easy_install m2crypto




-- Store credentials in the boto config file

cat ~/.aws/credentials
[default]
region = us-east-1
aws_access_key_id = xxxxxxxxxxxx
aws_secret_access_key = xxxxxxxxxxxx


-- Test boto connection to aws

python
Python 2.7.5 (default, Mar  9 2014, 22:15:05)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import boto
>>> ec2 = boto.connect_ec2()
>>> ec2.get_all_zones()
[Zone:us-east-1a, Zone:us-east-1b, Zone:us-east-1d]

-- Enable Debug

python
Python 2.7.5 (default, Mar  9 2014, 22:15:05)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import boto
>>> boto.set_stream_logger('paws')
>>> ec2 = boto.connect_ec2(debug=2)
2014-09-26 15:39:58,473 paws [DEBUG]:Using access key found in shared credential file.
2014-09-26 15:39:58,473 paws [DEBUG]:Using secret key found in shared credential file.

-- Update boto conf to extend http socket timeouts

-- [Boto]
http_socket_timeout = 5
