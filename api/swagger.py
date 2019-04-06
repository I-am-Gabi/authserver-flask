swagger_config = {
    "swagger": "2.0",
    "info": {
        "description": "This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key `special-key` to test the authorization     filters.",
        "version": "1.0.0",
        "title": "AuthServer API"
    },
    "basePath": "/api",
    "tags": [
        {
        "name": "user",
        "description": "Operations about user"
        }
    ],
    "schemes": [
        "http"
    ],
    "paths": {
        "/users": {
            "get": {
                "tags": [
                    "user"
                ],
                "summary": "Get all users","description": "",
                "operationId": "getAllUsers",
                "produces": [
                "application/xml",
                "application/json"
            ], 
            "responses": {
            "200": {
                "description": "successful operation",
                "schema": {
                "type": "string"
                },
                "headers": {
                "X-Rate-Limit": {
                    "type": "integer",
                    "format": "int32",
                    "description": "calls per hour allowed by the user"
                },
                "X-Expires-After": {
                    "type": "string",
                    "format": "date-time",
                    "description": "date in UTC when token expires"
                }
                }
            },
            "400": {
                "description": "Invalid username/password supplied"
            }
            }
        }
        },
        "/user": {
        "post": {
            "tags": [
            "user"
            ],
            "summary": "Create user",
            "description": "This can only be done by the logged in user.",
            "operationId": "createUser",
            "produces": [
            "application/xml",
            "application/json"
            ],
            "parameters": [
            {
                "in": "body",
                "name": "body",
                "description": "Created user object",
                "required": True,
                "schema": {
                "$ref": "#/definitions/User"
                }
            }
            ],
            "responses": {
            "default": {
                "description": "successful operation"
            }
            }
        }
        },
        "/user/login": {
        "get": {
            "tags": [
            "user"
            ],
            "summary": "Logs user into the system",
            "description": "",
            "operationId": "loginUser",
            "produces": [
            "application/xml",
            "application/json"
            ],
            "parameters": [
            {
                "name": "username",
                "in": "query",
                "description": "The user name for login",
                "required": True,
                "type": "string"
            },
            {
                "name": "password",
                "in": "query",
                "description": "The password for login in clear text",
                "required": True,
                "type": "string"
            }
            ],
            "responses": {
            "200": {
                "description": "successful operation",
                "schema": {
                "type": "string"
                },
                "headers": {
                "X-Rate-Limit": {
                    "type": "integer",
                    "format": "int32",
                    "description": "calls per hour allowed by the user"
                },
                "X-Expires-After": {
                    "type": "string",
                    "format": "date-time",
                    "description": "date in UTC when token expires"
                }
                }
            },
            "400": {
                "description": "Invalid username/password supplied"
            }
            }
        }
        },
        "/user/logout": {
        "get": {
            "tags": [
                "user"
            ],
            "summary": "Logs out current logged in user session",
            "description": "",
            "operationId": "logoutUser",
            "produces": [
                "application/xml",
                "application/json"
            ],
            "parameters": [],
            "responses": {
                "default": {
                    "description": "successful operation"
                }
            }
        }
        },
        "/user/{username}": {
        "get": {
            "tags": [
                "user"
            ],
            "summary": "Get user by user name",
            "description": "",
            "operationId": "getUserByName",
            "produces": [
                "application/xml",
                "application/json"
            ],
            "parameters": [
            {
                "name": "username",
                "in": "path",
                "description": "The name that needs to be fetched. Use user1 for testing. ",
                "required": True,
                "type": "string"
            }
            ],
            "responses": {
                "200": {
                    "description": "successful operation",
                    "schema": {
                    "$ref": "#/definitions/User"
                    }
                },
                "400": {
                    "description": "Invalid username supplied"
                },
                "404": {
                    "description": "User not found"
                }
            }
        },
        "put": {
            "tags": [
                "user"
            ],
            "summary": "Updated user",
            "description": "This can only be done by the logged in user.",
            "operationId": "updateUser",
            "produces": [
                "application/xml",
                "application/json"
            ],
            "parameters": [
            {
                "name": "username",
                "in": "path",
                "description": "name that need to be updated",
                "required": True,
                "type": "string"
            },
            {
                "in": "body",
                "name": "body",
                "description": "Updated user object",
                "required": True,
                "schema": {
                "$ref": "#/definitions/User"
                }
            }
            ],
            "responses": {
                "400": {
                    "description": "Invalid user supplied"
                },
                "404": {
                    "description": "User not found"
                }
            }
        },
        "delete": {
            "tags": [
                "user"
            ],
            "summary": "Delete user",
            "description": "This can only be done by the logged in user.",
            "operationId": "deleteUser",
            "produces": [
                "application/xml",
                "application/json"
            ],
            "parameters": [
                {
                    "name": "username",
                    "in": "path",
                    "description": "The name that needs to be deleted",
                    "required": True,
                    "type": "string"
                }
            ],
            "responses": {
                "400": {
                    "description": "Invalid username supplied"
                },
                "404": {
                    "description": "User not found"
                }
            }
        }
        }
    },
    "definitions": {
        "User": {
            "type": "object",
            "properties": { 
                "username": {
                    "type": "string"
                },
                "email": {
                    "type": "string"
                },
                "password": {
                    "type": "string"
                },
                "permissions": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "xml": {
                    "name": "User"
                }
            },
        "ApiResponse": {
            "type": "object",
            "properties": {
                "code": {
                "type": "integer",
                "format": "int32"
                },
                "type": {
                "type": "string"
                },
                "message": {
                "type": "string"
                }
            }
        }
    },
    "externalDocs": {
        "description": "Find out more about Swagger",
        "url": "http://swagger.io"
    }
}