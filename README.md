This module allows you to obfuscate some of the data in the database.
This is implemented via the pre_install hook, removing the data of the models 'ir.mail_server', 'fetchmail.server' and changing the password of the user with the login "admin".
You just need to install the module, log out of your account and make a backup.
