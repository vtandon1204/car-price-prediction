# 🚗 Car Price Prediction   

A machine learning project that predicts the price of cars based on various features like brand, year, mileage, fuel type, and more. This model helps users make informed decisions while buying or selling cars.  

---

## 📝 Project Overview  

This project leverages **Machine Learning** techniques to predict car prices. By analyzing historical data and key attributes, the model ensures high accuracy and practicality in the automotive marketplace.  

---

## ⚙️ Features  

- **Interactive Model**: Predict car prices based on user inputs.  
- **Feature Analysis**: Understand which factors influence car prices the most.  
- **Visualization**: Comprehensive charts and graphs for data insights.  

---

## 🔧 Tech Stack  

- **Programming Language**: Python  
- **Libraries**:  
  - Pandas  
  - NumPy  
  - Matplotlib  
  - Seaborn  
  - Scikit-learn
  - Streamlit 


---

## 📊 Exploratory Data Analysis  

Key findings from the data analysis include:  
1. **Brand and Age** are significant predictors of car price.  
2. **Mileage** inversely affects the car price.  
3. **Fuel Type** and **Transmission** impact pricing trends.  

---

## 🚀 How to Use  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/vtandon1204/car-price-prediction.git  
   cd car-price-prediction 

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Downlaod the dataset:
    ```bash
    pip install kaggle
    kaggle datasets download -d austinreese/craigslist-carstrucks-data

4. Extract the CSV file from the zip folder and store it in a folder named 'data'.

5. Run the application:
   ```bash
   streamlit run app.py
   
6. Access the app at http://localhost:8501.

---

## 📈 Model Performance
- **Model Used**: Random Forest Regressor
- **Evaluation Metrics**:
    - R² Score: 0.85
    - MAE: 2640 (approx.)
- **Comparison of Model Performance Metrics**
  ![Model Performance Metrics](Comparison_Model_Performace_Metrics.jpg)
- **Model Performance Graph**
  ![Model Performance Graph](Overall-Performance.jpg)
  

## 🛠️ Future Improvements
- Integration with live car price databases.
- Deployment as a fully functional web application.
- Addition of more advanced ML algorithms like Gradient Boosting.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and create a pull request.

## 📄 License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## 🙌 Acknowledgements
- Dataset: [Craigslist Cars and Trucks Data](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data)
- Special thanks to the open-source community.

