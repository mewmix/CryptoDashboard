# CryptoDashboard
Conky dashboard inspired by https://github.com/Gictorbit/victorconky - depends on Python 3 - untested with Python2 -
Also depends on an Etherscan API Key - for more information on obtaining one see here https://info.etherscan.com/etherscan-developer-api-key/


#Install Steps

1.Clone this Repo 

```

git clone https://github.com/mewmix/CryptoDashboard

```

Move the CryptoDashboard folder to your conky path 

```
mv CryptoDashboard ~/.conky 
```

2.Edit the sample .env file with your etherscan key and rename as .env

```
cp sample.env .env

```

3.Make start script executable and run

```
chmod +x start.sh  && ./start.sh

```

4. Screenshots

![ConkerGUI](https://user-images.githubusercontent.com/42463809/179452037-8c82a9a4-c733-400e-91bd-6b7075e49a18.png)
