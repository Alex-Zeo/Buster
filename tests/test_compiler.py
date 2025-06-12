import importlib


module = importlib.import_module('buster.compiler.report_compiler')
ReportCompiler = module.ReportCompiler


def test_compiler_import():
    assert hasattr(module, 'ReportCompiler')


def test_compile_fetches_url(monkeypatch):
    def fake_get(url, timeout=5):
        class Response:
            text = 'fetched'

            def raise_for_status(self):
                pass

        return Response()

    monkeypatch.setattr(module.httpx, 'get', fake_get)
    compiler = ReportCompiler()
    messages = [{
        'content': 'see http://example.com',
        'author': 'user',
        'timestamp': 't',
    }]
    result = compiler.compile(messages)
    assert result == {
        'messages': [{
            'author': 'user',
            'timestamp': 't',
            'content': 'see http://example.com',
            'evidence': [{'url': 'http://example.com', 'content': 'fetched'}],
        }]
    }


def test_compile_no_urls():
    compiler = ReportCompiler()
    messages = [{'content': 'hello', 'author': 'a', 'timestamp': 't'}]
    result = compiler.compile(messages)
    assert result['messages'][0]['evidence'] == []
