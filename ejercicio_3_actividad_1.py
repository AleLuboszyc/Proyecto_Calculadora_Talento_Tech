def sumar(num1, num2):
    try:
        return num1 + num2
    finally:
        print("Operación finalizada.")
          
    
    
     
def restar(num1, num2):
    try:
        return num1 - num2
    finally:
        print("Operación finalizada.")
          
       
    
    

def multiplicar(num1, num2):
    try:
        return num1 * num2  
    finally:
        print("Operación finalizada.")
          
    

def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print(f"Error: División por cero.")
        return None
    except ValueError:
        print("Error: Entrada inválida, no es un número entero.")
        return None
    finally:
        print("Operación finalizada.")


print(sumar(3, 3))
print(restar(10, 3))
print(multiplicar(10, 3))        
print(dividir(10, 0))
