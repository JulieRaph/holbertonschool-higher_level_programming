# RESTful API

In the evolving world of software development, understanding how to communicate and transfer data efficiently between systems is essential. This project delves into the domain of RESTful APIs, a cornerstone in the realm of web services. The Representational State Transfer (REST) architecture is a set of constraints that ensure a scalable, stateless, and cacheable communication system. This approach allows for the easy integration of web services, making them accessible to a wide range of applications.

## Learning Objectives:

* HTTP/HTTPS Basics: Grasp the foundational principles of the web’s primary protocol, understanding how data transfer occurs, methods involved, and the difference between the secure and non-secure versions.
* API Consumption with Command Line: Hands-on experience in interacting with APIs using basic command-line tools, laying the groundwork for more advanced interactions.
* API Consumption with Python: Elevate your data fetching skills by leveraging Python’s capabilities, allowing for more advanced processing and data manipulation.
* API Development with http.server: Understand the basics of crafting an API from scratch using Python’s built-in modules, setting a solid foundation.
* API Development with Flask: Dive deeper into API development using the lightweight Flask framework, focusing on routing, data management, and scalability.
* API Security & Authentication: Address the crucial aspect of security, understanding how to protect data transfer and ensure only authorized access to resources.
* API Standards & Documentation with OpenAPI: Conclude with the importance of maintaining standardized documentation, ensuring that APIs are usable, understandable, and maintainable.

## REST API Conceptual Diagram:
```
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database
```

Components:

- Client: The requester of the service, often a web browser or application.
- Web Server: Handles the incoming request, acts as a middleman before passing it to the API server.
- API Server: The actual logic layer that processes the request, determining what data or action is required.
- Database: Stores the data which the API might fetch or modify.

Flow:

- The client sends an HTTP/HTTPS request to the Web Server.
- The Web Server, after potential routing and load balancing, forwards the request to the API Server.
- The API Server processes the request, interacts with the database if needed.
- The API Server returns the processed response to the Web Server.
- The Web Server sends back the final HTTP/HTTPS response to the client.

## Tasks:

- [x] Basics of HTTP/HTTPS
- [x] Consume data from an API using command line tools (curl)
- [x] Consuming and processing data from an API using Python
- [x] Develop a simple API using Python with the `http.server` module
- [x] Develop a Simple API using Python with Flask
- [x] API Security and Authentication Techniques     
