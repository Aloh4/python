Tipos de dados:
	Int			= 1, 2, 3
	Float		= 1.1, 2.2, 3.3
	String		= 'Texto'
	Booleano	= True, False
-------------------------------------------------------
Comentários:

	# Assim comento uma linha
	''' Assim
		Comento
		várias linhas '''
-------------------------------------------------------
Verificar tipo da variável:
	type(var)
	...
-------------------------------------------------------
Alterar tipo da variável:
	var = 1
	print float(var)
	...
-------------------------------------------------------
Importar bibliotecas:

	import lib
-------------------------------------------------------
Exibir// Printar
	var1 = 192.168.0.99
	var2 = 'ASSET-EXEMPLO'

	#Exemplos:
		print 'O ip é'
		...
	# Concatenando strings
		ip = raw_input('Digite um endereco IP: ')
		print 'O endereco IP e: ' + ip + 'e um endereco valido'
	# Usando operadores
		ip = raw_input('Digite um endereco IP: ')
		print 'O endereco %s e um endereco valido' %ip
		print 'O endereco %s tem %d caracteres' %(ip,len(ip))
		print 'O endereco %s tem %d e vale exatamente %f' %(ip, int(ip), float(ip))
		print 'O endereco %s tem %d inteiros e %f floats' %(ip, len(ip), float(len(ip)))
	# Valores diretos
		print 'O endereco %s tem %d inteiros e %f floats' %('aaa', 1, 2.3)
		...
-------------------------------------------------------
Receber valores:
	input()			= Retorna valores já declarados.
	
	#Exemplo 1
		terra = 'Planeta'
		input(terra)
			output --> Planeta
	#Exemplo 2
		var = input()
		...
		print 'Digite um valor: ',var
	#Exemplo 3
		api = 'Chave secreta'
		usuario = input()
		...10030
		usuario = input()
		...api
		output --> api
		'Chave secreta' #Agora a variável usuário contém o valor de API (vulnerável)

	raw_input()		= Recebe strings
	#Exemplo 1
		valor = raw_input()
		...'12' <- é uma string.
	#Exemplo 2
		valor = int(raw_input())
		...12 <- Agora a variável valor é um inteiro.
	#Exemplo 3
		numero = int(raw_input('Digite um valor inteiro: '))
		...numero agora é int
-------------------------------------------------------
Contar tamanho da string:
	len()

	#Exemplo 1
		len('ad63589f761a4344e930486e05')
		...output --> 26
	#Exemplo 2 
		var = 'ad63589f761a4344e930486e05'
		len(var)
		...output --> 26
		type(var)
		...output --> str
	#Exemplo 3
		# Declarar uma str
			var = 'ad63589f761a4344e930486e05'
			...
		# Usar var2 para contar var em inteiro.
			var2 = len(var)
			...
		# var permanece str, var2 é i
			>>> var	
-------------------------------------------------------
Usando if, else, elif:

	#Exemplo 1, apenas if
		user = raw_input('Digite o user: ')
	#Atenção a identação
	if user == 'root':
		print 'Usuario valido'

	#Exemplo 2, apenas if
		user = raw_input('Digite o user: ')
		#Atencao a identacao
		user = raw_input('Digite o user: ')
		if user == 'root':
			print 'Usuario valido'
		else:
			print 'Usuario incorreto'
	#Exemplo 3, if-elif-else
		user = raw_input('Digite o user: ')
		if user == 'root':
			print 'Usuario %s valido' %user
		elif user = 'admin':
			print 'Usuario %s valido' %user
		else:
			print 'Usuario %s incorreto' %user
-------------------------------------------------------
Usando while:

	#Exemplo 1
		contador = 0
		while contador <= 4:
		print '192.168.0.%d' %contador
		contador = contador + 1
		print 'While finalizado, contador agora vale %d' %contador
	#Exemplo 2, utilizando break.
		while True:
			user = raw_input('Digite o user: ')
			print 'O user digitado foi %s' %user
			if user == 'root':
				print 'User logado'
				break
	#Exemplo 3, utilizando continue.
		Favor me adicione
