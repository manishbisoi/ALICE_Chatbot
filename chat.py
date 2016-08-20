#Manages the knowledge base used to think.
import os
import sys, glob
import aiml

kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "ai.xml", commands = "load aiml ai")
    kernel.saveBrain("bot_brain.brn")

kernel.learn("ai.xml")
kernel.respond("load aiml ai")

while True:
	message = raw_input("Enter your message to the bot: ")
	if message == "quit":
		exit()
	elif message == "save":
		kernel.saveBrain("bot_brain.brn")
	else:
		bot_response = kernel.respond(message)
        # Do something with bot_response
        print bot_response