### REST Api (REpresentational State Transfer)

- software design pattern used for web applications: treat objects on the server-side similar to rows in a database table that can be created or destroyed

- requests: `GET`, `PUT`, `POST`, `DELETE`

- **REST Principles**: client-server communication, stateless, cacheable, uniform interface

- one basic concept is URL formatting

  - use RESTful urls for retrieving data: see examples below

- `/posts`: Allow users to access all posts for display purposes

- `/posts/:id`: Allow users to access and view an individual post, retrieiving the post using a unique id

- `/posts/new`: Display a form for creating a new post

- `POST` request to `/users` would allow a user to create a new post on the db level

- `PUT` requests to `/users/:id` would allow you to update the attributes of a given post using the unique id

- `DELETE` requests to `/users/:id` would allow users to delete a post by a unique id