-------------------------------------------------------
Usando for
	#Sintaxe
		range([inicio],[fim],[passos])
		range(6)		--> #Contagem de 0 a 6
		range(1,6)		--> #Contagem de 1 a 6
		range(5,-1,-1)	--> #Contagem de 5 a 0
		range(5,0,-1)	--> #Contagem de 5 a 1
	#Exemplo 1
		for x in range(0,5):
			print '192.168.0.%d'%x
	#Exemplo 2, utilizando listas
		lista = [1,2,3,4,5]
		for x in lista:
			print print '192.168.0.%d'%x
	#Exemplo 3, utilizando if e break
		lista = ['a',2,3,4,5]
		for x in lista:
			ip = '192.168.0.%s'%x
			print ip
			if ip == '192.168.0.3':
				break
-------------------------------------------------------
Listas(1) e Slices #Conceitos
	#Declarar uma lista
		var1 = list()
		var2 = [,]
		var3 = [[],[]] --> Listas dentro de lista
		#Chama-se cada posição de index, iniciando-se por 0.
		var = [index0, index1, 'index3']
	#Exemplo 1
		var = [1,2,3]
		print var[1]
		...output --> 2, #Pois o índice 1 é o nº 2.
	#Exemplo 2 - Somando index
		var1 = [1,2,3]
		var2 = [1,2,3]
		print var1[0] + var2[2]
		...output --> 4
		
		var = [0,1,2,'ola ']
		print var[3] + "humano"
		...output --> 'ola humano'
	#Exemplo 3 - Listas dentro de Listas
		var = [[0,1,2],[3,4,5]]
		print var[0][0]	
		...output --> 0	#Exibe o index 0 posição 0
	
		var = [[0,1,2],[3,4,5]]
		print var[1][0]		
		...output --> 3 #Exibe o index 1 posição 0
	#Exemplo 4 - Listas com índices negativos
		var = [1,2,3,0]
		print var[-1]
		...output --> 0 #Exibe o último valor da lista

		var = [[1,2,3],[4,5,0]]
		print var[-1][-1]
		...output --> 0 #Exibe o último valor do índex 1.
	#Exemplo 5 - Alterando valores dos indexes
		var = [1,2,3,4]
		var = [0] = 5
		print var
		[5,2,3,4]
	#Exemplo 6 - Concatenando listas
		var1 = [1,2]
		var2 = ['a','b']
		print var1 + var2
		output... --> [1, 2, 'a', 'b']

		var1 = [1,2]
		print var1 * 2
		...output --> [1,2,1,2]
	#Exemplo 7 - Adicionando valores
		var = []
		var.append(1)
		var.append('ola')
		print var
		...output --> [1,'ola']

		var = [[],[]]
		var[0].append(1)
		var[1].append('ola')
		print var
		...output --> [[1], ['ola']]
	#Exemplo 8 - Removendo valores
		var = [1,2]
		del var[0]
		print var
		...output --> [2]

		var = [[0,1],[2,3]]
		del var[0][0]
		print var
		...output --> [[1], [2, 3]]
Slices
	var = ['ola','seres','humanos','e','fabulosos']
	#O slice : Vai até a posição X, porém não a exibe.
	var[:],var[0:],var[:5],var		#Vai até o fim da lista.
	var[0:2]	#Vai da posição 0 a 2, mas só exibe até a 1.
	var[0::4]	#Exibe o index 0 e 4
	var[0:-2]	#Exibe o index 0 e 2
