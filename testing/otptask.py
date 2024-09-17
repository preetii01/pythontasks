#TASK- random OTP generator
import random,math

def generateotp():
    dig="0123456789"
    OTP=""
    
    for i in range(6):
        OTP+=dig[math.floor(random.random() * 10)]
    return OTP

if __name__ == "__main__" :
     
    print("OTP of 6 digits:", generateotp())