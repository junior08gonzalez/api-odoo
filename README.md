# api-odoo
      tu_dominio/jsonrpc
      
# Login
         {
              "jsonrpc": "2.0",
              "method": "call",
              "params": {"service": "common", "method": "login", "args": ["db", "user", "password"]}
          }
          
# Obtener Productos
      {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
                    "service": "object", 
                    "method": "execute", 
                    "args": ["db", uid, "password", "product.template", "search_read", [], []]}
      }
# Ventas por cliente
      {
            "jsonrpc": "2.0",
              "method": "call",
              "params": {
                          "service": "object", 
                          "method": "execute", 
                          "args": ["db", uid, "password", "sale.order", "search_read", 
                                  [ ["partner_id", "=", 7 ] ], 
                                  ["name"]
                                  ]}
       }
# Eliminar Producto
      {
              "jsonrpc": "2.0",
              "method": "call",
              "params": {
                          "service": "object", 
                          "method": "execute", 
                          "args": ["db", uid, "password", "product.template", "unlink", [id] ]}
          }

# Validar una Venta
      {
              "jsonrpc": "2.0",
              "method": "call",
              "params": {
                          "service": "object", 
                          "method": "execute", 
                          "args": ["db", uid, "password", "sale.order", "action_confirm", [12] ]}
          }
# Crear Producto
      {
              "jsonrpc": "2.0",
              "method": "call",
              "params": {
                          "service": "object", 
                          "method": "execute", 
                          "args": ["db", uid, "password", "product.template", "create", {
                              "name" : "ladrillo",
                              "default_code" : "lad001"
                          }]}
          }
# Crear Ventas
      {
              "jsonrpc": "2.0",
              "method": "call",
              "params": {
                          "service": "object", 
                          "method": "execute", 
                          "args": ["db", uid, "password", "sale.order", "create", {
                              "partner_id" : 7,
                              "order_line" : [ 
                                                  [0,0, { 
                                                          "product_id": 165 , 
                                                          "product_uom_qty": 1,
                                                          "price_unit" : 5000
                                                          }] 
                                              ]
                              
                          }]}
          }
# Actualizar Pedido Venta
      {
              "jsonrpc": "2.0",
              "method": "call",
              "params": {
                          "service": "object", 
                          "method": "execute", 
                          "args": ["demo", 2, "3bfb702b135213cc69c11e6310a9fd4035b6e79a", "sale.order", "write",[[198],{
                              
                        "partner_id" : 86,
                        "order_line" : [ 
                                            [0,0, { 
                                                    "product_id": 165 , 
                                                    "product_uom_qty": 12,
                                                     "price_unit" : 5000
                                                    },
                                                    { 
                                                    "product_id": 166 , 
                                                    "product_uom_qty": 1,
                                                     "price_unit" : 52000
                                                    }
                                                    ],

                                                     [0,0,
                                                    { 
                                                    "product_id": 166 , 
                                                    "product_uom_qty": 1,
                                                     "price_unit" : 52000
                                                    }
                                                    ] 
                                        ]
                        
                    }] ]}
    }
