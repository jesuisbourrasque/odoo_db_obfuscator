from odoo import api, SUPERUSER_ID
import re
import uuid


def obfuscate_db_data(cr):

    env = api.Environment(cr, SUPERUSER_ID, {})
    admin_user = env['res.users'].search([('login', '=', 'admin')])
    admin_user.password = '12345'

    for partner in env['res.partner'].search([]):
        uuid_name = str(uuid.uuid4())
        partner.email = re.sub('.*@', uuid_name + '@', partner.email)
        partner.name = uuid_name

    for model_name in ('ir.mail_server', 'fetchmail.server'):
        for record in env[model_name].search([]):
            record.unlink()
