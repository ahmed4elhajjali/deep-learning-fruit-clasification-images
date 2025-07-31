import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np
from PIL import Image

st.header('Image Classification Model')

model = load_model(r'E://3rd//deep//deep project//DEEP PROJECT//Image_classification//final project//best//New folder//Image_classify_model.keras')

data_cat = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 'cauliflower',
            'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi',
            'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple', 'pomegranate',
            'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato', 'turnip', 'watermelon']

prices = {
    'apple': '3 USD per kg',
    'banana': '1.5 USD per kg',
    'beetroot': '2.5 USD per kg',
    'bell pepper': '2.8 USD per kg',
    'cabbage': '1.2 USD per kg',
    'capsicum': '3 USD per kg',
    'carrot': '1.7 USD per kg',
    'cauliflower': '2.3 USD per kg',
    'chilli pepper': '4 USD per kg',
    'corn': '0.8 USD per kg',
    'cucumber': '1.5 USD per kg',
    'eggplant': '2.2 USD per kg',
    'garlic': '5 USD per kg',
    'ginger': '4.5 USD per kg',
    'grapes': '3.5 USD per kg',
    'jalepeno': '3.2 USD per kg',
    'kiwi': '4.5 USD per kg',
    'lemon': '1.3 USD per kg',
    'lettuce': '1 USD per kg',
    'mango': '2 USD per kg',
    'onion': '1.1 USD per kg',
    'orange': '2.5 USD per kg',
    'paprika': '3.5 USD per kg',
    'pear': '3 USD per kg',
    'peas': '2.2 USD per kg',
    'pineapple': '4 USD per kg',
    'pomegranate': '4.5 USD per kg',
    'potato': '0.5 USD per kg',
    'raddish': '2 USD per kg',
    'soy beans': '3 USD per kg',
    'spinach': '1.5 USD per kg',
    'sweetcorn': '1.8 USD per kg',
    'sweetpotato': '2.3 USD per kg',
    'tomato': '1.2 USD per kg',
    'turnip': '2.5 USD per kg',
    'watermelon': '3 USD per kg'
}

recipes = {
    'apple': ['Apple Pie', 'Apple Crumble', 'Apple Smoothie'],
    'banana': ['Banana Bread', 'Banana Smoothie', 'Banana Pancakes'],
    'beetroot': ['Beetroot Soup', 'Beetroot Salad'],
    'bell pepper': ['Stuffed Bell Peppers', 'Bell Pepper Stir Fry'],
    'cabbage': ['Cabbage Soup', 'Cabbage Stir Fry', 'Coleslaw'],
    'capsicum': ['Capsicum Pizza', 'Capsicum Curry'],
    'carrot': ['Carrot Soup', 'Carrot Cake', 'Carrot Salad'],
    'cauliflower': ['Cauliflower Rice', 'Cauliflower Soup'],
    'chilli pepper': ['Chilli Sauce', 'Chilli Stir Fry'],
    'corn': ['Corn Soup', 'Grilled Corn'],
    'cucumber': ['Cucumber Salad', 'Cucumber Smoothie'],
    'eggplant': ['Eggplant Parmesan', 'Eggplant Stir Fry'],
    'garlic': ['Garlic Bread', 'Garlic Sauce'],
    'ginger': ['Ginger Tea', 'Ginger Soup'],
    'grapes': ['Grape Juice', 'Grape Salad'],
    'jalepeno': ['Jalapeño Poppers', 'Spicy Jalapeño Dip'],
    'kiwi': ['Kiwi Smoothie', 'Kiwi Salad'],
    'lemon': ['Lemonade', 'Lemon Cake', 'Lemon Tea'],
    'lettuce': ['Lettuce Wraps', 'Lettuce Salad'],
    'mango': ['Mango Smoothie', 'Mango Salad', 'Mango Ice Cream'],
    'onion': ['Onion Soup', 'Fried Onions'],
    'orange': ['Orange Juice', 'Orange Cake', 'Orange Salad'],
    'paprika': ['Paprika Chicken', 'Paprika Sauce'],
    'pear': ['Pear Pie', 'Pear Salad'],
    'peas': ['Peas Soup', 'Peas Pulao'],
    'pineapple': ['Pineapple Pizza', 'Pineapple Smoothie', 'Pineapple Upside-Down Cake'],
    'pomegranate': ['Pomegranate Juice', 'Pomegranate Salad'],
    'potato': ['Mashed Potatoes', 'Potato Fries', 'Potato Salad'],
    'raddish': ['Radish Salad', 'Pickled Radish'],
    'soy beans': ['Soybean Stir Fry', 'Soybean Soup'],
    'spinach': ['Spinach Soup', 'Creamed Spinach'],
    'sweetcorn': ['Sweetcorn Soup', 'Sweetcorn Salad'],
    'sweetpotato': ['Sweet Potato Fries', 'Sweet Potato Soup'],
    'tomato': ['Tomato Soup', 'Tomato Pasta', 'Tomato Salad'],
    'turnip': ['Turnip Soup', 'Mashed Turnips'],
    'watermelon': ['Watermelon Juice', 'Watermelon Salad']
}

