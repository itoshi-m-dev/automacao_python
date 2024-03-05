#Passo a Passo do projeto
#Passo1: Entrar no sistema da empresa
       #https://dlp.hashtagtreinamentos.com/python/intensivao/login
       #pip install pyautogui
import pyautogui
import time
pyautogui.PAUSE = 0.5

# clicar em algum lugar da tela -> pyautogui.click 
# escrever um texto -> pyautogui.write
# pressionar uma tecla do teclado -> pyautogui.press


#abrir o navegador (opera gx)
pyautogui.press("win")
pyautogui.write("opera gx")
pyautogui.press("enter")

#Entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#Dar uma pausa um pouco maior (3 segundos)
time.sleep(3)

#Passo2: Fazer Login

#Inserir Email
pyautogui.click(x=421, y=396)
pyautogui.write("iloveyou@gmail.com")

#Escrever senha
pyautogui.press("tab")
pyautogui.write("emanuel12@")

#Clicar no botao de logar
pyautogui.click(x=704, y=543)
time.sleep(3)

#Passo3:  Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")


#Passo4: Cadastrar 1 Produto
#para cada linha da minha tabela
for linha in tabela.index:

       #clicar no primeiro campo
       pyautogui.click(x=487, y=274)

       #Codigo do produto   
       codigo = tabela.loc[linha,"codigo"]
       pyautogui.write(codigo)
       pyautogui.press("tab")

       #Marca
       marca = tabela.loc[linha, "marca"]
       pyautogui.write(marca)
       pyautogui.press("tab")

       #Tipo
       tipo = tabela.loc[linha, "tipo"]
       pyautogui.write(tipo)
       pyautogui.press("tab")

       #Categoria
       pyautogui.write(str(tabela.loc[linha, "categoria"]))
       pyautogui.press("tab")

       #Preço
       pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
       pyautogui.press("tab")

       #Custo
       pyautogui.write(str(tabela.loc[linha, "custo"]))
       pyautogui.press("tab")

       #Observação
       obs = tabela.loc[linha, "obs"]
       if not pandas.isna(obs):11.99
       pyautogui.write(obs)
       pyautogui.press("tab")

       #Enviar
       pyautogui.press("enter")
       pyautogui.scroll(5000)



#Passo5: Repetir o processo de cadastro dos produtos até o fim da base de dados




