import pickle
import fakeTextInImage

"""
# Menu
print('Choose:\n
         1. Text\n
         2. Text in Image\n')
choice = int(input("Enter your choice: "))
if choice == 1:
    var = input("Please enter the news text you want to verify: ")
    print("You entered: " + str(var))
elif choice == 2:
    var = fakeTextInImage.imToString()
"""

# Function to run for prediction


def detecting_fake_news(var):
    # Retrieving the best model for prediction call
    load_model = pickle.load(open('final_model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    # return (print("The given statement is ", prediction[0]),
    #        print("The truth probability score is ", prob[0][1]))

    return (prediction[0], prob[0][1])


if __name__ == '__main__':
    detecting_fake_news(var)
