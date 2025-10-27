from odoo import models, fields

class WaterLeakModel(models.Model):
    _name = 'odoo19.fuites'
    _description = 'Declaration de fuite deau'

    source = fields.Selection([
        ('phone', 'Téléphone'),
        ('email', 'Email'),
        ('social', 'Réseaux sociaux'),
    ], string='Source', required=True)

    report_datetime = fields.Datetime(string='Date et Heure', required=True)
    leak_type = fields.Selection([
        ('potable', 'Eau potable'),
        ('waste', 'Assainissement'),
    ], string='Type de fuite', required=True)

    address = fields.Char(string='Adresse')
    photo = fields.Binary(string='Photo')
