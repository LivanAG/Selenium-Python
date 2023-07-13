
from distutils.log import error
import this
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import tkinter as tk
from tkinter import ttk
from functools import partial
from tkinter import *
from datetime import date
from datetime import datetime
from selenium.webdriver.common.by import By


def slow_typing(element, text):
   
    element.send_keys(text)
        
def killcookies(driver):
    cookie_b = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("id", "allowAllCookiesBtn"))
    cookie_b.click()

def login(driver):

    flag = False

    try:

        username =WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[1]/div/div[1]/div[3]/div/div/div[2]/form/div/div/div[1]/div/div[1]/div/input'))
        slow_typing(username, 'andreasantamaria')

        
        password = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[1]/div/div[1]/div[3]/div/div/div[2]/form/div/div/div[1]/div/div[2]/div/input'))
        slow_typing(password, 'Andrea*29')


        button_submit = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", "/html/body/div[1]/div/div[1]/div[3]/div/div/div[2]/form/div/div/div[2]/div/button"))
        button_submit.click() 

        flag = True
        return flag

    except Exception:

        return flag


def abrir_formulario_turismo(driver):

    def llenar_form(primera_vez):
        try:
            flag = True

       
            #Select Nacionalidad
            select_element = WebDriverWait(driver, timeout=4).until(lambda d: d.find_element("xpath",'/html/body/div[1]/div/div[2]/div/div/table/tbody/tr/td/form/table[1]/tbody/tr/td[2]/select'))

            select_object = Select(select_element)
            select_object.select_by_visible_text('CUBA')
            

            #Select Nacionalidad
            select_element = WebDriverWait(driver, timeout=4).until(lambda d: d.find_element("xpath",'/html/body/div[1]/div/div[2]/div/div/table/tbody/tr/td/form/table[1]/tbody/tr[2]/td[2]/select'))
            select_object = Select(select_element)
            select_object.select_by_visible_text('CUBA')
            


            #Select Tipo de Pasaporte
            select_element = WebDriverWait(driver, timeout=4).until(lambda d: d.find_element("xpath",'/html/body/div[1]/div/div[2]/div/div/table/tbody/tr/td/form/table[1]/tbody/tr[3]/td[2]/select'))  
            select_object = Select(select_element)
            select_object.select_by_visible_text('PASSAPORTE COMUM')
            
            if primera_vez:
                killcookies(driver)

            #Select Cantidad de dias a estar
            select_element = WebDriverWait(driver, timeout=4).until(lambda d: d.find_element("xpath",'/html/body/div[1]/div/div[2]/div/div/table/tbody/tr/td/form/table[1]/tbody/tr[4]/td[2]/select'))
            select_object = Select(select_element)
            select_object.select_by_visible_text('ATÉ 90 DIAS')

            

            #Select Vienes por razones de trabajo

            select_element = WebDriverWait(driver, timeout=4).until(lambda d: d.find_element("xpath",'/html/body/div[1]/div/div[2]/div/div/table/tbody/tr/td/form/table[1]/tbody/tr[5]/td[2]/select'))
            select_object = Select(select_element)
            select_object.select_by_visible_text('NÃO')
        

            #Select Motivo de la estadia

            select_element = WebDriverWait(driver, timeout=4).until(lambda d: d.find_element("xpath",'/html/body/div[1]/div/div[2]/div/div/table/tbody/tr/td/form/table[1]/tbody/tr[6]/td[2]/select'))
            select_object = Select(select_element)
            select_object.select_by_visible_text('TURISMO')
        
            
            #Select Tienes familia de EU
            select_element = WebDriverWait(driver, timeout=4).until(lambda d: d.find_element("xpath",'/html/body/div[1]/div/div[2]/div/div/table/tbody/tr/td/form/table[1]/tbody/tr[7]/td[2]/select'))
            select_object = Select(select_element)
            select_object.select_by_visible_text('NÃO')

      
            #Boton para abrir el form
            button_open_form = WebDriverWait(driver, timeout=4).until(lambda d: d.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/table/tbody/tr/td/form/table[2]/tbody/tr/td[2]/input"))
            time.sleep(0.5)
            button_open_form.click()   
            return flag

        except Exception:
            
            flag = False
            return flag   

    
    

    button1 = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", "/html/body/div[1]/div/div[1]/div[3]/div/div/div[1]/div/ul/li[1]/a "))
    button1.click()  
    
    
    flag = llenar_form(True)


    while flag == False:
        driver.refresh()
        llenar_form(False)
    
    return True



def llenar_formulario_primera_pagina(driver,data):
    #Select Posto Consular
    select_element = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[4]/td/select'))
    select_object = Select(select_element)
    select_object.select_by_visible_text('SECÇÃO CONSULAR DA EMBAIXADA DE PORTUGAL EM HAVANA')

    apellido1 = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[6]/td[1]/input'))
    slow_typing(apellido1, data["apellido1"])

    apellido2 = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[6]/td[2]/input'))
    slow_typing(apellido2, data["apellido2"])

    nombre = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[8]/td[1]/input'))
    slow_typing(nombre, data["nombre"])

    fecha_nacimiento = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[8]/td[2]/input'))
    slow_typing(fecha_nacimiento, data["fecha_nacimiento"])

    localidad = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[10]/td[1]/input'))
    slow_typing(localidad, data["localidad"])

    
    #Select pais_de_origen
    select_element = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[10]/td[2]/select'))
    select_object = Select(select_element)
    select_object.select_by_visible_text(data["pais_de_origen"])

    #Select nacionalidad_actual
    select_element = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[12]/td[1]/select'))
    select_object = Select(select_element)
    select_object.select_by_visible_text(data["nacionalidad_actual"])

    #Select nacioanlidad_origen
    select_element = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[12]/td[2]/select'))
    select_object = Select(select_element)
    select_object.select_by_visible_text(data["nacioanlidad_origen"])

    #Select sexo
    select_element = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[14]/td[1]/select'))
    select_object = Select(select_element)
    select_object.select_by_visible_text(data["sexo"])

    #Select estado_civil
    select_element = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[14]/td[2]/select'))
    select_object = Select(select_element)
    select_object.select_by_visible_text(data["estado_civil"])


    apellidos_del_padre_tutelar = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[15]/td/fieldset/table/tbody/tr[2]/td[1]/input'))
    slow_typing(apellidos_del_padre_tutelar, data["apellidos_del_padre_tutelar"])

    nombre_del_padre_tutelar = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[15]/td/fieldset/table/tbody/tr[2]/td[2]/input'))
    slow_typing(nombre_del_padre_tutelar, data["nombre_del_padre_tutelar"])

    direccion_del_padre_tutelar = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[15]/td/fieldset/table/tbody/tr[4]/td/input'))
    slow_typing(direccion_del_padre_tutelar, data["direccion_del_padre_tutelar"])

    telefono_del_padre_tutelar = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[15]/td/fieldset/table/tbody/tr[6]/td[1]/input'))
    slow_typing(telefono_del_padre_tutelar, data["telefono_del_padre_tutelar"])

    email_del_padre_tutelar = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[15]/td/fieldset/table/tbody/tr[6]/td[2]/input'))
    slow_typing(email_del_padre_tutelar, data["email_del_padre_tutelar"])
    
    #Select nacionalidad_del_padre_tutelar
    select_element = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[15]/td/fieldset/table/tbody/tr[8]/td/select'))
    select_object = Select(select_element)
    select_object.select_by_visible_text(data["nacionalidad_del_padre_tutelar"])


    carnet_de_identidad = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[17]/td[1]/input'))
    slow_typing(carnet_de_identidad, data["carnet_de_identidad"])


    button_next = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", "/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[1]/table/tbody/tr[18]/td[2]/a"))
    button_next.click()  



def llenar_formulario_segunda_pagina(driver,data):

    
    numero_de_pasaporte = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[2]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td[2]/input'))
    slow_typing(numero_de_pasaporte, data["numero_de_pasaporte"])

    fecha_de_emision_pasaporte = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[2]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[4]/td[1]/input'))
    slow_typing(fecha_de_emision_pasaporte, data["fecha_de_emision_pasaporte"])

    fecha_de_vencimiento_pasaporte = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[2]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[4]/td[2]/input'))
    slow_typing(fecha_de_vencimiento_pasaporte, data["fecha_de_vencimiento_pasaporte"])

    #Select PAIS DONDE FUE EMITIDO EL PASAPORTE
    select_element = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[2]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[6]/td/select'))
    select_object = Select(select_element)
    select_object.select_by_visible_text(data["pasaporte_emitido_por"])


    residencia_habitual = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[2]/table/tbody/tr[6]/td[1]/input'))
    slow_typing(residencia_habitual, data["residencia_habitual"])

    telefono_casa = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[2]/table/tbody/tr[6]/td[2]/input'))
    slow_typing(telefono_casa, data["telefono_casa"])

    button_next = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", "/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[2]/table/tbody/tr[8]/td[2]/a"))
    button_next.click()  

    
def llenar_formulario_tercera_pagina(driver,data):

    #Select Ocupacion Actual
    select_element = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[3]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td/select'))
    select_object = Select(select_element)
    select_object.select_by_value(data["ocupacion_actual"])

    entidad_laboral_o_estudiantil = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[3]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[4]/td/input'))
    slow_typing(entidad_laboral_o_estudiantil, data["entidad_laboral_o_estudiantil"])

    telefono_de_la_entidad_laboral_o_estudiantil = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[3]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[6]/td/input'))
    slow_typing(telefono_de_la_entidad_laboral_o_estudiantil, data["telefono_de_la_entidad_laboral_o_estudiantil"])

    info_porque_viene_a_portugal = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[3]/table/tbody/tr[4]/td/input'))
    slow_typing(info_porque_viene_a_portugal, data["info_porque_viene_a_portugal"])

    #Select 1ERA FORNTERA
    select_element = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[3]/table/tbody/tr[7]/td/select'))
    select_object = Select(select_element)
    select_object.select_by_visible_text(data["por_que_frontera_entra_a_portugal"])

    button_next = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", "/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[3]/table/tbody/tr[8]/td[2]/a"))
    button_next.click()  

def llenar_formulario_cuarta_pagina(driver,data):

    duracion_de_la_estadia_en_dias = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[4]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td[2]/input'))
    slow_typing(duracion_de_la_estadia_en_dias, data["duracion_de_la_estadia_en_dias"])

    fecha_de_llegada = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[4]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[4]/td[1]/input'))
    slow_typing(fecha_de_llegada, data["fecha_de_llegada"])

    button_next = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", "/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[4]/table/tbody/tr[4]/td[2]/a"))
    button_next.click() 

def llenar_formulario_quinta_pagina(driver,data):

    nombre_alojamiento = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[5]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td[1]/input'))
    slow_typing(nombre_alojamiento, data["nombre_alojamiento"])

    telefono_alojamiento = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[5]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td[2]/input'))
    slow_typing(telefono_alojamiento, data["telefono_alojamiento"])

    direccion_alojamiento = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[5]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td[1]/input'))
    slow_typing(direccion_alojamiento, data["direccion_alojamiento"])

    email_alojamiento = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[5]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[4]/td[2]/input'))
    slow_typing(email_alojamiento, data["email_alojamiento"])
    
    #Select condado_alojamiento
    select_element = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[5]/table/tbody/tr[3]/td/fieldset/table/tbody/tr[6]/td[1]/select'))
    select_object = Select(select_element)
    select_object.select_by_visible_text(data["condado_alojamiento"])

    #Select requerente1
    select_element = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[5]/table/tbody/tr[5]/td/fieldset/table/tbody/tr/td[1]/fieldset/table/tbody/tr[1]/td/select'))
    select_object = Select(select_element)
    select_object.select_by_value(data["requerente1"])

    #Select requerente2
    select_element = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[5]/table/tbody/tr[5]/td/fieldset/table/tbody/tr/td[1]/fieldset/table/tbody/tr[2]/td/select'))
    select_object = Select(select_element)
    select_object.select_by_value(data["requerente2"])


    button_next = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", "/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[5]/table/tbody/tr[6]/td[2]/a"))
    button_next.click() 

def llenar_formulario_sexta_pagina(driver,data):
    foto_carnet = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[6]/table/tbody/tr[1]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td[2]/input'))
    foto_carnet.send_keys("C:/Andrea/static/JPG/foto.jpg")
    
    anexo1 = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[6]/table/tbody/tr[1]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr[7]/td[2]/input'))
    anexo1.send_keys("C:/Andrea/static/PDF/Pasaport_Prereserva_Boleto_Andrea.pdf")

    anexo2 = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[6]/table/tbody/tr[1]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr[8]/td[2]/input'))
    anexo2.send_keys("C:/Andrea/static/PDF/Poder_Andrea.pdf")

    anexo3 = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[6]/table/tbody/tr[1]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr[9]/td[2]/input'))
    anexo3.send_keys("C:/Andrea/static/PDF/Reserva_hotel.pdf")

    anexo4 = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", '/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[6]/table/tbody/tr[1]/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr[10]/td[2]/input'))
    anexo4.send_keys("C:/Andrea/static/PDF/Seguro_Viaje_Andrea.pdf")
    
    button_next = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", "/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[6]/table/tbody/tr[2]/td[2]/a"))
    button_next.click()


def llenar_formulario_septima_pagina(driver,data):
    def abrir_almanaque():
      
        try:


            button = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", "/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[7]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td[1]/i"))
            button.click()

            button_next_month = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", "/html/body/div[4]/table/thead/tr[2]/td[4]"))
            button_next_month.click()

           

            ######seleccionamos el dia
            flag_no_encontro_fecha = False  
            try:
                #selecciona el dia
                button_cita = WebDriverWait(driver, timeout=1).until(lambda d: d.find_element("By.CLASS_NAME", "day.false"))
                button_cita.click()
                flag_no_encontro_fecha = True
            except Exception:
                    pass
            if flag_no_encontro_fecha == False:
                driver.refresh()
                llenar_todo_el_formulario(driver)
            ######seleccionamos el dia



            ######selecciona la hora
            select_element = WebDriverWait(driver, timeout=2).until(lambda d: d.find_element("xpath",'/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/div[2]/div[7]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[2]/td[2]/select'))
            select_object = Select(select_element)
         
            flag_no_encontro_hora = False
            for i in range(-1,-15):    
                try:
                    select_object.select_by_value(str(i))
                    flag_no_encontro_hora = True
                    break
                except Exception:
                    pass

            if flag_no_encontro_hora==False:
                driver.refresh()
                llenar_todo_el_formulario(driver)

            ######selecciona la hora


            ######ENVIAMOS todo y rezamos        
            button_fin = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element("xpath", "/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td/form/table/tbody/tr[6]/td/div/table[2]/tbody/tr/td[2]/input"))
            button_fin.click()
            ######ENVIAMOS todo y rezamos 
            
                

       
        except Exception:
            print('error')
            pass

    abrir_almanaque()
    

        


