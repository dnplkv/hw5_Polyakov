from unittest.mock import MagicMock

from main.models import Rate
from main.tasks import parse_privatbank


def test_parse_privatbank(mocker):
    cnt_before = Rate.objects.count()
    cur = [{'ccy': "USD", 'base_ccy': "UAH", 'buy': "27.20000", 'sale': "27.60000"},
           {'ccy': "EUR", 'base_ccy': "UAH", 'buy': "33.10000", 'sale': "33.70000"},
           {'ccy': "RUR", 'base_ccy': "UAH", 'buy': "0.36000", 'sale': "0.39000"},
           {'ccy': "BTC", 'base_ccy': "USD", 'buy': "34502.8418", 'sale': "38134.7198"}]
    requests_get_patcher = mocker.patch('requests.get')
    requests_get_patcher.return_value = MagicMock(
        status_code=200,
        json=lambda: cur,
    )

    parse_privatbank()
    assert Rate.objects.count() == cnt_before + 2

    # Дважды не сохранять Rate с одинаковыми: source, currency
    parse_privatbank()
    assert Rate.objects.count() == cnt_before + 2
