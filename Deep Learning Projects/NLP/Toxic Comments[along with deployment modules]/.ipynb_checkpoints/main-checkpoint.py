from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

class model_input(BaseModel):
    
    'transformed_text': object
        
# loading the saved model
toxic_comments_model = pickle.load(open('toxic_comment_model.pkl', 'rb'))

@app.post('/toxic_comments')
def diabetes_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    text = input_dictionary['transformed_text']
    
    
    input_list = [text]
    
    prediction = toxic_comments_model.predict([input_list])
    
    if (prediction[0][0] == 0):
        return 'The comment is not toxic'
    else:
        return 'The comment is toxic'