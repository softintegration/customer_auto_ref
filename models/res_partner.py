# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models
CUSTOMER_REF_SEQUENCE_CODE = "res.partner.customer.ref"

class Partner(models.Model):
    _inherit = 'res.partner'

    readonly_ref = fields.Boolean(compute='_compute_readonly_ref')

    @api.depends('customer_rank')
    def _compute_readonly_ref(self):
        for each in self:
            each.readonly_ref = each.customer_rank > 0

    def _set_customer_auto_ref(self):
        for each in self:
            ref = self.env['ir.sequence'].next_by_code(CUSTOMER_REF_SEQUENCE_CODE)
            each.write({'ref': ref})


    @api.model_create_multi
    def create(self, vals):
        """ When the partner is created as customer we have to give him auto reference"""
        partners = super(Partner, self).create(vals)
        for each in partners:
            if each.customer_rank < 1:
                continue
            each._set_customer_auto_ref()
        return partners
    
    def _increase_rank(self, field, n=1):
        """ When partner become a customer we have to give him auto reference"""
        if field != 'customer_rank':
            return super(Partner, self)._increase_rank(field,n=n)
        become_customers = self.env['res.partner']
        for each in self:
            if each.customer_rank < 1:become_customers |= each
        res = super(Partner, self)._increase_rank(field,n=n)
        for customer in become_customers:
            customer._set_customer_auto_ref()
        return res



