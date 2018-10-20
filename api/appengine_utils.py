import subprocess
import sys
import os


def _find_sdk_from_path():
    """Finds the location of the GAE SDK.

    Assumes `dev_appserver.py` is on your PATH - SDK installers set this up.
    Will fail if called within running dev_appserver due to stubs
    and os mocks from the sdk.

    Returns:
        str: Path to sdk directory
    """
    which = 'where' if sys.platform == "win32" else 'which'
    try:
        path = subprocess.check_output([which, 'dev_appserver.py']).strip()
    except Exception:
        raise RuntimeError('Could not find dev_appserver.py in PATH.')

    sdk_dir = os.path.dirname(os.path.realpath(path))

    if os.path.exists(os.path.join(sdk_dir, 'bootstrapping')):
        # Cloud SDK
        sdk_dir = os.path.abspath(os.path.join(sdk_dir,
                                               '..',
                                               'platform',
                                               'google_appengine'))
        if not os.path.exists(sdk_dir):
            raise RuntimeError(
                'The Cloud SDK is on the path, '
                'but the app engine SDK dir could not be found'
            )
        else:
            return sdk_dir
    else:
        # Regular App Engine SDK
        return sdk_dir


def add_gae_path():
    """Adds the GAE SDK to the path if not already set.

    Note:
        Does not instantiate the dev_appserver or any stubs.
    """
    try:
        from google.appengine.ext import ndb # noqa
    except ImportError:
        sdk_path = _find_sdk_from_path()
        sys.path.insert(1, sdk_path)
    import dev_appserver
    dev_appserver.fix_sys_path()
