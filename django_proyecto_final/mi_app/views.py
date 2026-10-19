from django.shortcuts import render

def inicio(request):
    contexto = {
        'titulo': 'Demostración Inicial Django',
        'mensaje': 'Ingeniero Guevara, ¡no nos ponga cero!',
        'integrantes': [
            'THYRONE GOYES',
            'CARLOS CALDERON',
            'TYRON BAYAS'
        ]
    }
    return render(request, 'mi_app/inicio.html', contexto)