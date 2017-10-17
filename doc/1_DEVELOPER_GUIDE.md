# Developer Guide

Though docker is not especially required to develop on here, you'll find the docker pattern to be much easier and 
 much closer to what the production behavior will be once your code deploys. 
 
Depending on your preference you should look at:

  - [Legacy](1A_DEVELOPER_LEGACY.md)
  - [Docker](1B_DEVELOPER_DOCKER.md)
  
  
Once you've completed the guide you can resume the setup here. 

  
You should be able to access the site via http://0.0.0.0:8000/admin/ and will have to create the default site. 
Start by logging into admin interface.

In the left hand menu select Pages and then again Pages. Add new child page and make sure
you select Home Page type. Give it a nice title and publish it. Now delete the default Welcome page.
Go to the Settings and select Sites. Add a site. Use localhost as a hostname and also give it a nice name. :)

Select a root page. There should be only one page available. Check 'Is default site:' and save the site.

Point your browser to http://127.0.0.1:8000 and it should be working.

Now you can start adding pages, blog index pages and blog posts.

Categories are hidden in the Snippets menu.

  
### Setting up stuff
#### Footer section

Right now there are 4 categories hardcoded in the `footer.html` template:

- geeks-abroad
- gaming
- osalt
- squirrel-army

This means that these categories have to exist and their _slugs_, have
to be the same as on this list. If they are not, then posts in those
categories won't be shown in the footer.  

TODO: Add a SQL or migration script to inject these entities automatically if they don't exist. 


