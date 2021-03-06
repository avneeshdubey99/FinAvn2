Forecasting Factors

A forecasting methodology is only as good as the factors chosen as predictors. 
There are a staggering number of potential factors to choose from when forecasting stock market index returns. 

In this project we are going to restrict the factors to time lags of the current percentage returns. 
This is not because they are the best predictors, rather it is because it is straightforward to demonstrate the process of forecasting on an easily obtained dataset.
Forecasting factor choice is extremely important, if not the most important, component of the forecaster. 

Even simple machine learning techniques will produce good results on well-chosen factors. Note that the converse is not often the case. 
"Throwing an algorithm at a problem" will usually lead to poor forecasting accuracy.
For this forecaster specifically, I have chosen the first and second time lags of the percentage returns as the predictors for the current stock market direction. This is a relatively arbitrary choice and there is plenty of scope for modification, for instance by adding in additional lags or the volume of shares traded. It is generally better to have fewer predictors in a model, although there are statistical tests available which can demonstrate the predictive capability of each factor.


Forecasting S&P500 with Logistic Regression, LDA and QDA

The S&P500 is a weighted index of the 500 largest publicly traded companies (by market capitalisation) in the US stock market. 
It is often considered an equities "benchmark". Many derivative products exist in order to allow speculation or hedging on the index. 
In particular, the S&P500 E-Mini Index Futures Contract is an extremely liquid means of trading the index.
In this section we are going to use three classifiers to predict the direction of the closing price at day N based solely on price information known at day N−1. 
An upward directional move means that the closing price at N is higher than the price at N−1, while a downward move implies a closing price at N lower than at N−1.
If we can determine the direction of movement in a manner that significantly exceeds a 50% hit rate, with low error and a good statistical significance, then we are on the road to forming a basic systematic trading strategy based on our forecasts. 
At this stage we're not concerned with the most up to date machine learning classification algorithms. Right now we're just introducing concepts and so we'll begin the discussion on forecasting with some elementary methods.

1. Logistic Regression

The first technique we will consider is logistic regression (LR). In our case we are going to use LR to measures the relationship between a binary categorical dependent variable ("Up" or "Down") and multiple independent continuous variables (the lagged percentage returns). The model provides the probability that a particular (following) day will be categorised as "Up" or "Down". In this implementation we have chosen to assign each day as "Up" if the probability exceeds 0.5. We could make use of a different threshold, but for simplicity I have chosen 0.5.
LR uses the logistic formula to model the probability of obtaining an "Up" day (Y=U) based on the lag factors (L1, L2):
p(Y=U|L1,L2)=eβ0+β1L1+β2L21+eβ0+β1L1+β2L2
The logistic function is used because it provides a probability between [0,1] for all values of L1 and L2, unlike linear regression where negative probabilities can be generated in the same setting.
To fit the model (i.e. estimate the βi coefficients) the maximum likelihood method is used. Fortunately for us, the implementation of the fitting and prediction of the LR model is handled by the scikit-learn library.

2. Linear Discriminant Analysis

The next technique used is Linear Discriminant Analysis (LDA). LDA differs from LR in because in LR we model P(Y=U|L1,L2) as a conditional distribution of the response Y given the predictors Li, using a logistic function. In LDA the distribution of the Li variables are modelled separately, given Y, and P(Y=U|L1,L2) is obtained via Bayes' Theorem.
Essentially, LDA results from assuming that predictors are drawn from a multivariate Gaussian distribution. After calculting estimates for the parameters of this distribution, the parameters can be input into Bayes' Theorem in order to make predictions about which class an observation belongs to.
LDA assumes that all classes share the same covariance matrix.
I won't dwell on the formulae for estimating the distribution or posterior probabilities that are needed to make predictions, as once again scikit-learn handles this for us.

3. Quadratic Discriminant Analysis

Quadratic Discriminant Analysis (QDA) is closely related to LDA. The significant difference is that each class can now possess its own covariance matrix.
QDA generally performs better when the decision boundaries are non-linear. LDA generally performs better when there are fewer training observations (i.e. when needing to reduce variance). QDA, on the other hand, performs well when the training set is large (i.e. variance is of less concern). The use of one or the other ultimately comes down to the bias-variance trade-off.
As with LR and LDA, scikit-learn takes care of the QDA implementation so we only need to provide it with training/test data for parameter estimation and prediction.

