{
    'name': 'POS Product Price on Card',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Show product price under product name in POS (Odoo 18)',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_product_price_card/static/src/**/*',
        ],
    },
    'installable': True,
    'application': False,
}
