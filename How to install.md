#Install Python3 and Pip
#Create a Virtual Environment
python3 -m venv venv
#Activate the Virtual Environment
source venv/bin/activate 
Note: Windows users will have different command
#Install Fast API and Uvicorn[standard]

pip install fastapi==0.135.2 "uvicorn[standard]==0.42.0"


What [standard] actually does
When you run pip install uvicorn, you just get the bare minimum, pure-Python version of the server. It works, but it isn't optimized.

When you add [standard], you are telling pip to install Uvicorn plus a specific bundle of optional, high-performance dependencies. Specifically, it grabs:

uvloop: This rips out Python's default, slow asynchronous event loop and replaces it with a drop-in replacement written in Cython (built on top of libuv, the exact same engine that makes Node.js so fast). This is where the massive speed boost comes from.

httptools: A heavily optimized HTTP request parser written in C.

websockets: Adds native support so your app can handle real-time WebSockets (which you will absolutely need later when you build the chat interface for your AI).

watchfiles: The library that watches your hard drive for changes. This is the exact tool that makes your --reload flag work seamlessly without eating up 100% of your CPU.