-------------------------------------------------------
Listas(2) #Utilização
	
	#Atribuição Múltipla
		var = [1,2]
		var1,var2 = var
	#Inserindo valores em loop com for
		var = list() #Pode ser var = []
		for x in range(0,11):
			var.append(x)
		print var	
	#Modo Arcaico com for
		var = list() #Pode ser var = []
		for x in range(0,3):
			resp = raw_input('Digite um numero: ')
			var.append(x)
		print var	
	#Modo Correto com for
		var = list() #Pode ser var = []
		for x in range(0,3):
			var.append(raw_input('Digite um valor: '))
		print var
	#Utilizando while
		var = list()
		while True: 			#Assume que sera inserido uma mensagem.
			msg = raw_input('Digite algo: ')
			if msg:				#Se inserir mensagem
				var.append(msg) #Adicione na lista
			else:				#Se não, pare.
				break
		print var
	#Lendo valores
		#Exemplo 1
		var = list()
		while True: 		
			msg = raw_input('Digite algo: ')
			if msg:				
				var.append(msg) 
			else:				
				break

		for valor in var:		
			print valor
		
		#Exemplo 2
		var = list()
		while True: 		
			msg = raw_input('Digite algo: ')
			if msg:				
				var.append(msg) 
			else:				
				break

		for valor in var:
			if valor == 'root':	
				print 'Usuario root existe no sistema'
	#In e not in
		#Verificar se um valor foi digitado
		lista = [1,2,3,4,5]
		if 1 in lista:
			print 'Existe o valor 1'
		else:
			print 'Nao existe o valor 6'

		lista = [1,2,3,4,5]
		if 1 not in lista:
			print 'Dados corretos'

		#Exemplo com String
		msg = 'Eu vou destruir a Copa'
		if 'destruir' and 'Copa' in msg:
			print 'alerta'
Métodos:
	var = [1,2,3,4,5]
	var2 = [6,7,8,9,0]
	var.index()		#Localiza o valor do index
	var.append()	#Adiciona o valor no final da lista
	var.insert()	#Adiciona o valor na posição escolhida
	var.extend()	#Adicionar o valor de var1 em var2
		var.extend(var2) #Não consegue se adicionar 'str'.
		var.extend('Oi') ...output var --> [1,2,3,4,5,'O','i'] 	
	var.remove()	#Remove uma posição 'primeira aparição'
	var.pop()		#Remove uma objeto do índice
	var.sort()		#Ordena em ordem alfabética
	var.reverse()	#Inverte o estado atual da lista
	var.count()		#Conta as aparições do item na lista	
-------------------------------------------------------
Tuplas:

	#Strings são dados imutáveis
	#Diferentes de Listas, onde pode-se mudar o seu conteúdo.

	#Tuplas são listas não mutáveis.

	#Exemplo 1 - Declarando Tuplas
		var = ()
		type(var)
		output... -> <type 'tuple'>

		var = tuple()
		type(var)
		output... -> <type 'tuple'>
	#Exemplo 2 - Adicionando apenas um valor
		var = ('valor 1',)
		Obs: A diferença de uma tupla para uma string é:
			string = ('Eu sou uma string')
			...
			string = 'Eu sou uma string'
			...
			tupla = ('Eu', 'sou','uma','tupla')
	#Exemplo 3 - Transformar tupla em lista
		var = ('aula','de','python')
		>>> list(var)
		output... -> ['tupla', 'de','python']
		type(var)			#Var continua sendo uma tupla
			<type 'tuple'>
		
		var = list(var) 
		type(var)			#Var agora é uma lista
			<type 'list'>
-------------------------------------------------------
Dicionários:
	#Elementos parecidos com listas, porém não são ordenados.

	#Dicionários possuem índices definidos pelo programador
	
		var = {'indice1':'valor', 'indice2': 'valor'}
		var = ['indice1']
		...output -> 'valor'

	#Exemplo 1 - Exibindo listas
		var = {'ip':'192.168.0.1','port':'80'}
		var['ip']+':'+str(var['port'])
		output... -> '192.168.0.1:80'
		#Obs: Também podemos adicionar índices com valores inteiros.
		var{'id' = 1}
		var['id']
		output -> 1
	#Exemplo 2 - Inserir, alterar, excluir valores
		#Alterar valores
		var['ip'] = '172.16.0.254'
		#Adicionar índice
		var['service'] = 'http'
		#Excluir índice:valor
		del var['service']
	#Exemplo 3 - Keys, values e items
		#Exibir apenas os índices
		var.keys()
		#Exibir apenas os valores
		var.values()
		#Exibir índices:valores	
		var.items()
		#Acessando item especifico:
		var.items()[1]
	#Exemplo 4 - Utilizando loops
		for indice,valor in var.items():
	 		print indice,valor
 
 		output...
			ip 192.168.0.1
			port 80
			service http
	#Exemplo 5 - Verificar existência de índices(in, not in)
		var = {'ip':'192.168.0.1', 'port':'80'}
			'ip' in var
				True
			'ip' not in var
				False
 	#Exemplo 6 - Funçao get() - retorna valores
 		var = {'ip':'192.168.0.1', 'port':'80'}
 		
 		var.get('ip','not founded')
			output... -> '192.168.0.1'
		var.get('host','not founded')
			output... -> 'not founded'
	#Exemplo 7 - Função setdefault()
		var = {'ip':'192.168.0.1', 'port':'80','service':'http'}
		#Service sempre será http
		var.setdefault('service','http')
