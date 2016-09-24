# backup-script-for-remotely-backing-up-databases
Simple backup script for remotely backing up databases

After downloading the script to your preferred location, modify thse four lines with the database credentials and backup directory preferred

username = 'cpdbbackups' 

password = 'p@ssw0Rd' 

hostname = 're.mo.te.ip 

backupfolder = '/home/dbbackups/servername'

Executing the script will generate backups of the databases under the user and save it in the backup directory. 

Also backups older than the `deletetime` specified will be rotated, so change this value as per personal choice.
