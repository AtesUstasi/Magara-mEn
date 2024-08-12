import discord

intents = discord.Intents.default()
import discord
import random 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

facts = [
    "Bal asla Bayatlamaz.",
    "Venüsde Bir Yıl Venüsde.",
    "Bananas are berries, but strawberries aren't.",
    "There are more stars in the universe than grains of sand on all the Earth's beaches.",
    "A group of flamingos is called a 'flamboyance'."
]
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!help'):
        await message.channel.send(f'Kullanabileceğiniz Komutlar Şunlardır: !Ozon Deliği ,!sonuçları, !nedenleri')
    if message.content.startswith('!easteregg'):
        await message.channel.send(f'U0001f642')
    if message.content.startswith('!OzonDeliği'):
        await message.channel.send(f"Ozon deliği, ozon tabakasındaki incelmedir ve kloroflorokarbonlar (CFC’ler), halonlar ve metil bromid gibi kimyasallar sebebiyle oluşur. Bu kimyasallar klima, buzdolabı, yangın söndürücüler ve tarımda kullanılır. Ozon tabakasının incelmesi Güney Kutbu'nda daha belirgindir ve küresel bir sorundur. İncelmenin sonucunda daha fazla UV ışını yeryüzüne ulaşarak güneş yanıkları, deri kanseri, katarakt ve bağışıklık sisteminin zayıflamasına neden olur. UV ışınları ayrıca tarımsal üretimi azaltır ve deniz besin zincirini bozar. Kaynakça: https://tr.wikipedia.org/wiki/Ozonosfer")
    if message.content.startswith('!sonuçları'):
        await message.channel.send(f"Iklim Değişikliği , okyanus ısınması, okyanus asitlenmesi ve deniz seviyesinin  yükselmesigıda ve su kıtlığı, artan seller, aşırı sıcaklara ve daha fazlasına sebep olur. https://tr.wikipedia.org/wiki/İklim_değişikliği")                   
    if message.content.startswith('!nedenleri'):
        await message.channel.send(f'Atmosferdeki sera gazlarının artması, ormanların yok edilmesi, endüstriyel faaliyetler, tarım uygulamaları ve fosil yakıt kullanımı gibi insan kaynaklı faktörler, iklimdeki değişimlerin başlıca nedenleridir. https://www.casem.com.tr/iklim-degisikligi-nedir')
"ultra mega gizli komut /easteregg" 
#sa-as
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ("Sa"):
        await message.channel.send("Aleyküm Selam Gardaş")

    if message.content == ("sa"):
        await message.channel.send("Aleyküm Selam Gardaş")
        await client.process_commands(message) 

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!random'):
        random_f = random.choice(facts)
        await message.channel.send(random_f)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!Kaynakça':
        file_path = "C:\Users\google amca\Downloads\Discord Proje\Discord Proje\kaynakça.txt"
        
        file = discord.File(file_path, filename="file.txt")
        
        await message.channel.send("Kaynakçamız:", file=file)

client.run("Tokın")
