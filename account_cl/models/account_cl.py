# -*- encoding: utf-8 -*-
from openerp.osv import osv, fields


class account_cl(osv.osv):

    _inherit = 'res.partner'
    _columns = {
                'test': fields.char ('Description', size=128, help="ie, Test",required=True)
        
    }