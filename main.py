#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "name": "Zork",
  "passages": [
    {
      "name": "West of House",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of House",
        }
      ],
      "cleanText": "This is an open field west of a white house, with a boarded front door."
    },
    {
      "name": "North of House",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "West of House",
        }
      ],
      "cleanText": "You are facing the north side of a white house. There is no door here, and all the windows are barred."
    }
  ]
}

current = "West of House"
response = ""
space = 0
while True:
    if response == "quit":
        break
    # Find passage (update)
    for j in range(len(world["passages"][space]["links"])):
      if world["passages"][space]["links"][j]["linkText"] == response.upper():
        current = world["passages"][space]["links"][j]["passageName"]
        if current == "North of House":
          space = 1
        else:
          space = 0
        
    # Display passage (render the world)
    print(world["passages"][space]["name"] + "\n")
    print(world["passages"][space]["cleanText"] + "\n")
    for i in range(len(world["passages"][space]["links"])):
      print(world["passages"][space]["links"][i]["linkText"] + "\n")
      print(world["passages"][space]["links"][i]["passageName"] + "\n")
    # Ask for response (get input)
    response = input("Where would you like to go? ")
