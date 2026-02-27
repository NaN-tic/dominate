
from dominate import tags
from dominate.community import htmx

# Import is intentional: importing this module patches tag attribute cleaning.
_ = htmx

def test_hx():
  d = tags.div(hx_foo=1)
  assert d.render() == '<div hx-foo="1"></div>'
