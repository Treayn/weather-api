import argparse
import json
import zmq

context = zmq.Context()

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--current_temperature", help="Retrieve the current temperature at the specified city.", nargs="?")
parser.add_argument("-l","--locations", help="Retrieve list of cities.")
parser.add_argument("-t", "--temperature", help="Retrieve daily max & min temperatures at the specified city.", , nargs="?")

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

if args.current_temperature:
    request = json.dumps({
        "command": "current_temp",
        "data": args.current_temperature
    })
    
    socket.send(request)
    response = json.loads(socket.recv())
    print("Current temperature is: %s F" % response["temperature"])

if args.location:
    request = json.dumps({
        "command": "cities",
        "data": ""
    })

    socket.send(request)
    response = json.loads(socket.recv())
    print("List of cities:\n" %s "\n".join(response["cities"]))

if args.temperature:
    request = json.dumps({
        "command": "temperature",
        "data": args.temperature
    })
    
    socket.send(request)
    response = json.loads(socket.recv())
    print("Daily temperature is: %s F max and %s F min" % (response["daily_max"], response["daily_min"]))