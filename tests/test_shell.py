import pytest
from unittest.mock import patch, MagicMock
from speedtest import shell, SpeedtestCLIError


@pytest.mark.parametrize("download,upload", [
    (True, True),
    (True, False),
    (False, True),
])
def test_shell_basic(download, upload):
    """
    shell() を基本パラメータで呼び出して、SpeedtestCLIError が
    raise されないことを確認
    """
    # Speedtest の内部呼び出しをモック
    with patch("speedtest.Speedtest") as mock_speedtest:
        mock_instance = MagicMock()
        # results オブジェクトに最低限の属性をセット
        mock_results = MagicMock()
        mock_results.download = 100_000_000
        mock_results.upload = 50_000_000
        mock_results.ping = 20
        mock_results.dict.return_value = {"download": 100, "upload": 50, "ping": 20}
        mock_results.json.return_value = '{"download":100,"upload":50,"ping":20}'
        mock_results.share.return_value = "http://example.com/share"
        mock_results.server = {"sponsor":"ISP","name":"Server","d":10,"latency":5,"latency":5}
        mock_instance.results = mock_results
        mock_instance.config = {"client": {"isp": "ISP", "ip": "1.2.3.4"}}
        mock_speedtest.return_value = mock_instance

        # shell を呼ぶ
        shell(
            download=download,
            upload=upload,
            single=False,
            units=("bit", 1),
            share=False,
            simple=False,
            json_output=False,
            server=None,
            exclude=None,
            mini=None,
            source=None,
            timeout=10,
            secure=False,
            pre_allocate=True,
            version_flag=False,
        )

def test_shell_no_download_upload(monkeypatch):
    """
    download=False, upload=False の場合は SpeedtestCLIError が raise される
    """
    # sys.exit をモックして SystemExit を防ぐ
    monkeypatch.setattr("speedtest.sys.exit", lambda code=0: None)

    with pytest.raises(SpeedtestCLIError):
        shell(download=False, upload=False)
