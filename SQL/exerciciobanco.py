import sqlite3

conexao = sqlite3.connect('bancodedados')
cursor = conexao.cursor()



# Resolução do Exercicios Banco de Dados (SQL)


# crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).

#resultado = cursor.execute('''create table alunos(id INTERGER, nome VARCHAR(250), idade INTERGER, curso VARCHAR(250))''')

# Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior

#resultado = cursor.execute('''INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "João", 21, "Dados"), (2, "Maria", 19, "Medicina"), (3, "Pedro", 23, "Direito"), (4, "Ana", 25, "Administração"), (5, "Paulo", 30, "Engenharia")''')

#Consultas Básicas

# Escreva consultas SQL para realizar as seguintes tarefas:
    #a) Selecionar todos os registros da tabela "alunos".

#resultado = cursor.execute('''select * from alunos''')
#for item in resultado:
 #   print(item)

    #b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

#resultado = cursor.execute('''select nome, idade from alunos where idade > 20''')
#for item in resultado:
 #   print(item)

    #c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

#resultado = cursor.execute('''select * from alunos where curso = "Engenharia" order by nome''')
#for item in resultado:
  #  print(item)

    #d) Contar o número total de alunos na tabela

#resultado = cursor.execute('''select count(*) from alunos''')
#for item in resultado:
  #  print(item)

# 4. Atualização e Remoção

        # a) Atualize a idade de um aluno específico na tabela.

#resultado = cursor.execute('''update alunos set idade = 25 where id = 1''')
#for item in resultado:
 #   print(item)

        #b) Remova um aluno pelo seu ID.

#resultado = cursor.execute('''delete from alunos where id = 1''')
#for item in resultado:
 #   print(item)

# 5. Criar uma Tabela e Inserir Dados

#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

#resultado = cursor.execute('''create table clientes (id INTEGER primary key, nome VARCHAR(250), idade INTEGER, saldo FLOAT)''')

#resultado = cursor.execute('''insert into clientes (id, nome, idade, saldo) values (1, "João", 21, 1000), (2, "Maria", 22, 200), (3, "Pedro", 23, 500), (4, "Clara", 40, 1200), (5, "Paulo", 25, 300)''')
#for item in resultado:
 #   print(item)


# 6. Consulta e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:

        #a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

#resultado = cursor.execute('''select nome, idade from clientes where idade >=30''')
#for item in resultado:
 #   print(item)

        #b) Calcule o saldo médio dos clientes.

#resultado = cursor.execute('''select AVG(saldo) from clientes''')
#for item in resultado:
 #   print(item)


        #c) Encontre o cliente com o saldo máximo.

#resultado = cursor.execute('''select nome from clientes where saldo = (select max(saldo) from clientes)''')
#for item in resultado:
 #   print(item)



        #d) Conte quantos clientes têm saldo acima de 1000.

#resultado = cursor.execute('''select count(*) from clientes where saldo >=1000''')
#for item in resultado:
 #   print(item)


#7. Atualização e Remoção com Condições

        # a) Atualize o saldo de um cliente específico.

#resultado = cursor.execute('''update clientes set saldo = 3500 where id =2''')

        # b) Remova um cliente pelo seu ID.

#resultado = cursor.execute('''delete from clientes where id = 5''')
 
# 8. Junção de Tabelas

#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 

#resultado = cursor.execute('''CREATE TABLE compras (id INTEGER PRIMARY KEY, cliente_id INTEGER, produto VARCHAR(250), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id));''')
#resultado = cursor.execute('''insert into compras (id, cliente_id, produto, valor) values (1,1, 'caneta', 15.0), (2,1,"Lapis", 1.50), (3, 2, "caderno", 20.0)''')

# Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

resultado = cursor.execute('''select c.nome, co.produto, co.valor from compras as co inner join clientes as c on c.id = co.cliente_id''')
for item in resultado:
    print(item)


# as informações só são enviadas quando chegar nesse comando
conexao.commit()

# encerra o processo
conexao.close 
