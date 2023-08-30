from django.shortcuts import render

def mi_vista(request, valor1, valor2):
    resultado = int(valor1) + int(valor2)
    return render(request, 'sumar/sumar.html', {'valor1': valor1, 'valor2': valor2, 'resultado': resultado})


