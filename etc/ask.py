CONFIG = {
    'mode': 'django',
    'environment': {
        'PYTHONPATH': '/home/box/web/ask',
    },
    'args': (
        '--bind=0.0.0.0:8000',
        '--workers=4',
        # '--worker-class=egg:gunicorn#sync',
        # '--timeout=30',
        'ask.settings',
    ),
}
