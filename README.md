Content Generation Microservice

What it does
--------------

This microservice gives you either a motivational quote or a habit suggestion.
It checks request.json for new requests, then writes the answer to response.json.
After it’s done, it marks the request as "completed" so it doesn’t do it again.

How to request data
--------------------

The microservice looks for a JSON file called request.json with these fields:

{
    "type": "quote",
    "status": "pending"
}

"type" can be "quote" or "habit"

"status" must be "pending" to get processed


What the response looks like
--------------------------------

After the microservice processes a request, it writes a JSON file called response.json:

{
    "type": "quote",
    "result": "The only way to do great work is to love what you do. - Steve Jobs",
    "status": "completed"
}

If the type is wrong, it gives an error:

{
    "type": "unknown",
    "result": "There was an error with the request",
    "status": "error"
}

How to run it
----------------

Make sure content_microservice.py and request.json are in the same folder.

Open terminal in that folder and run:

python content_microservice.py

To make a new request:

Open request.json

Change "status" to "pending"

Set "type" to "quote" or "habit"

Save it

Watch response.json get updated.

The microservice checks every second and updates request.json to "completed" after processing.


Notes
--------

The quotes and habits are stored in the code.

The microservice only processes requests with "status": "pending".

Invalid request types return an error.

UML Sequence Diagram
----------------------
<img width="838" height="493" alt="image" src="https://github.com/user-attachments/assets/af11327d-3d78-410a-b5f0-4896a15264cd" />

