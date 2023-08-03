import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
# import tensorflow
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error , mean_squared_error , r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# print(df['day'])
# stores = pd.read_csv('train.csv')

def linear_reg(stores):
    stores = stores.drop(['store','item'], axis=1)

    stores['date'] = pd.to_datetime(stores['date'])

    # Converting date to month period
    stores['date'] = stores['date'].dt.to_period('M')
    monthlySales = stores.groupby('date').sum().reset_index()

    monthlySales['date'] = monthlySales['date'].dt.to_timestamp()
    monthlySales['sales_diff'] = monthlySales['sales'].diff()
    monthlySales = monthlySales.dropna()
    monthlySales.head(10)

    supervised_data = monthlySales.drop(['date','sales'], axis=1)

    # Preparing The Supervised data
    for i in range(1,13):
        col_name= 'month'+ str(i)
        supervised_data[col_name] = supervised_data['sales_diff'].shift(i)

    supervised_data = supervised_data.dropna().reset_index(drop=True)
    supervised_data.head(10)

    train_data = supervised_data[:-12]
    test_data = supervised_data[-12:]
    print("Train Data shape:",train_data.shape)
    print("Test Data Shape:",test_data.shape)


    scaler = MinMaxScaler(feature_range=(-1,1))
    scaler.fit(train_data)
    train_data = scaler.transform(train_data)
    test_data = scaler.transform(test_data)

    x_train, y_train = train_data[:,1:], train_data[:,0:1]
    x_test, y_test = test_data[:,1:], test_data[:,0:1]
    y_train = y_train.ravel()
    y_test = y_test.ravel()
    print("x_train Shape:", x_train.shape)
    print("y_train Shape:", y_train.shape)
    print("x_test Shape:", x_test.shape)
    print("y_test Shape:", y_test.shape)

    #Make Prediction dataframe  to merge the predicted sales prices of all trained algorithms

    sales_dates = monthlySales['date'][-12:].reset_index(drop=True)
    predict_df = pd.DataFrame(sales_dates)

    act_sales = monthlySales['sales'][-13:].to_list()
    # Linear Regression model and Predicted output

    model = LinearRegression()
    model.fit(x_train,y_train)
    lr_pre = model.predict(x_test)

    lr_pre = lr_pre.reshape(-1,1)
    lr_pre_test_set = np.concatenate([lr_pre,x_test], axis=1)
    lr_pre_test_set = scaler.inverse_transform(lr_pre_test_set)

    result_list=[]
    for index in range(0, len(lr_pre_test_set)):
        result_list.append(lr_pre_test_set[index][0] + act_sales[index])
    lr_pre_series = pd.Series(result_list, name="Linear Prediction")
    predict_df = predict_df.merge(lr_pre_series, left_index= True, right_index= True)

    lr_mse = np.sqrt(mean_squared_error(predict_df['Linear Prediction'], monthlySales['sales'][-12:]))
    lr_mae = mean_absolute_error(predict_df['Linear Prediction'], monthlySales['sales'][-12:])
    lr_r2 = r2_score = (predict_df['Linear Prediction'], monthlySales['sales'][-12:])

    plt.figure(figsize=(15,5))
    #Actual sales
    plt.plot(monthlySales['date'],monthlySales['sales'])
    #predicted sales
    plt.plot(predict_df['date'],predict_df['Linear Prediction'])
    plt.title("Customer sales forecast using LR Model")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend(['Actual Sales','Predicted Sales'])
    # plt.show()

    plt.savefig('D:/Kaar/December/Digi/SalesForescastApplication/sfa-app/src/assets/images/plot.jpg')
    plt.show()
# linear_reg(stores)