-------------------------------------------------------
Manipulando strings:

	#Utilidades:
	#Obs úteis para análise de log - Testar com logs DNS, DHCP, apache
		upper()		- Transforma string em maiúscula
		lower() 	- Transforma string em minúscula
		isupper() 	- Verifica se string é maiúscula
		islower() 	- Verifica se string é minúsucula
		isalpha() 	- Somente letras, não vazia
		isnum()   	- Somente letras e números, não vazia
		isdecimal() - Somente números, não vazia
		isspace() 	- Somente espaço, tabulações e quebras de linha, não vazia
		istitle() 	- Somente strings que tenham a primeira letra em maiúsculo e o restante minúsculo.
		startswith()- Verifica se a string começa com a string informada
		endswith()	- Verifica se a sintrg termina com a string informada
		join()		- Concatenar lista
		split()		- Dividir string e gerar lista
		rstrip()	- Remove espaço da direita
		lstrip()	- Remove espaço da esquerda
		strip()		- Remove espaços em ambos os lados
-------------------------------------------------------
Funções:
	#Variáveis dentro de funções são locais, não globais.

	#Funções repetem tarefas
		def hello():
			print 'Hello World'

		>>> hello()
			...output -> 'Hello World'
	#Utilizando parâmetros
		def hello(thing)
			print 'Hello %s' %thing

		>>> hello('Mundo') #Pode-se passar qualquer valor ou string.
			...output -> 'Hello Mundo'
	#Variáveis locais e globais
		
		#Exemplo1
			def hello():
				var = 'Hello World'
				print var

			>>> var = 'Goodbye World'
				
				#Local
				>>>
				...output -> 'Hello World'
				#Global
				>>> var
				...output -> 'Goodbye World'
	#Retornar valor em variáveis globais
		def hello():
			var = 'Ola'
			return var #Retorna o valor para o programa(global)

		>>> hello()
		...output ->  'Ola' #Ele está RETORNANDO o valor, não printando 
		#Solução1:
			var_global = hello()
			>>> var_global
			output... -> 'Ola'
		#Solução2
			def hello():
				var1 = 'Ola'
				var2 = 'Mundo'
				return var, var2

			>>> hello()
			('Ola', 'Mundo')
		#Manipulando o Return
			>>> var1,var2 = hello()
			>>> var1
			'Ola'
			>>> var2
			'Mundo'
			>>> var_global = hello()
			>>> var_global
			('Ola', 'Mundo')

			>>> type(var_global) #Agora a variável global é uma tupla
			<type 'tuple'>
			>>> var_global[1]
			'Mundo'
	#Tratando Exceções
		def hello():
			try:
				var = 'Hello World'
				print var
			except: #Pode-se usar 'except Exception as e' -- Print o erro original.
				print 'error'

		#Exemplo1
			def conta(x):
				var = 10/x
				print var
			>>> conta(5)
				2
			>>> conta(0)
				Traceback (most recent call last):
				  File "<stdin>", line 1, in <module>
				  File "<stdin>", line 2, in conta
				ZeroDivisionError: integer division or modulo by zero
		#Exemplo2
			def conta(x):
				try:
            		var = 10/x
             		print var
     			except:
            		 print 'Impossivel dividir por Zero'

				>>> conta(5)
				2
				>>> conta(0)
				Impossivel dividir por Zero
		#Exemplo3
			def conta(x):
				try:
					print 10/x
	     		except Exception as e:
    	         	print str(e)
 
			>>> conta(5)
			2
			>>> conta(0)
			integer division or modulo by zero
