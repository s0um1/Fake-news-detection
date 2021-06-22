# FakeNewsBot
Detects fake news from text, from the text of images and also identifies morphed images.

Natural language processing techniques and machine learning algorithms are used to classifty fake news using python libraries. 

#### Dataset used
The data source used for this project is LIAR dataset in tsv format. The dataset used for this project were in csv format named train.csv, test.csv and valid.csv.

### File descriptions

#### Processing.py
This file contains all the pre processing functions needed to process all input documents and texts. The train, test and validation data files are read first followed by data pre processing like tokenizing, stemming, checking null or missing values etc.

#### Selecting.py
Feature selection and extraction are performed using methods from sci-kit learn python libraries like simple bag-of-words, n-grams etc and term frequency like tf-tdf weighting is also determined.

#### Classifier.py
The extracted features are fed into different classfiers like Naive-bayes, Logistic Regression, Linear SVM, Stochastic gradient decent and Random forest classifiers from sklearn. Once fitting the model, the f1 score is compared and the confusion matrix is checked. After fitting all the classifiers, the two best peforming models are selected as candidate models for fake news classification. Parameter tuning is also done by implementing GridSearchCV methos on these candidate models to chose best performing paramters for these classifier. Finally, the selected model is used for fake news detection with the probability of truth. 

#### Prediction.py
Our finally selected and best performnig classifer was ```Logistic Regression``` which was then saved on disk with name ```final_model.sav```. This model will be used by prediction.py file to classify the fake news. It takes a news statement or an image as input from user and displays the final classification output.
