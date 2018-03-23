#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-

import cryptocompare
from time import sleep

def scriptMessages(choice):
	"Affiche un message d'entrée ou de sortie du script"	
	if choice == 'hello':
		print("### Script qui récupère en temps réel le prix d'une Cryptomonnaie. ###\n")
	elif choice == 'bye':
		print("\nMerci de votre passage, à bientôt !\n")

def getData():
	"Récupére et renvoie toutes les cryptos classés alphabétiquement"
	get_all_crypto = cryptocompare.get_coin_list(format=True)
	get_all_crypto.sort()
	classified_crypto = {}

	for letter in get_all_crypto:
		first_letter = letter[:1]
		classified_crypto[first_letter] = []

	for crypto in get_all_crypto:
		first_char = crypto[:1]
		classified_crypto[first_char].append(crypto)

	for letter, cryptos in classified_crypto.items() :
	    print("Cryptomonnaie commençant par {} :".format(letter))
	    for crypto in cryptos:
	    	print(crypto, end=' | ')
	    print("\n")

def userAction():
	"Retourne un entier declenchant une action definit par la saisie utilisateur"
	print("Tapez 1 pour voir toutes les crypto monnaie disponible.")
	print("Tapez 2 pour sélectionner une monnaie spécifique.")
	print("Tapez 3 pour quitter le programme.")
	user_action = input("\nChoix : ")
	return user_action

def userCryptoChoice():
	"Retourne le choix de la crypto monnaie saisi par l'utilisateur"
	user_choice = input("\nDe quelle monnaie voulez-vous connaître la valeur ? (ex: 'bccoin') : ")
	return str.upper(user_choice)

###################
# Debut du script #
###################

scriptMessages('hello')

while 1:
	user_action = userAction()

	try:
		user_action = int(user_action)

		if user_action == 1:
			getData()
	
		elif user_action == 2:
			user_crypto_choice = userCryptoChoice()

			try: 
				get_price = cryptocompare.get_price(user_crypto_choice, 'EUR')
				for money, devise in get_price.items():
					for sub_devise, value in devise.items():
						print("\nLa monnaie {0} vaut actuellement {1} {2}.\n".format(money, value, sub_devise))
						sleep(2)

			except AttributeError:
				print("Désolé mais il n'y a aucune donnée pour '{}'. Veuillez réessayer avec un autre terme.\n".format(user_crypto_choice))

		elif user_action == 3:
			scriptMessages('bye')
			break

		else:
			print("\nErreur : Nombre invalide. Il doit être entre 1 et 3.\n")

	except ValueError:
		print("\nErreur : Un entier est requis.\n")
		sleep(1)

	