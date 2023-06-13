class NoHaySaldoException (Exception):
    pass

class UsuarioDesactivadoException (Exception):
    pass

class EstadoNoExistenteException (Exception):
    pass


DESACTIVADO = "estado_desactivado"
ACTIVADO = "estado_activado" 

PRECIO_TICKET = 70
PRIMARIO = "descuento_primario"
SECUNDARIO = "descuento_secundario"
UNIVERSITARIO = "descuento_universitario"
JUBILADO =  "descuento_jubilado"

DESCUENTOS = {
PRIMARIO: 50,
SECUNDARIO: 40,
UNIVERSITARIO: 30,
JUBILADO: 25,
}

class Sube:
        def __init__(self, saldo=0, estado= ACTIVADO, grupo_beneficiario = None):
             self.estado = estado
             self.saldo = saldo
             self.grupo_beneficiario = grupo_beneficiario
        def obtener_precio_ticket(self):
            if self.grupo_beneficiario == None:
                 return PRECIO_TICKET
            elif self.grupo_beneficiario == PRIMARIO:
                 return PRECIO_TICKET - (PRECIO_TICKET * 0.50)
            elif self.grupo_beneficiario == SECUNDARIO:
                 return PRECIO_TICKET - (PRECIO_TICKET*0.40)
            elif self.grupo_beneficiario == UNIVERSITARIO:
                 return PRECIO_TICKET - (PRECIO_TICKET*0.30)
            elif self.grupo_beneficiario == JUBILADO:
                 return PRECIO_TICKET - (PRECIO_TICKET*0.25)
        def pagar_pasaje(self):
               if self.estado == ACTIVADO:
                    if self.saldo >= PRECIO_TICKET and self.grupo_beneficiario == None:
                         self.saldo -= PRECIO_TICKET
                    if self.saldo >= PRECIO_TICKET and self.grupo_beneficiario == PRIMARIO:
                         self.saldo = PRECIO_TICKET - (PRECIO_TICKET - (PRECIO_TICKET*0.50)) 
                    if self.saldo >= PRECIO_TICKET and self.grupo_beneficiario == SECUNDARIO:
                         self.saldo -= PRECIO_TICKET - (PRECIO_TICKET*0.40)
                    if self.saldo >=  PRECIO_TICKET and self.grupo_beneficiario == UNIVERSITARIO:
                         self -= PRECIO_TICKET - (PRECIO_TICKET*0.30)
                    if self.saldo >= PRECIO_TICKET and self.grupo_beneficiario == JUBILADO:
                         self -= PRECIO_TICKET - (PRECIO_TICKET*0.25)
               else:
                   raise UsuarioDesactivadoException
        
        
                  
        
     
                          

    
                       
        