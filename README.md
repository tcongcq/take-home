
# Take-Home Project

This project combines NodeJS, Python, ExpressJS, Django, and MySQLite technologies into a unified solution.

### 1. Components:
- CRUD Server: NodeJS and ExpressJS, utilizing MySQLite as the data storage tool.
- Proxy: an intermediary server acting as a proxy, receiving requests from clients and forwarding them to the Express server.
- Django Web: quickly builds an admin page on the Django platform.

### 2. Usage Guide
- user-service: Install the latest NodeJS version, open the terminal, and execute the following commands:

`$ cd user-service`: Navigate to the user-service directory.

`$ npm installl`: Install the required dependencies.

`$ npm start`: Start the service.

After a successful run, the service will be running on port 3000. Use Postman to test CRUD APIs (http://localhost:3000) following the standard CRUD operations: get(users), get(users/:id), post(users), put(users/:id), delete(users/:id) with user information including {name, email}.

- Service djhome:  Install the latest Python (using python3 in this case) and run the following command:

`$ cd djhome`: Navigate to the djhome directory.

`$ python3 manage.py runserver 8080`: Run the service with port 8080.

Access http://localhost:8080/admin with the default account: username: test, password: test.

- Proxy: From the main project directory, install the Flask library and run the proxy

`$ pip install flask`: Install the required library.

`$ python3 proxy.py`: Run the proxy command.

Access http://localhost:8080/users to view the list of users added from the Express API through the proxy, forwarded from port 5009 to 3000.

Thank you for exploring this Take-Home Project! If you have any questions or feedback, feel free to reach out. Happy coding!