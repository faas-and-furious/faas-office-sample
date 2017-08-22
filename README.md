# faas-office-sample

Create a PowerPoint doc with FaaS

```
$ faas-cli -action build -f ./stack.yml 
$ faas-cli -action deploy -f ./stack.yml 
$ curl -d "FaaS community" http://localhost:8080/function/on-deck > faas.pptx
```

