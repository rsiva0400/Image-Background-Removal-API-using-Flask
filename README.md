# Image-Background-Removal-API-using-Flask.
This API provides a comprehensive set of endpoints tailored to handle user authentication and image background removal.

## Required packages
```python
pip install -r requirements.txt
```

## API Endpoints

1. **Signup** - *POST*
   - The Signup endpoint accepts JSON payloads containing a email address and password. It creates a new instance in the user database using the provided credentials. It creates an Unique AOI key and each user will have 5 free API calls.

2. **Login** - *POST*
   - The Login endpoint accepts JSON payloads containing a email address and password. It validates the provided credentials. If the credentials are valid, it'll return the API key associated with that account and the remaining free api calls. If not, proper error message will be returned along with http respose code.

3. **Remove Background** - *POST*
   - The Flask route remove_background handles POST requests to remove the background from an image. It checks for the presence of an image file and an API key in the request. After processing the image with remove_background_function, it returns the modified image if successful, or an error message otherwise.

## Testing
1. **Signup** - *POST*
``` cUrl
curl --location 'http://127.0.0.1:5000/signup' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email" : "user1@example.com",
    "password": "User$001"
}'
```
2. **Login** - *POST*
``` cUrl
curl --location 'http://127.0.0.1:5000/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email" : "user1@example.com",
    "password": "User$001"
}'
```
3. **Remove Background** - *POST*
``` cUrl
curl --location 'http://127.0.0.1:5000/remove_background' \
--form 'image=@"your-sample-image-path"' \
--form 'apiKey="your-api-key"'
```

## Testing in Postman
For testing in Postman API, use the same API url and change the JSON payload with respect to API endpoint.


*JSON Payload for login*
```
{
    "email" : "user1@example.com",
    "password": "User$001"
}
```
*Sample Output*
```
{
    "api_key": "167474caec6efabbc320a0b8e670d339",
    "available_api_calls": 5
}
```
