# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:00:39 2017

@AUTHor: rauli
"""

from flask import Flask, request, jsonify, abort, make_response, session, render_template
from flask_httpAUTH import HTTPBasicAUTH
from datetime import datetime
import sqlite3
import json
import hashlib
import numbers

DBNAME = './quiz.db'


def lambda_handler(event, context):
    """Handler do evento."""
    try:

        def not_equals(first, second):
            if isinstance(first, numbers.Number) and isinstance(
                    second, numbers.Number):
                return abs(first - second) > 1e-3
            return first != second

        ndes = int(event['ndes'])
        code = event['code']
        args = event['args']
        resp = event['resp']
        diag = event['diag']
        exec (code, locals())

        test = []
        for index, arg in enumerate(args):
            if not 'desafio{0}'.format(ndes) in locals():
                return "Nome da função inválido. Usar 'def desafio{0}(...)'".format(
                    ndes)

            if not_equals(eval('desafio{0}(*arg)'.format(ndes)), resp[index]):
                test.APPend(diag[index])

        return " ".join(test)
    except:
        return "Função inválida."


def converte_data(orig):
    """Converte a data"""
    return orig[8:10] + '/' + orig[5:7] + '/' + orig[0:4] + ' ' + orig[
        11:13] + ':' + orig[14:16] + ':' + orig[17:]


def get_quizes(user):
    """Pega os dados dos quizes no banco de dados"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    if user == 'admin' or user == 'fabioja':
        cursor.execute("SELECTthe_identification, numb from QUIZ".format(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    else:
        cursor.execute(
            "SELECTthe_identification, numb from QUIZ where release < '{0}'".
            format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    info = [reg for reg in cursor.fetchall()]
    conn.close()
    return info


def get_user_quiz(userid, quizid):
    """Pega o quiz do usuário no banco de dados"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute("""SELECT sent,answer,result from USERQUIZ 
        where userthe_identification= '{0}' and quizthe_identification= {1} order by sent desc"""
                   .format(userid, quizid))
    info = [reg for reg in cursor.fetchall()]
    conn.close()
    return info


def set_user_quiz(userid, quizid, sent, answer, result):
    """Coloca o quiz do usuário no banco de dados"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    cursor.execute(
        "insert into USERQUIZ(userid,quizid,sent,answer,result) values (?,?,?,?,?);",
        (userid, quizid, sent, answer, result))

    conn.commit()
    conn.close()


def get_quiz(the_identification, user):
    """Pega o quiz do banco de dados"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    if user == 'admin' or user == 'fabioja':
        cursor.execute(
            "SELECTthe_identification, release, expire, problem, tests, results, diagnosis, numb from QUIZ wherethe_identification= {0}"
            .format(the_identification))
    else:
        cursor.execute(
            "SELECTthe_identification, release, expire, problem, tests, results, diagnosis, numb from QUIZ wherethe_identification= {0} and release < '{1}'"
            .format(id,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    info = [reg for reg in cursor.fetchall()]
    conn.close()
    return info


def set_info(pwd, user):
    """Coloca as informações no banco de dados"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE USER set pass = ? where user = ?", (pwd, user))
    conn.commit()
    conn.close()


def get_info(user):
    """ Pega os dados do usuário"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT pass, type from USER where user = '{0}'".format(user))
    print("SELECT pass, type from USER where user = '{0}'".format(user))
    info = [reg[0] for reg in cursor.fetchall()]
    conn.close()
    if len(info) == 0:
        return None

    return info[0]


AUTH = HTTPBasicAUTH()

APP = Flask(__name__, static_url_path='')
APP.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?TX'


@APP.route('/', methods=['GET', 'POST'])
@AUTH.login_required
def main():
    """Rotina de acionar o banco de dados"""
    msg = ''
    ponto_p = 1
    challenges = get_quizes(AUTH.username())
    sent = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if request.method == 'POST' and 'the_identification' in request.args:
        the_identification = request.args.get('the_identification')
        quiz = get_quiz(the_identification, AUTH.username())
        if len(quiz) == 0:
            msg = "Boa tentativa, mas não vai dar certo!"
            ponto_p = 2
            return render_template('index.html',
                                   username=AUTH.username(),
                                   challenges=challenges,
                                   ponto_p=ponto_p,
                                   msg=msg)

        quiz = quiz[0]
        if sent > quiz[2]:
            msg = "Sorry... Prazo expirado!"

        f = request.files['code']
        filename = './upload/{0}-{1}.py'.format(AUTH.username(), sent)
        f.save(filename)
        with open(filename, 'r') as fp:
            answer = fp.read()

        args = {
            "ndes": the_identification,
            "code": answer,
            "args": eval(quiz[4]),
            "resp": eval(quiz[5]),
            "diag": eval(quiz[6])
        }

        feedback = lambda_handler(args, '')

        result = 'Erro'
        if len(feedback) == 0:
            feedback = 'Sem erros.'
            result = 'OK!'

        set_user_quiz(AUTH.username(), the_identification, sent, feedback,
                      result)

    if request.method == 'GET':
        if 'the_identification' in request.args:
            the_identification = request.args.get('the_identification')
        else:
            the_identification = 1

    if len(challenges) == 0:
        msg = "Ainda não há desafios! Volte mais tarde."
        ponto_p = 2
        return render_template('index.html',
                               username=AUTH.username(),
                               challenges=challenges,
                               ponto_p=ponto_p,
                               msg=msg)

    quiz = get_quiz(the_identification, AUTH.username())

    if len(quiz) == 0:
        msg = "Oops... Desafio invalido!"
        ponto_p = 2
        return render_template('index.html',
                               username=AUTH.username(),
                               challenges=challenges,
                               ponto_p=ponto_p,
                               msg=msg)

    answers = get_user_quiz(AUTH.username(), the_identification)

    return render_template('index.html',
                           username=AUTH.username(),
                           challenges=challenges,
                           quiz=quiz[0],
                           e=(sent > quiz[0][2]),
                           answers=answers,
                           ponto_p=ponto_p,
                           msg=msg,
                           expi=converte_data(quiz[0][2]))


@APP.route('/pass', methods=['GET', 'POST'])
@AUTH.login_required
def change():
    """Rotina de mudar dados no banco de dados"""
    if request.method == 'POST':
        velha = request.form['old']
        nova = request.form['new']
        repet = request.form['again']

        ponto_p = 1
        msg = ''
        if nova != repet:
            msg = 'As novas senhas nao batem'
            ponto_p = 3
        elif get_info(AUTH.username()) != hashlib.md5(
                velha.encode()).hexdigest():
            msg = 'A senha antiga nao confere'
            ponto_p = 3
        else:
            set_info(hashlib.md5(nova.encode()).hexdigest(), AUTH.username())
            msg = 'Senha alterada com sucesso'
            ponto_p = 3
    else:
        msg = ''
        ponto_p = 3

    return render_template('index.html',
                           username=AUTH.username(),
                           challenges=get_quizes(AUTH.username()),
                           ponto_p=ponto_p,
                           msg=msg)


@APP.route('/logout')
def logout():
    """Faz logout"""
    return render_template('index.html', ponto_p=2,
                           msg="Logout com sucesso"), 401


@AUTH.get_password
def get_password(username):
    """Pega a senha"""
    return get_info(username)


@AUTH.hash_password
def hash_pw(password):
    """Senha"""
    return hashlib.md5(password.encode()).hexdigest()


if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=80)
