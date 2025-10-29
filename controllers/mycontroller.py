from odoo import http
from odoo.http import request , Response
import json

class WaterLeakController(http.Controller):

    @http.route('/water', auth='public',type='http' ,website=True)
    def web_por(self, **kwargs):
        fuites = request.env['odoo19.fuites'].sudo().search([])
        return request.render('odoo19_fuites.technician_leaks_page', {
            'leaks': fuites
        })

    @http.route('/api/water', auth='public', type='http', methods=['GET'], csrf=False)
    def api_leaks(self, **kwargs):
        leaks = request.env['odoo19.fuites'].sudo().search([])
        result = []
        for leak in leaks:
            result.append({
                'source': leak.source,
                'report_datetime': leak.report_datetime,
                'leak_type': leak.leak_type,
                'address': leak.address,
                'photo': leak.photo,
            }) 
        return Response(
                json.dumps({"result": result}, default=str),
                content_type='application/json',
            )