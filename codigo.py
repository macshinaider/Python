import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

bot = pyautogui
bot.press('win')

bot.write("chrome")

bot.press('enter')

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
bot.write(link)
bot.press('enter')
time.sleep(3)
bot.press('tab')
bot.write("lucasadd15@gmail.com")
bot.press('tab')
bot.write("aulahastag")
bot.press('enter')

time.sleep(3)

tabela = pandas.read_csv("produtos.csv")
print("🚀 ~ tabela:", tabela)

   

for linha in tabela.index:

    bot.press('tab')
   

    bot.write(tabela.loc[linha, "codigo"])
    bot.press('tab')
    
    bot.write(tabela.loc[linha, "marca"])
    bot.press('tab')

    bot.write(tabela.loc[linha, "tipo"])
    bot.press('tab')

    bot.write(str(tabela.loc[linha, "categoria"]))
    bot.press('tab')

    bot.write(str(tabela.loc[linha, "preco_unitario"]))
    bot.press('tab')

    bot.write(str(tabela.loc[linha, "custo"]))
    bot.press('tab')
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        bot.write(obs)
    bot.press('tab')
    
    bot.press('enter')
    bot.PAUSE = 0.1
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')
    bot.press('tab')   
    bot.PAUSE = 0.5



