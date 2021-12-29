import requests
import argparse
import time
# Establish Arguements
parser = argparse.ArgumentParser(description="Program to send messages to Discord via the command line")
parser.add_argument("--message", help="Sends the supplied text to discord")
parser.add_argument("--url", help="URL for Discord Webhook", required=True)
parser.add_argument("--lines", help="File to read from and send message (one per line)")
parser.add_arguement("--delay", help="Delay between each message sent, default is 2 seconds", type=float, default=2.0)
args = vars(parser.parse_args())

# if the -m flag is present, assign whatever is behind the flag to the content variable, send request
def Message(content,destination):
    messageObject = {
        "content": content
    }
    send = requests.post(destination,data=messageObject)
# if the -l flag is present, open and loop through file, sending the contents of each line per message, waiting 2.5 seconds in between
def Lines(file, destination):
    file1 = open(file, 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
        count += 1
        messageObject = {
            "content": line
        }
        send = requests.post(destination,data=messageObject)
        time.sleep(args["delay"])
        



# Handle logic for flags. 
if bool(args['lines']) == False & bool(args['message']):
    print("Invoke message function")
    Message(args["message"],args["url"])
    exit()
elif bool(args['lines']) & bool(args['message']) == False:
    print("Invoke Lines function")
    Lines(args["lines"],args["url"])
    exit()
elif bool(args['lines']) & bool(args['message']):
    print("Error: Only one of the two message type flags should be supplied. Please see help menu and try again")
    exit()
