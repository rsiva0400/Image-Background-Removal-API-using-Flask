from flask import jsonify
from database import *
from rembg import remove
from PIL import Image
from io import BytesIO


def signup_function(email, password):
    if not email or not password:
        return 'EmailId and password are required', 400
    if get_user_by_email(email):
        return 'Email Id already exists', 400
    create_user(email, password)
    return 'User created successfully', 200



def login_function(email, password):
    user = get_user_by_email(email)
    if not user or user.check_password(password):
        return'Invalid Email ID or password', 400

    return jsonify({'api_key': user.apiKey, 'available_api_calls': user.availableApiCalls})

def remove_background_function(apiKey, imageFile):

    allowed_extensions = {'png', 'jpg', 'jpeg'}
    if '.' not in imageFile.filename or imageFile.filename.split('.')[-1].lower() not in allowed_extensions:
        return 'Invalid file', 400
    
    user = get_user_by_apikey(apiKey)
    
    if not user:
        return "Invalid API Key", 400
    
    if user.availableApiCalls <= 0:
        return "You've reached your API call limit.", 400
    
    input_image = Image.open(imageFile)

    # Remove the background
    output_image = remove(input_image)

    # Convert the PIL Image to bytes
    output_image_bytes = BytesIO()
    output_image.save(output_image_bytes, format='PNG')
    output_image_bytes.seek(0)

    update_available_api_calls(user)

    return output_image_bytes, 200
