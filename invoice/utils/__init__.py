from django.http import HttpResponse
from invoice.conf import settings


def format_currency(amount):
    return u"%s %.2f %s" % (
        settings.INV_CURRENCY_SYMBOL, amount, settings.INV_CURRENCY
    )


def pdf_response(draw_funk, file_name, *args, **kwargs):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename='%s'" % file_name
    draw_funk(response, *args, **kwargs)
    return response