-------------------------------------------------------
Módulos(request):

	#Para instalar módulos no python é necessário instalar o pip.
		curl https://bootstrap.pypa.io/get-pip.py | python
	#Opções de utilização:
		pip install requests #Instala o módulo requests (HTTP)
		pip install --upgrade requests #Verifica se há atualizações do módulo
		pip install -r dependencies.txt #Instala módulos a partir de uma lista.
		pip unninstal requests #Remove o módulo requests
	#Utilizando Módulos
		#1 - Importa o módulo requests
			import requests 
			requests.get('http://www.uol.com.br')
		#2 - Importa o módulo, renomeando-o para r.
			import requests as r 
			r.get('http://www.uol.com.br')
		#3 - Importa apenas o método get, do módulo requests
			from requests import get
			get('http://uol.com.br')
		#4 - Importa os métodos get e post do módulo requests
			from requests import get,post 
		#5 - Importa o método get do módulo requests renomeando-o para g.
			from requests import get as g
			g('http://uol.com.br')
-------------------------------------------------------
Módulos(os):
	
	#Interface para ações do OS

	Utilização:
		import os

	Métodos:
		os.path.join()		#Cria o path mantendo compatibilidade do código
			#Exemplo(linux):
				os.path.join('/root','Documents')
				...output ->'/root/Documents'
			#Exemplo(windows):
				os.path.join('C','Documents')
				...output ->'C:/Documents'
			#Utilizando listas
				files = ['teste1','teste2','teste3']
				for file in files:
					print os.path.join('/root','Documents')
				
				/root/Documents
				/root/Documents
				/root/Documents
		os.getcwd()			#Exibe o diretório atual
			os.getcwd()
			/root/Documents/Python
		os.chdir()			#Trocar de diretório
			os.chdir('/root/Documents')
			os.getcwd()
			'/root/Documents'
		os.makedirs()		#Cria diretórios // Pode-se passar o path
			os.makedirs('teste')
			os.listdir(os.getcwd())
			['consulta.txt', 'First.py', 'testes.py', 'teste']
		os.path.abspath()	#Retorna o path absoluto
			os.path.abspath('/root')
			'/root'
		os.path.isabs()		#Retorna True se o path for absoluto
			os.path.isabs('/root/Documents/')
			True
			os.path.isabs('../')
			False
		os.path.relpath()	#Retorna o path relativo dado um início
			os.getcwd()
			'/root'
			os.path.relpath('/var')
			'../var'
		os.path.dirname()	#Retorna uma string com tudo antes da última barra
			os.path.dirname('/root/Documents/general/commands/Python/First.py')
			'/root/Documents/general/commands/Python'
		os.path.basename()	#Retorna um string com tudo depois da última barra
			os.path.basename('/root/Documents/general/commands/Python/First.py')
			'First.py'
		os.path.split()		#Retorna Tupla com dirname e basename
			os.path.split('/root/Documents/general/commands/Python/First.py')
			('/root/Documents/general/commands/Python', 'First.py')
		os.path.sep()		#Remove as barras
			os.path.sep
			'/'
			os.getcwd().split(os.path.sep)
			['', 'root', 'Documents', 'general', 'commands', 'Python']
		os.path.getsize()	#Retorna o tamanho do path em bytes
			os.listdir(os.getcwd())
			['consulta.txt', 'First.py', 'testes.py', 'teste']
			os.path.getsize('consulta.txt')
			18409 #bytes
		os.listdir()		#Retorna lista de string com o nome de arquivos e diretórios
			os.listdir('.')
			['teste1', '1.txt', 'teste2', '2.txt', 'teste3']
			os.listdir(os.getcwd())
			['consulta.txt', 'First.py', 'testes.py', 'teste']
		os.path.exists()	#Retorna True se o arquivo ou diretório existir
			os.path.exists('/root/Documents/teste.txt')
			False
		os.path.isdir()		#Retorna True se o path for referente a um diretório
			os.path.isdir('/root/Documents/')
			True
		os.path.isfile()	#Retorna True se o path for referente a um arquivo
			os.path.isfile('/root/Documents/')
			False
	#Listagem de arquivos recursiva -- ls -R
		import os
		for pasta, subpastas, arquivos in os.walk('/root/teste_main/'):
			print 'Pasta atual %s' %pasta
			for subpasta in subpastas:
				print '\t%s/%s' %(pasta,subpasta)
			for arquivo in arquivos:
				print '\t%s/%s' %(pasta,arquivo)

		#Saída
		root@:~# python /root/Python/testes.py
			Pasta atual /root/teste_main/
				/root/teste_main/teste1
				/root/teste_main/teste2
				/root/teste_main/teste3
				/root/teste_main/1.txt
				/root/teste_main/2.txt
			Pasta atual /root/teste_main/teste1
				/root/teste_main/teste1/3.txt
			Pasta atual /root/teste_main/teste2
				/root/teste_main/teste2/4.txt
			Pasta atual /root/teste_main/teste3
				/root/teste_main/teste3/5.txt

