![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome CedricLittman,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!



Readme 

Introduction 

This site is to satisfy the requirements of the third Code Institute Full Stack Bootcamp project which I have implemented by writing the code for a take-away restaurant allowing users full CRUD functionality, each part being discharged as follows: 

Create – Entering orders 

Read – A dashboard allows those with allowed usernames and passwords to review orders and cash received 

Update – Orders can be paid for on collection or on order. The person ordering can pay with Paypal or pay on receipt. The payment status can be changed by staff which allows this to be updated. 

Delete -  

Throughout the project's development, Kanban boards were produced, and these are included in this document. The project was developed on Github so development of the app over time can be seen. 

The project requires users to be able to log in and out without difficulty and this can be done and it has been set up to be public on Github. 

 

Background 

It was decided to satisfy the Code Institute’s project requirements by programing an ordering system for a restaurant. To make this more interesting the restaurant is Kosher and, as submission of the project coincides with Passover, the restaurant is Kosher for Passover. This has additional requirements that have nothing to do with coding and are outlined in Appendix XXX. The project was planned using Kanban boards and the first is shown in the next section. 

The site enables management to add and remove dishes, change prices as needed, and provides basic management information. The management information provided is a list of the day's orders, how many orders were placed, and the day’s total revenue. The site runs on Django and uses an SQLite database, the default Django database, but the project required no SQL programming as that was all handled by Django. 

On the other hand Django programming did have to be learned and this will be discussed briefly later. Django allowed the database to be programmed which produced much of the functionality of the site ranging from showing what products are available, to recording management figures, to allowing permitted users to change the restaurant’s offerings.  

The screens seen by the user are HTML pages programmed by Django and are made responsive using Bootstrap.  

 

Preparation 

The site was built in the Github virtual environment so could be accessed from any of the college buildings and from home. While the site was being built, we were in three different classrooms in three different buildings, so a virtual environment was essential which also enabled the site to be worked on at home. 

A virtual workstation was set up with the Code Institute template and the following were installed using Pip3: 

Django – A high-level Python web framework that enables rapid development of secure and maintainable websites 

Allauth - an integrated set of Django applications dealing with account authentication, registration, management, and third-party (social) account authentication. In this project it is only used for validating staff so they can manage the site but it can be extended if required 

Crispy Forms - Django does not provide any form styling forms that look very bland. Crispy forms styles the forms. Although this is only evident in the login page in this project it can also generate emails which is where it would be used. As it stands the restaurant project only sends emails to the console 

Pillow - An imaging library that adds image processing capabilities to Python. It provides extensive file format support and powerful image processing capabilities.  

These were all installed with Pip3 which enables the installation and management of third-party software packages with features and functionality not found in the Python standard library. 

Python appeared to have been installed already. 

Having these installed allowed the Django site to be set up, 

 

Introduction To Django 

 When a conventional website receives an HTTP request from the client the application processes the correct response and it may then read or write information from a database or perform other tasks required to satisfy the request. The application will then return a response to the client, often dynamically creating an HTML page by inserting the retrieved data into placeholders in an HTML template. 

Django web applications typically group the code that handles each of these steps into separate files: 

 

Stages between a client request and a response to the browser 

 

 

 

 

 

 

 

 

 

 

 

 

 

The app has a home page which was wireframed and it shows the kitchen and two other pictures, one of a restaurant sign to give anyone chancing on the site an understanding of what it is and another that shows an open sign to convey willingness and the desire to serve. 

 