# main.py ou app.py

# Opção 1: Importar o módulo completo
import fibonacci

print("Usando o módulo fibonacci_module:")
num = 12
print(f"O {num}-ésimo número de Fibonacci (iterativo) é: {fibonacci_module.fibonacci_iterativo(num)}")
print(f"O {num}-ésimo número de Fibonacci (recursivo) é: {fibonacci_module.fibonacci_recursivo(num)}")

print("\n" + "="*30 + "\n")

# Opção 2: Importar funções específicas
# from fibonacci_module import fibonacci_iterativo
#
# print("Usando apenas fibonacci_iterativo do módulo:")
# outro_num = 7
# print(f"O {outro_num}-ésimo número de Fibonacci (iterativo) é: {fibonacci_iterativo(outro_num)}")

# Se você tentar usar fibonacci_recursivo sem importá-lo especificamente:
# print(f"O {outro_num}-ésimo número de Fibonacci (recursivo) é: {fibonacci_recursivo(outro_num)}")
# Isso geraria um NameError