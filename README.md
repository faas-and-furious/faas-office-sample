# faas-office-sample

This is a quick demo of what can be done easily with [OpenFaaS](https://github.com/alexellis/faas) and the existing Python module `python-pptx`.

> Sample adapted from: https://python-pptx.readthedocs.io/en/latest/user/quickstart.html

## Create a PowerPoint doc with FaaS

This takes a JSON input as defined in "sample.json" with a title, text and image URL then creates a presentation file.

```json
{
    "image_url": "https://pbs.twimg.com/profile_images/894625939652579328/Cmbsq0OP_400x400.jpg",
    "text": "OpenFaaS",
    "title": "Serverless on your servers.. yas"
}
```

Here is a quick way to deploy, if you already have FaaS and the CLI setup:

```
$ faas-cli -action build -f ./stack.yml 
$ faas-cli -action deploy -f ./stack.yml 
$ curl --data-binary @sample.json http://localhost:8080/function/on-deck > faas.pptx
```

![](https://pbs.twimg.com/media/DH6GSXdXcAAngBB.jpg)

## Watch for more

Keep an eye out for how to use this with a datasource like the top trending Tweets, Hacker News stories or news headlines.

* [Other libraries for serverless documents](https://gist.github.com/alexellis/33f946ea83607ed074df7e282c65be6a)

