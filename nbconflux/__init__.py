# These three lines comes from versioneer.
# Add to this file if you want, but do not remove these.
from ._version import get_versions
from .api import notebook_to_page

__version__ = get_versions()["version"]
del get_versions
