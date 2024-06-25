import xmlrpc.client
from odoo import api, fields, models

class ApiExternal(models.Model):

    _inherit = 'sale.order'

    response = fields.Text('Response from server')

    def Conection(self):
        url = "your_url"
        db = "db"
        username = "username_odoo"
        #Can you generate a random api key in Odoo
        password = "your_apikey"
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        try:
            # self.response = common.version()
            uid = common.authenticate(db, username, password, {})
            models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
            """VERIFICAMOS SI PODEMOS LEER EL MODELO RES PARTNER (CONTACTO)"""
            self.response = models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'],
                              {'raise_exception': False})
            """LISTA DE REGISTROS PUEDE SI NO CUMPLE LA CONDICION PUEDE SER VACION"""
            self.response = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
            """PAGINACION DE LISTA DE REGISTROS"""
            self.response = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 10, 'limit': 5})
            """CONTAR REGISTROS"""
            self.response = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
            """LEER LOS REGISTROS"""
            ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]],
                                    {'limit': 1})
            self.response = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids],
                              {'fields': ['name', 'country_id', 'comment']})
            """LISTAR CAMPOS DE REGISTRO"""
            self.response = models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [], {'attributes': ['string', 'help', 'type']})
            """BUCAR UN REGISTRO Y LEER LOS CAMPOS ESPECIFICADOS"""
            self.response = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]],
                              {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
            """CREAR REGISTROS"""
            id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "API EXTERNAL CUSTOMER"}])
            self.response = id
            """ACTUALIZAR REGISTROS"""
            models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {'name': "Newer partner"}])
            self.response = models.execute_kw(db, uid, password, 'res.partner', 'read', [[id], ['display_name']])
            """ELIMINAR REGISTROS"""
            models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[id]])
            """Verificamos si el registro ha sido eliminada"""
            models.execute_kw(db, uid, password, 'res.partner', 'search', [[['id', '=', id]]])
            """CREAR UN MODELO PERSONALIZADO"""
            # model_id = models.execute_kw(db, uid, password, 'ir.model', 'create', [{
            #     'name': "Neww Custom Model",#DEBE SER UNICO####
            #     'model': "x_neww_custom_model",#DEBE SER UNICO####
            #     'state': 'manual',
            # }])
            """CREAR UN CAMPO PERSONALIZADO"""
            # models.execute_kw(db, uid, password, 'ir.model.fields', 'create', [{
            #     'model_id': model_id,
            #     'name': 'x_neww_name',#DEBE SER UNICO###
            #     'ttype': 'char',
            #     'state': 'manual',
            #     'required': True,
            # }])
            # record_id = models.execute_kw(db, uid, password, 'x_neww_custom_model', 'create', [{'x_neww_name':'test record'}])
            # self.response = models.execute_kw(db, uid, password, 'x_neww_custom_model', 'read', [[record_id]])

        except():
            print("Uhh, Something wrong!!!!")


