"""
Um bot simples, com botões (keyboard) inline para direcionar o cliente
para uma das áreas principais de atendimento do banco.

A base do código foi baseada no exemplo 'inlinekeyboard2.py' em:
https://github.com/python-telegram-bot/python-telegram-bot/

Lá estão vários exemplos de telegram-bots, cada um com uma característica.

"""

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,\
    ConversationHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND, THIRD, FOURTH = range(4)

# Tipos de botões, indexados
DUV, SUG, CRIT = range(3)
CARD, SEG, CRED, PAG, PROM, OUTRO = range(6)
SIM, NAO = range(2)


# Função para o /start
def start(update, context):
    # Recebe o nome do usuário
    user = update.message.from_user
    # InlineKeyboard com os botões iniciais
    keyboard = [
        [InlineKeyboardButton("Dúvidas", callback_data=str(DUV)),
         InlineKeyboardButton("Sugestões", callback_data=str(SUG)),
         InlineKeyboardButton("Críticas", callback_data=str(CRIT))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Olá, {}! Como vai? Sobre qual assunto você gostaria de conversar?".format(user.first_name),
        reply_markup=reply_markup,
    )
    # Diz ao ConversationHandler que estamos em FIRST
    return FIRST


# Função para reiniciar o processo
def start_over(update, context):
    # CallbackQueries, as respostas ao envio dos botões, precisam ser respondidas,
    # mesmo sem nenhuma mensagem.
    # https://core.telegram.org/bots/api#callbackquery
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Dúvidas", callback_data=str(DUV)),
         InlineKeyboardButton("Sugestões", callback_data=str(SUG)),
         InlineKeyboardButton("Críticas", callback_data=str(CRIT))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Escolha novamente uma das opções:",
        reply_markup=reply_markup
    )
    return FIRST


# Função para as Dúvidas
def duv(update, context):
    query = update.callback_query
    query.answer()
    # Agora teremos as novas opções de botões
    keyboard = [
        [InlineKeyboardButton("Cartão Carrefour", callback_data=str(CARD)),
         InlineKeyboardButton("Seguros", callback_data=str(SEG))],
         [InlineKeyboardButton("Crédito Pessoal", callback_data=str(CRED)),
         InlineKeyboardButton("Pagamento de Contas", callback_data=str(PAG))],
         [InlineKeyboardButton("Promoções", callback_data=str(PROM)),
         InlineKeyboardButton("Outros", callback_data=str(OUTRO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Suas dúvidas são sobre qual dos nossos serviços?",
        reply_markup=reply_markup
    )
    # Mudar para outro estado (SECOND)
    return SECOND


# Função para as Sugestões
def sug(update, context):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Cartão Carrefour", callback_data=str(CARD)),
         InlineKeyboardButton("Seguros", callback_data=str(SEG))],
         [InlineKeyboardButton("Crédito Pessoal", callback_data=str(CRED)),
         InlineKeyboardButton("Pagamento de Contas", callback_data=str(PAG))],
         [InlineKeyboardButton("Promoções", callback_data=str(PROM)),
         InlineKeyboardButton("Outros", callback_data=str(OUTRO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Por favor, escolha para qual área você quer enviar sua sugestão:",
        reply_markup=reply_markup
    )
    return SECOND


# Função para as Críticas ou Reclamações
def crit(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Cartão Carrefour", callback_data=str(CARD)),
         InlineKeyboardButton("Seguros", callback_data=str(SEG))],
         [InlineKeyboardButton("Crédito Pessoal", callback_data=str(CRED)),
         InlineKeyboardButton("Pagamento de Contas", callback_data=str(PAG))],
         [InlineKeyboardButton("Promoções", callback_data=str(PROM)),
         InlineKeyboardButton("Outros", callback_data=str(OUTRO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Por favor, escolha para qual área você quer enviar sua crítica ou reclamação:",
        reply_markup=reply_markup
    )
    return SECOND


# Pedindo o envio da mensagem do usuário
def answer(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Pode enviar a sua mensagem!"
    )
    return THIRD


# Resposta genérica para qualquer opção
def again(update, context):
    keyboard = [
        [InlineKeyboardButton("Sim, gostaria.", callback_data=str(SIM)),
         InlineKeyboardButton("Não, obrigado!", callback_data=str(NAO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "A sua mensagem será enviada para a área responsável e você receberá "
        "uma resposta em algumas horas!"
        "\nGostaria de enviar uma mensagem sobre outro assunto?",
        reply_markup=reply_markup,
    )
    return FOURTH


# Encerramento da conversa
def end(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Ok, muito obrigado por conversar conosco!"
             "\nO Banco Carrefour está sempre buscando melhorar a comunicação com seus clientes!"
    )
    return ConversationHandler.END


# Aplicação principal
def main():
    # Cria o Updater e envia o token do Bot
    updater = Updater("1338690097:AAET37Fk57oXHeCFaEdkfR2XcsNTX4j5gXg", use_context=True)

    # através do 'dispatcher' iremos cadastrar os nossos comandos no Bot
    dp = updater.dispatcher

    # Setup do ConversationHandler com os 'estados' FIRST, QUALDUV, QUALSUG, QUALCRIT ou DENOVO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [CallbackQueryHandler(duv, pattern='^' + str(DUV) + '$'),
                    CallbackQueryHandler(sug, pattern='^' + str(SUG) + '$'),
                    CallbackQueryHandler(crit, pattern='^' + str(CRIT) + '$')],
            SECOND: [CallbackQueryHandler(answer, pattern='^' + str(CARD) + '$'),
                     CallbackQueryHandler(answer, pattern='^' + str(SEG) + '$'),
                     CallbackQueryHandler(answer, pattern='^' + str(CRED) + '$'),
                     CallbackQueryHandler(answer, pattern='^' + str(PAG) + '$'),
                     CallbackQueryHandler(answer, pattern='^' + str(PROM) + '$'),
                     CallbackQueryHandler(answer, pattern='^' + str(OUTRO) + '$')],
            THIRD: [MessageHandler(Filters.text & ~Filters.command, again)],
            FOURTH: [CallbackQueryHandler(start_over, pattern='^' + str(SIM) + '$'),
                     CallbackQueryHandler(end, pattern='^' + str(NAO) + '$')],
        },
        fallbacks=[CommandHandler('start', start)]
    )

    # Aqui nós adicionamos o ConversationHandler acima para o dispatcher,
    # para gerenciar as mudanças que cada botão vai provocar
    dp.add_handler(conv_handler)

    # Aqui nós iniciamos o Bot, pesquisando qualquer atualização enviada para ele
    updater.start_polling()

    # O idle() é para 'bloquear' a aplicação até que um comando ou o Ctrl-C pare o updater
    # comandos: SIGINIT, SIGTERM, SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
