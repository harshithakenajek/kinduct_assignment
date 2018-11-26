# kinduct_assignment

Note that you must have Python3 environment setup.

Clone the project using: git clone https://github.com/harshithakenajek/kinduct_assignment.git

    $ virtualenv -p python3 ENV
    $ source ENV/bin/activate
    (ENV) $ pip install -r requirements.txt
    (ENV) $

Run the app using:  python app.py
                    Hit the api (POST METHOD) from the postman http://127.0.0.1:5000/print_message with body message and delivery time.
                    Example: 
                    {
	                "message":"It should be printed",
	                "delivery_time":"2018-11-24T14:44"
                    } 
Api will return with success code 202, and at the given point of time the message will be printed on your console.
