


#**Satellite Collision Prediction Using Linear Regression**


#**Project Overview**  
This project aims to predict the probability of satellite collisions using key features like distance, velocity, and other orbital parameters. It leverages linear regression for its simplicity, computational efficiency, and interpretability, ensuring accurate predictions to minimize collision risks and optimize space operations.


## **Features**  
1. **Collision Risk Prediction**: Predicts the probability of collision based on input parameters.  
2. **Feature Importance**: Provides insights into the impact of features like distance and velocity on collision risk.  
3. **Assumption Validation**: Ensures linear regression assumptions (linearity, independence, homoscedasticity, normality) are met.  
4. **Performance Metrics**: Evaluates model accuracy using R², MSE, and residual analysis.  


## **Technologies Used**  
- **Programming Language**: Python  
- **Libraries**:  
  - NumPy and pandas for data manipulation  
  - Scikit-learn for regression modeling  
  - Matplotlib and Seaborn for data visualization  
  - Plotly for interactive timestamp analysis  


## **Dataset**  
- **Columns**:  
  - `Timestamp`: Time of the event  
  - `Distance`: Distance between objects  
  - `Velocity`: Relative velocity of objects  
  - `Collision_Probability`: Target variable  

## **Usage**  
1. Prepare your dataset in the specified format (CSV).  
2. Run the script to train the model:  
   ```bash  
   python train_model.py  
   ```  
3. Visualize predictions and feature importance using the provided notebooks or scripts.  

## **Key Results**  
 
- Identified critical features impacting collision probability.  
- Validated assumptions, ensuring robust model performance.  

## **Acknowledgments**  
Special thanks to my mentor Ms Ritham Sharma and my tema mates
Avni Gupta
Kavin
Supreeti Pattnaik
Sai Haritha
