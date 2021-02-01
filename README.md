# GPT-2 in your phone: Line bot with GPT-2 sentence completion

Because free tier Heroku doesn't have enough space, I run the transformer model on another local machine
and server the main app on Heroku (becuase line requires https web hook)

## How to Use

### Step 1: serve the model, 
* On the machine to serve the model:
  * `cd grpc-transformer`
  * install requirements: `make requirements`
  * compile gRPC related files: `make proto`
  * run the model: `python server.py [--ip IP] [--port PORT]` 
* [Optional] test the server is correctly created
  * `export GRPC_TRANSFORMER_HOST=<ip>:<port>`
  * `python client.py`

### Step 2: deploy the app on Heroku & line
* follow the official tutorial and push this repo