-------------------------------------------------------
Ler arquivos:

	#Abrindo arquivos
		f = open('log.txt')
		type(f)
		type <'file'>
	#Lendo arquivos com read()
		f.read()
		f = f.read()	#Realiza apenas a leitura
		>>> f
		'0   (NOERROR)  No error; successful update.\n1   (FORMERR)  Format error; DNS server did not understand the update request.\n0x2 (SERVFAIL) DNS server encountered an internal error, such as a forwarding timeout\n0x3 (NXDOMAIN) A name that should exist does not exist.\n0x4 (NOTIMP)   DNS server does not support the specified Operation code.\n0x5 (REFUSED)  DNS server refuses to perform the update because\n0x6 (YXDOMAIN) A name that should not exist does exist.\n0x7 (YXRRSET)  A resource record set that should not exist does exist.\n0x8 (NXRRSET)  A resource record set that should exist does not exist.\n0x9 (NOTAUTH)  DNS server is not authoritative for the zone named in the Zone section.\n0xA (NOTZONE)  A name used in the Prerequisite or Update sections is not within the zone specified by'
	#Lendo arquivos com readlines() -- Retorna o arquivo em uma lista
		f.readlines()
		f = f.readlines()   #Neste exemplo funcionou
		>>> f
		['0   (NOERROR)  No error; successful update.\n', '1   (FORMERR)  Format error; DNS server did not understand the update request.\n', '0x2 (SERVFAIL) DNS server encountered an internal error, such as a forwarding timeout\n', '0x3 (NXDOMAIN) A name that should exist does not exist.\n', '0x4 (NOTIMP)   DNS server does not support the specified Operation code.\n', '0x5 (REFUSED)  DNS server refuses to perform the update because\n', '0x6 (YXDOMAIN) A name that should not exist does exist.\n', '0x7 (YXRRSET)  A resource record set that should not exist does exist.\n', '0x8 (NXRRSET)  A resource record set that should exist does not exist.\n', '0x9 (NOTAUTH)  DNS server is not authoritative for the zone named in the Zone section.\n', '0xA (NOTZONE)  A name used in the Prerequisite or Update sections is not within the zone specified by']
	#Atribuindo para outra variável:	
		#O método correto para se declarar em outra variável é:
			#f = open('arquivo.txt').read() // readlines()
			#var = f
		log = f.read() 		#Utilizando variável com outro nome não funcinou
		f = f.readlines()   #Neste exemplo funcionou
		>>> f
			['0   (NOERROR)  No error; successful update.\n', '1   (FORMERR)  Format error; DNS server did not understand the update request.\n', '0x2 (SERVFAIL) DNS server encountered an internal error, such as a forwarding timeout\n', '0x3 (NXDOMAIN) A name that should exist does not exist.\n', '0x4 (NOTIMP)   DNS server does not support the specified Operation code.\n', '0x5 (REFUSED)  DNS server refuses to perform the update because\n', '0x6 (YXDOMAIN) A name that should not exist does exist.\n', '0x7 (YXRRSET)  A resource record set that should not exist does exist.\n', '0x8 (NXRRSET)  A resource record set that should exist does not exist.\n', '0x9 (NOTAUTH)  DNS server is not authoritative for the zone named in the Zone section.\n', '0xA (NOTZONE)  A name used in the Prerequisite or Update sections is not within the zone specified by']
	#Tratando a saída do arquivo
		f = open('log.txt')
		f = f.readlines()
		for valor in f:
			if not valor.isspace():	#Se o valor não for 'isspace'
				print valor.strip() 
		
		0   (NOERROR)  No error; successful update.
		1   (FORMERR)  Format error; DNS server did not understand the update request.
		0x2 (SERVFAIL) DNS server encountered an internal error, such as a forwarding timeout
		0x3 (NXDOMAIN) A name that should exist does not exist.
		0x4 (NOTIMP)   DNS server does not support the specified Operation code.
		0x5 (REFUSED)  DNS server refuses to perform the update because
		0x6 (YXDOMAIN) A name that should not exist does exist.
		0x7 (YXRRSET)  A resource record set that should not exist does exist.
		0x8 (NXRRSET)  A resource record set that should exist does not exist.
		0x9 (NOTAUTH)  DNS server is not authoritative for the zone named in the Zone section.
		0xA (NOTZONE)  A name used in the Prerequisite or Update sections is not within the zone specified by
