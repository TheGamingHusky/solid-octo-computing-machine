from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    # import the magic random picker
    import random, urllib2
    # list of things to pick from
    url_for_list="https://raw.githubusercontent.com/TheGamingHusky/Something-very-very-very-very-very-very-very-new/master/I%20dont%20know%20what%20i'm%20making.lst"
    raw_typing_options = urllib2.urlopen(url_for_list)
    list_of_options=raw_typing_options.read()
    real_list=list_of_options.split()
    #print "DEBUG - raw typing options is " + str(real_list)
    typing_options = ['1','2','3','4','5','6','7','8','9']
    #find a way to pick something
    typing_choice = random.choice(real_list) 
    # a way to tell the user what to do
    program_info = """This is the activity picker program it will
        pick a random typing program to use
        Todays activity is """ +typing_choice
    
    
    print program_info
    return program_info
if __name__ == "__main__":
    # go get the PORT from the environment
    port = os.environ.get("PORT")
    # run the app with the port and bind to any ip
    app.run(
      "0.0.0.0"
    , port
    )
