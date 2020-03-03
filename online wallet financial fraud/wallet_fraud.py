import testing, wallet_no_wallet, ModeOfContact , MoneyStatus
import pickle
import json
import random
import time

class PredictionTree(object):
    def welcome(self):
        WELCOME_INTENT = ["Hello! I am CyberEye. How may I help you?\n",
                          "Hi! I am CyberEye. How may I help you?\n",
                          "Hey! I am CyberEye. How may I help you?\n"]
        print(random.choice(WELCOME_INTENT))
        pc = PredictionTree()
        return pc.predict_crime(input())
     ##this is aboyt Wallet or no wallet , this is done 
    def predict_crime(self, query):
        #load model
        loaded_model = pickle.load(open(testing.filename, 'rb'))
        matrix = [0,0,0]
        # target_names = ['lottery', 'no_crime']
        # print("accuracy score: " + str(loaded_model.score(testing.X_test, testing.y_test)))
        tag = testing.model.predict([query])
        print(tag)
        print(matrix)
        moc = PredictionTree()
        return moc.mode_of_contact()
    ##Here , it is about UPI Fraud or No UPI
    def mode_of_contact(self):
        print("Okay, Did you approve a request from any unverified/unidentified user or you shared your UPI Pin with anyone ?\n")
        query = input()
        loaded_model = pickle.load(open(ModeOfContact.filename, 'rb'))
        mode = ModeOfContact.model.predict([query])
        print(mode)
        ms = PredictionTree()
        if mode == "upi_fraud" :
          print("You've been a victim of E wallet fraud")## call the response function which gives the information here
        else:
          return ms.money_status()

    def money_status(self):
        print("Did you share any OTP for UPI Transaction?\n")
        query = input()
        loaded_model = pickle.load(open(MoneyStatus.filename, 'rb'))
        money = MoneyStatus.model.predict([query])
        time.sleep(2.0)
        if money == "yes" :
          print("You have been a victim of UPI Fraud")## call the response function which gives the information here
          time.sleep(1.0)
          print
        else:
            print("You are a probable victim of UPI Fraud")## call the response function which gives the information here
        

## create an instance of the class PredictionTree()
pt = PredictionTree()
print(pt.welcome())
