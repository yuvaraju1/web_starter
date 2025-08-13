# Welcome to your first Flask app :)

# Imports usually happen at the top of the file in python. They load
# in all the other libraries that your code will be using, so that you
# can call the functions they define, or instantiate the classes they create.

# Import the main class from the "Flask" library that we need to create our
# web application, as well as the `render_template` function for returning
# HTML files as responses, as well as the `request` objects which contains
# information about requests that we recieve, like the URL and cookies and
# stuff like that.
from flask import Flask, render_template, request

# Create the variable `app` which is an instance of the Flask class that
# we just imported. Being an "instance of a class" is something pretty
# import to any kind of software development, but you don't need to know
# exactly what it means right now.
app = Flask(__name__)


# Here, we're creating the homepage of our application. We're defining a
# function called `homepage` which doesn't take any arguments (nothing
# inside the parentheses). Above the function definiton, we're adding a
# "decorator" which tells our app which "route" (ie URL) should be mapped
# to this function. So if you wanted to add more pages to your app, you
# could add new python functions for them, and decorate them with new routes.
@app.route("/")
def homepage():
    
    # Inside this function, you can run whatever logic you want, running any python
    # code your heart desires. You could check the cookies on the request to see if
    # there's a logged in user making the requests, you could read or write to a
    # database or run any kind of functions you want. Here, we're just returning a 
    # simple string to be returned as the response.
    return "Hello, Yuvaraju Sai Kumar"


@app.route("/basic-page/")
def basic_page():
    # But you don't want to have to write the HTML for your webpages inside a python
    # string. That'd get really annoying quickly. Thankfully, most web frameworks
    # come with a "template engine" that can take basic HTML files and spit it out
    # in a response. Here, we're rendering the 'basic-page.html' file inside the
    # templates folder, which is where Flask looks for template files by default.
    # Rending just means taking the template and turning it into a complete HTML documet.
    return render_template("basic-page.html")

# Using templates is cool and all, but web applications are supposed to by dynamic,
# not just showing the same content every time you load the page. So let's build a
# page that returns different output based on some query arguments that the user
# passes in. Those are the parts of the URL after the "?" sign.
@app.route("/dynamic-page/")
def dynamic_page():

    # If there are no query arguments on the URL (ie length of query arguments is 0)
    # then tell the user to try adding some.
    if len(request.args) == 0:
        return "Add some query arguments to the end of the URL. Like this ?name=Ben"

    # Here, we're rendering a different template, and passing the query arguments
    # to the template to be mixed into the content. This will create a variable
    # called `user_data` that we can user in the HTML template, and it contains the
    # values that were in the query arguments. Go check out that file to see how that
    # works.
    return render_template("dynamic-page.html", user_data=request.args)


# Some boilerplate code that just says "if you're running this from the command
# line, start here." It's not critical to know what this means yet.
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
