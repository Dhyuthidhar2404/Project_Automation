# Introduction

Machine Learning become everything in our day-to-day life these days. We can see ML models everywhere in this world from nano (medicine) to macro (cars) technologies you can see using machine learning models. There are four types of Machine Learning Models.

## Supervised Learning Models

Supervised Machine learning Models are the models that predict data using labelled data which means the data which is used has a target variable and some extra features which are used to predict that target variable. Imagine you have data of a triangle like base value and height value and you have to find the perimeter of the triangle here base and height are features which are used to find the target and perimeter is the target feature. There are two types of supervised models -:

* Regression

* Classification

### Regression

Regression is a method which tells the relationship between independent and dependent variables using a hyperplane. In the cricket scorecard, you can see the batsman stats where you can how many 1’s and 2’s he took and how many 4s and 6s he smashed based on this data you can find his score. This can be an example of regression taking features like 1’s and 2’s and 4’s and 6’s as features which are used to find the target feature and the target feature is the score of the batsman. One of the best examples of Regression is Linear Regression.

If you are a cricket lover, like my blog😉

### Classification

It is a method of grouping similar objects and separating them into classes. It will learn from the data and classify them into classes(groups). Imagine in New York there is a family where there is a mom and two sons. Those two sons always play with specific toys and whenever they want to play they ask their mom to give them those toys so the mom used to give them every time and every time after they played they used to mess that place. So one day Mom did one thing based on their properties she divided them into groups and took around 4 boxes which were labeled with toy names and placed them in different boxes based on their properties. This process is known as Classification. One of the best examples for classification in ml is the Decision Tree. One of the examples of classification is spam checkers in Gmail.

## Unsupervised Learning Models

In Contrast to Supervised ML, Unsupervised ML models have no labelled data. I think this is not a full-fledged definition. In Unsupervised ML there will be labels for the data but there won't be any target feature in the data to predict. So it will learn the patterns from the data and make them into clusters. Clusters are almost similar to classes which are done in classification but clusters are made using similarities and classes are predefined. I can give the same previous example but instead of labelled boxes there are 4 boxes and the mom labelled them using the pattern she learned from the data. One of the best examples of Unsupervised ML is KMeans.

## Semi-Supervised Learning Models

It is a combination of labelled data and unlabelled data. There is most percentage of unlabelled data and less percentage of labelled data. First, it will use the data and make the unsupervised model from it so that it will get the grouping of data and from these insights, it will make a supervised model and get the predictions from it. One of the best real-time examples for this model is medical diagnosis, we will have the data where known diseases are labelled data which are less in quantity(less known data) and unknown diseases which are unlabelled data that are more in quantity(more known data). This model can help doctors to diagnose the disease accurately.

## Reinforcement Learning Models

Reinforcement learning models are designed to learn from their interactions with an environment. These models aim to maximize a reward signal by taking actions and observing the consequences. One of the fundamental algorithms in reinforcement learning is Q-learning. One of the best real-time examples of this model is self-driving cars like Tesla cars. These cars will learn how to drive safely on the roads using reinforcement learning.

## Conclusion

Machine learning models come in various forms, each suited for different problems. Supervised learning models are trained on labelled data and are used for prediction and classification tasks. Unsupervised learning models find patterns in unlabeled data and are useful for exploratory analysis and clustering. Reinforcement learning models learn from interactions with an environment and are often used in scenarios where trial and error is required. Understanding these different types of machine learning models can help us choose the right approach for solving specific problems and advancing the field of artificial intelligence. You can refer to the documentation of Sckitlearn to learn more about this topic. If you like my writings and want to learn from my blogs wait and watch soon you will get more in-depth explanations on these topics.