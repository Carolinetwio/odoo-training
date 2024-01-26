from odoo import http

class MotorcycleStock(http.Controller):

    @http.route('/hello_world/', auth='public', website=True, sitemap=True)
    def hello_world(self, **kw):
        return 'Hello World!'

    @http.route('/motorcycle_registry/motorcycles', auth='public', website=True, sitemap=True)
    def motorcycles(self, **kw):
        motorcycles = http.request.env['product.template'].search([])
        return http.request.render('motorcycle_website.comparison_website',{
            'motorcycles': motorcycles,
        })

    @http.route('/motorcycle_registry/<model("product.template"):motorcycle>/', auth='user', website=True, sitemap=True)
    def motorcycle(self, motorcycle):
        return http.request.render('motorcycle_website.motorcycle_website',{
            'motorcycle': motorcycle
        })
        
    