top_producers = {
        'apple': ['China', 'USA', 'Poland', 'India'],
        'banana': ['India', 'China', 'Indonesia', 'Brazil'],
        'beetroot': ['Russia', 'India', 'USA', 'Poland'],
        'bell pepper': ['China', 'Mexico', 'Turkey', 'Indonesia'],
        'cabbage': ['China', 'India', 'Russia', 'USA'],
        'capsicum': ['Mexico', 'China', 'Turkey', 'USA'],
        'carrot': ['China', 'Russia', 'USA', 'India'],
        'cauliflower': ['China', 'India', 'USA', 'Italy'],
        'chilli pepper': ['China', 'India', 'Mexico', 'Thailand'],
        'corn': ['USA', 'China', 'Brazil', 'Argentina'],
        'cucumber': ['China', 'India', 'Russia', 'Turkey'],
        'eggplant': ['China', 'India', 'Egypt', 'Turkey'],
        'garlic': ['China', 'India', 'Argentina', 'Egypt'],
        'ginger': ['India', 'China', 'Nigeria', 'Indonesia'],
        'grapes': ['China', 'Italy', 'USA', 'Spain'],
        'jalepeno': ['Mexico', 'USA', 'Brazil', 'India'],
        'kiwi': ['Italy', 'New Zealand', 'Chile', 'Greece'],
        'lemon': ['India', 'Mexico', 'Argentina', 'Spain'],
        'lettuce': ['China', 'USA', 'Spain', 'India'],
        'mango': ['India', 'China', 'Thailand', 'Indonesia'],
        'onion': ['China', 'India', 'USA', 'Russia'],
        'orange': ['Brazil', 'USA', 'India', 'China'],
        'paprika': ['Mexico', 'Spain', 'Turkey', 'Hungary'],
        'pear': ['China', 'USA', 'Argentina', 'Italy'],
        'peas': ['China', 'India', 'USA', 'Russia'],
        'pineapple': ['Costa Rica', 'Philippines', 'Thailand', 'India'],
        'pomegranate': ['India', 'Iran', 'China', 'USA'],
        'potato': ['China', 'India', 'Russia', 'USA'],
        'raddish': ['China', 'India', 'USA', 'Mexico'],
        'soy beans': ['USA', 'Brazil', 'Argentina', 'China'],
        'spinach': ['China', 'USA', 'India', 'Italy'],
        'sweetcorn': ['USA', 'China', 'Brazil', 'India'],
        'sweetpotato': ['China', 'USA', 'Nigeria', 'Indonesia'],
        'tomato': ['China', 'India', 'USA', 'Turkey'],
        'turnip': ['China', 'India', 'Russia', 'USA'],
        'watermelon': ['China', 'Turkey', 'India', 'Brazil']
        
    }

