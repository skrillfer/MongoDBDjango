
from django.shortcuts import render
from django.db import connection
from django.forms import ModelForm
from django.http import HttpResponseRedirect

import json
import logging

import sys

import os
from django.conf.urls import  patterns, include, url
#from django.conf.urls.defaults import *
from django.views.generic.list import ListView
from django.shortcuts import render_to_response, render
from django.template import  RequestContext
from forms import *
from django.http import HttpResponse
from django.utils import timezone
from random import randint, uniform,random

import tokrules
import parser_rules

from ply.lex import lex
from ply.yacc import yacc


import socket

logger = logging.Logger('catch_all')

HOST = "localhost"
PORT = 8000

#-------------- iniciando la conexion al Servidor Java--------------------------
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.sendall("Hello\n")

data = sock.recv(1024)
print data

USER = ""

def loginUsuario(request):
    if request.method=='GET':
        form=loginForm(request.GET)
        if form.is_valid():
            username = request.GET['username']
            password = request.GET['password']
            data=paqueteLogin(username,password)
            sock.sendall(data+"\n")# se  envia la data al Servidor JAVA
            data = sock.recv(1024)#se obtiene la data que responde el Servidor JAVA
            print "JAVA:" + data
            try:
                resp_login=parsearLogin(data)
                if resp_login[0]=='true':
                        USER = username
                        print "ha ingresado " + USER
                        print resp_login[1]
                        f = open( 'some_file.txt', 'w')
                        f.write(resp_login[1])
                        f.close()
                        return HttpResponseRedirect('/home/'+ USER) # Redirect after POST
                else:
                    form= loginForm()
                    return render(request,"login.html",{'form':form})
            except Exception as e:
                if hasattr(e, 'message'):
                    print(e.message)
                else:
                    print(e)
                pass
            return HttpResponseRedirect('/home/') # Redirect after POST
            #return render(request, 'home.html')
        else:
            form= loginForm()
            return render(request,"login.html",{'form':form})


def homeView(request,anystring):
    if request.method=='GET':
        print "soy GET"
        data = {}
        print "aca:" + anystring
        data['usuario'] = anystring
        data['json'] = ""
        return render(request, 'home.html',{'data':data})

    if request.method=='POST':
        print "soy POST"
        if request.is_ajax():
            paquete = request.POST.get('paquete', None)
            if (paquete=="usql"):
                instruccion = request.POST.get('instruccion', None)
                usuario = request.POST.get('usuario', None)
                basedatos = request.POST.get('basedatos', None)
                idpet = str(randint(1000,3000))
                data  = paqueteUSQL(paquete,instruccion,usuario,idpet,basedatos)
                sock.sendall(data+"\n")# se  envia la data al Servidor JAVA
                data  = sock.recv(1024)# se obtiene la data que responde el Servidor JAVA
                x = data.split("#")
                Paq_Mess = x[0]
                Paq_Plan = x[1]
                Paq_Ply  = x[2]
                Paq_Err  = x[3]
                parametros=[]
                response_data = {}
                try:
                    parametros=parsearUSQL(Paq_Ply)
                except Exception as e:
                    if hasattr(e, 'message'):
                        print(e.message)
                    else:
                        print(e)
                    pass
                response_data['Errores'] = ""
                try:
                    response_data['Errores'] = parsearERROR(Paq_Err)
                except Exception as e:
                    if hasattr(e, 'message'):
                        print(e.message)
                    else:
                        print(e)
                    pass
                response_data['BaseDatos'] = ""
                if(len(parametros)>0):
                    response_data['BaseDatos'] = parametros[0]
                response_data['Mensajes'] = Paq_Mess
                response_data['Plan'] = Paq_Plan
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data = {}
                f = open( 'some_file.txt', 'r')
                json_str=f.read()
                f.close()
                print paquete
                json_str=json_str.replace("#","[")
                json_str=json_str.replace("$","]")
                json_str=json_str.replace("\'","\"")
                response_data['json']=json_str
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            #another_param = request.POST.get('another param', None)
            # construct your JSON response by calling a data method from elsewhere
            #items, summary = build_my_response(param, another_param)
            #return JsonResponse({'result': 'OK', 'data': {'items': items, 'summary': summary}})

def paqueteUSQL(paquete,instruccion,usuario,idpet,basedatos):
    data="["
    data+="\"paquete\":"     + "\"" + paquete     + "\"" + ","
    data+="\"instruccion\":" + "\"" + instruccion + "\"" + ","
    data+="\"usuario\":"     + "\"" +  usuario    + "\"" + ","
    data+="\"validar\":"     + idpet + ","
    data+="\"basedatos\":"   + "\"" +  basedatos    + "\""
    data+="]"
    return data

def metodoAbrir():
    print "da"

def fetch_data(request):
    print "hola"
    if request.is_ajax():
        # extract your params (also, remember to validate them)
        param = request.POST.get('param', None)
        print param
        another_param = request.POST.get('another param', None)
        # construct your JSON response by calling a data method from elsewhere
        items, summary = build_my_response(param, another_param)
        return JsonResponse({'result': 'OK', 'data': {'items': items, 'summary': summary}})
    return HttpResponseBadRequest()

def paqueteLogin(username,password):
    data="["
    data+="\"validar\":" + str(randint(1000,3000)) + ","
    data+="\"login\":" + " ["
    data+="\"usuario\":" + "\"" +  username + "\","
    data+="\"password\":" + "\"" + password + "\""
    data+="]"
    data+="]"
    return data

def parsearLogin(data):
    print "hola"
    lexer = lex(module=tokrules)
    parser = yacc(module=parser_rules)
    ast = parser.parse(data, lexer)
    resp_login = [ast.hijos[2].hijos[0].hijos[2].getValor(),ast.hijos[1].getValor()]
    return resp_login

def parsearUSQL(data):
    lexer = lex(module=tokrules)
    parser = yacc(module=parser_rules)
    ast = parser.parse(data, lexer)
    x = [ast.hijos[1].getValor(),ast.hijos[2].getValor()] #el tamano del arreglo al final deberia ser 3
    #        basedatos          , idpet
    return x
    #x[0]=  -> se obtiene el nombre de la base de datos que se usa
    #x[1]=  -> se obtiene el id de la peticion
    #de ultimo deberia agregar la cadena de datos

def parsearERROR(data):
    lexer = lex(module=tokrules)
    parser = yacc(module=parser_rules)
    print data
    ast = parser.parse(data, lexer)
    if(len(ast.hijos[1].hijos)==0):
        print "errores ninugno"
    elif (len(ast.hijos[1].hijos)==1):
        data_JSON ="[";
        listaNods = ast.hijos[1].hijos[0]
        for erro_r in listaNods.hijos:
            str1 = erro_r.hijos[0]
            data_JSON += "{" ;
            data_JSON += "\"tipo\":"+ "\"" + str1.hijos[0].getValor()+ "\",";
            data_JSON += "\"mensaje\":"+ "\"" + str1.hijos[1].getValor()+ "\",";
            data_JSON += "\"fila\":"+ "\"" + str1.hijos[2].getValor()+ "\",";
            data_JSON += "\"columna\":"+ "\"" + str1.hijos[3].getValor()+ "\"";
            data_JSON += "},"
        data_JSON = data_JSON[0:-1]
        data_JSON +="]"
        return  data_JSON
