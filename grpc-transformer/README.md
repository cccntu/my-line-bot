# Use gRPC to run transformer inference on another machine

Because free tier Heroku doesn't have enough space, I will run the transformer model on another local machine

## How to Use

* On the machine to serve the model:
  * install requirements: `make requirements`
  * compile gRPC related files: `make proto`
  * run the model: `python server.py [--ip IP] [--port PORT]` 
* [Optional] test the server is correctly created
  * `export GRPC-TRANSFORMER-HOST=<ip>:<port>`
  * `python client.py`

