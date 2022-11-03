# WebhookTesting

An echo server that allows you to store and search for payloads. Useful for testing webhooks. Assumes a single client. Payloads are stored in memory and are cleared upon server restart. This is a standard FastAPI service.

## Getting started

### Run the service locally
```
$ pip install webhook-testing
$ uvicorn --host localhost --port 8080 webhooktesting.main:app
```

### Check version
```
$ curl http://localhost:8080/webhooktesting/version 
{"version":"0.4.0"}`
```

### Send a payload
```
$ curl -X PUT http://localhost:8080/webhooktesting -d 'hello world'
"Successfully added b'hello world'"
```

### Search for a payload (substring match)
```
$ curl "http://localhost:8080/webhooktesting/search?query=hello"
true
```

### Clear all payloads from cache.
```
$ curl -X DELETE http://localhost:8080/webhooktesting              
"Successfully cleared cache"
```

There are a few more handy endpoints but if you're planning to use this service, you probably just want to read the code - there isn't much.
