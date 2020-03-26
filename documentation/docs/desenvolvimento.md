# Guia de Desenvolvimento

## Configurando o ambiente de desenvolvimento
### Instalando as dependências
Instalar as seguintes bibliotecas python:
> sqlite3 json hashlib flask

Instalar também o SQLite3 na máquina.


## Instalando o software
### Configurando O Banco de Dados
Criar o Banco de Dados da aplicação:
```bash
sqlite3 quiz.db < quiz.sql
```

### Rodando o servidor
Rode o arquivo **softdes.py**;

```bash
python3 softdes.py
```

Abra um navegador e siga para [este endereço](http://0.0.0.0:80)/


## Estrutura do Código

O código desse software se encontra dividido em 2 arquivos python.

No arquivo **softdes.py**, se encontra o código do servidor, onde ele vai fazer seguir a estrutura da [API](api.md).

No arquivo **adduser.py**, se encontra o código que adiciona novos usuários para o banco de dados.

No arquivo **quiz.sql**, se encontra a estrutura do banco de dados da aplicação.

No arquivo **user.sql**, se encontra a estrutura do banco de dados do usuário.

O arquivo **desafio.py** é a resposta de um exemplo de um desafio do software.