##Написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для лотерей.

import random
def get_numbers_ticket(min: int, max:int, quantity:int):    
    if min >=1 and max <= 1000 and quantity >= min and quantity <= max:
        list_of_numbers = range(min, max)        
        numbers = random.sample(list_of_numbers, quantity)
        numbers.sort()
        return numbers         
  
    else:
        numbers = []
        return numbers      
    


