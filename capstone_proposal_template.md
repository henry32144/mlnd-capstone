# Machine Learning Engineer Nanodegree
## Capstone Proposal
CHENG HAN WU
January 7, 2018

## Stock Pirce Indicator Proposal

### Domain Background

In investment and trading, the buy and sell decision have been made by human. But there are lots of factors that influence human and cause loss. So how about machine? there are wealth of information is available in the form of stock prices and company performance, so it is suitable for machine learning.

Investment firms, hedge funds and even individuals have been using financial models to better understand market behavior and models can provide some predicts for trader reference.

### Problem Statement

Our problem is that trading decisions made by human is not always reasonable, such as me. So, I want try to use machine learning to train a model which can give the predicted stock price value in some days range, and see it can help trader to make better decision or not.

### Datasets and Inputs

I decided to get data from [Yahoo finance](https://hk.finance.yahoo.com/), it provide historical data that can be download as csv, I choose **TWII(Taiwan Stock Exchange)** which is similar to **NASDAQ**, we can know whether the market was opened or closed by **TWII**. And **TSMC(Taiwan Semiconductor Manufacturing Company)** which is the weighted stock in Taiwan stock market, so it has high liquidity and it's not easily affected by single major institutional investors.

The historical data fetch from Yahoo finance has seven columns, **Date,Open,High,Low,Close,Adjusted Close and Volume**, I would take them and use Adjusted Close instead of Close as input, the difference between Adjusted Close and Close described [here](https://budgeting.thenest.com/adjusted-closing-price-vs-closing-price-32457.html). 

The data date range I choose is from 2000/01/04 to 2017/12/29, there are some null values because stock market is close in these days, and I would preprocess the data before training.  

### Solution Statement

Because the output is linear, so I would like to choose some supervised regression algorithms, such as **Linear Regression, Logistic Regression, SVM, RVM** and a model that bagging them together.  I would try them separately and choose the one which performance the best.

The model take input which include the original data(from Yahoo finance) and some calculated indicators, like [Moving Average](https://en.wikipedia.org/wiki/Moving_average) and [Bollinger Bands](https://en.wikipedia.org/wiki/Bollinger_Bands), the way to get them would be described in **Project Design** part. The model would return the forecast stock Adj Close value in the chosen day range(7 days for example).

### Benchmark Model

I would choose the regression algorithm has the best performance from above, and take only original data, not include Moving Average and Bollinger Bands. By doing so, could compare which one is better, the evaluation metric would be describe below.

### Evaluation Metrics

I supposed to use RMSE as the evaluation metrice, RMSE(root-mean-square error) is a popular evaluation metric used in regression problem. RMSE is the square root of the average of squared errors, the formula is:

<img src="http://latex.codecogs.com/gif.latex?\sqrt{\frac{\sum_{i=1}^{n}&space;(Predicted&space;-&space;Actual)^{2}}{N}}" title="\sqrt{\frac{\sum_{i=1}^{n} (Predicted - Actual)^{2}}{N}}" />

And the lower RMSE value represent the predicted value has less error, which means the value predicted by the model is accuracy, so when we apply this evaluation metric to both our solution model and benchmark model, we choose the one have lower RMSE value and say that one is better. 

### Project Design

In my opinion, this project can be seperated into three parts. Data, Model and User Interface.

**Data part**

The data fetch from Yahoo Finance has seven columns, **Date, Open, High, Low, Close, Adjusted Close and Volume**, as mentioned above, we choosed Adjust Close as our target value, so we would not use Close. We want to forecast it by input **Open , High, Low, Volume, Moving Average and Bollinger Bands**, there are some different time series in **Moving Average** like 5days, 20days ...etc, I supposed to use 5days and 10days because I think that there are too many factorsto affect the stock price, so the technical analysis is hard to have accuracy result in predicting the price in far future. And below are formulas of Moving Average and Bollinger Bands.

<img src="http://latex.codecogs.com/gif.latex?\frac{\sum_{i&space;=&space;1}^{n}&space;pi}{n}" title="\frac{\sum_{i = 1}^{n} pi}{n}" />

**n** is the time series, we choose 5days and 10days in the project, so **n** is 5 and 10. **p** is the close price, we use **Adj Close** in this project.

<img src="http://latex.codecogs.com/gif.latex?nMA&space;\pm&space;2*(n\sigma&space;)" title="nMA \pm 2*(n\sigma )" />

**n** is the same as the time series of **Moving Average**. For example, if we choose 5MA, the **Bollinger Bands** are **5MA +- 2 * the Standard Deviation of close price in 5 days**.

There are some null values in the data, so we should preprocess them before using them to train the model, by using fillna function in [pandas](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html), we can easily replace null values to the price of previous trading day and throw the null value out in training, because the price in the days that the market close would not change, so we can simply not use it.

**Model part**

In the project, we want to build a model that can forecast the Adjusted Close price in the chosen days after, like predict the Adjusted Close price 7 days later. And we first take these features to train, **Open, High, Low, Volume, 5MA, 10MA, Bollinger Bands in 5MA**, and by using the feature importance function, we can discover which feature is important and then modify our training feature. 

Also the data need to be normalize before train, there are two different normalize types in these features. The price part, such as **Open, High, Low, 5MA, 10MA, Bollinger Bands**, these feature would be divided by the Adjusted Close price in the first day we choosed. The Volume value is usually about tens of billion, so we could divide them by one hundred billion, so the Volume value after normalize would be in range of 0 to 1.

And we try these algorithms, **Linear Regression, Logistic Regression, SVM, RVM** and Ensemble Learner combine them together, after adjust and test them, we compare the performance of these algorithms and pick up the best one.

**UI part**

I suppose to use web page as the platform of this project. For this project, we need to have a user interface to accept inputs and display the result to user, so we need a front end page. And also a backend script to put the input to the model and return the output result back to user.

- FrontEnd: Html web page

have a component to accept user input features, and a display area to show the forecast price.

- BackEnd: Python Flask

to deal with input and pass the input which has been processed to the model, return the result to front end from the model.


-----------

**Before submitting your proposal, ask yourself. . .**

- Does the proposal you have written follow a well-organized structure similar to that of the project template?
- Is each section (particularly **Solution Statement** and **Project Design**) written in a clear, concise and specific fashion? Are there any ambiguous terms or phrases that need clarification?
- Would the intended audience of your project be able to understand your proposal?
- Have you properly proofread your proposal to assure there are minimal grammatical and spelling mistakes?
- Are all the resources used for this project correctly cited and referenced?
