from django import template
import re

register = template.Library()

@register.filter(name='highlight')
def highlight(text, phrase):
    if not phrase:
        return text
    pattern = re.compile(re.escape(phrase), re.IGNORECASE)
    return pattern.sub(lambda m: f'<mark>{m.group(0)}</mark>', text)
