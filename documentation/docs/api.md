# Servidor de Desafios API

# adduser.py
Adiciona novo usuário ao quiz.db para cada usuário no arquivo users.csv.

## add_user(user, pwd, tipe)
Adiciona novo usuário ao quiz.db, faz commit das mudanças e fecha a conexão.

# desafio.py
Arquivo a ser enviado ao sistema.

## desafio1(number)
Função que retorna o valor encontrado.

# softdes.py
Software desenvolvido pelo professor Raul Ikeda para a disciplina Design de Software como servidor de desafios. Considere este o algoritmo Python principal do Servidor de Desafios. Abaixo, listadas as funções disponíveis.

## lambda_handler(event, context)
Lida com o lambda. Dentro dele, há a função not_equals(first, second) que é utilizada para lidar com o lambda. Em condições normais de temperatura e pressão, você não deve utilizar esta função explicitamente.

## converteData(orig)
Função de conversão de datas para tradução. Em condições normais de temperatura e função, você não deve utilizar esta função explicitamente.

## get_quizer(user)
Pega todos os quizes de um usuário específico.

## get_user_quiz(user_id, quiz_id)
Pega um quiz específico de um usuário específico.

## set_user_quiz(userid, quizid, sent, answer, result)
Insere no banco de dados a resposta enviada por um usuário para um quiz. 

## get_quiz(id, user)
Pega o quiz de um usuário no banco de dados.

## set_info(pwd, user)
Estabelece ou atualiza a senha de login um usuário no banco de dados.

## get_info(user)
Mostra os dados de um usuário no banco de dados.

## change(void)
Altera a senha de um usuário, solicitando a senha antiga, a senha nova e uma confirmação da senha nova. Altera se a senha antiga for correta e se a confirmação de senha corresponder à senha nova.

## logout(void)
Faz logout do usuário do sistema.

## get_password(username)
Invoca a função get_info com o parâmetro username.

## hash_pw(password)
Criptografa a senha do usuário.

