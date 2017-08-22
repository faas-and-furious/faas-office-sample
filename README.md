# faas-office-sample

Create a PowerPoint doc with FaaS

```
$ faas-cli -action build -f ./stack.yml 
$ faas-cli -action deploy -f ./stack.yml 
$ curl -d "FaaS community" http://localhost:8080/function/on-deck > faas.pptx
```

![](https://user-images.githubusercontent.com/6358735/29585241-546cd994-877e-11e7-88dc-127d65fdf3f7.png)
