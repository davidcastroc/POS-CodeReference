/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/store/models";

// Añade la referencia interna al export que usa el template del recibo
patch(Orderline.prototype, {
    export_for_printing() {
        const data = super.export_for_printing(...arguments);
        data.product_default_code = this.product?.default_code || "";
        return data;
    },
});