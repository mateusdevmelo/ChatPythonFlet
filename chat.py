# Título: Hashzao
# Botão de iniciar chat
    # clicou no botão
    # popup / modal
        # Título: bem-vindo ao Hashzap
        # campo: escreva seu nome no chat
        # botão: entrar no chat
# chat
# embaixo do chat
    # campo de Digite sua mensagem
    # botão de enviar
    
# flet -> framework do Python

import flet as ft

def main(pagina):
    texto = ft.Text("Hashzap")
    
    def entrar_chat(evento):
        print("Entrar no chat")
        popup.open = False
        
        pagina.update()
    
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )
    
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    pagina.add(texto)
    pagina.add(botao_iniciar)

    
ft.app(target=main)
