# -*- coding: utf-8 -*-
{
    "name": "Odoo CiviCRM Sync",
    "summary": """Odoo CiviCRM Sync""",
    "description": """Sync partner, invoice and payment records with CiviCRM.""",
    "version": "1.0",
    "author": "Compucorp Ltd.",
    "website": "https://www.compucorp.co.uk",
    "license": "LGPL-3",
    "category": "Data Synchronisation",
    "maintainer": "Compucorp Ltd.",
    "depends": [
        "base",
        "account",
        "product",
    ],
    'data': [
        'views/civicrm_sync_settings.xml',
        'data/product_data.xml',
    ],
    "application": True,
}
