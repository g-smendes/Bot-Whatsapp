
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib


contatos_df = pd.read_excel("Enviar.xlsx")
print(contatos_df)

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")
time.sleep(100)

while len(navegador.find_elements(By.ID,"side")) < 1:
    time.sleep(100)

# já estamos com o login feito no whatsapp web
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements(By.ID,"side")) < 1:
        time.sleep(10)
    navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div/p').send_keys(Keys.ENTER)
    time.sleep(10)
        
    





