# Local Backend Setup

#### Install Python3 and Pip
#### Create a Virtual Environment
```python3 -m venv venv```
#### Activate the Virtual Environment
```source venv/bin/activate ```
Note: Windows users will have different command
#### Install Fast API and Uvicorn[standard]

```pip install fastapi==0.135.2 "uvicorn[standard]==0.42.0"```


#### What [standard] actually does
*When you run pip install uvicorn, you just get the bare minimum, pure-Python version of the server. It works, but it isn't optimized.*

*When you add [standard], you are telling pip to install Uvicorn plus a specific bundle of optional, high-performance dependencies. Specifically, it grabs:*