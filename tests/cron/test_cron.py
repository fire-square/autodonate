from autodonate.lib.utils.cron import Callback, callbacks, register_function


def test_cron_job_add():
    def func():
        pass

    c = Callback(function=func, timeout=5)
    register_function(func, 5)
    assert c in callbacks
