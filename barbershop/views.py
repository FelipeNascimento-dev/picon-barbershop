from django.shortcuts import render

def index(request):
    return render(request, 'global/base.html')

barbeiros = {
    "vinicius": {
        "nome": "Vinicius Marins",
        "foto": "/static/global/images/logo2.png",
        "descricao": "Me chamo Vinicius, sou barbeiro e tenho paixão pelo que faço. Me considero dedicado, responsável e sempre busco oferecer o melhor atendimento e resultado para cada cliente. Valorizo o respeito, e o atendimento e estou sempre em busca de evolução, tanto na vida pessoal quanto profissional."
    },

    "theo": {
        "nome": "Theo",
        "foto": "/static/global/images/logo2.png",
        "descricao": """Eu sou o Théo, um barbeiro de 25 anos, natural de Minas Gerais que reside há 20 anos em São Paulo, na zona leste.

    Sou apaixonado pela minha família, pela vida e pela Barbearia. Sonhador e comprometido em servir a quem precisa 
    e transformar visuais e vidas que sentam na minha cadeira.

    Sou especializado em cortes na tesoura, fade e cortes inovadores, barboterapia, nanopigmentação em barba 
    e também estou entrando no ramo de trancista.

    Meu foco é voltado 100% ao bem-estar, oferecendo um atendimento que combine qualidade e atenção personalizada.

    Acredito que cada cliente merece um espaço acolhedor e um atendimento humanizado. 
    É um compromisso real atender às suas expectativas.

    Estou aqui para ajudar você a se sentir confiante, mostrar autoridade e se sentir satisfeito com seu novo visual e sua identidade.

    Estamos juntos para encontrar o estilo que melhor reflete quem você é!

    Meu lema é: SERVIR PARA SER SERVIDO!"""
    },

    "eduarda": {
        "nome": "Eduarda",
        "foto": "/static/global/images/logo2.png",
        "descricao": "Cortes criativos e atendimento de excelência."
    },
    "wendel": {
        "nome": "Wendel",
        "foto": "/static/global/images/logo2.png",
        "descricao": "Me chamo Wendel, mais conhecido como negão. Tenho 20 anos e trabalho com a barbearia faz 5 anos, procuro sempre atender todas necessidades do cliente, desde o que ele precisa, ate o que ele deseja, sempre gostei muito do ramo, levo a serio e faço com muita paixão. Agende sua experiência comigo!"
    },
    "ste": {
        "nome": "Ste",
        "foto": "/static/global/images/logo2.png",
        "descricao": "Sou especialista em tranças afro. Trabalho com oque eu amo há 4 anos. Adoro criar artes do zero e personalizadas com as suas características. Meu objetivo é fazer com que você se sinta confiante e lindo/a com suas tranças."
    }
}

def detalhe_barbeiro(request, nome):
    barbeiro = barbeiros.get(nome)
    if not barbeiro:
        return render(request, 'barbershop/404.html', status=404)
    return render(request, 'barbershop/detalhe_barbeiro.html', {'barbeiro': barbeiro})