<h1>Password Manager Python Project</h1>
<h2>Description</h2>
This simple Python project provides a basic password manager functionality. It allows users to create a password file, load an existing password file, add passwords for different websites, and retrieve passwords based on the input of a website name.
Version 1.1.0 has two more features added: displaying all passwords and deleting a password based on a website name
<h2>Features</h2>
<ul>

<li><b>Create Password File:</b> You can create a new password file to store your passwords securely.</li>

<li><b>Load Password File:</b> You can load an existing password file to access previously stored passwords.</li>

<li><b>Add Passwords:</b> Add passwords for different websites along with the corresponding website names.</li>

<li><b>Retrieve Passwords:</b> Retrieve passwords based on the input of a website name.</li>

<li><b>Retrieve All Passwords:</b> Retrieve all the passwords.</li>

<li><b>Delete a Password:</b> Delete a password based on a website name</li>

</ul>

<h2>Prerequisites</h2>
Make sure you have Python installed on your system. If not, you can download and install Python from the official website.

<h2>Getting Started</h2>
Clone the repository to your local machine:
<pre><code>git clone https://github.com/Elhaoua-Alaaeddine/PasswordManager.git</code></pre>

Navigate to the project directory:
<pre><code>cd password-manager</code></pre>

Run the password_manager.py script:
<pre><code>python password_manager.py</code></pre>

<h2>Usage</h2>
<ol>
<li>Create a New Password File:</li>
<ul>
<li>Select option 1 to create a new password file. Follow the prompts to provide a file name.</li>
</ul>
  <br></br>
<li>Load an Existing Password File:</li>
<ul>
<li>Select option 2 to load an existing password file. Enter the file name when prompted.</li>
</ul>
    <br></br>
<li>Add Passwords:</li>
<ul>
<li>Select option 3 to add passwords. Enter the website name and the corresponding password when prompted.</li>
</ul>
    <br></br>
<li>Retrieve Password:</li>
<ul>
<li>Select option 4 to retrieve a password. Enter the website name for which you want to retrieve the password.</li>
</ul>
    <br></br>
  <li>Retrieve All Passwords:</li>
<ul>
<li>Select option 5 to retrieve all passwords.</li>
</ul>
    <br></br>
  <li>Delete a Password:</li>
<ul>
<li>Select option 6 to delete a password. Enter the name of the website that you want to delete with its password.</li>
</ul>
    <br></br>
<li>Exit:</li>
<ul>
<li>Select option 7 to exit the password manager.</li>
</ul>
</ol>
<h2>Example</h2>
<pre>

Welcome to the Password Manager!

1. Create a new password file
2. Load a password file
3. Add a new password
4. Get a password
5. Get all passwords
6. Delete a password
7. Exit

Enter your choice: 1
Enter the name of the file to store the passwords in: passwords.pass

Password file 'passwords.pass' created successfully!

Enter your choice: 3
Enter the website: facebook
Enter the password: 123456
Password added successfully for 'facebook'!

Enter your choice: 4
Enter website name: facebook
the password of the site 'facebook': 123456

Enter your choice: 5
All passwords:
'Site': Password
'facebook': 123456

Enter your choice: 6
Enter the site that you want to delete: facebook
The site facebook and it's password have been deleted

Enter your choice: 7
Exiting password manager...
</pre>
<h2>
Contributors
</h2>
Elhaoua-Alaaeddine
