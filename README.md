Aqui está a descrição detalhada do que cada parte do código faz:  

---

### 📌 **Descrição do Código**
Este script automatiza o envio de mensagens pelo **WhatsApp Web** usando **Python, Selenium e Pandas**. Ele lê uma lista de contatos e mensagens de um arquivo Excel e envia mensagens personalizadas para cada contato pelo **WhatsApp Web**.

---

### 📌

1. **Importação das bibliotecas necessárias:**  
   ```python
   import pandas as pd
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   from selenium.webdriver.common.keys import Keys
   import time
   import urllib
   ```
   - `pandas` → Manipula e lê arquivos Excel.  
   - `selenium` → Permite a automação do navegador para acessar o WhatsApp Web.  
   - `time` → Utilizado para adicionar pausas no código.  
   - `urllib` → Necessário para formatar mensagens corretamente ao serem enviadas por URL.  

2. **Carregando os contatos do arquivo Excel:**  
   ```python
   contatos_df = pd.read_excel("Enviar.xlsx")
   print(contatos_df)
   ```
   - Lê o arquivo **"Enviar.xlsx"**, que contém os contatos e mensagens.  
   - Exibe os dados no terminal para conferência.  

3. **Abrindo o navegador e acessando o WhatsApp Web:**  
   ```python
   navegador = webdriver.Chrome()
   navegador.get("https://web.whatsapp.com/")
   time.sleep(100)
   ```
   - Abre o navegador **Google Chrome**.  
   - Acessa o site do **WhatsApp Web**.  
   - Aguarda **100 segundos** para que o usuário escaneie o QR Code e faça login.  

4. **Verificando se o login foi concluído:**  
   ```python
   while len(navegador.find_elements(By.ID,"side")) < 1:
       time.sleep(100)
   ```
   - Aguarda até que o **WhatsApp Web** carregue completamente, verificando a existência do elemento com ID `"side"` (barra lateral do WhatsApp Web).  

5. **Loop para enviar mensagens personalizadas:**  
   ```python
   for i, mensagem in enumerate(contatos_df['Mensagem']):
       pessoa = contatos_df.loc[i, "Pessoa"]
       numero = contatos_df.loc[i, "Número"]
   ```
   - Itera sobre cada linha da planilha, pegando a **mensagem, o nome da pessoa e o número do contato**.  

6. **Criando o link para envio da mensagem:**  
   ```python
   texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
   link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
   ```
   - Usa `urllib.parse.quote()` para formatar o texto corretamente na URL.  
   - Gera o link de envio de mensagem direta no WhatsApp Web.  

7. **Acessando o link gerado e aguardando o carregamento da conversa:**  
   ```python
   navegador.get(link)
   while len(navegador.find_elements(By.ID,"side")) < 1:
       time.sleep(10)
   ```
   - O navegador acessa a URL gerada.  
   - Aguarda até que a tela de conversa do WhatsApp carregue.  

8. **Enviando a mensagem automaticamente:**  
   ```python
   navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div/p').send_keys(Keys.ENTER)
   ```
   - Localiza a caixa de mensagem no WhatsApp Web através do XPath.  
   - Pressiona a tecla `ENTER` para enviar a mensagem.  

9. **Pausa entre os envios:**  
   ```python
   time.sleep(10)
   ```
   - Espera **10 segundos** antes de enviar a próxima mensagem para evitar bloqueios ou travamentos do WhatsApp.  

---

### 📌 **Resumo**
1. Lê uma lista de contatos e mensagens de um arquivo Excel.  
2. Abre o **WhatsApp Web** e espera o usuário fazer login.  
3. Para cada contato na planilha:
   - Gera um link de mensagem automática.  
   - Abre a conversa e espera carregar.  
   - Envia a mensagem personalizada.  
4. Aguarda um tempo antes de passar para o próximo contato.  

---

### 🛠 **Possíveis Melhorias**
✅ **Reduzir o tempo de espera** (`time.sleep(100)`) usando uma verificação mais eficiente.  
✅ **Tratar exceções** para evitar erros caso o número esteja incorreto ou a mensagem não seja enviada.  
✅ **Fechar o navegador automaticamente** após o envio das mensagens.  
✅ **Usar um WebDriver Manager** para evitar a necessidade de atualizar manualmente o ChromeDriver.  