-------------------------------------------------------
Escrever Arquivos:

	Métodos:
		w - write 	#Escrita
		a - append 	#Adição
		r - read	#Leitura (built in)
		b - binary	#Binário

	#Exemplo1 - Write
		f = open('teste.txt','w')
		f.write('Hello World')
		f.close()
		f = open('teste.txt','r')
		f.read()
		'Hello World'
	#Exemplo2 - Write
		f = open('teste.txt','w')
		f.write('Hello World')
		f.close()
		f = open('teste.txt').read()
		f
		'Hello World'
	#Exemplo3 - Append
		f = open('teste.txt','a')
		f.write('Hello World, again.')
		f.close()
		f = open('teste.txt').read()
		f
		'Hello World\nHello World, again.'
	#Exemplo4 - Binário
		import requests
		url = 'https://sourceforge.net/projects/gnuwin32/files/wget/1.11.4-1/wget-1.11.4-1-setup.exe/'
		r = requests.get(url)
		f = open('saida.exe','ab')
		f.write(r.content)
		f.close()

		root@:~# ls
		saida.exe
		root@:~# file saida.exe 
		saida.exe: PE32 executable (GUI) Intel 80386, for MS Windows
-------------------------------------------------------
Organizar Arquivos:

		Métodos:
		shutil.copy()	#Copia arquivos -- Pode-se passar outro diretório para o arquivo destino
			os.listdir('.')
			['teste1', '1.txt', 'teste2', '2.txt', 'teste3']
			shutil.copy('1.txt','1.1.txt')
			os.listdir('.')
			['teste1', '1.1.txt', '1.txt', 'teste2', '2.txt', 'teste3']
		shutil.move()	#Move ou sobescreve arquivos
			shutil.copy('1.txt','1.1.txt')
			os.listdir('.')
			['teste1', '1.1.txt', '1.txt', 'teste2', '2.txt', 'teste3']
			shutil.move('1.1.txt','1.2.txt')
			os.listdir('.')
			['teste1', '1.txt', '1.2.txt', 'teste2', '2.txt', 'teste3']
			shutil.move('1.2.txt','teste1')
			os.listdir('.')
			['teste1', '1.txt', 'teste2', '2.txt', 'teste3']
			os.listdir('teste1')
			['3.txt', '1.2.txt']
		os.unlink()		#Apaga arquivos
			os.listdir('.')
			['teste1', '1.txt', 'teste2', '2.txt', 'teste3']
			os.unlink('1.txt')
			os.listdir('.')
			['teste1', 'teste2', '2.txt', 'teste3']
		os.rmdir()		#Apaga diretórios vazios
			os.rmdir('teste')

			Traceback (most recent call last):
  			File "<stdin>", line 1, in <module>
			OSError: [Errno 2] No such file or directory: 'teste'

			os.unlink('teste1/3.txt')
			os.unlink('teste1/1.2.txt')
			os.rmdir('teste')
			os.listdir('.')
			['teste1', 'teste2', '2.txt', 'teste3']
			os.rmdir('teste1')
			os.listdir('.')
			['teste2', '2.txt', 'teste3']
		shutil.rmtree()	#Apaga diretório e seu conteúdo
			os.listdir('.')
			['2.txt', 'teste3']
			os.listdir('teste3')
			['5.txt']
			shutil.rmtree('teste3')
			os.listdir('.')
			['2.txt']
-------------------------------------------------------

-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------


