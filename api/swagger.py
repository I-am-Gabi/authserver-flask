swagger_config = {
    "swagger": "2.0",
    "info": {
        "description": "This is a sample authentication server.  You can find out more about the project at [https://github.com/I-am-Gabi/authserver-flask).",
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
                "summary": "Get all users",
                "description": "",
                "operationId": "getAllUsers",
                "produces": [
                    "application/json"
                ], 
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "token": {
                            "type": "string"
                        },
                        "schema": {
                            "type": "string"
                        }, 
                    },
                    "400": {
                        "description": "Invalid username/password supplied"
                    }
                },
                "parameters": [
                    {
                        "name": "Authorization",
                        "in": "body",
                        "description": "The user name for login",
                        "required": True,
                        "type": "string"
                    }, 
                ],
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
        "/user/{username}": {
            "get": {
                "tags": [
                    "user"
                ],
                "summary": "Get user by user name",
                "description": "",
                "operationId": "getUserByName",
                "produces": [
                
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
        },
        "/login": {
            "post": {
                "tags": [
                    "user"
                ],
                "summary": "Logs user into the system",
                "description": "",
                "operationId": "loginUser",
                "produces": [
                    "application/json", 
                ],
                "parameters": [
                    {
                        "name": "username",
                        "in": "formData",
                        "description": "The user name for login",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "password",
                        "in": "formData",
                        "description": "The password for login in clear text",
                        "required": True,
                        "type": "string"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "successful operation", 
                    },
                    "400": {
                        "description": "Invalid username/password supplied"
                    }
                }
            }
        },
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
    'securityDefinitions': {
        'Bearer': {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    },
    "externalDocs": {
        "description": "Find out more about the project.",
        "url": "https://github.com/I-am-Gabi/authserver-flask"
    },
}