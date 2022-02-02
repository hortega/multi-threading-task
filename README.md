
### Setup

- Clone or [download](https://github.com/hortega/multi-threading-task/archive/master.zip) this repository
- Make sure you have [`docker`](https://www.docker.com/get-started) and [`docker-compose`](https://docs.docker.com/compose/install/) installed
- From within the project directory run `docker-compose up`. Once all containers are up, fire requests like the one below:
```
curl http://localhost:8008/domains -H "Content-Type: application/json" -X POST -d '{"domains":["google.com", "microsoft.com"]}'
```

A list of titles will be returned for those sites in which one could be found.
Add as many domains as you like, although the request may not return any titles if it takes more than 10 seconds.

### Thought process
I had not used before FastAPI, but wanted to give a try since I read about how easy to use was. It's apparently faster and more flexible than Django or Flask, although I couldn't check that on this project.

So I started with the Docker setup to have everything available plus a simple ping endpoint to check that everything works.

Then implemented the basic crawler logic, check the times for a fix list of domains and then implemented it concurrently to compare that the new times were improved. And they were by about 4x-5x.

Finally I implemented the usage stats endpoint using MongoDB.

### Challenges
FastAPI was indeed a challenge but the learning curve is not steep at all. I hadn't Mongo in a while, so I had to check how to use set it up again.

### Improvements
On a different framework and with a bit more time I would have started doing TDD, but this time and with only 2-3 hours I decided to leave them to the end if I had time, which I didn't. Anyway I would have used *requests* to query some mocked domains, plus some unit tests for the individual modules.

Linting, make scripts and some more comments would come next. Then setup a CI pipeline in Github.

### Scalability and deployment
Depending on the use case I could see this going on a couple of directions:
* For requests with large number of domains, I would implement multiprocessing, batching the domains across a few Celery workers. 
* For many requests coming from the same user, we could take advantage of websockets or long polling since FastAPI implements those out of the box.
 