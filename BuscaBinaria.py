def busca_binaria(arr, menor, maior, num):
    if maior >= menor:
 
        meio = (maior + menor) // 2
 
        if arr[meio] == num:
            print("Meio")
            return meio
 
        elif arr[meio] > num:
            print("Lado Esquerdo ")
            return busca_binaria(arr, menor, meio - 1, num)

        else:
            print("Lado direito")
            return busca_binaria(arr, meio + 1, maior, num)
 
    else:
        return -1
 
# Teste
arr = [ 5, 62, 71, 95, 103 ]
num = 103
 
resultado = busca_binaria(arr, 0, len(arr)-1, num)
 
if resultado != -1:
    print(f"O Elemento está na posição {resultado}")
else:
    print("O Elemento não está presente")
