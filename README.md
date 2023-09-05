# api-odoo
jsonrpc
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
