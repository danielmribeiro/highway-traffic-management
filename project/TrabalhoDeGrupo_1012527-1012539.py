#TrabalhoDeGrupo_1012527/1012539
######################################################################################################### DONOS ############################################################################################################################

def inserirdono():
    idutente = eval(input("IDUtente ?"))
    nome = input("Nome ?")
    nde = input("Numero Dispositivo eletronico?")
    ref_ficheiro = open("donosNOVO.txt", "at")
    print(idutente, ";", nome, ";", nde, file=ref_ficheiro)
    ref_ficheiro.close()

def ReadAllLinesVectorAlterarDono():
    fname = 'donos2.txt'
    infile = open(fname, "r")
    lines = infile.readlines()
    infile.close()
    print("Registos: ", len(lines))
    SearchIDUtente = input("IDUtente a alterar?")
    pos = -1
    for i in range(len(lines)):
        colunas = lines[i].split(';')
        if (len(colunas) < 3):
            continue
        IDUtente                        = colunas[0]
        Nome                            = colunas[1]
        NumeroDispositivoEletronico     = colunas[2]
        if (SearchIDUtente == IDUtente):
            pos = i
            print ('\n' * 3)    
            print ('IDUtente encontrado na posição ', i)
            print ('\n' * 2)    
            print ('IDUtente......................... :', IDUtente)
            print ('Nome............................. :', Nome)
            print ('Numero Dispositivo Eletronico.... :', NumeroDispositivoEletronico)
            op = input("Alterar ? (s/n) ?")
            if (op == 's'):
                print('Alterar ')
                IDUtente = input("IDUtente ?")
                Nome 	  = input("Nome ?")
                NumeroDispositivoEletronico    = input("Numero Dispositivo Eletronico ?")
                outfile = open(fname, "w")
                for i in range(len(lines)):
                    if (i != pos):
                        line = lines[i]
                        line[0:len(line)-1]
                        print(line, file=outfile, end='')
                    else:
                        print(IDUtente, Nome, NumeroDispositivoEletronico, sep=';',file=outfile)
                outfile.close();
                break;
    if (pos == -1):
        print('Esse Utente não existe')        




def ReadAllLinesVectorEliminarDono():
    fname = 'donos2.txt'
    infile = open(fname, "r")
    lines = infile.readlines()
    infile.close()
    print("Registos: ", len(lines))
    SearchIDUtente = input("IDUtente ?")
    pos = -1
    for i in range(len(lines)):
        colunas = lines[i].split(';')
        if (len(colunas) < 3):
            continue
        IDUtente                        = colunas[0]
        Nome                            = colunas[1]
        NumeroDispositivoEletronico     = colunas[2]
        if (SearchIDUtente == IDUtente):
            pos = i
            print ('\n' * 3)    
            print ('IDUtente encontrado na posição ', i)
            print ('\n' * 2)    
            print ('IDUtente......................... :', IDUtente)
            print ('Nome............................. :', Nome)
            print ('Numero Dispositivo Eletronico.... :', NumeroDispositivoEletronico)
            op = input("Eliminar ? (s/n) ?")
            if (op == 's'):
                print('Eliminando ... ')
                outfile = open(fname, "w")
                for i in range(len(lines)):
                    if (i != pos):
                        line = lines[i]
                        line[0:len(line)-1]
                        print(line, file=outfile, end='')
                outfile.close();
                break;
    if (pos == -1):
        print('Esse Utente não existe')
               
