# RemoteDebug
This is a simple tool for remote debugging. 

Sometimes you are working on a device who do not have a displayer, debugging can be a problem. I can't do anything if I can't see what is going on. This tool shows a simple way to visualize images and texts through HTTP.
To use this work, feel free to change the code according to you needs.

## How it works ?

The **Device** sends the debug data (image and text) to the **Server**, and then
The **Web browser** get the data from the **Server** and displays the results.



## Try it out
### Start server

```
python server.py
```

### Open Web browser

By default you will see this:

![](https://github.com/cnzeki/py-tools/blob/master/RemoteDebug/demo.jpg)

### Start a client
The client updates the debug data on the sever through HTTP Post. This should be done on you device, here we just demo how to use it.

```
python client.py
```
Now you can see that the **browser** page has been updated.
