# dio-carrefour-techchallenge

Tech Challenge da Digital Innovation One e do Banco Carrefour

Requisitos:

	Otimizar a comunicação entre clientes e Banco Carrefour
	Utilizar .NET ou Python
	Utilizar Angular (opcional), caso tenha front-end
	Utilizar a API do Telegram

Esse é um projeto simples, em Python, para um Telegram-Bot.

Sei que é meio óbvio mas, para rodar, é preciso ter instalados o Python, o Flask e a API-Telegram-Bot.

Como não estou conseguindo rodar o Bot a partir da app do Flask, tive que criar dois arquivos, que precisam ser inicializados separadamente. Como só conheci o Flask nessa semana, estou estudando para integrar tudo em um único 'run'.

O arquivo mainflaskapp.py faz a chamada para uma webpage-cover do Banco Carrefour (https://www.carrefoursolucoes.com.br), com um único link que faz a chamada para o Bot.
Caso possua o Telegram instalado, a página vai perguntar se pode abri-lo, mas se preferir, pode-se abrir a versão web também.

O arquivo telegramkeyex.py é o app do Bot. Na linha 173, é preciso colocar o token do bot:

    updater = Updater("TOKEN", use_context=True)

Com esse token, qualquer um pode acessar e alterar o bot, por isso ele foi retirado.

No HTML (carrefour_telegram.html), o link do bot também não está disponível:

    <p class="text-center"><a href="http://t.me/NOMEDOBOT">

Para testar, é preciso criar um Bot, através do BotFather, que vai dar essas duas informações. Aí é só coloca-las nos lugares certos.

O Bot que foi criado se chama 'BotCarrefourDoMau'. Se tentar conversar com ele, não vai funcionar porque ele não está em nenhum Host, só na minha máquina. 

Como o tempo foi curto, também não deu para estudar melhor todos os objetos e comandos do Telegram, por isso ainda tenho várias dúvidas:

• Não sei como impedir/bloquear o envio de mensagens antes que o usuário clique em um botão do InlineKeyboard

• Como no BotFather, gostaria de saber como abrir um menu de opções quando o usuário entra com um caractere, como o '/', por exemplo.

Mas vou continuar estudando para descobrir tudo!

A webpage-cover foi feita em HTML/CSS/Bootstrap, só para 'enfeitar' um pouco o projeto. Não utilizei o Angular porque ainda não estudei o bastante para fazer a integração entre ele e as outras tecnologias (conheci o Python, o Flask, a API dos Telegram-bots e o próprio Angular há poucas semanas...) por isso ainda deve dar para melhorar muito todo o projeto, mas estou satisfeito em ter conseguido finaliza-lo dentro do prazo!
