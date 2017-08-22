# faas-office-sample

This is a quick demo of what can be done easily with [OpenFaaS](https://github.com/alexellis/faas) and the existing Python module `python-pptx`.

> Sample adapted from: https://python-pptx.readthedocs.io/en/latest/user/quickstart.html

## Create a PowerPoint doc with FaaS

This is a quick way to deploy, if you already have FaaS and the CLI setup.

```
$ faas-cli -action build -f ./stack.yml 
$ faas-cli -action deploy -f ./stack.yml 
$ curl -d "FaaS community" http://localhost:8080/function/on-deck > faas.pptx
```

![](https://user-images.githubusercontent.com/6358735/29585241-546cd994-877e-11e7-88dc-127d65fdf3f7.png)

## Watch for more

Keep an eye out for how to use this with a datasource like the top trending Tweets, Hacker News stories or news headlines.
