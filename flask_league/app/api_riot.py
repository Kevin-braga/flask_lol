import requests, json


class API_RIOT():

	api_key = "?"

	def __init__(self,name):
		self.summonerName = name

	def get_summoner(self):

		r = requests.get("https://br1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{1}?api_key={0}".format(self.api_key,self.summonerName))

		if r.status_code == 200:

			j = json.loads(r.text)
			print(j)
			self.summonerId = j.get('id')

		else:
			print("Invocador não localizado")

	def get_champion_masteries(self):

		r = requests.get("https://br1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/{1}?api_key={0}".format(self.api_key,self.summonerId))

		if r.status_code == 200:

			j = json.loads(r.text)
			
			for i in j:

				champion_id = i.get('championId')
				champion = self.get_champion_info(champion_id)

				mastery_level = i.get('championLevel')
				mastery_points = i.get('championPoints')

				print(champion,mastery_level,mastery_points)


	def get_champions_list(self):

		r = requests.get("https://br1.api.riotgames.com/lol/platform/v3/champions?api_key={0}".format(self.api_key))

		if r.status_code == 200:

			j = json.loads(r.text)
			
			print(j)


	def get_champion_info(self,champion_id):

		r = requests.get("https://br1.api.riotgames.com/lol/static-data/v3/champions/{1}?api_key={0}".format(self.api_key,champion_id))

		if r.status_code == 200:

			j = json.loads(r.text)

			name = j.get('name')

			return(name)

		else:
			return None


if __name__ == "__main__":	

	print("=================================\n")
	name = input("Digite o nome do seu Invocador : ")

	api = API_RIOT(name)
	api.get_summoner()
	api.get_champion_masteries()

	input('GADO')