from flask import Flask, render_template, request
from discord_webhook import DiscordWebhook
    
    
app = Flask(__name__)
    
    
@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Discord sunucumuz ne işe yarar') == 'Discord sunucumuz ne işe yarar':
                # pass
            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/852844127846006784/oVe-C3K1IT8-CdCznCj0MvYXOGeaOcH49XXDNDvo0dhRbH84y38Z3Ns5L597iNXyCns2', content='Discord Sunucumuz Sizi Bilgilendirmek Ve Arkadaş Çevresi Oluşturmak için Yapılmıştır')
            response = webhook.execute()
        elif  request.form.get('Kanala abone ol!') == 'Kanala abone ol!':
                # pass # do something else
            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/852844127846006784/oVe-C3K1IT8-CdCznCj0MvYXOGeaOcH49XXDNDvo0dhRbH84y38Z3Ns5L597iNXyCns2', content='https://www.youtube.com/channel/UC_q6e2_Um5qiRZZTqY1JgbQ')
            response = webhook.execute()
        else:
                # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':   
            # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")
    
    
if __name__ == '__main__':
    app.run()