import logging
import re
import warnings

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


# Make sure that DeprecationWarning within this package always gets printed
warnings.filterwarnings(
    "always", category=DeprecationWarning, module=r"^{0}\.".format(re.escape(__name__))
)

# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
#

__version__ = "0.0.1"
