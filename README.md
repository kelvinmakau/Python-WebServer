A SIMPLE PYTHON WEBSERVER

I was driven by the Pesapal Challenge Interview questions to come up with this and I hope its worth it.

Its a simple Python HTTP web-server application which can listen on a configurable TCP port(in this case localhost:8000) and serve both static HTML and dynamically generated HTML.

I have not been able to implement https secure protocol at the moment.

To run the program;first ensure python3.6 and above is install in your machine.

Clone the program into your desktop

Open terminal and run pyhton main.py, (this starts the server and the set port)

Then open your favorite browser and type localhost/8000. A webpage is displayed.
The displayed page can be found in the program's template folder. At the moment this page does not do anything but just display simple stuff, but it can be edited to  display whatever the user wants. 

The public folder contains all static files, css, js, images and the likes.

localhost/8000 displays the index.html page
If you want to navigate to another page, make sure it is in the templates folder and its link is in the routes/main.py

for instance in our templates we have images.html and it is routed in the routes/main.py as images. If you want to access it you simply type localhost:8000/images
