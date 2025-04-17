import math
from fractions import Fraction

def enthtopy_calc(val):
    H = 0
    for num in val:
        H-=num*math.log2(num)
        
    return H

def weighted_average(entropies, weights):
    return sum(prob * enth for prob, enth in zip(weights, entropies))

def main():
    all_entropies = []
    
    print("Welcome to the entropy calculator!")
    print("You can enter space-separated fractions like: 1/2 1/2, or 1/4 1/4 1/2")
    
    while True:
        val = input("\nEnter values for entropy calculation ('q' to quit): ")
   
        if val.strip().lower() == 'q':
                print("Exiting program.")
                break
        else:
            
            try:
                values = val.split(',')
                
                for nums in values:
                    enthtopy = nums.split()
                    enth = []
                    for f in enthtopy:
                        enth.append(float(Fraction(f)))
                    H = enthtopy_calc(enth)
                    print(f"\n Entropy for values {enthtopy} is {H}")
                    all_entropies.append(H)
                
            except Exception as e:
                 print(f"Error: {e}. Please try again with valid input.")
            
            probs = input("\n Please enter the probavilities for each feature or quite (q): ")
            
            if probs.strip().lower() == 'q':
                print("Exiting program.")
                break
            else:
                prob_val = [float(Fraction(f)) for f in probs.split()]
                if len(prob_val) != len(all_entropies):
                    print(f"❌ Error: Number of weights doesn't match number of entropies.")
                    print(f"Entropies: {all_entropies}")
                    print(f"Weights:   {prob_val}")
                else:
                    avg_entropy = weighted_average(all_entropies, prob_val)
                    print(f"✅ Weighted average entropy: {avg_entropy}")
           
    
    
 
    
if __name__ == "__main__":
    main()
    