health_benefits_dict = {
        'apple': 'Good source of fiber and Vitamin C.',
        'banana': 'High in potassium, supports heart health.',
        'beetroot': 'Rich in antioxidants, supports blood pressure.',
        'bell pepper': 'Packed with Vitamin C, helps immune system.',
        'cabbage': 'High in fiber, supports digestion.',
        'capsicum': 'Rich in Vitamin A and C, good for eyes.',
        'carrot': 'Rich in Vitamin A, good for vision.',
        'cauliflower': 'High in fiber, supports heart health.',
        'chilli pepper': 'Boosts metabolism, high in Vitamin C.',
        'corn': 'Rich in fiber, good for digestion.',
        'cucumber': 'Hydrating, helps in weight management.',
        'eggplant': 'Low in calories, supports heart health.',
        'garlic': 'Has antibacterial properties, supports immune system.',
        'ginger': 'Helps with digestion, reduces inflammation.',
        'grapes': 'Rich in antioxidants, supports heart health.',
        'jalepeno': 'Boosts metabolism, high in Vitamin C.',
        'kiwi': 'Rich in Vitamin C, supports immune function.',
        'lemon': 'High in Vitamin C, supports immune system.',
        'lettuce': 'Low in calories, good for hydration.',
        'mango': 'Rich in Vitamin C, supports immune system.',
        'onion': 'Good for heart health, anti-inflammatory.',
        'orange': 'Rich in Vitamin C, supports immune function.',
        'paprika': 'High in Vitamin A, supports vision.',
        'pear': 'Good source of fiber, supports digestion.',
        'peas': 'Rich in protein, supports muscle growth.',
        'pineapple': 'Rich in Vitamin C, helps with digestion.',
        'pomegranate': 'Rich in antioxidants, supports heart health.',
        'potato': 'Good source of carbohydrates, provides energy.',
        'raddish': 'Helps with digestion, good for skin.',
        'soy beans': 'High in protein, supports muscle growth.',
        'spinach': 'Rich in iron, supports healthy blood flow.',
        'sweetcorn': 'Good source of fiber and carbohydrates.',
        'sweetpotato': 'Rich in Vitamin A, supports vision.',
        'tomato': 'High in antioxidants, supports heart health.',
        'turnip': 'Rich in Vitamin C, supports immune system.',
        'watermelon': 'Hydrating, good for skin health.'
    }

season_dict = {
    'apple': 'Fall',
    'banana': 'Year-round',
    'beetroot': 'Spring, Fall',
    'bell pepper': 'Spring, Summer',
    'cabbage': 'Spring, Fall',
    'capsicum': 'Spring, Summer',
    'carrot': 'Spring, Fall',
    'cauliflower': 'Fall',
    'chilli pepper': 'Summer',
    'corn': 'Summer',
    'cucumber': 'Summer',
    'eggplant': 'Summer',
    'garlic': 'Spring',
    'ginger': 'Year-round',
    'grapes': 'Summer, Fall',
    'jalepeno': 'Summer',
    'kiwi': 'Winter, Spring',
    'lemon': 'Year-round',
    'lettuce': 'Spring, Fall',
    'mango': 'Summer',
    'onion': 'Year-round',
    'orange': 'Winter, Spring',
    'paprika': 'Summer',
    'pear': 'Fall',
    'peas': 'Spring',
    'pineapple': 'Year-round',
    'pomegranate': 'Fall',
    'potato': 'Spring, Fall',
    'raddish': 'Spring, Fall',
    'soy beans': 'Summer',
    'spinach': 'Fall, Winter',
    'sweetcorn': 'Summer',
    'sweetpotato': 'Fall',
    'tomato': 'Summer',
    'turnip': 'Fall',
    'watermelon': 'Summer'
}

def get_seasonality(predict):
    if predict in season_dict:
        return season_dict[predict]
    else:
        return "No season data available for this category."

def get_health_benefits(predict):
    if predict in health_benefits_dict:
        return health_benefits_dict[predict]
    else:
        return "No health data available for this category."

def get_top_producers(predict):
    if predict in top_producers:
        return top_producers[predict]
    else:
        return ["No top producers available for this category."]

def get_price(predict):
    if predict in prices:
        return prices[predict]
    else:
        return "No price data available for this category."

def suggest_recipes(predict):
    if predict in recipes:
        return recipes[predict]
    else:
        return ["No recipes available for this category."]

img_height = 180
img_width = 180

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    image = image.resize((img_width, img_height))  
    img_arr = np.array(image)  
    img_bat = np.expand_dims(img_arr, axis=0)  

    model_output = model.predict(img_bat)  
    score = tf.nn.softmax(model_output[0])  
    class_id = np.argmax(score)
    predict = data_cat[class_id]
    confidence = 100 * np.max(score)

    st.write(f"This image is most likely a {predict} with a {confidence:.2f} percent confidence.")

    st.subheader("Top Producers:")
    top_producers_list = get_top_producers(predict)
    for country in top_producers_list:
        st.write(f"- {country}")

    st.subheader("Price Information:")
    price = get_price(predict)
    st.write(price)

    st.subheader("Suggested Recipes:")
    recipes_list = suggest_recipes(predict)
    for recipe in recipes_list:
        st.write(f"- {recipe}")

    st.subheader("Health Benefits:")
    health_benefits = get_health_benefits(predict)
    st.write(health_benefits)

    st.subheader("Seasonality Information:")
    season_info = get_seasonality(predict)
    st.write(f"The season of {predict} is {season_info}.")
