#!/usr/bin/env python
import ConfigParser
import os
import time

# Variable Definition
username = 'cpdbbackups'
password = 'p@ssw0Rd'
hostname = 're.mo.te.ip
backupfolder = '/home/dbbackups/servername'

filestamp = time.strftime('%Y-%m-%d-%H')
deletetime = time.time() - 7 * 86400

# Delete old files

for backup_file in os.listdir (backupfolder):
 full_file_path = os.path.join(backupfolder, backup_file)
 if os.path.getmtime(full_file_path) < deletetime:
 os.unlink(full_file_path)

# Get a list of databases with :
database_list_command="mysql -u%s -p%s -h %s --silent -N -e 'show databases'" % (username, password, hostname)
for database in os.popen(database_list_command).readlines():
 database = database.strip()

 if database == 'information_schema':
 continue
 filename = "%s/%s-%s.sql" % (backupfolder, database, filestamp)
 os.popen("mysqldump -u%s -p%s -h %s -e --opt -c %s | gzip -c > %s.gz" % (username, password, hostname, database, filename))
