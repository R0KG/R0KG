To test the example on Almighty follow these steps:
---------------------------------------------------

1. Edit these two lines in DatabaseHelper.php:
    const username = 'a01234567'; // Use a + your matriculation number
    const password = '**********'; // Use your oracle db password
    
2. Upload all *.php files to your personal document root directory on Almighty
    /home/[your-u:space-username]/public_html/
    
    Note: If the 'public_html' directory is missing => simply create it!
    
3. Execute the statements contained by the file 'Create.sql' on your Oracle database

4. Open the URL: http://wwwlab.cs.univie.ac.at/~[your-u:space-username]/ in your browser


Note:
---------------------------------------------------
Almighty uses (affects also the home directory): 
    u:space account 
    u:space password 

Your Oracle Database independently uses: 
    a + matriculation number
    your password (initial password: dbs17)


Tipp:
---------------------------------------------------

To publish more than one website at the same time, you can store your *.php files in subdirectories. E.g.

if you store your files in a subdirectory 'tutorial' like:
/home/a1234567/public_html/tutorial/

the URL would be:
http://wwwlab.cs.univie.ac.at/~a1234567/tutorial