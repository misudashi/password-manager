q = 'Quels identifiants souhaitez-vous obtenir? (entrer un site web) | Tapper list pour obtenir la liste des comptes possibles\n\n==> '

a = input(q)
if a == "discord.com":
    print("\n--------------- Nous avons trouvé vos identifiants --------------- \n\nEmail: your@mail.com\n\nPassword: pswrd1234\n\n\nSite web: " + a )

elif a == "list":
    print("\n--------------- Voici la liste des comptes possibles: ---------------\n\ndiscord.com")
    a = input(q)
    if a == "discord.com":
        print("\n--------------- Nous avons trouvé vos identifiants --------------- \n\nEmail: your@mail.com\n\nPassword: pswrd1234\n\n\nSite web: " + a )
    else: print("Nous n'avons pas pu trouver vos identifiants.")
else: print("Nous n'avons pas pu trouver vos identifiants.")

input("\nAppuyez sur une touche pour fermer cette fenêtre.")