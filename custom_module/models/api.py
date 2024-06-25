
from odoo import api, fields, models
# Configuration
API_KEY = 'Api-Key '+ 'data'
import requests
import json

class Factura(models.Model):
    _inherit = 'account.move'

    response = fields.Text('Response', readonly=True)

    reference = fields.Text('Reference', readonly=True)

    def list_customer(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': API_KEY
        }
        url = 'your_url'

        response = requests.request('GET', url, headers=headers)
        if response.status_code == 200:
            if response.headers.get('content-type') == 'application/json':
                print('Success')
                data = response.json()
                list_customers = [customer['cedula'] for customer in data['results']]
                return list_customers

    def api_list_customer(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': API_KEY
        }
        url = 'your_url'
        response = requests.request('GET', url, headers=headers)
        if response.status_code == 200:
            if response.headers.get('content-type') == 'application/json':
                print('Success')
                data = response.json()
                # print(data)
                filter_ci = "1226579"
                customers = [customer for customer in data['results'] if
                                      filter_ci == customer['cedula']]

                for customer in customers:
                    self.env['res.partner'].create({'name': customer['nombre'],
                                 'email': customer['email'],
                                 'vat': customer['cedula'],
                                 'website': customer['direccion']
                                 })
                return True
        return True


    def api_list_invoice(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': API_KEY
        }
        url = 'your_url'

        response = requests.request('GET',url,headers = headers)
        if response.status_code == 200:
            if response.headers.get('content-type') == 'application/json':
                print('Success')
                data = response.json()
                # print(data)
                list_customer = self.list_customer()
                reference_data = ''
                filter_date = "2024-06-07"
                invoices = [factura for factura in data['results'] if filter_date in factura['fecha_emision']]
                print("#####success#####")
                for data_cust in data['results']:
                    cliente = data_cust['cliente']
                    if cliente['cedula']:
                        if cliente['cedula'] in list_customer:
                            print(cliente['cedula'])

                for data_invoice in invoices:
                    if data_invoice['referencia']:
                        self.create({'ref':data_invoice['referencia'],
                                     'reference':data_invoice['referencia'],
                                     'invoice_date':data_invoice['fecha_emision'],
                                     'partner_id':34156,
                                     'move_type': 'out_invoice'
                                     })
                        reference_data = data_invoice['referencia']
                        print(data_invoice['referencia'])
                        if data_invoice['fecha_emision']:
                            print(type(data_invoice['fecha_emision']))
                obj = self.env['account.move'].search([('id', '=',28316)])
                if obj:
                    obj.write({'reference':reference_data,'response':"Connection success, Statu "+ str(response.status_code)})
                return True


    def fetch_invoices_from_external_api(self):
        headers = {
            'Content-Type': 'application/json',
            'Api-Key': API_KEY
        }
        url = 'your_url'

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            if response.headers.get('content-type') == 'application/json':
                try:
                    data = response.json()

                    for invoice_data in data.get('params', {}).get('data', []):
                        print(invoice_data['partner_id'])

                except json.decoder.JSONDecodeError as e:
                    error_message = f'Error when decoding the JSON: {e}. Response: {response.text}'
                    print(error_message)
            else:
                print("Response doesn't a JSON")
        else:

            error_message = response.json().get('params', {}).get('error', 'Unknown error')
            print(f"Failed to fetch invoices: {error_message}")