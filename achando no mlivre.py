from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install()) #instalando chrome na biblioteca para concatenar ao computador
driver = webdriver.Chrome(service=service) #atribuindo o service 

start_time = time.time() #contando o tempo 

driver.get('https://www.mercadolivre.com.br/ofertas') #pegando o site de referência 

carrosseis = driver.find_elements(By.CLASS_NAME, 'carousel_item') #Selecionando elemento 

total_promotions = 0  #inicializando contador de promoções 

for i in range(len(carrosseis)): #passando por cada atributo do carrossel 
    carrossel = carrosseis[i] #atualizando o valor do carrossel na estrutura de repetição  
    if not carrossel.is_displayed(): #se o carrossel não estiver na página  
        proxbutton = driver.find_elements(By.CLASS_NAME, 'andes-carousel-snapped__control--next')[0] #identifica o botão de pular para a próxima inicializando na primeira 
        proxbutton.click() #clica no botão
        time.sleep(3) #espera 3 segundos para começar a tomar uma nova ação
        carrosseis = driver.find_elements(By.CLASS_NAME, 'carousel_item') #repetindo o código das linhas 14 e 19 para a iteração funcionar na condicional também 
        carrossel = carrosseis[i]

    carrossel.click() #por fim, clicando no carrossel 
    time.sleep(2) #espera 2 segundos para começar a tomar uma nova ação
    carrosseis = driver.find_elements(By.CLASS_NAME, 'carousel_item') #definindo novamente após sair do for 
    carrossel = carrosseis[i]
    nomecarrossel = carrossel.find_element(By.TAG_NAME, 'p').text #identificando qual carrossel o código vai se referir 

    promotion_items = driver.find_elements(By.CLASS_NAME, 'promotion-item__description') #identificando os itens em promoção 

    for p in promotion_items: #iterando sobre cada item em promoção 
        description = p.find_element(By.CLASS_NAME, 'promotion-item__title').text #localizando o item 
        discount_elements = p.find_elements(By.CLASS_NAME, 'promotion-item__discount-text') #localizando o valor do disconto 

        if discount_elements: #se houver disconto ele exibe no terminal 
            promotion_value = discount_elements[0].text #coloca ele iniciando no zero, para sempre iniciar na ordem certa 
        else:
            promotion_value = '0% OFF' 

        print(f"{nomecarrossel} / {description} / {promotion_value}") #imprimindo cada mensagemn 
        total_promotions += 1  #voltando ao contador de promoções depois de todas essas etapas, no caso ele somará 1 a cada promoção identificada 


end_time = time.time() #terminando a contagem 


elapsed_time = end_time - start_time #identifiando a contagem de tempo exata 
print(f"Tempo total decorrido: {elapsed_time:.2f} segundos") 


print(f"Total de promoções encontradas: {total_promotions}")  

driver.quit() #fim do programa 
