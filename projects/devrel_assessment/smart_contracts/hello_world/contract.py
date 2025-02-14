from algopy import ARC4Contract, String, BoxMap, arc4
from algopy.arc4 import abimethod
class Message(arc4.Struct):
    message: arc4.String

class HelloWorld(ARC4Contract):
    
    # Initialize the contract with a box to store the greeting message
    def __init__(self) -> None:
        # Create a BoxMap to store a collection of greetings, stored under a key the caller chooses
        self.message_boxes = BoxMap(String, Message, key_prefix="")
    
    @abimethod()
    def hello(self, message: String, box_name: String) -> arc4.String:
        # Create and format the greeting message
        message_to_add = arc4.String("Hello, " + message)
        
        # Store the message in the BoxMap
        self.message_boxes[box_name] = Message(message = message_to_add)
        
        # Return the greeting message
        return message_to_add

    @abimethod()
    def getMessage(self, box_name: String ) -> Message:        
        # Return the stored message associated with the key provided
        return self.message_boxes[box_name]
