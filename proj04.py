##########################################################################
#    Computer Project #4
#    Algorithm
#        Prompt to enter choice.
#        4 functions defined.
#        Main function to interact with user.
#        Calls function and returns value based on user input.
##########################################################################

DELTA = 10**-7  #used for the zeta function

def int_to_base13(n):
    """
    Converts parameter n to a base 13 number.
    Value: int (base 10)
    Returns: String.
    """
    ans = ""    #Empty string
    while True:    #Conversions.
        rem = n % 13
        if rem == 10:
            ans += "A"
        elif rem == 11:
            ans += "B"
        elif rem == 12:
            ans += "C"
        else:
            ans += str(rem)
        n = n // 13
        if n == 0:
            break

    ans = ans[::-1]    #Reversing string
    return ans

def tridecimal_expansion(n_str):
    """
    Converts base 13 value to a trideciaml value.
    Value: String which is base 13 value.
    Returns: String which is tridecimal value.
    """
    n_str = n_str.replace("A", "+")    #Conversions.
    n_str = n_str.replace("B", "-")
    n_str = n_str.replace("C", ".")
    return n_str
        
def tridecimal_to_conway(n_str):
    """
    Converts tridecimal value to a Conway float.
    Value: String which is tridecimal value.
    Returns: Float which is Conway FLoat.
    """
    #Loop to check if Conway float exists or not. 
    for i,ch in enumerate(n_str):
        if ch == "+" or ch == "-":
            try:
                int(n_str[i+1:])
                return 0
                break
            except ValueError:
                try:
                    float(n_str[i+1:])
                    return float(n_str[i+1:])
                    break
                except ValueError:
                    continue
        elif n_str[-1] == "+" or n_str == "-":
            return 0

    #If there are no "+" or "-" in the parameter.
    else:
        if "+" not in n_str or "-" not in n_str:
            try:
                int(n_str)
                return 0
            except ValueError:
                try:
                    float(n_str)
                    return float(n_str)
                except ValueError:
                    return 0 

def zeta(n):
    """
    Calculates the Zeta function for the parameter.
    Value: Float.
    Returns: Float which is Zeta value.
    """
    n = float(n)
    #n must be positive integer.
    if n <= 0:
        return None
    i = 1    #Value to be looped.
    ans = 0    #Stores answer.
    temp = 2    #Stores temporary value for each loop iteration.
    #Loop calculates zeta value.
    while (temp - (1/i**n)) > DELTA:
        temp = (1/i**n)
        ans += temp
        i += 1
    return ans

def main():
    # by convention "main" doesn't need a docstring

    print("Functions")
    prompt =input("Enter Z for Zeta, C for Conway, Q to quit: ")

    #Error message because input is invald.
    while prompt.lower() not in 'zcq':
        print("Error in input. Please try again.")
        prompt=input("Enter Z for Zeta, C for Conway, Q to quit: ")
    
    #loop for zeta and conway functions.
    while prompt.lower() in 'zc': 
        if prompt.lower()=='z':
            print('Zeta')
            
            #Function to check if string is a float.
            def float_check(b):
                try:
                    float(b)
                    return True
                
                except ValueError:
                    return False
            h=str(input('Input a number: '))
            while float_check(h)==False:
                print("Error in input.  Please try again.")
                h=str(input('Input a number: '))
            else:
                print(zeta(h))
        elif prompt.lower()=='c':
            print('Conway')
            q=input('Input a positive integer: ')
            while q.isdigit()==False:
                print("Error in input.  Please try again.")
                q=input('Input a positive integer: ')
            else:
                q = int(q)
                y=int_to_base13(q)
                print('Base 13: ',y)
                z=tridecimal_expansion(y)
                print('Tridecimal: ',z)
                w=tridecimal_to_conway(z)
                print('Conway float:',w)
        prompt=input("Enter Z for Zeta, C for Conway, Q to quit: ")

    #If choice is "q" which quits the program.            
    else: 
        if prompt.lower()=='q':
            print("\nThank you for playing.")    
        
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()
        
    
