from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def index(request):
    dados_usuarios =[
        {'Nome': 'Fulano', 'Matrícula': '202311181110001', 'Idade': '17', 'Cidade': 'São Paulo do Potengi'},
        {'Nome': 'Cicrano', 'Matrícula': '202311181110001', 'Idade': '17', 'Cidade': 'Santa Maria'},
        {'Nome': 'Bruce', 'Matrícula': '202311181110001', 'Idade': '18', 'Cidade': 'Gotham'},
        {'Nome': 'Beltrano', 'Matrícula': '202311181110001', 'Idade': '18', 'Cidade': 'Pau dos ferros'},
        {'Nome': 'Véyr', 'Matrícula': '202311181110001', 'Idade': '17', 'Cidade': 'Elói de Souza'},
        ]
    return render(request, "usuarios.html", dados_usuarios)