def listatodosdonos():
    fname = 'donos2.txt'
    infile = open(fname, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        IDUtente= colunas[0]
        Nome= colunas[1]
        NumeroDispositivoEletronico= colunas[2]
        print ("{0:15}{1:^60}{2:>15}".format(IDUtente,Nome,NumeroDispositivoEletronico))
    infile.close()

def listarDonosbin():
    import struct
    donoFormato = struct.Struct('i80s20s');
    f_bin = open("donos2.bin","rb")
    f_bin.seek(0,2)
    r = int(f_bin.tell() / donoFormato.size)
    f_bin.seek(0,0)
    for i in range (0,r):
        donoBinario = f_bin.read(donoFormato.size)
        IDUtente, Nome, NumeroDispositivoEletronico = donoFormato.unpack(donoBinario)
        Nome = Nome.decode()
        NumeroDispositivoEletronico = NumeroDispositivoEletronico.decode()
        print("{0:<12}".format(IDUtente),end='')       
        print("{0:50}".format(Nome), end='')
        print("{0:15}".format(NumeroDispositivoEletronico))
    f_bin.close
    
#def PesquisaDonoBinario():
#    import struct
#    carroFormato = struct.Struct('i80s20s');
#    nome = input("Nome a procurar ?")
#    f_bin = open("donos2.bin", "rb")   ## leitura, binário
#    f_bin.seek(0, 2)
#    r = int(f_bin.tell() / carroFormato.size)
#    f_bin.seek(0, 0)
#    pos = -1
#    for i in range(0, r):
#        carroBinario = f_bin.read(carroFormato.size)
#        IDUtente, Nome, NumeroDispositivoEletronico = carroFormato.unpack(carroBinario)
#        Nome = Nome.decode()
#        if (Nome.find(nome)>=0):
#            pos = i
#            break
#    f_bin.close()
#    if (pos != -1):
#        # 1º registo é o ZERO 
#        print('Dono encontrado na posição', pos + 1)  
#        print(IDUtente, Nome, NumeroDispositivoEletronico)
#    else:
#        print('Dono não encontrado!')

def pesquisapornome():
    nomeProcurar = input("Diga o nome a procurar?")
    fname = 'donos2.txt'
    infile = open(fname, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        IDUtente= colunas[0]
        Nome= colunas[1]
        NumeroDispositivoEletronico= colunas[2]
        if (Nome.find(nomeProcurar)>=0):
            print ("{0:15}{1:^60}{2:>15}".format(IDUtente,Nome,NumeroDispositivoEletronico))
    infile.close()

def pesquisaporNomeEQuantidade():
    nomeProcurar = input("Diga o nome a procurar?")
    fname = 'donos2.txt'
    infile = open(fname, "r")
    n = 0
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        IDUtente= colunas[0]
        Nome= colunas[1]
        NumeroDispositivoEletronico= colunas[2]
        primeiroNome = Nome.split(" ")
        primeiroNome = primeiroNome[0]
        if nomeProcurar==primeiroNome:
            n = n + 1
    print("Numero de pessoas com o nome",nomeProcurar, n)
    infile.close()

def ConverteDonosTextoEmDonosBinario():
    import struct
    donoFormato = struct.Struct('i80s20s');

    f_texto = open('donos2.txt', "r")
    f_bin = open("donos2.bin", "wb")
    lines = f_texto.readlines();
    for i in range(1, len(lines)):
        line = lines[i]
        line = line[0:len(line)-1]
        colunas = line.split(';')

        IDUtente = eval(colunas[0])
        Nome = colunas[1].encode()
        NumeroDispositivoEletronico = colunas[2].encode()
        #print(IDUtente, Nome, NumeroDispositivoEletronico) 
        donoBinario = donoFormato.pack(IDUtente, Nome, NumeroDispositivoEletronico)
        f_bin.write(donoBinario)
    print('Fim de conversão')    
    f_bin.close()
    f_texto.close()
    
    
def gestaodedonos ():
    while True:
        print("1  - Inserir dono (.txt)")
        print("2  - Alterar dono (.txt)")
        print("3  - Eliminar dono (.txt)")
        print("4  - Listar todos os donos (.txt) ")
        print("5  - Listar todos os donos (.bin) ")
        print("6  - Pesquisa por Nome (.txt)") 
        print("7  - Pesquisa por Nome e Quantidade (.txt)")
        print("8 - Converter donos2.txt em donos2.bin")
        print()
        print("0 - Voltar")
        print()
        
        op=input("?")
        if op=="0":
            break
        elif op=="1":
            inserirdono()
        elif op=="2":
            ReadAllLinesVectorAlterarDono()
        elif op=="3":
            ReadAllLinesVectorEliminarDono()
        elif op=="4":
            listatodosdonos()
        elif op=="5": 
            listarDonosbin()
        elif op=="6":
            pesquisapornome()
        elif op=="7":
            pesquisaporNomeEQuantidade()
        elif op=="8":
            ConverteDonosTextoEmDonosBinario()
        else:
            print("Escolha uma opção contida na lista apresentada")

###########################################################################################################   CARROS   ############################################################################################################
            
def inserircarro():
    Matricula = input("Matricula ?")
    Marca = input("Marca ?")
    Modelo = input("Modelo ?")
    Ano = input("Ano ?")
    IDUtenteFK = input("IDUtenteFK ?")
    IDCarro = input("IDCarro ?")
    ref_ficheiro = open("carrosNOVO.txt", "at")
    print(Matricula, ";", Marca, ";", Modelo, ";", Ano, ";", IDUtenteFK, ";", IDCarro, ";", file=ref_ficheiro)
    ref_ficheiro.close()

def inserircarrobin():
    import struct
    carroFormato = struct.Struct('15s20s20siii');
    Matricula = input ('Matricula ?')
    Marca = input ('Marca ?');
    Modelo = input ('Modelo ?');
    Ano = eval(input ('Ano ?'));
    IDUtenteFK = eval(input ('IDUtenteFK ?'))
    IDCarro = eval(input ('IDCarro ?'))
    #                            12345678901234567890
    Matricula = Matricula.encode() ####### '69-20'AO'
    Marca = Marca.encode()
    Modelo = Modelo.encode()
    

    carroBinario= carroFormato.pack(Matricula, Marca, Modelo, Ano, IDUtenteFK, IDCarro)
    
    f = open("carros.bin2", "ab") ## escrita, fim
    f.write(carroBinario)
    f.close()
    print('Carro inserido com sucesso.')

def ReadAllLinesVectorAlterarCarro():
    fname = 'carros.txt'
    infile = open(fname, "r")
    lines = infile.readlines()
    infile.close()
    print("Registos: ", len(lines))
    SearchMatricula = input("Matricula a alterar?")
    pos = -1
    for i in range(len(lines)):
        colunas = lines[i].split(';')
        if (len(colunas) < 6):
            continue
        Matricula  = colunas[0]
        Marca      = colunas[1]
        Modelo     = colunas[2]
        Ano        = colunas[3]
        IDUtenteFK = colunas[4]
        IDCarro    = colunas[5]
        if (SearchMatricula == Matricula):
            pos = i
            print ('\n' * 3)    
            print ('Carro encontrado na posição ', i)
            print ('\n' * 2)    
            print ('Matricula. :', Matricula)
            print ('Marca..... :', Marca)
            print ('Modelo.... :', Modelo)
            print ('Ano....... :', Ano)
            print ('IDUtenteFK :', IDUtenteFK)
            print ('IDCarro... :', IDCarro)
            op = input("Alterar ? (s/n) ?")
            if (op == 's'):
                print('Alterar ')
                Matricula = input("Matricula ?")
                Marca 	  = input("Marca ?")
                Modelo    = input("Modelo ?")
                Ano		= eval(input("Ano"))	
                IDUtenteFK 	= eval(input("Número do dono ?"))	
                IDCarro 	= eval(input("Número do carro"))	
                outfile = open(fname, "w")
                for i in range(len(lines)):
                    if (i != pos):
                        line = lines[i]
                        line[0:len(line)-1]
                        print(line, file=outfile, end='')
                    else:
                        print(Matricula, Marca, Modelo, Ano, IDUtenteFK, IDCarro, sep=';',file=outfile)
                outfile.close();
                break;
    if (pos == -1):
        print('Esse carro não existe')

def ReadAllLinesVectorEliminarCarro():
    fname = 'carros.txt'
    infile = open(fname, "r")
    lines = infile.readlines()
    infile.close()
    print("Registos: ", len(lines))
    SearchMatricula = input("Matricula ?")
    pos = -1
    for i in range(len(lines)):
        colunas = lines[i].split(';')
        if (len(colunas) < 6):
            continue
        Matricula  = colunas[0]
        Marca      = colunas[1]
        Modelo     = colunas[2]
        Ano        = colunas[3]
        IDUtenteFK = colunas[4]
        IDCarro    = colunas[5]
        if (SearchMatricula == Matricula):
            pos = i
            print ('\n' * 3)    
            print ('Carro encontrado na posição ', i)
            print ('\n' * 2)    
            print ('Matricula. :', Matricula)
            print ('Marca..... :', Marca)
            print ('Modelo.... :', Modelo)
            print ('Ano....... :', Ano)
            print ('IDUtenteFK :', IDUtenteFK)
            print ('IDCarro... :', IDCarro)
            op = input("Eliminar ? (s/n) ?")
            if (op == 's'):
                print('Eliminando ... ')
                outfile = open(fname, "w")
                for i in range(len(lines)):
                    if (i != pos):
                        line = lines[i]
                        line[0:len(line)-1]
                        print(line, file=outfile, end='')
                outfile.close();
                break;
    if (pos == -1):
        print('Esse carro não existe')

            
def listatodoscarros():
    fbrand = 'carros.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        Matricula= colunas[0]
        Marca= colunas[1]
        Modelo= colunas[2]
        Ano= colunas[3]
        IDUtenteFK= colunas[4]
        IDCarro= colunas[5]
        print ("{0:15}{1:^15}{2:^15}{3:^15}{4:^15}{5:>15}".format(Matricula,Marca,Modelo,Ano,IDUtenteFK,IDCarro))
    infile.close()

def ListarCarrosbin():
    import struct
    carroFormato = struct.Struct('15s20s20siii');
    f_bin = open("carros.bin", "rb") ##leitura, binario
    f_bin.seek(0, 2)
    r = int(f_bin.tell() / carroFormato.size)
    f_bin.seek(0, 0)
    pos = -1
    for i in range(0, r):
        carroBinario = f_bin.read(carroFormato.size)
        Matricula, Marca, Modelo, Ano, IDUtenteFK, IDCarro = carroFormato.unpack(carroBinario)
        Matricula = Matricula.decode()
        Marca = Marca.decode()
        Modelo = Modelo.decode()
        print ("{0:10}".format(Matricula), end='')
        print ("{0:15}".format(Marca), end='')
        print ("{0:15}".format(Modelo), end='')
        print ("{0:10}".format(Ano), end='')
        print ("{0:12}".format(IDUtenteFK), end='')
        print ("{0:8}".format(IDCarro), end='')
    f_bin.close()

def pesquisapormarca():
    marcaProcurar = input("Diga a Marca a procurar?")
    fbrand = 'carros.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        Matricula= colunas[0]
        Marca= colunas[1]
        Modelo= colunas[2]
        Ano= colunas[3]
        IDUtenteFK= colunas[4]
        IDCarro= colunas[5]
        if (Marca.find(marcaProcurar)>=0):
            print ("{0:15}{1:^15}{2:^15}{3:^15}{4:^15}{5:>15}".format(Matricula,Marca,Modelo,Ano,IDUtenteFK,IDCarro))
    infile.close()

def pesquisaporMarcaEQuantidade():
    marcaProcurar = input("Diga a Marca a procurar?")
    fbrand = 'carros.txt'
    infile = open(fbrand, "r")
    n = 0
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        Matricula= colunas[0]
        Marca= colunas[1]
        Modelo= colunas[2]
        Ano= colunas[3]
        IDUtenteFK= colunas[4]
        IDCarro= colunas[5]
        if (Marca==marcaProcurar):
            n = n + 1
    print("Numero de pessoas com a marca",marcaProcurar, n)
    infile.close()

def ConverteCarrosTextoEmCarrosBinario():
    import struct
    carroFormato = struct.Struct('15s20s20siii');

    f_texto = open('carros.txt', "r")
    f_bin = open("carros.bin", "wb")
    lines = f_texto.readlines();
    for i in range(2, len(lines)):
        line = lines[i]
        line = line[0:len(line)-1]
        colunas = line.split(';')

        Matricula = colunas[0].encode()
        Marca = colunas[1].encode()
        Modelo = colunas[2].encode()
        Ano= eval(colunas[3])
        IDUtenteFK = eval(colunas[3])
        IDCarro = eval(colunas[4])
        #print(Matricula, Marca, Modelo, Ano, IDUtenteFK, IDCarro)
       
        carroBinario = carroFormato.pack(Matricula, Marca, Modelo, Ano, IDUtenteFK, IDCarro)
        f_bin.write(carroBinario)
    print('Fim de conversão')    
    f_bin.close()
    f_texto.close()

def gestaodecarros ():
    while True:
        print("1 - Inserir carro (.txt)")
        print("2 - Inserir carro (.bin)")
        print("3 - Alterar carro (.txt)")
        print("4 - Eliminar carro (.txt)")
        print("5 - Listar Todos os carros (.txt)")
        print("6 - Listar Todos os carros (.bin)")
        print("7 - Pesquisa por Marca ou modelo (.txt)")
        print("8 - Pesquisa por Marca ou modelo e Quantidade (.txt)")
        print("9 - Converter carros.txt em carros.bin")
        print()
        print("0 - Voltar")
        print()
        
        op=input("?")
        if op=="0":
            break
        elif op=="1":
            inserircarro()
        elif op=="2":
            inserircarrobin()
        elif op=="3":
            ReadAllLinesVectorAlterarCarro() 
        elif op=="4":
            ReadAllLinesVectorEliminarCarro()
        elif op=="5":
            listatodoscarros()
        elif op=="6":    
            ListarCarrosbin()
        elif op=="7":
            pesquisapormarca()
        elif op=="8":
            pesquisaporMarcaEQuantidade()
        elif op=="9":        
            ConverteCarrosTextoEmCarrosBinario()
        else:
            print("Escolha uma opção contida na lista apresentada")


######################################################################################################### CIDADES #######################################################################################

            
def inserircidade():
    IDCidade = eval(input("IDCidade ?"))
    Cidade = input("Cidade ?")
    ref_ficheiro = open("cidadesNOVO.txt", "at")
    print(IDCidade, ";", Cidade, ";",file=ref_ficheiro)
    ref_ficheiro.close()
    
def ReadAllLinesVectorAlterarCidade():
    fname = 'cidades.txt'
    infile = open(fname, "r")
    lines = infile.readlines()
    infile.close()
    print("Registos: ", len(lines))
    SearchIDCidade = input("IDCidade a alterar?")
    pos = -1
    for i in range(len(lines)):
        colunas = lines[i].split(';')
        if (len(colunas) < 2):
            continue
        IDCidade                        = colunas[0]
        Cidade                          = colunas[1]
        if (SearchIDCidade == IDCidade):
            pos = i
            print ('\n' * 3)    
            print ('IDCidade encontrado na posição ', i)
            print ('\n' * 2)    
            print ('IDCidade......................... :', IDCidade)
            print ('Cidade........................... :', Cidade)
           
            op = input("Alterar ? (s/n) ?")
            if (op == 's'):
                print('Alterar ')
                IDCidade = input("IDCidade ?")
                Cidade 	  = input("Cidade ?")
                outfile = open(fname, "w")
                for i in range(len(lines)):
                    if (i != pos):
                        line = lines[i]
                        line[0:len(line)-1]
                        print(line, file=outfile, end='')
                    else:
                        print(IDCidade, Cidade, sep=';',file=outfile)
                outfile.close();
                break;
    if (pos == -1):
        print('Essa cidade não existe')


def ReadAllLinesVectorEliminarCidade():
    fname = 'cidades.txt'
    infile = open(fname, "r")
    lines = infile.readlines()
    infile.close()
    print("Registos: ", len(lines))
    SearchIDCidade = input("IDCidade ?")
    pos = -1
    for i in range(len(lines)):
        colunas = lines[i].split(';')
        if (len(colunas) < 2):
            continue
        IDCidade                        = colunas[0]
        Cidade                          = colunas[1]
        if (SearchIDCidade == IDCidade):
            pos = i
            print ('\n' * 3)    
            print ('IDCidade encontrado na posição ', i)
            print ('\n' * 2)    
            print ('IDCidade......................... :', IDCidade)
            print ('Cidade........................... :', Cidade)
            op = input("Eliminar ? (s/n) ?")
            if (op == 's'):
                print('Eliminando ... ')
                outfile = open(fname, "w")
                for i in range(len(lines)):
                    if (i != pos):
                        line = lines[i]
                        line[0:len(line)-1]
                        print(line, file=outfile, end='')
                outfile.close();
                break;
    if (pos == -1):
        print('Essa cidade não existe')

def listatodascidades():
    fbrand = 'cidades.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        idcidade= colunas[0]
        cidade= colunas[1]
        print ("{0:15}{1:^15}".format(idcidade,cidade))
    infile.close()

def pesquisaporidcidade():
    idcidadeProcurar = input("Diga o IDCidade a procurar?")
    fbrand = 'cidades.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        idcidade= colunas[0]
        cidade= colunas[1]
        if (idcidade.find(idcidadeProcurar)>=0):
            print ("{0:15}{1:^15}".format(idcidade,cidade))
    infile.close()
            
def pesquisaporNomeDaCidade():
    cidadeProcurar = input("Diga a Cidade a procurar?")
    fbrand = 'cidades.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        IDCidade= colunas[0]
        cidade= colunas[1]
        if (cidade.find(cidadeProcurar)>=0):
            print ("{0:15}{1:^15}".format(IDCidade,cidade))
    infile.close()

def gestaodecidades ():
    while True:
        print("1 - Inserir")
        print("2 - Alterar")
        print("3 - Eliminar")
        print("4 - Listar Todas")
        print("5 - Pesquisa por IDCidade")
        print("6 - Pesquisa por Nome da cidade")
        print()
        print("0 - Voltar")
        print()
        
        op=input("?")
        if op=="0":
            break
        elif op=="1":
            inserircidade()
        elif op=="2":
            ReadAllLinesVectorAlterarCidade()
        elif op=="3":
            ReadAllLinesVectorEliminarCidade()
        elif op=="4":
            listatodascidades()
        elif op=="5":
            pesquisaporidcidade()
        elif op=="6":
            pesquisaporNomeDaCidade()
        else:
            print("Escolha uma opção contida na lista apresentada")


########################################################################################################### DISTANCIA ##########################################################################################

            
def inserirdistancia():
    IDCidadeA = eval(input("IDCidade A ?"))
    IDCidadeB = input("IDCidade B ?")
    Distancia = input("distancia ?")
    Preco = input("Preço ?")
    ref_ficheiro = open("distanciasNOVO.txt", "at")
    print(IDCidadeA, ";", IDCidadeB, ";", Distancia, ";", Preco, ";", file=ref_ficheiro)
    ref_ficheiro.close()
    
def ReadAllLinesVectorAlterarDistancia():
    fname = 'distancias.txt'
    infile = open(fname, "r")
    lines = infile.readlines()
    infile.close()
    print("Registos: ", len(lines))
    SearchIDCidadeA = input("IDCidadeA a alterar?")
    pos = -1
    for i in range(len(lines)):
        colunas = lines[i].split(';')
        if (len(colunas) < 4):
            continue
        IDCidadeA  = colunas[0]
        IDCidadeB  = colunas[1]
        Distancia  = colunas[2]
        Preco      = colunas[3]
        if (SearchIDCidadeA == IDCidadeA):
            pos = i
            print ('\n' * 3)    
            print ('IDCidadeA encontrado na posição ', i)
            print ('\n' * 2)    
            print ('IDCidadeA. :', IDCidadeA)
            print ('IDCidadeB. :', IDCidadeB)
            print ('Distancia. :', Distancia)
            print ('Preço..... :', Preco)
            op = input("Alterar ? (s/n) ?")
            if (op == 's'):
                print('Alterar ')
                IDCidadeA = input("IDCidadeA ?")
                IDCidadeB = input("IDCidadeB ?")
                Modelo    = input("Distancia ?")
                Preco           = eval(input("Preço"))	
                outfile = open(fname, "w")
                for i in range(len(lines)):
                    if (i != pos):
                        line = lines[i]
                        line[0:len(line)-1]
                        print(line, file=outfile, end='')
                    else:
                        print(IDCidadeA, IDCidadeB, Distancia, Preco, sep=';',file=outfile)
                outfile.close();
                break;
    if (pos == -1):
        print('Essa distancia não existe')

def ReadAllLinesVectorEliminarDistancia():
    fname = 'distancias.txt'
    infile = open(fname, "r")
    lines = infile.readlines()
    infile.close()
    print("Registos: ", len(lines))
    SearchIDCidadeA = input("IDCidadeA ?")
    pos = -1
    for i in range(len(lines)):
        colunas = lines[i].split(';')
        if (len(colunas) < 4):
            continue
        IDCidadeA  = colunas[0]
        IDCidadeB  = colunas[1]
        Distancia  = colunas[2]
        Preco      = colunas[3]
        if (SearchIDCidadeA == IDCidadeA):
            pos = i
            print ('\n' * 3)    
            print ('IDCidadeA encontrado na posição ', i)
            print ('\n' * 2)    
            print ('IDCidadeA. :', IDCidadeA)
            print ('IDCidadeB. :', IDCidadeB)
            print ('Distancia. :', Distancia)
            print ('Preço..... :', Preco)
            op = input("Eliminar ? (s/n) ?")
            if (op == 's'):
                print('Eliminando ... ')
                outfile = open(fname, "w")
                for i in range(len(lines)):
                    if (i != pos):
                        line = lines[i]
                        line[0:len(line)-1]
                        print(line, file=outfile, end='')
                outfile.close();
                break;
    if (pos == -1):
        print('Essa distancia não existe')

def listatodasdistancias():
    fbrand = 'distancias.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        idcidadeA= colunas[0]
        idcidadeB= colunas[1]
        distancia= colunas[2]
        preco= colunas[3]
        print ("{0:15}{1:^15}{2:^15}{3:^15}".format(idcidadeA,idcidadeB,distancia,preco))
    infile.close()

def pesquisaporIDcidadeA():
    idcidadeAProcurar = input("Diga a cidade de partida a procurar [IDcidadeA]?")
    fbrand = 'distancias.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        idcidadeA= colunas[0]
        idcidadeB= colunas[1]
        distancia= colunas[2]
        preco= colunas[3]
        if (idcidadeA.find(idcidadeAProcurar)>=0):
            print ("{0:15}{1:^15}{2:^15}{3:^15}".format(idcidadeA,idcidadeB,distancia,preco))
    infile.close()

def pesquisaporIDcidadeB():
    idcidadeBProcurar = input("Diga a cidade de chegada a procurar [IDcidadeB]?")
    fbrand = 'distancias.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        idcidadeA= colunas[0]
        idcidadeB= colunas[1]
        distancia= colunas[2]
        preco= colunas[3]
        if (idcidadeB.find(idcidadeBProcurar)>=0):
            print ("{0:15}{1:^15}{2:^15}{3:^15}".format(idcidadeA,idcidadeB,distancia,preco))
    infile.close()
            
def pesquisapordistancia():
    distanciaProcurar = input("Diga a distancia a procurar?")
    fbrand = 'distancias.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        idcidadeA= colunas[0]
        idcidadeB= colunas[1]
        distancia= colunas[2]
        preco= colunas[3]
        if (distancia.find(distanciaProcurar)>=0):
            print ("{0:15}{1:^15}{2:^15}{3:^15}".format(idcidadeA,idcidadeB,distancia,preco))
    infile.close()

def pesquisaporpreço():
    precoProcurar = input("Diga o preço a procurar?")
    fbrand = 'distancias.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        idcidadeA= colunas[0]
        idcidadeB= colunas[1]
        distancia= colunas[2]
        preco= colunas[3]
        if (preco.find(precoProcurar)>=0):
            print ("{0:15}{1:^15}{2:^15}{3:^15}".format(idcidadeA,idcidadeB,distancia,preco))
    infile.close()


def gestaodedistancias ():
    while True:
        print("1 - Inserir")
        print("2 - Alterar")
        print("3 - Eliminar")
        print("4 - Listar Todos")
        print("5 - Pesquisa por cidade de partida")
        print("6 - Pesquisa por cidade de chegada")
        print("7 - Pesquisa por distancia")
        print("8 - Pesquisa por Preço")
        print()
        print("0 - Voltar")
        print()
        
        op=input("?")
        if op=="0":
            break
        elif op=="1":
            inserirdistancia()
        elif op=="2":
            ReadAllLinesVectorAlterarDistancia()
        elif op=="3":
            ReadAllLinesVectorEliminarDistancia()
        elif op=="4":
            listatodasdistancias()
        elif op=="5":
            pesquisaporIDcidadeA()
        elif op=="6":
            pesquisaporIDcidadeB()
        elif op=="7":
            pesquisapordistancia()
        elif op=="8":
            pesquisaporpreço()
        else:
            print("Escolha uma opção contida na lista apresentada")


############################################################################################################ PASSAGEM #######################################################################

            
def inserirpassagem():
    IDCidade = eval(input("IDCidade?"))
    IDUtenteFK = input("IDUtenteFK ?")
    Data = input("data e hora ?")
    Entsai = input("Entrada-0 ou saida-1 ?")
    ref_ficheiro = open("passagensNOVO.txt", "at")
    print(IDCidade, ";", IDUtenteFK, ";", Data, ";", Entsai, ";", file=ref_ficheiro)
    ref_ficheiro.close()

def ReadAllLinesVectorAlterarPassagem():
    fname = 'passagens.txt'
    infile = open(fname, "r")
    lines = infile.readlines()
    infile.close()
    print("Registos: ", len(lines))
    SearchIDUtenteFK = input("IDUtenteFK a alterar?")
    pos = -1
    for i in range(len(lines)):
        colunas = lines[i].split(';')
        if (len(colunas) < 4):
            continue
        IDCidade     = colunas[0]
        IDUtenteFK   = colunas[1]
        Data         = colunas[2]
        EntradaSaida = colunas[3]
        if (SearchIDUtenteFK == IDUtenteFK):
            pos = i
            print ('\n' * 3)    
            print ('IDUtenteFK encontrado na posição ', i)
            print ('\n' * 2)    
            print ('IDCidade.............. :', IDCidade)
            print ('IDUtenteFK............ :', IDUtenteFK)
            print ('Data.................. :', Data)
            print ('Entrada-0 Saida-1..... :', EntradaSaida)
            op = input("Alterar ? (s/n) ?")
            if (op == 's'):
                print('Alterar ')
                IDCidade        = input("IDCidade ?")
                IDUtenteFK 	= input("IDUtenteFK ?")
                Data            = input("Data (DD-MM-AAAA HH:MM:SS.sss) ?")
                EntradaSaida	= eval(input("Entrada-0 Saida-1 ?"))	
                outfile = open(fname, "w")
                for i in range(len(lines)):
                    if (i != pos):
                        line = lines[i]
                        line[0:len(line)-1]
                        print(line, file=outfile, end='')
                    else:
                        print(IDCidade, IDUtenteFK, Data, EntradaSaida, sep=';',file=outfile)
                outfile.close();
                break;             
    if (pos == -1):
        print('Essa passagem não existe')

def ReadAllLinesVectorEliminarPassagem():
    fname = 'passagens.txt'
    infile = open(fname, "r")
    lines = infile.readlines()
    infile.close()
    print("Registos: ", len(lines))
    SearchData = input("Data ?")
    pos = -1
    for i in range(len(lines)):
        colunas = lines[i].split(';')
        if (len(colunas) < 4):
            continue
        IDCidade  = colunas[0]
        IDUtenteFK  = colunas[1]
        Data  = colunas[2]
        EntradaSaida = colunas[3]
        if (SearchData == Data):
            pos = i
            print ('\n' * 3)    
            print ('Data encontrado na posição ', i)
            print ('\n' * 2)    
            print ('IDCidade...... :', IDCidade)
            print ('IDUtenteFK.... :', IDUtenteFK)
            print ('Data.......... :', Data)
            print ('EntradaSaida.. :', EntradaSaida)
            op = input("Eliminar ? (s/n) ?")
            if (op == 's'):
                print('Eliminando ... ')
                outfile = open(fname, "w")
                for i in range(len(lines)):
                    if (i != pos):
                        line = lines[i]
                        line[0:len(line)-1]
                        print(line, file=outfile, end='')
                outfile.close();
                break;
    if (pos == -1):
        print('Essa passagem não existe')

def listatodaspassagens():
    fbrand = 'passagens.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        IDCidade = colunas[0]
        IDUtenteFK = colunas[1]
        Data = colunas[2]
        Entsai = colunas[3]
        print ("{0:15}{1:^15}{2:^15}{3:^15}".format(IDCidade,IDUtenteFK,Data,Entsai))
    infile.close()

def pesquisaporIDCidade():
    IDCidadeProcurar = input("Diga a cidade a procurar [IDcidade]?")
    fbrand = 'passagens.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        IDCidade= colunas[0]
        IDUtenteFK= colunas[1]
        Data= colunas[2]
        Entsai= colunas[3]
        if (IDCidade.find(IDCidadeProcurar)>=0):
            print ("{0:15}{1:^15}{2:^15}{3:^15}".format(IDCidade,IDUtenteFK,Data,Entsai))
    infile.close()

def pesquisaporIDUtenteFK():
    IDUtenteFKProcurar = input("Diga o IDUtenteFK a procurar?")
    fbrand = 'passagens.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        IDCidade= colunas[0]
        IDUtenteFK= colunas[1]
        Data= colunas[2]
        Entsai= colunas[3]
        if (IDUtenteFK.find(IDUtenteFKProcurar)>=0):
            print ("{0:15}{1:^15}{2:^15}{3:^15}".format(IDCidade,IDUtenteFK,Data,Entsai))
    infile.close()
            
def pesquisapordata():
    DataProcurar = input("Diga a data e hora a procurar?")
    fbrand = 'passagens.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        IDCidade= colunas[0]
        IDUtenteFK= colunas[1]
        Data= colunas[2]
        Entsai= colunas[3]
        if (Data.find(DataProcurar)>=0):
            print ("{0:15}{1:^15}{2:^15}{3:^15}".format(IDCidade,IDUtenteFK,Data,Entsai))
    infile.close()

def pesquisaporentradasaida():
    EntsaiProcurar = input("O que pretende procurar? [entrada -> 0 ; saida -> 1]")
    fbrand = 'passagens.txt'
    infile = open(fbrand, "r")
    for line in infile:
        line = line[0:len(line)-1]
        colunas = line.split(';')
        IDCidade= colunas[0]
        IDUtenteFK= colunas[1]
        Data= colunas[2]
        Entsai= colunas[3]
        if (Entsai.find(EntsaiProcurar)>=0):
           print ("{0:15}{1:^15}{2:^15}{3:^15}".format(IDCidade,IDUtenteFK,Data,Entsai)) 
    infile.close()

def PassagensTXT2BIN():
    # IDCidade;IDUtenteFK;Data;EntradaSaida
    # 4;1006;25-06-2004 07:43:52.803;0
    # 7;1006;25-06-2004 09:31:24.440;1
    import struct
    import datetime
    import time
    passagemFormato = struct.Struct('iifi');

    f_texto = open('passagens.txt', "r")
    f_bin = open("passagens.bin", "wb")
    lines = f_texto.readlines();
    i = 0
    print ('Início de conversão')
    start = start = time.time()
    for i in range(1, len(lines)):
    #for i in range(2, 10000):
        line = lines[i]
        line = line[0:len(line)-1]
        colunas = line.split(';')

        IDCidade = eval(colunas[0])
        IDUtenteFK = eval(colunas[1])
        EntradaSaida = eval(colunas[3])
        #print(i,IDCidade, IDUtenteFK, colunas[2], EntradaSaida)
   
        Data =  datetime.datetime.strptime(colunas[2], "%d-%m-%Y %H:%M:%S.%f")
        # float
        Data = time.mktime(Data.timetuple())    
        

        
        passagemBinario = passagemFormato.pack(IDCidade, IDUtenteFK, Data, EntradaSaida)
        f_bin.write(passagemBinario)
        i = i + 1
        if ((i % 1000)==0):
            print (i, sep=' ', end='')
             
    print ('Fim de conversão')
    f_texto.close()
    f_bin.close()
    end = time.time()
    print('Tempo de conversão (segundos)', end - start)


def gestaodepassagens ():
    while True:
        print("1 - Inserir")
        print("2 - Alterar")
        print("3 - Eliminar")
        print("4 - Listar Todas")
        print("5 - Pesquisa por cidade [IDCidade]")
        print("6 - Pesquisa por IDUtenteFK")
        print("7 - Pesquisa por data")
        print("8 - Pesquisa por entrada[escrever 0] ou saida[escrever 1]")
        print("9 - Converter ficheiro .txt em .bin")
        print()
        print("0 - Voltar")
        print()
        
        op=input("?")
        if op=="0":
            break
        elif op=="1":
            inserirpassagem()
        elif op=="2":
            ReadAllLinesVectorAlterarPassagem()
        elif op=="3":
            ReadAllLinesVectorEliminarPassagem()
        elif op=="4":
            listatodaspassagens()
        elif op=="5":
            pesquisaporIDCidade()
        elif op=="6":
            pesquisaporIDUtenteFK()
        elif op=="7":
            pesquisapordata()
        elif op=="8":
            pesquisaporentradasaida()
        elif op=="9":
            PassagensTXT2BIN()
        else:
            print("Escolha uma opção contida na lista apresentada")


#################################################################################### MENU ##############################################################

def menuprincipal():
    while True:
        print("1 - Dono")
        print("2 - Carros")
        print("3 - Cidades")
        print("4 - Distâncias")
        print("5 - Passagens")
        print()
        print("0 - Terminar")
        print()
        
        op=input("?")
        if op=="0":
            break
        elif op=="1":
            gestaodedonos()
        elif op=="2":
            gestaodecarros()
        elif op=="3":
            gestaodecidades()
        elif op=="4":
            gestaodedistancias()
        elif op=="5":
            gestaodepassagens()
        else:
            print("Escolha uma opção contida na lista apresentada")
            
    
menuprincipal()
