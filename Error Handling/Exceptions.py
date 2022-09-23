
#float("124.4") -> 123.4
#float("N/A") -> error

keyWord = "Hello"


try:
    print(int(keyWord))
    #raise ValueError
    #raise NameError("Error1")
#except Exception as e:
 #   print("Got a ValueError")
 
#except ValueError:
    #print("Error Value")
except:
    print("Other Excpetion")
    
    #raise

finally:
    print("finally")

print("Past Exception")
