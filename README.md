# California Housing Price Prediction
A full-stack machine learning project predicting California housing prices using XGBoost, deployed with FastAPI and a Streamlit frontend. Includes data preprocessing pipelines, model evaluation, API with JWT authentication, and Dockerized deployment.
 
# 🔍 Project Overview
The project uses the California Housing dataset to predict median house values based on features such as:
•	Longitude & Latitude
•	Housing Median Age
•	Total Bedrooms
•	Median Income
•	Ocean Proximity

Key components:
1.	Data preprocessing:
o	Handling missing values (total_bedrooms) using imputation.
o	Scaling & encoding (OneHotEncoder for categorical features).
o	Managing negative longitude values without special transformation.
2.	Modeling:
o	XGBoost Regressor with standard and hyperparameter-tuned versions (RandomizedSearchCV).
o	Evaluation metrics: RMSE (Root Mean Squared Error)
Dataset	RMSE
Validation	49,768.54
Test (Default XGBoost)	47,761.38
Test (Random Search)	47,416.80
3.	API:
o	Built with FastAPI.
o	JWT authentication for secure predictions.
o	Endpoint /predict receives JSON input and returns predicted house value.
o	Predictions are stored in a PostgreSQL/SQLite database using SQLAlchemy ORM.
4.	Frontend:
o	Streamlit app for user-friendly interaction.
o	Users can login, enter feature values, and get predictions in real-time.
o	Two-column layout for input features for better UX.
5.	Deployment:
o	Dockerized with Dockerfile and docker-compose.
o	Services: FastAPI (port 8000) and Streamlit (port 8501).
o	Volumes enable live code changes during development.
 
# 🛠️ Installation & Setup

## Clone the repository
git clone https://github.com/maryamkhosravii/housing-prediction.git
cd housing-prediction

## Install dependencies
pip install -r requirements.txt

## Run FastAPI
uvicorn main:app --reload

## Run Streamlit
streamlit run app.py

## OR Docker (recommended)
docker-compose build
docker-compose up
•	FastAPI → http://localhost:8000
•	Streamlit → http://localhost:8501
 
# 🧪 Usage
1️⃣ Login
•	Use credentials: 
•	username: admin
•	password: 1234
•	Retrieve JWT token via /token endpoint or Streamlit sidebar.
2️⃣  Enter Features
•	Fill all input fields in Streamlit (longitude, latitude, total_bedrooms, etc.)
3️⃣  Get Prediction
•	Click Predict → receive median house value prediction.
 
# 🛠️ Technologies Used
•	Python 3.11
•	XGBoost, scikit-learn, pandas
•	FastAPI with JWT authentication
•	SQLAlchemy ORM for database operations
•	Streamlit for interactive UI
•	Docker & Docker Compose for containerized deployment
 
# 🔒 Security
•	JWT token-based authentication for /predict endpoint
•	Password stored as plain text for demonstration (can be replaced with hashed credentials in production)
 
# 💡 Features & Best Practices
•	Fully reproducible ML pipeline
•	Clean, modular code structure: 
o	main.py → FastAPI endpoints
o	predict.py → Model loading & prediction
o	crud.py → Database operations
o	auth_security.py → JWT authentication
o	schemas.py → Pydantic models for request/response validation
•	Streamlit frontend for easy testing & deployment
•	Dockerized for cross-platform compatibility
 
# 🚀 Next Steps / Improvements
•	Replace SQLite with PostgreSQL for production
•	Implement hashed password storage
•	Add feature importance visualization in Streamlit
•	Deploy on cloud (AWS/GCP/Heroku)

# Contact
Email: mrm.khosravi@yahoo.com
Project Link: https://github.com/maryamkhosravii/housing-prediction

Made with ❤️ by Maryam Khosravi


