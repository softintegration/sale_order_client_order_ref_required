# -*- coding: utf-8 -*-

from odoo import models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        for order in self:
            if not order.client_order_ref:
                raise ValidationError(_("Client order reference is required in order to confirm quotation order"))
        return super(SaleOrder, self).action_confirm()
