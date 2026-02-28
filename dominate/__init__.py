from .version import __version__, version
from .document import document
from .dom_tag import (DASHED_ATTRIBUTES, add_dashed_attributes,
  reset_dashed_attributes)

__all__ = ['__version__', 'version', 'document', 'DASHED_ATTRIBUTES',
  'add_dashed_attributes', 'reset_dashed_attributes']
