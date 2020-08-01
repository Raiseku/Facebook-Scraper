import facebook
import json
import hashlib


if __name__ == '__main__':
    
    access_token ="inserisci_qui_la_tua_api_key"
    
    input("Inserisci l'id dell'utente : ")
    
    input("Inserisci l'id del post : ")
    
    post_id = user_id + "_" + post_code
    
    try:
        graph = facebook.GraphAPI(access_token, version="3.0")
        print("\nIl Graph è stato definito correttamente\n")
    except Exception as e:
        print("Errore" + e)

    #Prendo il nome e l'id dell'utente per inserirlo dentro una variabile
    post = graph.get_object( user_id + "?fields=id,name")
    utente = post['name']
    
    #print("Stai visualizzando l' [utente] : " + post['name'] + " con [id] : " + post['id'] +"\n")
    
    #Entro nel post tramite id = post_id e ottengo il messaggio tramite 'message'
    post = graph.get_object(id=post_id, fields='message')
    testo_post_principale =json.dumps(post['message'], indent = 4) 
    
    print("Il Post è stato scritto da : " + utente +"\n")
    print("Il Post ha come testo : " + testo_post_principale +"\n") 
    
    comment_code = input("Inserisci l'id del commento da ottenere : ")

    comment_id = post_id + "_" + comment_code
    
    data2 = graph.get_object(id=comment_id, fields= 'message, created_time, from') #Inserire anche Attachment nel caso
    commento_principale =json.dumps(data2['message'], indent = 4) 
    scritto_da = json.dumps(data2['from'], indent = 4) 
    #allegato = json.dumps(data2['attachment'], indent = 4) Qui è commentato perchè nel caso in cui non ci fosse da errore
    creato_il = json.dumps(data2['created_time'], indent = 4) 
    
    print("Il testo principale del commento è : "+ commento_principale +"\n")
    #print("L'eventuale allegato è stato : "+ allegato +"\n")
    print("E' stato scritto da : "+ scritto_da + " il "+creato_il+ "\n")
    
    print("Le risposte al commento sono : \n")
    data3 = graph.get_connections(id=comment_id, connection_name='comments?&filter=stream&summary=1', fields = 'attachment, message, created_time, from')
    
    lista_commenti = json.dumps(data3['data'], indent = 4)
    print(lista_commenti)    

    print("Creazione del file protetto da Hash in corso : ")
    
    nome_file = "lista_commenti.txt"
    
    f = open(nome_file, "w+")
    f.write("Il Post è stato scritto da : " + utente +" \n")
    f.write("Testo del Post : " +post['message']+" \n")
    f.write("Il commento selezionato è il seguente : " +commento_principale+" ")
    f.write("scritto da : "+ scritto_da + " il "+creato_il+ "\n")
    f.write("Le risposte al commento sono :" +lista_commenti+"       \n")
    
    #Chiudo il file
    f.close()
    
    BLOCKSIZE = 65536 #Varibile utile nel caso in cui le dimensioni del file siano molto grandi
    hasher = hashlib.md5() #Creo l'Hash tramite la funzione .md5()
    with open(nome_file, 'rb') as afile: #Apro il file creato precedentemente con i commenti al suo interno
        buf = afile.read(BLOCKSIZE) #Leggo il file a blocchi di 64 kb
        while len(buf) > 0: #Finchè la lettura del file non è completata fai :
            hasher.update(buf) #Update della Hash precedentemente definita in base al contenuto del documento
            buf = afile.read(BLOCKSIZE) #Aggiorno la variabile buf per il prossimo ciclo
            
    stringa_hash = hasher.hexdigest()
    print(stringa_hash) #Stampo a video l'Hash appena creata

    print("Il file è stato correttamente protetto con HASH ")
    print("Essa risiede all'interno del file hash.txt")
    
    h = open("hash.txt", "w+")
    h.write("L'hash per il file " + nome_file + " è la seguente : " + stringa_hash)
    
    
    