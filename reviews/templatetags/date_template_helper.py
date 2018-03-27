# coding=utf-8
from django import template

register = template.Library()


@register.filter
def reformat_date(value):
    content = value.split('-')
    result = content[0] + ' '
    if content[1] == u'01':
        result += u'Января'

    if content[1] == u'02':
        result += u'Февраля'

    if content[1] == u'03':
        result += u'Марта'

    if content[1] == u'04':
        result += u'Апреля'

    if content[1] == u'05':
        result += u'Мая'

    if content[1] == u'06':
        result += u'Июня'

    if content[1] == u'07':
        result += u'Июля'

    if content[1] == u'08':
        result += u'Августа'

    if content[1] == u'09':
        result += u'Сентября'

    if content[1] == u'10':
        result += u'Октября'

    if content[1] == u'11':
        result += u'Ноября'

    if content[1] == u'12':
        result += u'Декабря'

    result += u', 20' + content[2]
    return result




