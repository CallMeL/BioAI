from ..registry import register

@register("spotify")
def shell():
    from .api import build_tool
    return build_tool