# dio-carrefour-techchallenge

Tech Challenge da Digital Innovation One e do Banco Carrefour

Requisitos:

	Otimizar a comunicação entre clientes e Banco Carrefour
	Utilizar .NET ou Python
	Utilizar Angular (opcional), caso tenha front-end
	Utilizar a API do Telegram

Esse é um projeto simples, em Flask/Python, para um Telegram-Bot.

Sei que é meio óbvio mas, para rodar, é preciso ter instalados o Python, o Flask e a API-Telegram-Bot,
mas dá pra tirar o Flask e rodar só o .py pra testar se o bot tá funcionando.

O Flask faz a chamada para uma webpage-cover do Banco Carrefour (https://www.carrefoursolucoes.com.br), com um único link que faz a chamada para o Bot.
Caso possua o Telegram instalado, a página vai perguntar se pode abri-lo, mas se preferir, pode-se abrir a versão web também.

Esse link, no HTML, quanto o TOKEN do bot, que fica no arquivo .py, não estão definidos. Para testar, é preciso criar um Bot, através do BotFather,
que vai dar essas duas informações. Aí é só coloca-las nos lugares certos para testar.

Como o tempo foi curto, não deu para estudar melhor todos os objetos e comandos do Telegram, por isso ainda tenho várias dúvidas:

• Não sei como impedir/bloquear o envio de mensagens antes que o usuário clique em um botão do InlineKeyboard;
• Assim como no BotFather, não sei como abrir um menu de opções quando o usuário entra com um caractere, como o '/', por exemplo.

A webpage-cover foi feita em HTML/CSS/Bootstrap, só para 'enfeitar' um pouco o projeto. Não utilizei o Angular porque ainda não estudei o bastante para fazer a integração entre ele e as outras tecnologias (conheci o Python, o Flask, a API dos Telegram-bots e o próprio Angular há poucas semanas...) por isso ainda deve dar para melhorar muito todo o projeto, mas estou satisfeito em ter conseguido finaliza-lo dentro do prazo!