def llenar_todo_el_formulario(driver):
    
    with open("andrea.json") as json_file:

        data = json.load(json_file)

        llenar_formulario_primera_pagina(driver,data)
        llenar_formulario_segunda_pagina(driver,data)
        llenar_formulario_tercera_pagina(driver,data)
        llenar_formulario_cuarta_pagina(driver,data)
        llenar_formulario_quinta_pagina(driver,data)
        llenar_formulario_sexta_pagina(driver,data)
        llenar_formulario_septima_pagina(driver,data)


def function_use(driver,root):
    root.destroy()

    root = tk.Tk()
    root.config(width=300, height=200)
    root.title("CITA")


    boton = ttk.Button(text="Refresh", command=partial(refresh,driver, root))
    boton.place(x=50, y=50)
    root.mainloop()


def refresh(driver,root):
    driver.refresh()
    llenar_todo_el_formulario(driver)
    function_use(driver,root)

def function_principal(driver,root):
    

    
    root.destroy()

    paso1=login(driver)

    if paso1:

        paso2= abrir_formulario_turismo(driver)

        if paso2:

            llenar_todo_el_formulario(driver)
            root = tk.Tk()
            root.config(width=300, height=200)
            root.title("CITA")


            boton = ttk.Button(text="Refresh", command=partial(refresh,driver, root))
            boton.place(x=50, y=50)
            root.mainloop()
        
    #function_use(driver,root)    
    
    
    

    

    


    

driver = webdriver.Chrome(executable_path="C:/Andrea/static/chrome_webdriver/chromedriver.exe")


driver.get("https://pedidodevistos.mne.gov.pt/")

root = tk.Tk()
root.config(width=300, height=200)
root.title("CITA")


boton = ttk.Button(text="PLAY", command=partial(function_principal, driver, root))
boton.place(x=50, y=50)
root.mainloop()







#driver.close()

