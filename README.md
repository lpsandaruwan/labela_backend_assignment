# Autocompany Backend
### Entity Diagram

![](docs/erd.svg)

### Prerequisites
Ensure you have docker-compose installed. You can find installation instructions here, https://docs.docker.com/compose/install/.

### Running the Server
```shell
# Prepare docker images.
docker-compose build
# To run the application,
docker-compose up -d
```

- The server is accessible via http://localhost:8000.
- For API documentation, please refer to the Postman collection, [Autocompany APIs.](docs/Autocompany%20APIs.postman_collection.json)

### User Stories Breakdown
> #### Assumptions and Skipped Functionalities:
> - Authentication is not enabled on APIs. User IDs are manually added to requests due to time constraints. Ideally, user data should be obtained from logged-in sessions.
> - Dummy values are used for roles and permissions. User operations can be enhanced to restrict based on user role permissions.
> - Product creation endpoints should be accessible only for admin and product owner roles.

The Postman collection is organized into folders for the following user stories:

#### User Story 1
> - As a company, I want all my products in a database, so I can offer them via our new platform to customers.

A data migration file has been created for this purpose, including the creation of a product owner and enrichment of some products.

#### User Story 2
> - As a client, I want to add a product to my shopping cart, so I can order it at a later stage.

The frontend workflow is as follows:

1. Create a new user with guest/customer role.
2. List available products.
3. Select desired products and quantities to add to the cart.
4. Upon the first selection, create a cart and set it as the user's default.
5. Each addition to the cart creates a cart_item object, responsible for mapping between cart and product.

#### User Story 3
> - As a client, I want to remove a product from my shopping cart, so I can tailor the order to what I actually need.

The workflow involves:

1. Listing cart items.
2. Removing selected cart items.

#### User Stories 4 & 5
> - I want to order the current contents in my shopping cart, so I can receive the products I need to repair my car.
> - As a client, I want to select a delivery date and time, so I will be there to receive the order.

This functionality can be achieved by:

1. Creating a user address.
2. Creating an order object to map cart, user, address, and delivery details.

#### User Stories 6 & 7
> - As a client, I want to see an overview of all the products, so I can choose which product I want.
> - As a client, I want to view the details of a product, so I can see if the product satisfies my needs.

To fulfill these needs:

1. List all available products.
2. Retrieve detailed information about individual products.

#### API grocery

1. GET `api/v1.0/app_user_roles` - get user roles.
2. GET `api/v1.0/app_user_roles/<str:uid>` - get_user_role_by_uid
3. POST `api/v1.0/app_users` - create user
4. GET `api/v1.0/app_users/<str:uid>` - get user by uid
5. PATCH `api/v1.0/app_users/<str:uid>` - update user by uid
6. GET `api/v1.0/products` -  get products
7. POST - `api/v1.0/products` - create product
8. GET - `api/v1.0/products/<str:uid>` - get product by uid
9. PATCH - `api/v1.0/products/<str:uid>` - update product by uid
10. GET - `api/v1.0/addresses?app_user<str:uid>` - get app user addresses
11. POST - `api/v1.0/addresses` - create address
12. GET `api/v1.0/addresses/<str:uid>` - get address by uid
13. GET `api/v1.0/carts?app_user=<str:uid>` - get app user carts
14. POST `api/v1.0/carts` - create a cart
15. GET `api/v1.0/carts/<str:uid>` - get cart
16. GET `api/v1.0/cartitems?cart=<str:uid>` - get cart items for cart uid
17. POST `api/v1.0/cartitems` - create a cart item
18. GET `api/v1.0/cartitems/<str:uid>` - get cart item by uid
19. GET `api/v1.0/orders?app_user=<str:uid>` - get orders by user uid
20. POST `api/v1.0/orders` - create an order
21. GET `api/v1.0/orders/<str:uid>` - get order by uid
22. PATCH `api/v1.0/orders/<str:uid>` - update order by uid

### LICENSE
MIT, 2024
