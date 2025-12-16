{
    "name": "POS Receipt - Ref Code",
    "version": "18.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Show product internal reference (default_code) on POS printed receipt",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale._assets_pos": [
            "q_pos_ticket/static/src/js/receipt_refcode.js",
            "q_pos_ticket/static/src/xml/receipt_refcode.xml",
        ],
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}