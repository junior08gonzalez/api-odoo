# -*- coding: utf-8 -*-
import requests
from odoo import http
from odoo.http import route
# Configuration
API_KEY = 'Api-Key '+'data'


class ExternalAPIController(http.Controller):

    @http.route('/list_invoice', type="http", auth='none', cors="*")
    def api_list_invoice(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': API_KEY
        }
        url = 'https://api.wisphub.io/api/facturas/'

        response = requests.request('GET',url,headers = headers)
        data = response.json()
        return str(data)

    @route('/test', type="http", auth="public", cors='*')
    def websocket(self):
        return {"status":200, "body":"Hello"}


    @http.route('/external_api_connector/fetch_invoices', type='http', auth='none',cors="*")
    def fetch_invoices(self, **kwargs):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': API_KEY
        }
        url = 'your_url'

        response = requests.request('GET',url, headers=headers)
        print("controlador")
        if response.status_code == 200:
            data = response.json()
            return {
                'params': {
                    'success': True,
                    'data': data
                }
            }
        else:
            return {
                'params': {
                    'success': False,
                    'error': 'Failed to fetch data',
                    'status_code': response.status_code
                }
            }



